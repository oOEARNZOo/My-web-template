document.getElementById('toggle-dark').onclick = function() {
    document.body.classList.toggle('dark-mode');
    this.textContent = document.body.classList.contains('dark-mode') ? '☀️ Light Mode' : '🌙 Dark Mode';
};

window.addEventListener("scroll", function() {
    const about = document.querySelector(".about");
    const windowHeight = window.innerHeight;
    const elementTop = about.getBoundingClientRect().top;

    if (elementTop < windowHeight - 100) {
        about.classList.add("show");
    }
});
    