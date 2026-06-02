document.addEventListener('DOMContentLoaded', function () {

  /* ─── Menú hamburguesa (mobile) ─── */
  const menuToggle = document.getElementById('menuToggle');
  const mobileMenu = document.getElementById('mobileMenu');

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', function () {
      const isOpen = mobileMenu.classList.toggle('is-open');
      menuToggle.setAttribute('aria-expanded', isOpen);
      mobileMenu.setAttribute('aria-hidden', !isOpen);

      // Cambiar ícono
      const icon = menuToggle.querySelector('.material-symbols-outlined');
      if (icon) icon.textContent = isOpen ? 'close' : 'menu';
    });

    // Cerrar al hacer clic en un link del menú móvil
    mobileMenu.querySelectorAll('.navbar__mobile-link').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileMenu.classList.remove('is-open');
        menuToggle.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('aria-hidden', 'true');
        const icon = menuToggle.querySelector('.material-symbols-outlined');
        if (icon) icon.textContent = 'menu';
      });
    });
  }

});