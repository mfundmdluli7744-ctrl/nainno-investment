document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('active');
        });
    }

    // Form Validations
    const contactForm = document.getElementById('contact-form');
    const quoteForm = document.getElementById('quote-form');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            if (validateForm(contactForm)) {
                const name = document.getElementById('name').value;
                const email = document.getElementById('email').value;
                const phone = document.getElementById('phone').value;
                const message = document.getElementById('message').value;

                const whatsappNumber = '26876526669';
                const text = `*New Contact Message*%0A%0A*Name:* ${name}%0A*Email:* ${email}%0A*Phone:* ${phone}%0A%0A*Message:* ${message}`;
                
                const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${text}`;
                window.open(whatsappUrl, '_blank');
            }
        });
    }

    if (quoteForm) {
        quoteForm.addEventListener('submit', (e) => {
            const description = quoteForm.querySelector('[name="description"]');
            if (description && description.value.length < 20) {
                alert('Description must be at least 20 characters.');
                e.preventDefault();
                return;
            }
            if (!validateForm(quoteForm)) {
                e.preventDefault();
            }
        });
    }

    function validateForm(form) {
        let isValid = true;
        const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
        
        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                input.style.borderColor = 'red';
            } else {
                input.style.borderColor = 'rgba(255, 255, 255, 0.1)';
            }
        });

        if (!isValid) {
            alert('Please fill in all required fields.');
        }

        return isValid;
    }
});
