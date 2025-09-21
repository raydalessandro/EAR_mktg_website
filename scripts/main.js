// /scripts/main.js
document.addEventListener('DOMContentLoaded', () => {
  // Evidenzia la pagina corrente nel menu
  const here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-menu a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === here) a.classList.add('is-active');
  });

  // Toggle menu mobile
  const btn = document.querySelector('.nav-toggle');
  const menu = document.querySelector('#nav-menu');
  if (btn && menu) {
    btn.addEventListener('click', () => {
      const open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      menu.classList.toggle('open', !open);
    });
  }

  // Sicurezza link esterni
  document.querySelectorAll('a[target="_blank"]').forEach(a => {
    if (!a.rel.includes('noopener')) a.rel += (a.rel ? ' ' : '') + 'noopener';
  });
});
