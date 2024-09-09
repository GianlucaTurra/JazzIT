function loadColorTheme() {
    let colorTheme = localStorage.getItem('theme');
    if (colorTheme === null) {
        colorTheme = 'light';
    }
    document.getElementById('main').classList.add(colorTheme);
}

function changeTheme() {
    const html = document.getElementById('main');
    const newTheme = html.classList.contains('light') ? 'dark' : 'light';
    html.classList.remove('light', 'dark');
    html.classList.add(newTheme);
}

window.onload = function() {
    loadColorTheme();
}
