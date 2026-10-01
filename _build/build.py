"""Builds the icm.energy pages (EN + NL) from one template.

Run from the repo root:  python3 _build/build.py
Edit texts in the T dictionary below, then rebuild. Methodology is edited directly in methodology/index.html.
"""
import json, os, re, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANGS = ['en']  # add 'nl' once the Dutch texts are proofread
EMAIL = 'ideles@icm.energy'
LINKEDIN = 'https://www.linkedin.com/in/idel%C3%A8s-kaandorp/'

T = {
 'en': dict(
  lang='en', base='/', other='/nl/', other_label='NL', other_lang='nl', other_name='Nederlands',
  title="BESS Benchmark: understand the true value of a BESS asset | The ICM",
  desc="See how a battery compares, BESS-to-BESS, with comparable batteries in the Netherlands, and outsource the research for a trusted optimizer when there is more to earn.",
  og_title="Understand and secure the true value of a BESS asset",
  skip='Skip to content', nav_how='How it works', nav_faq='FAQ', nav_about='About', talk='Talk to us', menu='Main',
  eyebrow='BESS Benchmark',
  h1_a='Understand and secure', h1_b='the true value of a BESS asset',
  lead='For owners with a nagging sense their BESS could earn more. See how an asset compares, BESS-to-BESS, and outsource the research for a trusted optimizer when there is more to earn.',
  book='Talk to us', start='Get started', more='Learn more', how_link='How it works',
  chart_title='Project score: 87% of the peer benchmark', chart_sub='EUR per MW per year, by month · gross revenue',
  chart_aria="Illustrative chart: a project's monthly revenue per MW compared with the peer benchmark",
  months=['Oct','Dec','Feb','Apr','Jun','Aug'], chart_you='This project', chart_peer='Peer benchmark (≥ 5 assets, ≥ 3 organisations)',
  chart_note='Illustrative example with fictional data.',
  why_eyebrow='Why it matters', why_h='BESS assets deliver vastly different results',
  why_p='Independent information is missing as long as no one works together.',
  stats=['EUR 145k', 'EUR 185k', 'EUR 240k'], per='per MW per year', stats_note='Illustrative example: gross market revenues of three BESS assets.',
  learn='How it works',
  which='Which one is yours?',
  how_eyebrow='How it works', how_h='Become a member of <span class="nw">the BESS Benchmark</span>',
  rules=[
   ('Registration', 'New members submit 6 months of historical data and complete a 45-minute intake that collects the relevant project information. A membership lasts at least 3 months and can be cancelled every month after that.'),
   ('Participation', 'Members share their earnings every month, for instance by asking their optimizer to CC the ICM on its monthly performance report. The ICM anonymises the data and adds it to the BESS Benchmark.'),
   ('Contribution', 'Members pay a symbolic handling fee of 0.5% of what their BESS assets earned that month: EUR 75 for a project delivering EUR 15,000. After referring 5 members, the contribution drops to 0.1% for 6 months.'),
   ('Give-to-get', 'Members only see the BESS Benchmark for the months to which they contributed. If no data is shared for August, September and October, the BESS Benchmark stays blank for those months.'),
   ('Silent by design', 'The Dutch saying "geen bericht, goed bericht" applies here. The ICM reaches out to members whose projects earn below 80% of the BESS Benchmark. Otherwise, the ICM stays quiet.'),
   ('Proof of performance', 'The BESS Benchmark can serve as concrete input for (re)financing conversations, contract negotiations with optimizers and insurance/warranty claims.'),
  ],
  shot_alt='The BESS Benchmark app: project score, revenue per MW and the benchmark over the last 12 months (fictional example data)',
  story_note='Enter figures to adjust. Illustrative example.',
  calc_eyebrow='Calculator', calc_h='What is the missed opportunity?',
  calc_p='Enter the battery size and what it earns today, to see what it could have earned if it had matched comparable batteries.',
  calc_mw='Battery size', calc_months='Period', calc_months_unit='months', calc_rev='Current revenue',
  calc_assume='Assumption: comparable batteries earned 30% more per MW. Illustrative – the BESS Benchmark shows the real gap.',
  calc_you='This battery', calc_bench='Comparable batteries', calc_missed='Missed opportunity over 6 months', calc_cta='Find the real gap',
  demo_eyebrow='Open now', demo_h='The BESS Benchmark', demo_p='Clarity is our goal. Real, anonymised revenues, compared BESS-to-BESS.', demo_note='Fictional example data.',
  demo_btn='Try the demo', demo_title='BESS Benchmark interactive demo (fictional data)', demo_new='Open in a new tab',
  shot_cap='The BESS Benchmark is a dynamic view on the EUR per MW per year across the assets of all members. Fictional example data.',
  faq_link='Read the FAQ',
  real_eyebrow='Real data, not a model', real_h='Why real revenues beat a simulated index',
  idx_h='A simulated revenue index', idx=['Models a theoretical battery with fixed assumptions','Assumes a full grid connection and no downtime','Cannot show how an optimizer performs comparatively'],
  ours_h='The BESS Benchmark', ours=['Is based on realised revenues, as members received them from their optimizers','Anticipates restrictions such as CSC terms, TDTR limits and downtime','Compares a battery with batteries set up alike'],
  about_eyebrow='About the ICM', about_h='Why an Independent Capacity Market matters',
  about_p='We are not owners. We are not optimizers. Nor will we ever be.<br><br>We are an energy tech company. We compare BESS-to-BESS, introduce owners to optimizers and oversee the switch, so batteries keep earning.',
  roles='Open roles', careers='Careers',
  open_now='Open now', waitlist='Join the waitlist',
  p1=('BESS Benchmark',"Real, anonymised revenues, compared BESS-to-BESS. Become a member to see how an asset is doing."),
  p1b=('BESS Backtest','Understand the drivers of the capture rate. A deep dive into the full potential of complex, co-located set-ups.'),
  p2=('BESS Broker','Outsource the search for a trusted optimizer. One form, a standardised process and terms banks appreciate.'),
  p3=('BESS Bridge','Switch optimizers without going dark. Our API platform connects optimizers with local infra.'),
  contact_eyebrow='Talk to us', contact_h='Book time with us', contact_p='',
  prefer='Prefer email?', subject='BESS Benchmark intake request',
  f_name='Name', f_company='Company', f_email='Email', f_mw='Portfolio or project size in MW',
  f_msg='Context and objectives', f_ph='E.g., asset from 3 MW, trading revenues below expectations, interested in the BESS Benchmark',
  f_submit='Send', f_fine='Details are used only to get in touch about the ICM.', f_ok='Thank you – we will be in touch.',
  foot_tag='The ICM brings clarity, trusted partners and continuity to those adding capacity to the grid.',
  founded='Founded by', foot_bench='Learn more', methodology='Methodology', contact='Contact',
  terms='Terms & Conditions', privacy='Privacy statement', disclaimer='Benchmark figures are outcome data as reported by optimizers, not advice.',
  faq_title='Frequently asked questions about the BESS Benchmark | The ICM', faq_desc='Answers to common questions about the BESS Benchmark: data, costs, privacy and who can join.',
  faq_h='Frequently asked questions', faq_lead='Real, anonymised revenues, compared BESS-to-BESS. Missing something? Just ask us.', faq_more='Still have a question?',
  faqs=[
   ('How does the BESS Benchmark help?', '<p>There are roughly 4 reasons people are keen to become and stay a member.</p><ol><li><b>Clarity on performance.</b> It removes doubt by comparing apples with apples and pears with pears.</li><li><b>Stronger claims.</b> Independent figures on what comparable batteries earned make insurance and warranty claims stronger.</li><li><b>A better optimizer contract.</b> The BESS Benchmark helps negotiate a better optimizer contract ("floor of at least 80% of the benchmark"; "right to terminate at 60% of the benchmark").</li><li><b>A realistic business case.</b> A basis for sizing the next project and a check on bankable forecasts. Real data helps understand what a realistic business case could look like.</li></ol>'),
   ('How is this different from other benchmarks, forecasts and indices?', 'Virtual batteries with fixed assumptions give a suboptimal view. The BESS Benchmark shows what assets actually delivered: real revenues from optimizers\' statements, including grid restrictions, downtime and degradation. That makes it the reality check for those models.'),
   ('Who becomes a member?', 'Batteries in the Netherlands that an optimizer trades under a merchant contract. We focus on assets from 3 MW and decide per project in the intake.'),
   ('How does one become a member?', 'A 45-minute intake is our starting point. We use this time to discuss the context and objectives, understand which decisions the BESS Benchmark can help make and share what is needed to become and contribute as a member. New members share 6 months of historical data and decide how they will share revenue data each month. One route is for the optimizer to CC the ICM on their monthly performance report. Thereafter, the BESS Benchmark can be accessed at any time. The ICM will proactively reach out when the project performs poorly (below 80% of the BESS Benchmark).'),
   ('What does the BESS Benchmark cost?', 'Members pay a symbolic handling fee set at 0.5% of the gross revenues earned in that month. This number is excluding VAT. After referring 5 members, the fee drops to 0.1% for 6 months.'),
   ('How long is the commitment?', 'New members are asked to stay at least 3 months. After that, membership renews monthly.'),
   ('Who sees the data?', 'Only the member and the ICM see the raw data. The ICM anonymises submitted information before it adds it to the BESS Benchmark. We do not share individual member data with other members, or third parties. The BESS Benchmark itself is based on aggregated, anonymised information.'),
   ('Can members share their results?', 'Yes. Members may share their BESS Benchmark freely. It belongs to the member and may benefit conversations with installers, advisers and financiers.'),
   ('I advise or finance BESS assets. Can we work together?', 'Yes. Reach out to <a href="mailto:ideles@icm.energy">ideles@icm.energy</a> to explore the options to work together and join our partner network.'),
   ('How is the BESS Benchmark calculated?', 'The BESS Benchmark divides revenues by MW and annualises the result to show EUR per MW per year. Several filters allow members to compare batteries with a similar duration and set-up. Unavailable hours are excluded (maintenance, fault). Results are preliminary for 3 months, anticipating potential corrections.'),
   ('Why do BESS assets earn differently?', 'Various factors restrict the full earnings potential of a battery: (i) the battery itself (e.g., round-trip efficiency, minimum/maximum state of charge) and its local set-up (e.g., size of the grid connection, congestion contract), (ii) the markets it is active in and (iii) maintenance and malfunctions are the most commonly mentioned factors.'),
   ('Can members see which optimizer performs best?', 'No. The BESS Benchmark does not show results per optimizer, or rankings of optimizers. Members can compare their battery with peers that use the same or other optimizers, without names. Our BESS Broker proposition is designed to source and evaluate optimizers for owners.'),
   ('Is the ICM independent?', 'Yes. We do not own BESS assets. We are not an optimizer. Nor will we ever be. For more information about our governance, please reach out to <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>.'),
  ],
  terms_title='Terms & Conditions | The ICM', terms_h='Terms & Conditions',
  terms_body='<p>The Terms &amp; Conditions are shared with prospective members.</p><p>Please email <a href="mailto:ideles@icm.energy">ideles@icm.energy</a> to request a version of our Terms &amp; Conditions.</p>',
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
  book='Plan een intake', how_link='Zo werkt het',
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
  faq_link='Lees de veelgestelde vragen',
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
  f_msg='Vertel ons kort over je situatie en doelen', f_ph='Bijv. asset vanaf 3 MW, handelsopbrengsten onder verwachting',
  f_submit='Vraag een intake aan', f_fine='We gebruiken je gegevens alleen om contact met je op te nemen over de ICM.', f_ok='Dank je – we nemen contact met je op.',
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
   ('Welke batterijen kunnen meedoen?', 'Batterijen in Nederland met een merchant-contract. We richten ons op assets vanaf 3 MW en beslissen per project in de intake.'),
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
  ('What we collect', 'When you use the contact form: your name, company, email address, portfolio or project size and message. The website does not use tracking or analytics cookies.'),
  ('Why', 'To answer your request and plan an intake. We do not sell your data or use it for other purposes.'),
  ('Who processes it for us', 'Fillout receives the contact form on our behalf and stores it in the United States.'),
  ('How long we keep it', 'Contact details are kept as long as needed to follow up on your request, and at most two years after our last contact, unless you become a member.'),
  ('Your rights', 'You can ask to see, correct or delete your data, or object to its use, by emailing <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>. You can also file a complaint with the Dutch Data Protection Authority (Autoriteit Persoonsgegevens).'),
 ],
 'nl': [
  ('Wie we zijn', 'Independent Capacity Market B.V. (“de ICM”), Amsterdam, is verantwoordelijk voor de persoonsgegevens die hier worden beschreven. Contact: <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>.'),
  ('Wat we verzamelen', 'Via het contactformulier: je naam, bedrijf, e-mailadres, omvang van je portefeuille en je bericht. De website gebruikt geen tracking- of analytische cookies.'),
  ('Waarom', 'Om je verzoek te beantwoorden en een intake te plannen. We verkopen je gegevens niet en gebruiken ze niet voor andere doelen.'),
  ('Wie ze voor ons verwerkt', 'Fillout ontvangt het contactformulier namens ons en slaat het op in de Verenigde Staten.'),
  ('Hoe lang we ze bewaren', 'Contactgegevens bewaren we zolang nodig is om je verzoek op te volgen, en maximaal twee jaar na ons laatste contact, tenzij je lid wordt.'),
  ('Jouw rechten', 'Je kunt je gegevens inzien, laten corrigeren of verwijderen, of bezwaar maken tegen het gebruik, via <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>. Je kunt ook een klacht indienen bij de Autoriteit Persoonsgegevens.'),
 ],
}

