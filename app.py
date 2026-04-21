from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "nainno_investment_secret_key_2026"

# Database configuration
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# --- Routes ---

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

# Service detail routes
@app.route("/services/it")
def service_it():
    return render_template("services/it.html")

@app.route("/services/logistics")
def service_logistics():
    return render_template("services/logistics.html")

@app.route("/services/construction")
def service_construction():
    return render_template("services/construction.html")

@app.route("/services/pharmaceutical")
def service_pharmaceutical():
    return render_template("services/pharmaceutical.html")

@app.route("/services/stationery")
def service_stationery():
    return render_template("services/stationery.html")

@app.route("/services/cybersecurity")
def service_cybersecurity():
    return render_template("services/cybersecurity.html")

@app.route("/services/agriculture")
def service_agriculture():
    return render_template("services/agriculture.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        # Server-side validation
        if not all([name, email, phone, message]):
            flash("All fields are required.", "error")
            return redirect(url_for("contact"))

        try:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO contact_submissions (name, email, phone, message) VALUES (?, ?, ?, ?)",
                (name, email, phone, message)
            )
            conn.commit()
            conn.close()
            flash("Message sent! We'll be in touch shortly.", "success")
        except Exception as e:
            flash("Something went wrong. Please try again.", "error")
            print(f"Error: {e}")

        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route("/quote", methods=["GET", "POST"])
def quote():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        company = request.form.get("company")
        service = request.form.get("service")
        description = request.form.get("description")

        # Server-side validation
        if not all([full_name, email, phone, company, service, description]):
            flash("All fields are required.", "error")
            return redirect(url_for("quote"))

        if len(description) < 20:
            flash("Description must be at least 20 characters.", "error")
            return redirect(url_for("quote"))

        try:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO quote_requests (full_name, email, phone, company, service, description) VALUES (?, ?, ?, ?, ?, ?)",
                (full_name, email, phone, company, service, description)
            )
            conn.commit()
            conn.close()
            flash("Quote request submitted! Our team will contact you soon.", "success")
        except Exception as e:
            flash("Something went wrong. Please try again.", "error")
            print(f"Error: {e}")

        return redirect(url_for("quote"))

    return render_template("quote.html")

# Error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
