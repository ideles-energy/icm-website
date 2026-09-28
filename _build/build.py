"""Builds the icm.energy pages (EN + NL) from one template.

Run from the repo root:  python3 _build/build.py
Edit texts in the T dictionary below, then rebuild. Methodology is edited directly in methodology/index.html.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATTERIES = open(os.path.join(ROOT, '_build', 'batteries.html'), encoding='utf-8').read()
EMAIL = 'ideles@icm.energy'
LINKEDIN = 'https://www.linkedin.com/in/idel%C3%A8s-kaandorp/'

T = {
 'en': dict(
  lang='en', base='/', other='/nl/', other_label='NL', other_lang='nl', other_name='Nederlands',
  title="BESS Benchmark – understand the true value of your battery | The ICM",
  desc="See how your battery compares, BESS-to-BESS, with comparable batteries in the Netherlands – and find an alternative optimizer via the ICM.",
  og_title="Understand and secure the true value of your BESS asset",
  skip='Skip to content', nav_how='How it works', nav_faq='FAQ', nav_about='About', talk='Talk to us', menu='Main',
  eyebrow='BESS Benchmark · Netherlands',
  h1_a='Understand and secure', h1_b='the true value of your asset',
  lead='For owners with a nagging sense their BESS assets could earn more. See how your assets compare, BESS-to-BESS, and find an alternative optimizer via the ICM.',
  book='Book an intake →', how_link='How it works →',
  chart_title='Project score: 87% of the peer benchmark', chart_sub='EUR per MW per year, by month · gross revenue',
  chart_aria="Illustrative chart: a project's monthly revenue per MW compared with the peer benchmark",
  months=['Oct','Dec','Feb','Apr','Jun','Aug'], chart_you='Your project', chart_peer='Peer benchmark (≥ 5 assets, ≥ 3 organisations)',
  chart_note='Illustrative example with fictional data.',
  why_eyebrow='Why it matters', why_h='Same battery, same set-up, vastly different results',
  why_p='Independent information on BESS performance is missing. You could be leaving 30,000 to 70,000 euro per MW per year on the table. Without a BESS benchmark, there is no way of knowing.',
  which='Which one is yours?',
  how_eyebrow='How it works', how_h='Our membership model',
  rules=[
   ('Registration', 'We ask new members to share 6 months of BESS performance data and stay a member for at least 3 months. After that, membership can be cancelled monthly.'),
   ('Contribution', 'Members pay 0.5% of what their battery earned that month. At €15,000 per MW, that is €75 per MW. After referring 5 members, the contribution drops to 0.1% for 6 months.'),
   ('Give-to-get', 'You see the benchmark only for the months you contributed to. The same principle applies to installers, advisers and financiers who want access.'),
   ('Strictly anonymous', 'A benchmark is shown only for groups of at least 5 assets from at least 3 organisations. We never publish results per optimizer.'),
  ],
  faq_link='Read the FAQ →',
  real_eyebrow='Real data, not a model', real_h='Why real revenues beat a simulated index',
  idx_h='A simulated revenue index', idx=['Models a theoretical battery with fixed assumptions','Assumes a full grid connection and no downtime','Cannot tell you how your optimizer performs'],
  ours_h='The BESS Benchmark', ours=["Realised revenues from optimizers' credit invoices",'Anticipates restrictions such as CSC terms, TDTR limits and downtime','Compares your battery with batteries set up like yours'],
  about_eyebrow='About the ICM', about_h='Why an Independent Capacity Market matters',
  about_p='We are not owners. We are not optimizers. Nor will we ever be. We are an energy tech company, serving those who add capacity to the grid, but are in the dark on the potential of their assets. We compare BESS-to-BESS, introduce owners to optimizers and oversee the switch, so your battery keeps earning.',
  open_now='Open now', waitlist='Join the waitlist',
  p1=('BESS Benchmark','Compare what your battery earns per MW with comparable batteries. Give-to-get, anonymised, independent.'),
  p2=('BESS Broker','Outsource the search for a trusted optimizer. One form, a standardised process and terms banks appreciate.'),
  p3=('BESS Integration','Embed a new project into the portfolio. Our API platform derisks a switch by connecting optimizers with local infra.'),
  contact_eyebrow='Talk to us', contact_h='Book a 45-minute intake', contact_p='Tell us a little about your batteries and we will plan the intake together.',
  prefer='Prefer email?', subject='BESS Benchmark intake request',
  f_name='Name', f_company='Company', f_email='Email', f_mw='Portfolio size (MW, approximately)',
  f_msg='Tell us a little bit about your context and objectives', f_ph='E.g., asset of 3-30 MW, trading revenues below expectations',
  f_submit='Request an intake →', f_fine='We use your details only to contact you about the ICM.', f_ok='Thank you – we will be in touch.',
  foot_tag='The Independent Capacity Market (“the ICM”) brings clarity, trusted partners and continuity to those adding capacity to the grid.',
  founded='Independent Capacity Market B.V., Amsterdam. Founded by', foot_bench='BESS Benchmark', methodology='Methodology', contact='Contact',
  terms='Terms & Conditions', privacy='Privacy statement', disclaimer='Benchmark figures are outcome data as reported by optimizers, not advice.',
  faq_title='Frequently asked questions – BESS Benchmark | The ICM', faq_desc='Answers to common questions about the BESS Benchmark: data, costs, privacy and who can join.',
  faq_h='Frequently asked questions', faq_lead='Short answers about the BESS Benchmark. Missing something? Ask us in the intake.', faq_more='Still have a question?',
  faqs=[
   ('What data do I share?', 'Your monthly revenue per battery, as shown on your optimizer\'s credit invoice. Plus the optimizer fee and any hours the battery was down. To start, we ask for the last 6 months.'),
   ('Do you need my trading strategy or prices?', 'No. We only use the result: what the battery earned. Never bids, prices or trading strategies.'),
   ('Am I allowed to share this under my optimizer contract?', 'Usually yes. If your contract limits sharing, you and your optimizer sign a short mandate. Your optimizer then sends the figures to us directly.'),
   ('Who sees my data?', 'Only you see your own figures. Other members see averages of at least 5 batteries from at least 3 companies. We never show results per optimizer.'),
   ('Which batteries can join?', 'Batteries in the Netherlands on a merchant contract. We focus on 3 to 30 MW and decide per project in the intake.'),
   ('What does it cost?', '0.5% of what your battery earned that month, excluding VAT. The 6 months you share at the start are free. So is a month with negative revenue.'),
   ('How long do I commit?', 'At least 3 months. After that you can cancel every month.'),
   ('Can I show the results to my bank?', 'Yes. You can print a report with your own figures and the benchmark. It never contains data of other companies.'),
   ('How do you calculate the benchmark?', 'We add up the revenue of all comparable batteries and divide it by their MW and the hours they were available. The result is shown in euro per MW per year. All rules are in the <a href="/methodology/">methodology</a>.'),
  ],
  terms_title='Terms & Conditions | The ICM', terms_h='Terms & Conditions',
  terms_body='<p>The Terms &amp; Conditions of the BESS Benchmark are shared with every prospective member before signing, together with the methodology.</p><p>Would you like to read them first? Email <a href="mailto:ideles@icm.energy">ideles@icm.energy</a> and we will send you the current version.</p>',
  privacy_title='Privacy statement | The ICM', privacy_h='Privacy statement',
 ),
 'nl': dict(
  lang='nl', base='/nl/', other='/', other_label='EN', other_lang='en', other_name='English',
  title="BESS Benchmark – ken de echte waarde van je batterij | de ICM",
  desc="Zie hoe jouw batterij presteert naast vergelijkbare batterijen in Nederland, BESS-to-BESS – en vind via de ICM een alternatieve optimizer.",
  og_title="Ken en borg de echte waarde van je BESS",
  skip='Naar de inhoud', nav_how='Zo werkt het', nav_faq='Vragen', nav_about='Over de ICM', talk='Neem contact op', menu='Hoofdmenu',
  eyebrow='BESS Benchmark · Nederland',
  h1_a='Ken en borg', h1_b='de echte waarde van je batterij',
  lead='Voor eigenaren die het knagende gevoel hebben dat hun batterijen meer kunnen verdienen. Zie hoe je assets presteren, BESS-to-BESS, en vind via de ICM een alternatieve optimizer.',
  book='Plan een intake →', how_link='Zo werkt het →',
  chart_title='Projectscore: 87% van de benchmark', chart_sub='EUR per MW per jaar, per maand · bruto-opbrengst',
  chart_aria='Illustratieve grafiek: maandelijkse opbrengst per MW van een project naast de benchmark',
  months=['okt','dec','feb','apr','jun','aug'], chart_you='Jouw project', chart_peer='Benchmark (≥ 5 assets, ≥ 3 organisaties)',
  chart_note='Illustratief voorbeeld met fictieve data.',
  why_eyebrow='Waarom het ertoe doet', why_h='Zelfde batterij, zelfde opzet, totaal andere resultaten',
  why_p='Onafhankelijke informatie over hoe batterijen presteren, ontbreekt. Mogelijk laat je 30.000 tot 70.000 euro per MW per jaar liggen. Zonder BESS-benchmark is dat niet te weten.',
  which='Welke is de jouwe?',
  how_eyebrow='Zo werkt het', how_h='Ons lidmaatschapsmodel',
  rules=[
   ('Inschrijving', 'We vragen nieuwe leden om 6 maanden aan prestatiedata van hun batterijen te delen en ten minste 3 maanden lid te blijven. Daarna is het lidmaatschap maandelijks opzegbaar.'),
   ('Contributie', 'Leden betalen 0,5% van wat hun batterij die maand verdiende. Bij €15.000 per MW is dat €75 per MW. Na het aandragen van 5 leden daalt de contributie 6 maanden naar 0,1%.'),
   ('Give-to-get', 'Je ziet de benchmark alleen voor de maanden waaraan je hebt bijgedragen. Dat geldt ook voor installateurs, adviseurs en financiers die toegang willen.'),
   ('Strikt anoniem', 'Een benchmark wordt alleen getoond voor groepen van ten minste 5 assets van ten minste 3 organisaties. We publiceren nooit resultaten per optimizer.'),
  ],
  faq_link='Lees de veelgestelde vragen →',
  real_eyebrow='Echte data, geen model', real_h='Waarom echte opbrengsten meer zeggen dan een gesimuleerde index',
  idx_h='Een gesimuleerde opbrengstindex', idx=['Rekent met een theoretische batterij en vaste aannames','Gaat uit van een volledige netaansluiting en geen stilstand','Zegt niets over hoe jouw optimizer presteert'],
  ours_h='De BESS Benchmark', ours=['Gerealiseerde opbrengsten uit creditfacturen van optimizers','Houdt rekening met beperkingen zoals CSC-voorwaarden, TDTR-limieten en stilstand','Vergelijkt jouw batterij met batterijen in een vergelijkbare opzet'],
  about_eyebrow='Over de ICM', about_h='Waarom een Independent Capacity Market ertoe doet',
  about_p='We zijn geen eigenaar. We zijn geen optimizer. En dat worden we ook nooit. We zijn een energietechbedrijf voor wie capaciteit toevoegt aan het net, maar in het duister tast over wat hun assets kunnen opbrengen. We vergelijken BESS-to-BESS, brengen eigenaren in contact met optimizers en begeleiden de overstap, zodat je batterij blijft verdienen.',
  open_now='Nu open', waitlist='Op de wachtlijst',
  p1=('BESS Benchmark','Vergelijk wat je batterij per MW verdient met vergelijkbare batterijen. Give-to-get, anoniem, onafhankelijk.'),
  p2=('BESS Broker','Besteed de zoektocht naar een betrouwbare optimizer uit. Eén formulier, een gestandaardiseerd proces en voorwaarden die banken waarderen.'),
  p3=('BESS Integration','Neem een nieuw project op in de portefeuille. Ons API-platform maakt een overstap veiliger door optimizers te verbinden met de lokale infrastructuur.'),
  contact_eyebrow='Neem contact op', contact_h='Plan een intake van 45 minuten', contact_p='Vertel ons kort over je batterijen, dan plannen we samen de intake.',
  prefer='Liever mailen?', subject='BESS Benchmark intakeverzoek',
  f_name='Naam', f_company='Bedrijf', f_email='E-mail', f_mw='Omvang portefeuille (MW, ongeveer)',
  f_msg='Vertel ons kort over je situatie en doelen', f_ph='Bijv. asset van 3-30 MW, handelsopbrengsten onder verwachting',
  f_submit='Vraag een intake aan →', f_fine='We gebruiken je gegevens alleen om contact met je op te nemen over de ICM.', f_ok='Dank je – we nemen contact met je op.',
  foot_tag='The Independent Capacity Market (“de ICM”) brengt duidelijkheid, betrouwbare partners en continuïteit voor wie capaciteit toevoegt aan het net.',
  founded='Independent Capacity Market B.V., Amsterdam. Opgericht door', foot_bench='BESS Benchmark', methodology='Methodologie (Engels)', contact='Contact',
  terms='Algemene voorwaarden', privacy='Privacyverklaring', disclaimer='Benchmarkcijfers zijn uitkomstdata zoals gerapporteerd door optimizers, geen advies.',
  faq_title='Veelgestelde vragen – BESS Benchmark | de ICM', faq_desc='Antwoorden op veelgestelde vragen over de BESS Benchmark: data, kosten, privacy en wie mee kan doen.',
  faq_h='Veelgestelde vragen', faq_lead='Korte antwoorden over de BESS Benchmark. Mis je iets? Vraag het ons in de intake.', faq_more='Nog een vraag?',
  faqs=[
   ('Welke data deel ik?', 'De maandelijkse opbrengst per batterij, zoals op de creditfactuur van je optimizer. Plus de optimizer-fee en de uren dat de batterij stil stond. Bij de start vragen we de laatste 6 maanden.'),
   ('Hebben jullie mijn handelsstrategie of prijzen nodig?', 'Nee. We gebruiken alleen het resultaat: wat de batterij verdiende. Nooit biedingen, prijzen of handelsstrategieën.'),
   ('Mag ik dit delen onder mijn optimizer-contract?', 'Meestal wel. Beperkt je contract het delen, dan tekenen jij en je optimizer een korte machtiging. Je optimizer stuurt de cijfers dan rechtstreeks naar ons.'),
   ('Wie ziet mijn data?', 'Alleen jij ziet je eigen cijfers. Andere leden zien gemiddelden van ten minste 5 batterijen van ten minste 3 bedrijven. We tonen nooit resultaten per optimizer.'),
   ('Welke batterijen kunnen meedoen?', 'Batterijen in Nederland met een merchant-contract. We richten ons op 3 tot 30 MW en beslissen per project in de intake.'),
   ('Wat kost het?', '0,5% van wat je batterij die maand verdiende, exclusief btw. De 6 maanden die je bij de start deelt zijn gratis. Een maand met negatieve opbrengst ook.'),
   ('Hoe lang zit ik eraan vast?', 'Ten minste 3 maanden. Daarna kun je elke maand opzeggen.'),
   ('Mag ik de resultaten aan mijn bank laten zien?', 'Ja. Je kunt een rapport printen met je eigen cijfers en de benchmark. Daarin staan nooit gegevens van andere bedrijven.'),
   ('Hoe berekenen jullie de benchmark?', 'We tellen de opbrengst van alle vergelijkbare batterijen op en delen die door hun MW en de uren dat ze beschikbaar waren. De uitkomst staat in euro per MW per jaar. Alle regels staan in de <a href="/methodology/" hreflang="en">methodologie</a> (Engels).'),
  ],
  terms_title='Algemene voorwaarden | de ICM', terms_h='Algemene voorwaarden',
  terms_body='<p>De algemene voorwaarden (Terms &amp; Conditions) van de BESS Benchmark ontvangt elk aspirant-lid vóór het tekenen, samen met de methodologie.</p><p>Wil je ze eerst lezen? Mail naar <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>, dan sturen we je de actuele versie.</p>',
  privacy_title='Privacyverklaring | de ICM', privacy_h='Privacyverklaring',
 ),
}

PRIVACY = {
 'en': [
  ('Who we are', 'Independent Capacity Market B.V. (“the ICM”), Amsterdam, is responsible for the personal data described here. Contact: <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>.'),
  ('What we collect', 'When you use the contact form: your name, company, email address, portfolio size and message. When you visit the site: anonymous usage statistics through Google Analytics.'),
  ('Why', 'To answer your request and plan an intake, and to understand how the website is used. We do not sell your data or use it for other purposes.'),
  ('Who processes it for us', 'Formspree receives the contact form on our behalf. Google provides Google Analytics.'),
  ('How long we keep it', 'Contact details are kept as long as needed to follow up on your request, and at most two years after our last contact, unless you become a member.'),
  ('Your rights', 'You can ask to see, correct or delete your data, or object to its use, by emailing <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>. You can also file a complaint with the Dutch Data Protection Authority (Autoriteit Persoonsgegevens).'),
 ],
 'nl': [
  ('Wie we zijn', 'Independent Capacity Market B.V. (“de ICM”), Amsterdam, is verantwoordelijk voor de persoonsgegevens die hier worden beschreven. Contact: <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>.'),
  ('Wat we verzamelen', 'Via het contactformulier: je naam, bedrijf, e-mailadres, omvang van je portefeuille en je bericht. Bij een bezoek aan de site: anonieme gebruiksstatistieken via Google Analytics.'),
  ('Waarom', 'Om je verzoek te beantwoorden en een intake te plannen, en om te begrijpen hoe de website wordt gebruikt. We verkopen je gegevens niet en gebruiken ze niet voor andere doelen.'),
  ('Wie ze voor ons verwerkt', 'Formspree ontvangt het contactformulier namens ons. Google levert Google Analytics.'),
  ('Hoe lang we ze bewaren', 'Contactgegevens bewaren we zolang nodig is om je verzoek op te volgen, en maximaal twee jaar na ons laatste contact, tenzij je lid wordt.'),
  ('Jouw rechten', 'Je kunt je gegevens inzien, laten corrigeren of verwijderen, of bezwaar maken tegen het gebruik, via <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>. Je kunt ook een klacht indienen bij de Autoriteit Persoonsgegevens.'),
 ],
}

GA = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-8RMBG4V4VG"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-8RMBG4V4VG');</script>'''

def head(t, title, desc, path, alt_path=None, jsonld=None, og_title=None):
    alt = ''
    if alt_path:
        en, nl = (path, alt_path) if t['lang'] == 'en' else (alt_path, path)
        alt = (f'<link rel="alternate" hreflang="en" href="https://icm.energy{en}">\n'
               f'<link rel="alternate" hreflang="nl" href="https://icm.energy{nl}">\n'
               f'<link rel="alternate" hreflang="x-default" href="https://icm.energy{en}">\n')
    ld = f'<script type="application/ld+json">\n{json.dumps(jsonld, ensure_ascii=False, indent=1)}\n</script>\n' if jsonld else ''
    return f'''<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://icm.energy{path}">
{alt}<meta property="og:type" content="website">
<meta property="og:url" content="https://icm.energy{path}">
<meta property="og:title" content="{og_title or title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://icm.energy/assets/og-image.png">
<meta property="og:site_name" content="The Independent Capacity Market">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
{GA}
{ld}</head>
<body>
<a class="sr-only" href="#main">{t['skip']}</a>
'''

def nav(t, other_href):
    b = t['base']
    return f'''    <header class="nav">
      <a class="logo" href="{b}" aria-label="The Independent Capacity Market, home"><span class="logo-text">The Independent<br>Capacity Market</span></a>
      <nav aria-label="{t['menu']}">
        <ul class="nav-links">
          <li class="hide-sm"><a href="{b}#how">{t['nav_how']}</a></li>
          <li class="hide-sm"><a href="{b}faq/">{t['nav_faq']}</a></li>
          <li class="hide-sm"><a href="{b}#about">{t['nav_about']}</a></li>
          <li><a class="lang" href="{other_href}" hreflang="{t['other_lang']}" lang="{t['other_lang']}">{t['other_label']}</a></li>
          <li><a class="btn btn-lilac" href="{b}#contact">{t['talk']}</a></li>
        </ul>
      </nav>
    </header>
'''

def footer(t, other_href):
    b = t['base']
    return f'''<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <h3>The Independent Capacity Market</h3>
        <p class="foot-tag">{t['foot_tag']}</p>
        <p>{t['founded']} <a href="{LINKEDIN}" rel="noopener">Idelès Kaandorp</a>.</p>
      </div>
      <div>
        <h3>{t['foot_bench']}</h3>
        <ul>
          <li><a href="{b}#how">{t['nav_how']}</a></li>
          <li><a href="{b}faq/">{t['nav_faq']}</a></li>
          <li><a href="/methodology/">{t['methodology']}</a></li>
        </ul>
      </div>
      <div>
        <h3>{t['contact']}</h3>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{other_href}" hreflang="{t['other_lang']}" lang="{t['other_lang']}">{t['other_name']}</a></li>
        </ul>
      </div>
    </div>
    <p class="legal"><span>© 2026 Independent Capacity Market B.V.</span><span><a href="{b}terms/">{t['terms']}</a></span><span><a href="{b}privacy/">{t['privacy']}</a></span><span>{t['disclaimer']}</span></p>
  </div>
</footer>
'''

def chart(t):
    m = t['months']
    return f'''      <figure class="chart-card" aria-labelledby="chart-title">
        <h2 id="chart-title">{t['chart_title']}</h2>
        <p class="sub">{t['chart_sub']}</p>
        <svg viewBox="0 0 520 260" role="img" aria-label="{t['chart_aria']}">
          <g stroke="#DDE6E8" stroke-width="1"><line x1="44" x2="508" y1="30" y2="30"/><line x1="44" x2="508" y1="90" y2="90"/><line x1="44" x2="508" y1="150" y2="150"/><line x1="44" x2="508" y1="210" y2="210"/></g>
          <g fill="#4E6167" font-size="11" text-anchor="end"><text x="38" y="34">300k</text><text x="38" y="94">200k</text><text x="38" y="154">100k</text><text x="38" y="214">0</text></g>
          <g fill="#274A50"><rect x="54" y="98" width="22" height="112" rx="3"/><rect x="92" y="110" width="22" height="100" rx="3"/><rect x="130" y="86" width="22" height="124" rx="3"/><rect x="168" y="104" width="22" height="106" rx="3"/><rect x="206" y="128" width="22" height="82" rx="3"/><rect x="244" y="80" width="22" height="130" rx="3"/><rect x="282" y="92" width="22" height="118" rx="3"/><rect x="320" y="74" width="22" height="136" rx="3"/><rect x="358" y="118" width="22" height="92" rx="3"/><rect x="396" y="100" width="22" height="110" rx="3"/><rect x="434" y="88" width="22" height="122" rx="3"/><rect x="472" y="96" width="22" height="114" rx="3"/></g>
          <polyline fill="none" stroke="#D392EB" stroke-width="3" stroke-linejoin="round" points="65,86 103,92 141,80 179,84 217,90 255,70 293,78 331,62 369,82 407,86 445,74 483,80"/>
          <g fill="#4E6167" font-size="11" text-anchor="middle"><text x="65" y="230">{m[0]}</text><text x="141" y="230">{m[1]}</text><text x="217" y="230">{m[2]}</text><text x="293" y="230">{m[3]}</text><text x="369" y="230">{m[4]}</text><text x="445" y="230">{m[5]}</text></g>
          <g font-size="12"><rect x="54" y="244" width="12" height="12" rx="2" fill="#274A50"/><text x="72" y="254" fill="#16242A">{t['chart_you']}</text><line x1="170" x2="190" y1="250" y2="250" stroke="#D392EB" stroke-width="3"/><text x="196" y="254" fill="#16242A">{t['chart_peer']}</text></g>
        </svg>
        <p class="chart-note">{t['chart_note']}</p>
      </figure>
'''

def home(t):
    b = t['base']
    other = t['other']
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": "https://icm.energy/#org", "name": "Independent Capacity Market B.V.", "alternateName": "The ICM",
         "url": "https://icm.energy/", "email": EMAIL, "address": {"@type": "PostalAddress", "addressLocality": "Amsterdam", "addressCountry": "NL"},
         "founder": {"@type": "Person", "name": "Idelès Kaandorp", "sameAs": LINKEDIN}},
        {"@type": "Service", "name": "BESS Benchmark", "provider": {"@id": "https://icm.energy/#org"}, "areaServed": "NL",
         "serviceType": "Battery energy storage revenue benchmark", "description": t['desc']}]}
    rules = '\n'.join(f'      <div class="rule"><h3>{h}</h3><p>{p}</p></div>' for h, p in t['rules'])
    idx = ''.join(f'<li>{x}</li>' for x in t['idx']); ours = ''.join(f'<li>{x}</li>' for x in t['ours'])
    return head(t, t['title'], t['desc'], b, other, ld, t['og_title']) + f'''
<div class="hero-shell">
  <div class="wrap">
{nav(t, other)}
    <div class="hero" id="main">
      <div>
        <span class="eyebrow">{t['eyebrow']}</span>
        <h1>{t['h1_a']} <span>{t['h1_b']}</span></h1>
        <p class="lead">{t['lead']}</p>
        <div class="hero-ctas">
          <a class="btn btn-lilac" href="#contact">{t['book']}</a>
          <a class="btn btn-ghost" href="#how">{t['how_link']}</a>
        </div>
      </div>
{chart(t)}    </div>
  </div>
</div>

<section class="dark" style="border-top:1px solid rgba(255,255,255,.08)">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">{t['why_eyebrow']}</span>
      <h2>{t['why_h']}</h2>
      <p>{t['why_p']}</p>
    </div>
    <div class="batteries">
      {BATTERIES}
    </div>
    <p class="which">{t['which']}</p>
    <div class="cta-row"><a class="btn btn-lilac" href="#contact">{t['book']}</a></div>
  </div>
</section>

<section class="rules-wrap" id="how">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{t['how_eyebrow']}</span>
      <h2>{t['how_h']}</h2>
    </div>
    <div class="rules">
{rules}
    </div>
    <div class="cta-row" style="justify-content:flex-start;margin-top:36px">
      <a class="btn btn-lilac" href="#contact">{t['book']}</a>
      <a class="btn btn-outline teal" href="{b}faq/">{t['faq_link']}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{t['real_eyebrow']}</span>
      <h2>{t['real_h']}</h2>
    </div>
    <div class="compare">
      <div class="index"><h3>{t['idx_h']}</h3><ul>{idx}</ul></div>
      <div class="ours"><h3>{t['ours_h']}</h3><ul>{ours}</ul></div>
    </div>
  </div>
</section>

<section class="more" id="about">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{t['about_eyebrow']}</span>
      <h2>{t['about_h']}</h2>
      <p>{t['about_p']}</p>
    </div>
    <div class="more-grid">
      <article><span class="tag">{t['open_now']}</span><h3>{t['p1'][0]}</h3><p>{t['p1'][1]}</p></article>
      <article><a class="tag soft" href="#contact">{t['waitlist']}</a><h3>{t['p2'][0]}</h3><p>{t['p2'][1]}</p></article>
      <article><a class="tag soft" href="#contact">{t['waitlist']}</a><h3>{t['p3'][0]}</h3><p>{t['p3'][1]}</p></article>
    </div>
    <div class="cta-row"><a class="btn btn-lilac" href="#contact">{t['book']}</a></div>
  </div>
</section>

<section id="contact">
  <div class="wrap contact">
    <div class="intro">
      <span class="eyebrow" style="color:var(--teal)">{t['contact_eyebrow']}</span>
      <h2>{t['contact_h']}</h2>
      <p>{t['contact_p']}</p>
      <p>{t['prefer']} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <form class="form" id="contact-form" action="https://formspree.io/f/mbdqdpql" method="POST">
      <input type="hidden" name="_subject" value="{t['subject']}">
      <input type="hidden" name="source" value="icm.energy ({t['lang'].upper()})">
      <div class="row">
        <label>{t['f_name']}<input name="name" autocomplete="name" required></label>
        <label>{t['f_company']}<input name="company" autocomplete="organization" required></label>
      </div>
      <div class="row">
        <label>{t['f_email']}<input type="email" name="email" autocomplete="email" required></label>
        <label>{t['f_mw']}<input name="portfolio_mw" inputmode="decimal"></label>
      </div>
      <label>{t['f_msg']}<textarea name="message" placeholder="{t['f_ph']}"></textarea></label>
      <button class="btn btn-lilac" type="submit">{t['f_submit']}</button>
      <p class="fine">{t['f_fine']}</p>
      <div class="form-ok" id="form-ok" role="status">{t['f_ok']}</div>
    </form>
  </div>
</section>

{footer(t, other)}
<script src="/main.js" defer></script>
</body>
</html>
'''

def simple_page(t, path, other_path, title, desc, h1, lead, body, jsonld=None):
    return head(t, title, desc, path, other_path, jsonld) + f'''
<div class="hero-shell">
  <div class="wrap">
{nav(t, other_path)}
    <div class="page-hero" id="main">
      <span class="eyebrow">{t['eyebrow']}</span>
      <h1>{h1}</h1>
      {f'<p>{lead}</p>' if lead else ''}
    </div>
  </div>
</div>
<main class="page-body">
  <div class="wrap">
{body}
  </div>
</main>
{footer(t, other_path)}
</body>
</html>
'''

def faq(t):
    items = '\n'.join(f'      <details><summary>{q}</summary><p>{a}</p></details>' for q, a in t['faqs'])
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in t['faqs']]}
    body = f'''    <div class="faq">
{items}
    </div>
    <div class="faq-cta"><p>{t['faq_more']}</p><a class="btn btn-lilac" href="{t['base']}#contact">{t['book']}</a></div>'''
    return simple_page(t, t['base'] + 'faq/', t['other'] + 'faq/', t['faq_title'], t['faq_desc'], t['faq_h'], t['faq_lead'], body, ld)

def terms(t):
    body = f'    <div class="prose">{t["terms_body"]}</div>'
    return simple_page(t, t['base'] + 'terms/', t['other'] + 'terms/', t['terms_title'], t['terms_title'], t['terms_h'], '', body)

def privacy(t):
    secs = ''.join(f'<h2>{h}</h2><p>{p}</p>' for h, p in PRIVACY[t['lang']])
    body = f'    <div class="prose">{secs}<p style="color:var(--muted);font-size:14px">28-09-2026</p></div>'
    return simple_page(t, t['base'] + 'privacy/', t['other'] + 'privacy/', t['privacy_title'], t['privacy_title'], t['privacy_h'], '', body)

def write(rel, html):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(html)

for lang, t in T.items():
    pre = '' if lang == 'en' else 'nl/'
    write(pre + 'index.html', home(t))
    write(pre + 'faq/index.html', faq(t))
    write(pre + 'terms/index.html', terms(t))
    write(pre + 'privacy/index.html', privacy(t))
print('built')

# Keep the methodology page's header and footer in sync with the rest of the site.
mp = os.path.join(ROOT, 'methodology', 'index.html')
m = open(mp, encoding='utf-8').read()
m = re.sub(r'    <header class="nav">.*?</header>\n', lambda _: nav(T['en'], '/nl/'), m, flags=re.S)
m = re.sub(r'<footer>.*?</footer>\n', lambda _: footer(T['en'], '/nl/'), m, flags=re.S)
open(mp, 'w', encoding='utf-8').write(m)
print('methodology synced')