GA = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-8RMBG4V4VG"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-8RMBG4V4VG');</script>'''

def head(t, title, desc, path, alt_path=None, jsonld=None, og_title=None):
    alt = ''
    if alt_path and len(LANGS) > 1:
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
<link rel="stylesheet" href="/styles.css?v={V_CSS}">
{ld}</head>
<body>
<a class="sr-only" href="#main">{t['skip']}</a>
'''

def _v(f):
    return hashlib.md5(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f),'rb').read()).hexdigest()[:8]
V_CSS, V_JS = _v('styles.css'), _v('main.js')

SOLUTIONS = [('BESS Benchmark', 'Open now', '/solutions/#benchmark'), ('BESS Backtest', 'Join the waitlist', '/solutions/#backtest'),
             ('BESS Broker', 'Join the waitlist', '/solutions/#broker'), ('BESS Bridge', 'Join the waitlist', '/solutions/#bridge')]

def nav(t, other_href):
    b = t['base']
    subs = ''.join(f'<li><a href="{h}"><b>{n}</b><span>{s}</span></a></li>' for n, s, h in SOLUTIONS)
    msubs = ''.join(f'<a class="m-sub" href="{h}">{n}</a>' for n, s, h in SOLUTIONS)
    return f'''    <header class="nav">
      <a class="logo" href="{b}" aria-label="The Independent Capacity Market, home"><img src="/assets/logo-header.png" alt="The Independent Capacity Market" width="796" height="119"></a>
      <nav aria-label="{t['menu']}">
        <ul class="nav-links">
          <li class="has-sub hide-sm"><button type="button" class="sub-btn" aria-expanded="false" aria-haspopup="true">Solutions</button><ul class="sub">{subs}</ul></li>
          <li class="hide-sm"><a href="/resources/">Resources</a></li>
          <li class="hide-sm"><a href="/company/">Company</a></li>
          <li><a class="btn btn-lilac" href="{b}#contact">{t['talk']}</a></li>
          <li class="show-sm"><button type="button" class="menu-btn" aria-expanded="false" aria-label="Open menu"><span></span><span></span><span></span></button></li>
        </ul>
      </nav>
      <div class="m-menu" hidden><p class="m-h">Solutions</p>{msubs}<a href="/resources/">Resources</a><a href="/company/">Company</a></div>
    </header>
