const { shell } = require('electron');

document.getElementById('launch').addEventListener('click', () => {
    const url = document.getElementById('url').value;
    if (url === '') {
        console.log('Please enter a URL');
        return;
    }

    shell.openExternal(url);
});