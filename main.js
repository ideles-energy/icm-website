// Contact form: submit to Formspree without leaving the page.
(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  var ok = document.getElementById('form-ok');
  var nl = document.documentElement.lang === 'nl';
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var btn = form.querySelector('button[type="submit"]');
    btn.disabled = true;
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error('status ' + r.status);
        form.querySelectorAll('label, .row, button, .fine').forEach(function (el) { el.style.display = 'none'; });
        ok.style.display = 'block';
      })
      .catch(function () {
        btn.disabled = false;
        ok.style.display = 'block';
        ok.textContent = nl
          ? 'Er ging iets mis. Mail ons direct via bessbenchmark@icm.energy.'
          : 'Something went wrong. Please email us at bessbenchmark@icm.energy.';
      });
  });
})();

// Interactive demo in a dialog (falls back to the /demo/ page without JavaScript).
(function () {
  var dlg = document.getElementById('demo-dialog');
  if (!dlg || typeof dlg.showModal !== 'function') return;
  var frame = dlg.querySelector('iframe');
  document.querySelectorAll('[data-demo]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (window.innerWidth < 900) return; // small screens: open the demo page itself
      e.preventDefault();
      if (!frame.src) frame.src = a.getAttribute('href');
      dlg.showModal();
    });
  });
  dlg.querySelector('[data-close]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
})();

// Missed-opportunity sentence (illustrative: a similar asset can deliver 30% more revenue per MW).
(function () {
  var UPLIFT = 0.30;
  var $ = function (id) { return document.getElementById(id); };
  if (!$('s-mw')) return;
  var num = function (el) { return Math.max(0, +String(el.value).replace(/[^0-9.]/g, '') || 0); };
  var k = function (v) { return (Math.round(v * 10) / 10).toLocaleString('en-GB', { maximumFractionDigits: 1 }) + 'k'; };
  function size(el) { el.style.width = (Math.max(1, String(el.value).length) + 0.4) + 'ch'; }
  function calc() {
    var mw = num($('s-mw')), revK = num($('s-rev'));
    var upK = revK * UPLIFT;
    $('s-peer').textContent = 'EUR ' + k(revK + upK);
    $('s-up').textContent = 'EUR ' + k(upK);
    $('s-missed').textContent = 'EUR ' + (Math.round(upK * 1000 * mw / 100) * 100).toLocaleString('en-GB');
    ['s-mw', 's-rev'].forEach(function (id) { size($(id)); });
    dots(revK * 1000 * mw, upK * 1000 * mw);
  }
  // Abstract figure: one dot per fixed amount of yearly revenue; filled = delivered, outlined = missed.
  var svg = $('why-dots');
  function eur(v) { return 'EUR ' + (Math.round(v / 100) * 100).toLocaleString('en-GB'); }
  function dots(del, mis) {
    if (!svg) return;
    var total = del + mis, units = [1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6, 2e6, 5e6, 1e7, 2e7, 5e7];
    var unit = units[units.length - 1];
    for (var i = 0; i < units.length; i++) { if (total / units[i] <= 300) { unit = units[i]; break; } }
    var nD = Math.round(del / unit), nM = Math.max(0, Math.floor(total / unit) - nD);
    var rows = 10, n = nD + nM, cols = Math.max(12, Math.ceil(n / rows)), g = 20, r = 6.2;
    svg.setAttribute('viewBox', '0 0 ' + (cols * g) + ' ' + (rows * g));
    var out = '';
    for (var k = 0; k < n; k++) {
      var c = Math.floor(k / rows), y = k % rows, cx = c * g + g / 2, cy = y * g + g / 2;
      var d = (c * 0.06 + y * 0.015).toFixed(2);
      out += k < nD
        ? '<circle class="dd" cx="' + cx + '" cy="' + cy + '" r="' + r + '" style="transition-delay:' + d + 's"/>'
        : '<circle class="dm" cx="' + cx + '" cy="' + cy + '" r="' + (r - 0.8) + '" style="transition-delay:' + d + 's"/>';
    }
    svg.innerHTML = out;
    $('f-del').textContent = eur(del);
    $('f-mis').textContent = eur(mis);
    $('f-unit').textContent = '1 dot = ' + eur(unit) + ' a year';
  }
  ['s-mw', 's-rev'].forEach(function (id) { $(id).addEventListener('input', calc); });
  calc();
  // show the dots once, calmly, when the figure first scrolls into view; afterwards they stay still
  var fig = svg && svg.parentNode;
  if (fig && 'IntersectionObserver' in window) {
    fig.classList.add('pre');
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { fig.classList.remove('pre'); io.disconnect(); } }, { threshold: 0.3 });
    io.observe(fig);
  }
})();

// Info tooltips: tap to toggle on touch screens.
document.querySelectorAll('.info-i button').forEach(function (b) {
  b.addEventListener('click', function () { b.parentNode.classList.toggle('open'); });
});

// Navigation: Solutions menu (click/tap) and mobile menu.
(function () {
  document.querySelectorAll('.has-sub').forEach(function (li) {
    var b = li.querySelector('.sub-btn');
    b.addEventListener('click', function (e) { e.stopPropagation(); var o = li.classList.toggle('open'); b.setAttribute('aria-expanded', o); });
  });
  var mb = document.querySelector('.menu-btn'), mm = document.querySelector('.m-menu');
  if (mb && mm) mb.addEventListener('click', function (e) { e.stopPropagation(); mm.hidden = !mm.hidden; mb.setAttribute('aria-expanded', !mm.hidden); });
  document.addEventListener('click', function () {
    document.querySelectorAll('.has-sub.open').forEach(function (li) { li.classList.remove('open'); li.querySelector('.sub-btn').setAttribute('aria-expanded', false); });
    if (mm && !mm.hidden) { mm.hidden = true; mb.setAttribute('aria-expanded', false); }
  });
  document.querySelectorAll('.sub a, .m-menu a').forEach(function (a) { a.addEventListener('click', function () { if (mm) mm.hidden = true; }); });
})();

// Keep the menu bar visible once the page scrolls past it.
(function () {
  var nav = document.querySelector('header.nav');
  if (!nav) return;
  var shell = nav.closest('.hero-shell'), h = 0, fixed = false;
  function onScroll() {
    var should = window.scrollY > (nav.offsetTop + nav.offsetHeight);
    if (should === fixed) return;
    if (should) { h = nav.offsetHeight; if (shell) shell.style.paddingTop = h + 'px'; }
    else if (shell) shell.style.paddingTop = '';
    document.body.classList.toggle('nav-fixed', should);
    fixed = should;
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