'''

def footer(t, other_href):
    b = t['base']
    return f'''<footer>
  <div class="wrap foot2">
    <div class="f-about">
      <p class="f-name">The Independent Capacity Market</p>
      <p class="f-tag">{t['foot_tag']}</p>
    </div>
    <a class="f-logo" href="/" aria-label="The ICM, home"><img src="/assets/logo-footer.png" alt="The ICM" width="302" height="449" loading="lazy"></a>
    <nav class="f-links" aria-label="Footer">
      <a href="/solutions/">Solutions</a>
      <a href="/resources/">Resources</a>
      <a href="/company/">Company</a>
    </nav>
    <div class="f-legal">
      <p>Website designed by Salt &amp; Chalk</p>
      <p><a href="{b}terms/">{t['terms']}</a> | <a href="{b}privacy/">{t['privacy']}</a></p>
      <p>© 2026 Independent Capacity Market B.V.</p>
    </div>
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
        {"@type": "Organization", "@id": "https://icm.energy/#org", "name": "Independent Capacity Market B.V.", "alternateName": "The ICM", "logo": "https://icm.energy/assets/logo-footer.png",
         "url": "https://icm.energy/", "email": EMAIL, "address": {"@type": "PostalAddress", "addressLocality": "Amsterdam", "addressCountry": "NL"},
         "founder": {"@type": "Person", "name": "Idelès Kaandorp", "sameAs": LINKEDIN}},
        {"@type": "Service", "name": "BESS Benchmark", "provider": {"@id": "https://icm.energy/#org"}, "areaServed": "NL",
         "serviceType": "Battery energy storage revenue benchmark", "description": t['desc']}]}
    rules = '\n'.join(f'        <div class="rule"><h3>{h}</h3><p>{p}</p></div>' for h, p in t['rules'])
    def icon(n):
        bars = ''.join(f'<rect x="{7 + 11*k}" y="8" width="8" height="12" rx="1.5" fill="#0E1B2B"' + ('' if k < n else ' fill-opacity="0.18"') + '/>' for k in range(3))
        return f'<span class="stat-icon" aria-hidden="true"><svg viewBox="0 0 48 28"><rect x="2" y="3" width="38" height="22" rx="4" fill="none" stroke="#0E1B2B" stroke-width="3"/><rect x="41" y="10" width="5" height="8" rx="1.5" fill="#0E1B2B"/>{bars}</svg></span>'
    stats = '\n'.join(f'      <div class="stat">{icon(k + 1)}<p><b>{v}</b><span>{t["per"]}</span></p></div>' for k, v in enumerate(t['stats']))
    idx = ''.join(f'<li>{x}</li>' for x in t['idx']); ours = ''.join(f'<li>{x}</li>' for x in t['ours'])
    return head(t, t['title'], t['desc'], b, other, ld, t['og_title']) + f'''
<div class="hero-shell hero-photo">
  <img class="hero-img" src="/assets/img/hero-bulb.jpg" alt="" width="1920" height="1080" fetchpriority="high">
  <div class="wrap">
{nav(t, other)}
    <div class="hero" id="main">
      <div>
        <h1>Understand and<br>secure the true value<br>of a BESS asset</h1>
        <p class="lead">{t['lead']}</p>
        <div class="hero-ctas">
          <a class="btn btn-lilac" href="#contact">{t['book']}</a>
          <a class="btn btn-outline" href="#demo">{t['how_link']}</a>
        </div>
      </div>
    </div>
  </div>
</div>

<section class="dark" style="border-top:1px solid rgba(255,255,255,.08)">
  <div class="wrap">
    <div class="why-grid">
    <div>
    <span class="eyebrow why-eyebrow">{t['why_eyebrow']}</span>
    <div class="story" id="calculator" aria-live="polite">
      <p class="story-h">It's a waste to miss out on <b class="out" id="s-missed">EUR 555,000</b> a year.</p>
      <p class="story-p">A similar BESS asset, same size and setup, can deliver <a class="story-link" href="https://www.flower.se/insights/case/ra-energy-switch-optimizer/" target="_blank" rel="noopener">30% more revenue</a>. A <label class="pill"><input class="in" id="s-mw" type="number" min="1" max="500" step="1" value="10" aria-label="Project size in MW"><svg class="pen" viewBox="0 0 16 16" aria-hidden="true"><path d="M11.5 2.5l2 2L6 12l-2.8.8L4 10z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></label> MW project could have earned <b class="out" id="s-peer">EUR 240.5k</b> per MW per year, instead of the EUR <label class="pill"><input class="in" id="s-rev" type="number" min="1" max="1000" step="1" value="185" aria-label="Revenue it delivered, in thousand euro per MW per year"><svg class="pen" viewBox="0 0 16 16" aria-hidden="true"><path d="M11.5 2.5l2 2L6 12l-2.8.8L4 10z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></label>k per MW per year it delivered. That's a missed opportunity of <b class="out" id="s-up">EUR 55.5k</b> per MW.</p>
      <p class="hint"><svg class="pen" viewBox="0 0 16 16" aria-hidden="true"><path d="M11.5 2.5l2 2L6 12l-2.8.8L4 10z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>{t['story_note']}</p>
    </div>
    <div class="cta-row"><a class="btn btn-lilac" href="#contact">{t['book']}</a><a class="btn btn-outline" href="#demo">{t['more']}</a></div>
    </div>
    <figure class="why-fig" aria-hidden="true">
      <svg id="why-dots" role="presentation"></svg>
      <figcaption class="why-legend"><span><i class="d"></i>Delivered <b id="f-del">EUR 1,850,000</b></span><span><i class="m"></i>Missed <b id="f-mis">EUR 555,000</b></span><span class="unit" id="f-unit">1 dot = EUR 10,000 a year</span></figcaption>
    </figure>
    </div>
  </div>
</section>

<section class="demo-section" id="demo">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">{t['demo_eyebrow']}</span>
      <h2>{t['demo_h']}</h2>
      <p>{t['demo_p']}</p>
    </div>
    <figure class="shot shot-wide">
      <a class="demo-open" href="/demo/" data-demo><img src="/assets/benchmark-preview.jpg" width="1600" height="912" alt="{t['shot_alt']}" loading="lazy"><span class="demo-badge">{t['demo_btn']}</span></a>
      <figcaption>{t['demo_note']}</figcaption>
    </figure>
    <dialog class="demo-dialog" id="demo-dialog" aria-label="{t['demo_btn']}">
      <div class="demo-bar"><span></span><a href="/demo/" target="_blank" rel="noopener">{t['demo_new']}</a><button type="button" data-close aria-label="Close">×</button></div>
      <iframe title="{t['demo_title']}" loading="lazy"></iframe>
    </dialog>
  </div>
</section>

<section class="rules-wrap" id="how">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{t['how_eyebrow']}</span>
      <h2>{t['how_h']}</h2>
      <p>For merchant-traded BESS assets from 3 MW in the Netherlands.</p>
    </div>
    <div class="rules-row">
{rules}
    </div>
    <div class="cta-row" style="justify-content:flex-start;margin-top:36px">
      <a class="btn btn-lilac" href="#contact">{t['start']}</a>
      <a class="btn btn-outline teal" href="{b}faq/">{t['faq_link']}</a>
    </div>
  </div>
</section>

<section class="more" id="about">
  <div class="wrap about-grid">
    <div class="section-head">
      <span class="eyebrow">{t['about_eyebrow']}</span>
      <h2>{t['about_h']}</h2>
      <p>{t['about_p']}</p>
      <div class="cta-row" style="justify-content:flex-start;margin-top:28px">
        <a class="btn btn-lilac" href="#contact">{t['book']}</a>
        <a class="btn btn-outline" href="/solutions/">Our solutions</a>
        <a class="btn btn-outline" href="/company/#careers">{t['roles']}</a>
      </div>
    </div>
    <div class="about-visual"><img class="about-img" src="/assets/img/about-pylon.jpg" alt="High-voltage pylon against the evening sky" width="960" height="1080" loading="lazy"></div>
  </div>
</section>

<section id="contact">
  <div class="wrap contact">
    <div class="intro">
      <span class="eyebrow" style="color:var(--teal)">{t['contact_eyebrow']}</span>
      <h2>{t['contact_h']}</h2>
      <p>Our starting point is a 45-minute call to understand context and objectives.</p>
      <p>{t['prefer']} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="form fillout">
      <div style="width:100%;height:560px" data-fillout-id="icWpPN8hsgus" data-fillout-embed-type="standard" data-fillout-inherit-parameters data-fillout-dynamic-resize></div>
      <script src="https://server.fillout.com/embed/v1/" defer></script>
      <noscript><a href="https://forms.fillout.com/t/icWpPN8hsgus">Open the contact form</a></noscript>
    </div>
  </div>
</section>

{footer(t, other)}
<script src="/main.js?v={V_JS}" defer></script>
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
    items = '\n'.join(f'      <details><summary>{q}</summary>{a if a.startswith("<") else "<p>"+a+"</p>"}</details>' for q, a in t['faqs'])
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in t['faqs']]}
    body = f'''    <div class="faq">
{items}
    </div>
    <div class="faq-cta"><p>{t['faq_more']}</p><a class="btn btn-lilac" href="{t['base']}#contact">{t['book']}</a></div>'''
    return simple_page(t, t['base'] + 'faq/', t['other'] + 'faq/', t['faq_title'], t['faq_desc'], t['faq_h'], t['faq_lead'], body, ld)

def terms(t):
    body = f'    <div class="prose">{t["terms_body"]}</div>'
    return simple_page(t, t['base'] + 'terms/', t['other'] + 'terms/', t['terms_title'], 'How to receive the Terms & Conditions of the BESS Benchmark by the Independent Capacity Market.', t['terms_h'], '', body)

def privacy(t):
    secs = ''.join(f'<h2>{h}</h2><p>{p}</p>' for h, p in PRIVACY[t['lang']])
    body = f'    <div class="prose">{secs}<p style="color:var(--muted);font-size:14px">29-09-2026</p></div>'
    return simple_page(t, t['base'] + 'privacy/', t['other'] + 'privacy/', t['privacy_title'], 'How the Independent Capacity Market handles personal data from its website and contact form.', t['privacy_h'], '', body)

ROLES = [('Founders Associate', 'Amsterdam'), ('Commercial Lead', 'Amsterdam'), ('Legal Counsel', 'Amsterdam'), ('Software Engineer', 'Amsterdam')]

def page_shell(t, path, title, desc, hero, body, jsonld=None):
    return head(t, title, desc, path, None, jsonld) + f'''
