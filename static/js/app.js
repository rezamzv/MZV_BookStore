
    (function () {
    const toggle = document.querySelector('.account-menu-toggle');
    const dropdown = document.getElementById('account-dropdown');

    if (!toggle || !dropdown) return;

    function openMenu() {
    dropdown.classList.add('is-open');
    dropdown.setAttribute('aria-hidden', 'false');
    toggle.setAttribute('aria-expanded', 'true');
}

    function closeMenu() {
    dropdown.classList.remove('is-open');
    dropdown.setAttribute('aria-hidden', 'true');
    toggle.setAttribute('aria-expanded', 'false');
}

    toggle.addEventListener('click', function (e) {
    e.stopPropagation();
    const isOpen = dropdown.classList.contains('is-open');
    isOpen ? closeMenu() : openMenu();
});

    document.addEventListener('click', function (e) {
    if (!toggle.contains(e.target) && !dropdown.contains(e.target)) {
    closeMenu();
}
});

    document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
});
})();
