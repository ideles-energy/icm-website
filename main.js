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

// Missed-opportunity sentence (illustrative: a similar asset earned 30% more per MW).
(function () {
  var UPLIFT = 0.30;
  var $ = function (id) { return document.getElementById(id); };
  if (!$('s-mw')) return;
  var fmtK = function (v) { return (Math.round(v * 10) / 10).toLocaleString('en-GB', { maximumFractionDigits: 1 }) + 'k'; };
  function size(el) { el.style.width = (Math.max(2, String(el.value).length) + 1.6) + 'ch'; }
  function calc() {
    var mw = Math.max(0, +$('s-mw').value || 0), revK = Math.max(0, +$('s-rev').value || 0), months = Math.max(0, +$('s-m').value || 0);
    var peerK = revK * (1 + UPLIFT);
    var missed = (peerK - revK) * 1000 * mw * months / 12;
    $('s-missed').textContent = 'EUR ' + (Math.round(missed / 100) * 100).toLocaleString('en-GB');
    $('s-peer').textContent = 'EUR ' + fmtK(peerK);
    ['s-mw', 's-rev', 's-m'].forEach(function (id) { size($(id)); });
  }
  ['s-mw', 's-rev', 's-m'].forEach(function (id) { $(id).addEventListener('input', calc); });
  calc();
})();