<div class="hero-shell">
  <div class="wrap">
{nav(t, path)}
{hero}
  </div>
</div>
{body}
{footer(t, path)}
</body>
</html>
'''

def resources(t):
    hero = '''    <div class="page-hero" id="main">
      <h1>Resources</h1>
      <p>All Independent Capacity Market resources are listed below, including documents and brand assets.</p>
    </div>'''
    body = f'''<main class="res">
  <section class="wrap res-sec">
    <h2>Documents</h2>
    <p class="res-lead">Find answers to common questions about the BESS Benchmark, or read our API documents. Anything missing? Just ask.</p>
    <div class="res-cards">
      <div class="res-card res-thumb"><img src="/assets/brand/thumb-api.jpg" alt="" width="1425" height="552" loading="lazy"><div><span>API documents</span><small>Guides and reference for the ICM Platform API</small></div><a class="btn btn-lilac" href="https://docs.icm.energy/" target="_blank" rel="noopener">Access →</a></div>
      <div class="res-card res-thumb"><img src="/assets/brand/thumb-faq.jpg" alt="" width="1000" height="428" loading="lazy"><div><span>BESS Benchmark FAQ</span><small>Answers on membership, data and results</small></div><a class="btn btn-lilac" href="/faq/">Read →</a></div>
    </div>
  </section>
  <section class="wrap res-sec">
    <h2>Brand assets</h2>
    <p class="res-lead">Download the official brand assets of the ICM. Use these resources to ensure a consistent and professional representation of the ICM in all designs and communications.</p>
    <div class="res-cards">
      <div class="res-card res-thumb"><img src="/assets/brand/thumb-logos.jpg" alt="" width="640" height="360" loading="lazy"><div><span>Logos</span><small>PNG and SVG, header and footer versions</small></div><a class="btn btn-lilac" href="/assets/brand/ICM-logos.zip" download>Download →</a></div>
      <div class="res-card res-thumb"><img src="/assets/brand/thumb-images.jpg" alt="" width="640" height="360" loading="lazy"><div><span>Images</span><small>Seven brand photos, high resolution</small></div><a class="btn btn-lilac" href="/assets/brand/ICM-images.zip" download>Download →</a></div>
    </div>
  </section>
