function loadColorTheme() {
    let colorTheme = localStorage.getItem('data-theme');
    if (colorTheme === null) {
        colorTheme = 'light';
    }
    document.getElementById('main').setAttribute('data-theme', colorTheme);
}

function changeTheme() {
    const html = document.getElementById('main');
    const newTheme = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('data-theme', newTheme);
}

window.onload = function() {
    loadColorTheme();
}
