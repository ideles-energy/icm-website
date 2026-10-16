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

// Missed-opportunity calculator (illustrative: a similar asset can deliver 30% more revenue per MW). Works per .why-calc block.
document.querySelectorAll('.why-calc').forEach(function (root) {
  var UPLIFT = 0.30;
  var Q = function (c) { return root.querySelectorAll('.' + c); };
  var mwEl = Q('js-mw')[0], revEl = Q('js-rev')[0];
  if (!mwEl || !revEl) return;
  var set = function (c, t) { Q(c).forEach(function (e) { e.textContent = t; }); };
  var num = function (el) { return Math.max(0, +String(el.value).replace(/[^0-9.]/g, '') || 0); };
  var k = function (v) { return (Math.round(v * 10) / 10).toLocaleString('en-GB', { maximumFractionDigits: 1 }) + 'k'; };
  function size(el) { if (el.classList.contains('fit')) el.style.width = (Math.max(1, String(el.value).length) + 0.4) + 'ch'; }
  var svg = Q('js-dots')[0];
  function eur(v) { return 'EUR ' + (Math.round(v / 100) * 100).toLocaleString('en-GB'); }
  function dots(del, mis) {
    if (!svg) return;
    var total = del + mis, units = [1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6, 2e6, 5e6, 1e7, 2e7, 5e7];
    var unit = units[units.length - 1];
    for (var i = 0; i < units.length; i++) { if (total / units[i] <= 300) { unit = units[i]; break; } }
    var nD = Math.round(del / unit), nM = Math.max(0, Math.floor(total / unit) - nD);
    var rows = +svg.getAttribute('data-rows') || 10, n = nD + nM, cols = Math.max(12, Math.ceil(n / rows)), g = 20, r = 6.2;
    svg.setAttribute('viewBox', '0 0 ' + (cols * g) + ' ' + (rows * g));
    var out = '';
    for (var j = 0; j < n; j++) {
      var c = Math.floor(j / rows), y = j % rows, cx = c * g + g / 2, cy = y * g + g / 2;
      var d = (c * 0.06 + y * 0.015).toFixed(2);
      out += j < nD
        ? '<circle class="dd" cx="' + cx + '" cy="' + cy + '" r="' + r + '" style="transition-delay:' + d + 's"/>'
        : '<circle class="dm" cx="' + cx + '" cy="' + cy + '" r="' + (r - 0.8) + '" style="transition-delay:' + d + 's"/>';
    }
    svg.innerHTML = out;
    set('js-del', eur(del)); set('js-mis', eur(mis)); set('js-unit', '1 dot = ' + eur(unit) + ' a year');
  }
  function calc() {
    var mw = num(mwEl), revK = num(revEl), upK = revK * UPLIFT;
    set('js-should', 'EUR ' + k(revK + upK));
    set('js-gap', 'EUR ' + k(upK));
    set('js-missed', 'EUR ' + (Math.round(upK * 1000 * mw / 100) * 100).toLocaleString('en-GB'));
    set('js-missedk', 'EUR ' + Math.round(upK * mw).toLocaleString('en-GB') + 'k');
    [mwEl, revEl].forEach(size);
    dots(revK * 1000 * mw, upK * 1000 * mw);
  }
  [mwEl, revEl].forEach(function (el) { el.addEventListener('input', calc); });
  calc();
  var fig = svg && svg.parentNode;
  if (fig && 'IntersectionObserver' in window) {
    fig.classList.add('pre');
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { fig.classList.remove('pre'); io.disconnect(); } }, { threshold: 0.3 });
    io.observe(fig);
  }
});

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
  function lum(el) {
    while (el) {
      var c = getComputedStyle(el).backgroundColor.match(/[\d.]+/g);
      if (c && (c.length < 4 || +c[3] > 0.5)) return (0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]) / 255;
      el = el.parentElement;
    }
    return 1;
  }
  function tone() {
    var y = nav.offsetHeight + 2, secs = document.querySelectorAll('.hero-shell, body > section, body > main > section, body > div'), light = false;
    for (var i = 0; i < secs.length; i++) {
      var r = secs[i].getBoundingClientRect();
      if (r.top <= y && r.bottom > y && secs[i] !== nav) { light = lum(secs[i]) > 0.6; }
    }
    document.body.classList.toggle('nav-light', light);
  }
  function onScroll() {
    var should = window.scrollY > (nav.offsetTop + nav.offsetHeight);
    if (should === fixed) { if (fixed) tone(); return; }
    if (should) { h = nav.offsetHeight; if (shell) shell.style.paddingTop = h + 'px'; }
    else if (shell) shell.style.paddingTop = '';
    document.body.classList.toggle('nav-fixed', should);
    fixed = should;
    if (should) tone(); else document.body.classList.remove('nav-light');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

/* Talk to us and Solutions: always start at the top (the Fillout embed can pull the page down) */
(function () {
  if (location.hash) return;
  var moved = false;
  function mark() { moved = true; }
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (e) { window.addEventListener(e, mark, { passive: true, once: true }); });
  try { history.scrollRestoration = 'manual'; } catch (e) {}
  function top() { if (!moved && window.scrollY > 0) window.scrollTo(0, 0); }
  top(); window.addEventListener('load', top); window.addEventListener('message', top);
  var n = 0, iv = setInterval(function () { top(); if (++n > 50 || moved) clearInterval(iv); }, 120);
})();

/* Partner reward slider (Solutions) */
(function(){var w=document.querySelector('.js-partner');if(!w)return;var r=w.querySelector('.js-ps-range'),o=w.querySelector('.js-ps-mw'),p=w.querySelector('.js-ps-pay');
function u(){var v=+r.value;o.textContent=(v<1?Math.round(v*1000)+' kW':v+' MW');p.textContent='EUR '+(v*500).toString().replace(/\B(?=(\d{3})+(?!\d))/g,',');}
r.addEventListener('input',u);u();})();

/* Email gate before the Backtest product: work-email form (Fillout) in a pop-up */
(function(){
  var g=document.getElementById('gate'); if(!g) return;
  var go=g.querySelector('.js-gate-go'), loaded=false;
  function open(mode){g.hidden=false;document.body.style.overflow='hidden';
    if(!loaded){loaded=true;var s=document.createElement('script');s.src='https://server.fillout.com/embed/v1/';document.body.appendChild(s);}
    if(go)go.hidden=(mode==='start');}
  function close(){g.hidden=true;document.body.style.overflow='';}
  document.querySelectorAll('.js-gate-open').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();open(b.getAttribute('data-gate'));});});
  g.querySelector('.js-gate-close').addEventListener('click',close);
  g.addEventListener('click',function(e){if(e.target===g)close();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!g.hidden)close();});
  
})();

/* Work-email forms on Solutions: validate, then go on to the intake form */
(function(){
  var free=/@(gmail|googlemail|hotmail|outlook|live|yahoo|icloud|me|proton|protonmail|aol|gmx|msn)\./i;
  document.querySelectorAll('.gs-form').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var i=f.querySelector('input'),err=f.querySelector('.gate-err'),v=i.value.trim();
      if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)||free.test(v)){err.hidden=false;i.focus();return;}
      err.hidden=true;
      var ep=window.ICM_GATE_ENDPOINT;
      if(ep){try{navigator.sendBeacon(ep,new Blob([JSON.stringify({email:v,source:'solutions-get-started'})],{type:'application/json'}));}catch(x){}}
      location.href='/talk-to-us/?topic=start';
    });
  });
})();