</main>'''
    return page_shell(t, '/resources/', 'Resources | The ICM', 'Documents and brand assets of the Independent Capacity Market.', hero, body)

ROLES = [('Founders Associate', 'Amsterdam'), ('Commercial Lead', 'Amsterdam'), ('Legal Counsel', 'Amsterdam'), ('Software Engineer', 'Amsterdam')]

def company(t):
    rows = '\n'.join(f'        <li><span><b>{r}</b><em>{c}</em></span><a class="btn btn-lilac" href="/?role={r.replace(" ", "%20")}#contact">Apply →</a></li>' for r, c in ROLES)
    hero = '''    <div class="page-hero" id="main">
      <h1>About The Independent Capacity Market</h1>
      <img class="co-img" src="/assets/img/company-grid.jpg" alt="High-voltage substation against the evening sky" width="1920" height="1080">
    </div>'''
    body = f'''<section class="dark co-who">
  <div class="wrap co-grid">
    <p class="co-label">Who we are</p>
    <div>
      <p>The ICM serves those who add capacity to the grid, but are in the dark on the potential of their assets.</p>
      <p>We believe in a new standard: an independent benchmark based on real assets, backtesting that looks at all constraints, access to trusted optimizers, and switching made less costly and less risky.</p>
      <p>A more transparent flex space rewards optimizers that perform, builds a stronger grid in uncertain times, and delivers more affordable power to us all.</p>
      <a class="btn btn-lilac" href="/#contact">Talk to us</a>
    </div>
  </div>
