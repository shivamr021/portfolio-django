document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll(".tab");
    const skillsContainer = document.querySelectorAll(".skills-container > div");

    // Hide all sections except frontend on load
    skillsContainer.forEach(skill => skill.classList.remove('active'));
    document.querySelector('.skill-frontend').classList.add('active'); // Show only frontend

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs and skill sections
            tabs.forEach(t => t.classList.remove('active-tab'));
            skillsContainer.forEach(skill => skill.classList.remove('active'));

            // Add active class to clicked tab
            tab.classList.add('active-tab');

            // Show the corresponding skill section
            const target = tab.getAttribute('data-target');
            document.querySelector(`.${target}`).classList.add('active');
        });
    });
});
