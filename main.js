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

// Missed-opportunity calculator (illustrative: comparable batteries earn 30% more per MW).
(function () {
  var UPLIFT = 0.30;
  var $ = function (id) { return document.getElementById(id); };
  if (!$('c-mw')) return;
  var pairs = [['c-mw', 'c-mw-n'], ['c-m', 'c-m-n'], ['c-r', 'c-r-n']];
  var eur = function (v) { return 'EUR ' + Math.round(v).toLocaleString('en-GB'); };
  var round = function (v, step) { return Math.round(v / step) * step; };
  function calc() {
    var mw = Math.max(0, +$('c-mw-n').value || 0);
    var months = Math.max(0, +$('c-m-n').value || 0);
    var you = Math.max(0, +$('c-r-n').value || 0);
    var bench = you * (1 + UPLIFT);
    var missedYear = (bench - you) * mw;
    var missed = missedYear * months / 12;
    $('c-you').textContent = eur(you);
    $('c-bench').textContent = eur(bench);
    $('c-missed').textContent = eur(round(missed, 100));
    $('c-year').textContent = '≈ ' + eur(round(missedYear, 100)) + ' per year for ' + mw + ' MW';
    $('c-math').textContent = eur(bench - you) + ' per MW per year × ' + mw + ' MW × ' + months + '/12 months';
    $('c-k').textContent = 'Missed opportunity over ' + months + (months === 1 ? ' month' : ' months');
    var max = bench || 1;
    $('c-bar-you').style.width = (you / max * 100) + '%';
    $('c-bar-bench').style.width = (you / max * 100) + '%';
    $('c-bar-gap').style.left = (you / max * 100) + '%';
    $('c-bar-gap').style.width = ((bench - you) / max * 100) + '%';
  }
  pairs.forEach(function (p) {
    var r = $(p[0]), n = $(p[1]);
    r.addEventListener('input', function () { n.value = r.value; calc(); });
    n.addEventListener('input', function () { r.value = n.value; calc(); });
  });
  calc();
})();