</section>
<section class="dark co-team">
  <div class="wrap">
    <p class="co-label">The team</p>
    <div class="team">
      <a class="member" href="https://www.linkedin.com/in/idel%C3%A8s-kaandorp/" target="_blank" rel="noopener"><img class="ph" src="/assets/team-ideles.jpg" alt="Idelès Kaandorp" width="600" height="600" loading="lazy"><b>Idelès Kaandorp</b><em>LinkedIn →</em></a>
      <a class="member" href="https://www.linkedin.com/in/edo-rivai-78b66a17/" target="_blank" rel="noopener"><img class="ph" src="/assets/team-edo.jpg" alt="Edo Rivai" width="512" height="512" loading="lazy"><b>Edo Rivai</b><em>LinkedIn →</em></a>
      <div class="member tbc"><span class="ph ph-empty"></span><b>Coming soon</b><em>&nbsp;</em></div>
    </div>
    <div class="team-cta"><a class="btn btn-lilac" href="/#contact">Get in touch →</a></div>
  </div>
</section>
<section class="co-careers" id="careers">
  <div class="wrap">
    <p class="co-label dark-t">Open roles</p>
    <h2 class="co-big">A more equitable grid.<span>Do work that matters with people who care.</span></h2>
    <hr>
    <ul class="co-roles">
{rows}
    </ul>
    <p class="co-open">Open applications are welcome. Please include a CV and what you want to achieve at the ICM, to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>'''
    ld = {"@context": "https://schema.org", "@type": "AboutPage", "url": "https://icm.energy/company/", "mainEntity": {"@type": "Organization", "@id": "https://icm.energy/#org", "name": "Independent Capacity Market B.V.", "alternateName": "The ICM", "logo": "https://icm.energy/assets/logo-footer.png", "url": "https://icm.energy/",
          "founder": {"@type": "Person", "name": "Idelès Kaandorp", "sameAs": "https://www.linkedin.com/in/idel%C3%A8s-kaandorp/"},
          "employee": [{"@type": "Person", "name": "Idelès Kaandorp", "sameAs": "https://www.linkedin.com/in/idel%C3%A8s-kaandorp/"}, {"@type": "Person", "name": "Edo Rivai", "sameAs": "https://www.linkedin.com/in/edo-rivai-78b66a17/"}]}}
    return page_shell(t, '/company/', 'Company | The ICM', 'About the Independent Capacity Market: who we are, our team and open roles in Amsterdam.', hero, body, ld)

def solutions(t):
    icons = {
      'benchmark': '<path d="M5 20V12M12 20V4M19 20V9"/><path d="M3 20h18"/>',
      'backtest': '<path d="M3.5 12a8.5 8.5 0 1 0 2.6-6.1"/><path d="M3.5 4.5v4h4"/><path d="M12 7.5V12l3 2"/>',
      'broker': '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/><path d="M8 10.5l2 2 3.5-4"/>',
      'bridge': '<path d="M4 8h13m0 0-3.5-3.5M17 8l-3.5 3.5"/><path d="M20 16H7m0 0 3.5-3.5M7 16l3.5 3.5"/>',
    }
    items = [
      ('benchmark', 'BESS Benchmark', True, "Real, anonymised revenues, compared BESS-to-BESS. Become a member to see how an asset is doing."),
      ('backtest', 'BESS Backtest', False, 'Understand the drivers of the capture rate. A deep dive into the full potential of complex, co-located set-ups.'),
      ('broker', 'BESS Broker', False, 'Outsource the search for a trusted optimizer. One form, a standardised process and terms banks appreciate.'),
      ('bridge', 'BESS Bridge', False, 'Switch optimizers without going dark. Our API platform connects optimizers with local infra.'),
    ]
    cards = ''
    for k, name, live, body in items:
        tag = '<span class="tag live">Open now</span>' if live else '<span class="tag soft">Coming soon</span>'
        cta = '<a class="btn btn-lilac" href="/#demo">Try the demo</a><a class="btn btn-outline" href="/#how">Learn more</a>' if live else '<a class="btn btn-lilac" href="/#contact">Join the waitlist</a>'
        cards += f'''    <article class="sol" id="{k}">
      <span class="sol-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="#97F2F5" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{icons[k]}</svg></span>
      <div class="sol-body">
        {tag}
        <h2>{name}</h2>
        <p>{body}</p>
        <div class="cta-row" style="justify-content:flex-start;margin-top:22px">{cta}</div>
      </div>
    </article>
