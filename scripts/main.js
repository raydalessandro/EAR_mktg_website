/* Nodo 432 – main.js minimal
   - Menu mobile (opzionale): richiede [data-nav-toggle] e [data-nav]
   - Traccia WhatsApp click (Plausible, no-op se non presente)
*/
(function () {
  var d = document;

  // Menu mobile (se esistono gli elementi)
  var toggle = d.querySelector('[data-nav-toggle], .nav-toggle');
  var menu = d.querySelector('[data-nav], #nav-menu');

  if (toggle && menu) {
    var open = function(){ menu.classList.add('open'); toggle.setAttribute('aria-expanded','true'); };
    var close = function(){ menu.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); };
    var isOpen = function(){ return menu.classList.contains('open'); };

    toggle.addEventListener('click', function(e){
      e.preventDefault();
      isOpen() ? close() : open();
    });

    // Chiudi cliccando fuori o con ESC
    d.addEventListener('click', function(e){
      if (!isOpen()) return;
      if (!menu.contains(e.target) && !toggle.contains(e.target)) close();
    });
    d.addEventListener('keydown', function(e){
      if (e.key === 'Escape' && isOpen()) close();
    });
  }

  // Plausible safe no-op
  window.plausible = window.plausible || function(){};

  // Traccia click WhatsApp (tutti i link wa.me)
  d.addEventListener('click', function(e){
    var a = e.target.closest('a[href^="https://wa.me/"]');
    if (a) {
      try { window.plausible('whatsapp_click'); } catch(_) {}
    }
  });

  // Traccia eventuali CTA con data-goal
  d.addEventListener('click', function(e){
    var g = e.target.closest('a[data-goal], button[data-goal]');
    if (g) {
      try { window.plausible(g.getAttribute('data-goal')); } catch(_) {}
    }
  });
})();
