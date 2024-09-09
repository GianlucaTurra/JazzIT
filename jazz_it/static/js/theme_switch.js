document.addEventListener('DOMContentLoaded', function() {
    console.log('QUALCOSA')
    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.classList.add(currentTheme);
    themeToggle.addEventListener('click', function(){
        const newTheme = document.documentElement.classList.contains('light') ? 'dark' : 'light';
        document.documentElement.classList.remove('light', 'dark');
        document.documentElement.classList.add(newTheme);
        localStorage.setItem('theme', newTheme);
        console.log('currentTheme')
    });
});