'''
    title = 'Solutions | The ICM'
    desc = 'The ICM solutions for BESS owners: BESS Benchmark, BESS Backtest, BESS Broker and BESS Bridge.'
    return head(t, title, desc, '/solutions/') + f'''
<div class="hero-shell hero-photo sol-hero">
  <img class="hero-img" src="/assets/img/solutions-veins.jpg" alt="" width="1920" height="1080" fetchpriority="high">
  <div class="wrap">
{nav(t, '/solutions/')}
    <div class="page-hero" id="main">
      <h1>Solutions</h1>
      <p>The ICM serves those who add capacity to the grid, but are in the dark on the potential of their assets. We compare BESS-to-BESS, introduce owners to optimizers and oversee the switch, so batteries keep earning.</p>
    </div>
  </div>
</div>
<section class="dark sol-wrap">
  <div class="wrap">
{cards}  </div>
</section>
{footer(t, '/solutions/')}
<script src="/main.js?v={V_JS}" defer></script>
</body>
</html>
'''

REDIRECT = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Careers | The ICM</title><meta name="robots" content="noindex"><link rel="canonical" href="https://icm.energy/company/#careers"><meta http-equiv="refresh" content="0; url=/company/#careers"></head><body><a href="/company/#careers">Careers have moved to our company page.</a></body></html>'''

def write(rel, html):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(html)

for lang in LANGS:
    t = T[lang]
    pre = '' if lang == 'en' else 'nl/'
    write(pre + 'index.html', home(t))
    write(pre + 'faq/index.html', faq(t))
    write(pre + 'terms/index.html', terms(t))
    write(pre + 'privacy/index.html', privacy(t))
    if lang == 'en':
        write('careers/index.html', REDIRECT)
        write('resources/index.html', resources(t))
        write('company/index.html', company(t))
        write('solutions/index.html', solutions(t))
print('built')

# Methodology page, generated from _build/methodology.md (same text as the Methodology doc).
import markdown
FORMULAS = [
 '<div class="formula" role="math" aria-label="B sub m equals the sum over peers of revenue, divided by the sum over peers of MW times active hours, times 8760">B<sub>m</sub> = <span class="frac"><span>Σ<sub>i∈P</sub> R<sub>i,m</sub></span><span>Σ<sub>i∈P</sub> MW<sub>i</sub> × H<sub>i,m</sub></span></span> × 8,760</div>',
 '<div class="formula" role="math" aria-label="Score equals the project revenue per MW-hour over the period divided by the peer revenue per MW-hour over the same months, times 100 percent">Score<sub>T</sub> = <span class="frac"><span>Σ<sub>m∈T</sub> Σ<sub>i∈A</sub> R<sub>i,m</sub> ÷ Σ<sub>m∈T</sub> Σ<sub>i∈A</sub> MW<sub>i</sub> × H<sub>i,m</sub></span><span>Σ<sub>m∈T</sub> Σ<sub>j∈P<sub>m</sub></sub> R<sub>j,m</sub> ÷ Σ<sub>m∈T</sub> Σ<sub>j∈P<sub>m</sub></sub> MW<sub>j</sub> × H<sub>j,m</sub></span></span> × 100%</div>',
]
md = open(os.path.join(ROOT, '_build', 'methodology.md'), encoding='utf-8').read()
md = re.sub(r'^# .*\n', '', md, count=1)
version = re.search(r'This is version ([\d.]+) of ([^.]+)\.', md)
blocks = re.findall(r'```latex\n.*?\n```', md, flags=re.S)
for i, b in enumerate(blocks):
    md = md.replace(b, f'[[F{i}]]')
