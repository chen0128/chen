document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggle-black-and-white');
    toggleButton.addEventListener('click', function() {
        document.body.classList.toggle('black-and-white');
    });
});