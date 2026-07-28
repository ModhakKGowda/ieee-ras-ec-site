document.addEventListener('DOMContentLoaded', () => {
    const contactBtn = document.getElementById('contactBtn');
    const contactModal = document.getElementById('contactModal');
    const closeModalBtn = document.getElementById('closeModalBtn');
    const contactForm = document.getElementById('contactForm');

    // Open Modal
    contactBtn.addEventListener('click', (e) => {
        e.preventDefault();
        contactModal.classList.add('active');
    });

    // Close Modal via button
    closeModalBtn.addEventListener('click', () => {
        contactModal.classList.remove('active');
    });

    // Close Modal via clicking dark backdrop
    contactModal.addEventListener('click', (e) => {
        if (e.target === contactModal) {
            contactModal.classList.remove('active');
        }
    });

    // Form submission stub
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('userName').value,
            srn: document.getElementById('userSrn').value,
            email: document.getElementById('userEmail').value,
            message: document.getElementById('userMessage').value
        };

        console.log("Form Data Captured:", formData);
        
        alert("Thank you! Your message has been logged. (Email delivery integration pending).");
        contactForm.reset();
        contactModal.classList.remove('active');
    });
});
