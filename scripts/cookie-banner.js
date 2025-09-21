// /scripts/cookie-banner.js
(function(){
  const KEY = 'cookieConsent_v1';
  const TTL_DAYS = 180;
  const banner = document.getElementById('cookie-banner');
  const prefsForm = document.getElementById('cookie-prefs');
  const reopen = document.getElementById('open-cookie-prefs');

  const get = () => {
    try {
      const obj = JSON.parse(localStorage.getItem(KEY) || '{}');
      if (!obj.ts) return null;
      const age = (Date.now() - obj.ts) / 86400000;
      return age > TTL_DAYS ? null : obj;
    } catch { return null; }
  };
  const set = (consent) => localStorage.setItem(KEY, JSON.stringify({ ...consent, ts: Date.now() }));

  const enableScriptsFor = (allowedCats) => {
    document.querySelectorAll('script[type="text/plain"][data-cookiecategory]').forEach(s => {
      const cat = s.getAttribute('data-cookiecategory');
      if (allowedCats.includes(cat)) {
        const clone = document.createElement('script');
        clone.text = s.text;
        [...s.attributes].forEach(a => {
          if (a.name !== 'type') clone.setAttribute(a.name, a.value);
        });
        clone.type = 'text/javascript';
        s.replaceWith(clone);
      }
    });
  };

  const saved = get();
  if (saved) {
    enableScriptsFor(saved.allowed || []);
  } else if (banner) {
    banner.hidden = false;
  }

  banner?.addEventListener('click', (e) => {
    const act = e.target?.dataset?.action;
    if (!act) return;

    if (act === 'reject') {
      set({ allowed: [] });
      banner.hidden = true;
    }
    if (act === 'accept') {
      const consent = { allowed: ['analytics','marketing'] };
      set(consent);
      enableScriptsFor(consent.allowed);
      banner.hidden = true;
    }
    if (act === 'prefs') {
      prefsForm.hidden = !prefsForm.hidden;
    }
    if (act === 'save') {
      e.preventDefault();
      const allowed = [];
      if (prefsForm.analytics.checked) allowed.push('analytics');
      if (prefsForm.marketing.checked) allowed.push('marketing');
      set({ allowed });
      enableScriptsFor(allowed);
      banner.hidden = true;
    }
  });

  reopen?.addEventListener('click', () => {
    const s = get();
    if (s) {
      prefsForm.analytics.checked = s.allowed?.includes('analytics');
      prefsForm.marketing.checked = s.allowed?.includes('marketing');
      prefsForm.hidden = false;
    }
    banner.hidden = false;
  });
})();