body = markdown.markdown(md, extensions=['tables'])
for i, f in enumerate(FORMULAS):
    body = body.replace(f'<p>[[F{i}]]</p>', f)
# the comparison table becomes two cards
def cards(m):
    rows = re.findall(r'<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>', m.group(0), flags=re.S)
    l = ''.join(f'<li>{a}</li>' for a, _ in rows); r = ''.join(f'<li>{b}</li>' for _, b in rows)
    return f'<div class="compare"><div class="index"><h3>A simulated revenue index</h3><ul>{l}</ul></div><div class="ours"><h3>The BESS Benchmark</h3><ul>{r}</ul></div></div>'
body = re.sub(r'<table>\s*<thead>\s*<tr>\s*<th>A simulated revenue index</th>.*?</table>', cards, body, count=1, flags=re.S)
body = body.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')
toc = []
def h2(m):
    t = m.group(1); sl = re.sub(r'[^a-z0-9]+', '-', re.sub('<[^>]+>', '', t).lower()).strip('-'); toc.append((sl, t))
    return f'<h2 id="{sl}">{t}</h2>'
body = re.sub(r'<h2>(.*?)</h2>', h2, body)
body = body.replace('bessbenchmark@icm.energy', '<a href="mailto:bessbenchmark@icm.energy">bessbenchmark@icm.energy</a>')
toc_html = '\n'.join(f'<li><a href="#{a}">{b}</a></li>' for a, b in toc)
te = T['en']
ld = {"@context": "https://schema.org", "@type": "TechArticle", "headline": "BESS Benchmark methodology", "version": version.group(1), "inLanguage": "en",
      "publisher": {"@type": "Organization", "name": "Independent Capacity Market B.V.", "url": "https://icm.energy/"}}
page = head(te, 'BESS Benchmark methodology: how we calculate revenue per MW | The ICM',
            f'How the ICM calculates the BESS Benchmark and the Project Score: data, quality control, active hours, duration bands, filters, anonymity thresholds and corrections. Version {version.group(1)}.',
            '/methodology/', None, ld, f'BESS Benchmark methodology, version {version.group(1)}') + f"""
<div class="hero-shell">
  <div class="wrap">
{nav(te, '/nl/')}
    <div class="page-hero" id="main">
      <span class="eyebrow">BESS Benchmark · Methodology v{version.group(1)} · {version.group(2)}</span>
      <h1>How we calculate the BESS Benchmark</h1>
      <p>From the data we collect and anonymise to how we present the results.</p>
    </div>
  </div>
</div>
<main class="wrap doc-layout">
  <nav class="toc" aria-label="Contents"><b>Contents</b><ol>
{toc_html}
  </ol></nav>
  <article class="prose">
{body}
  </article>
</main>
{footer(te, '/nl/')}
</body>
</html>
"""
write('methodology/index.html', '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>The ICM</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=/#demo"></head><body><a href="/#demo">Go to the BESS Benchmark</a></body></html>')
print('methodology built, v' + version.group(1), len(toc), 'sections')


# Interactive demo: the prototype (fictional data) served at /demo/, embedded on the homepage.
demo = open(os.path.join(ROOT, '_build', 'prototype.html'), encoding='utf-8').read()
demo = demo.replace('<a href="https://app.box.com/s/52dy3lyuocqpj3ss3rf47sdyveq7b1ir">Methodology</a> · ', '')
demo = demo.replace('<a href="\'+LINK_METH+\'">Methodology</a> · ', '').replace('https://app.box.com/s/3hmk2batlg2l2nv91e59gafzu2p1hek6', '/terms/')
demo = demo.replace('<title>BESS Benchmark Report</title>', '<title>BESS Benchmark interactive demo | The ICM</title><meta name="robots" content="noindex">')
demo = demo.replace("document.querySelectorAll('.seg[data-key]').forEach(el=>{\n  const key=el.dataset.key;", "document.querySelectorAll('.seg[data-key]').forEach(el=>{\n  const key=el.dataset.key;if(!OPTS[key])return;")
# a way back to the website (target=_top also works when the demo is shown inside the homepage dialog)
back = ('<div class="no-report" style="background:#061530;border-bottom:1px solid #1C3356;margin:-20px -16px 20px;padding:10px 16px;font:600 14px Figtree,system-ui,sans-serif">'
        '<a href="/#how" target="_top" style="color:#97F2F5;text-decoration:none">← Back to icm.energy</a></div>')
demo = demo.replace('<div class="wrap" id="page1">', back + '\n<div class="wrap" id="page1">', 1)
# open in light mode, at the top of the page
demo = demo.replace('<body>', '<body class="light">', 1)
demo = demo.replace('data-v="dark" aria-pressed="true">Dark</button><button type="button" data-v="light" aria-pressed="false">', 'data-v="dark" aria-pressed="false">Dark</button><button type="button" data-v="light" aria-pressed="true">', 1)
demo = demo.replace('</body>', "<script>if('scrollRestoration' in history)history.scrollRestoration='manual';window.scrollTo(0,0);addEventListener('load',function(){window.scrollTo(0,0)});</script>\n</body>", 1)
write('demo/index.html', demo)
print('demo built')
