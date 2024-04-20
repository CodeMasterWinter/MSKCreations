function alertErase() {
    var alerts = document.getElementsByClassName('alert')

    for (alert of alerts) {
        alert.style.opacity = '0';
        alert.style.visibility = 'hidden';
    }
}

window.onload = function() {
    setTimeout(alertErase, 8000);
};