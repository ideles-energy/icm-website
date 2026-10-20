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
  why_eyebrow='Our why', why_h='BESS assets deliver vastly different results',
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
  about_p='We are not owners. We are not optimizers. Nor will we ever be.<br><br>We are an energy tech company.<br><br>We compare BESS-to-BESS, introduce owners to optimizers and oversee the switch, so batteries keep earning.',
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
  terms='Terms & Conditions', privacy='Privacy statement', cookie='Cookie policy', disclaimer='Benchmark figures are outcome data as reported by optimizers, not advice.',
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
  terms_body='<p>Please email <a href="mailto:ideles@icm.energy">ideles@icm.energy</a> to request a version of our Terms &amp; Conditions.</p>',
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
  terms='Algemene voorwaarden', privacy='Privacyverklaring', cookie='Cookiebeleid', disclaimer='Benchmarkcijfers zijn uitkomstdata zoals gerapporteerd door optimizers, geen advies.',
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

PRIVACY_EN = [
 ('About this statement', 'This privacy statement explains how Independent Capacity Market B.V. (“the ICM”, “we”, “us”), Amsterdam, handles personal data collected through icm.energy and through our contact with owners, installers, optimizers and other visitors. It applies to this website. Other ICM services, such as the BESS Backtest, may come with additional terms or notices.'),
 ('Who is responsible', 'The ICM is the controller of the personal data described here. You can reach us at <a href="mailto:info@icm.energy">info@icm.energy</a>.'),
 ('Personal data we collect', 'We collect the data you give us when you use one of our forms or email us: your name, company, email address, the size of your portfolio or project, and your message. We also receive technical data that every website receives, such as your IP address and browser type, when your browser requests a page. We do not ask for special categories of personal data and we ask you not to send them to us.'),
 ('How we use personal data', 'We use your data to answer your request, prepare a custom report, follow up by email about our services, keep our website secure and working, and meet legal obligations. We do not sell your data, we do not use it for advertising and we do not use it for automated decision-making.'),
 ('Legal bases', 'We rely on our legitimate interest in answering business enquiries and keeping our website secure, on steps taken at your request before entering into a contract, on a legal obligation where one applies, and on your consent where we ask for it.'),
 ('Who we share it with', 'We share personal data only with service providers that help us run our business, under agreements that protect your data. Fillout receives our forms on our behalf. Our hosting provider, GitHub Pages, serves the website. We may also share data with advisers or authorities where the law requires.'),
 ('Transfers outside the EEA', 'Some of these providers are based in, or store data in, the United States. Where that is the case we rely on safeguards such as the EU-US Data Privacy Framework or standard contractual clauses.'),
 ('How long we keep it', 'We keep contact details for as long as needed to follow up on your request and at most two years after our last contact, unless you become a client or the law requires us to keep them longer.'),
 ('How we protect it', 'We limit access to personal data to people who need it, use trusted providers and keep our systems up to date. No online service is completely secure, so please do not send us confidential data you do not need to share.'),
 ('Your rights', 'You can ask to see, correct, delete or receive a copy of your personal data, restrict or object to its use, and withdraw consent you have given. Email <a href="mailto:info@icm.energy">info@icm.energy</a> and we will respond within one month. You can also file a complaint with the Dutch Data Protection Authority (Autoriteit Persoonsgegevens).'),
 ('Cookies', 'The ICM website does not use analytics or advertising cookies. See our <a href="/cookies/">cookie policy</a> for details.'),
 ('Changes to this statement', 'We may update this statement from time to time. The date below shows when it was last changed.'),
]
PRIVACY = {'en': PRIVACY_EN, 'nl': PRIVACY_EN}

COOKIES_EN = [
 ('What are cookies', 'Cookies are small text files that a website stores on your device when you visit it. Similar technologies, such as local storage and pixels, work in the same way. We use the word “cookies” for all of them.'),
 ('How we use cookies', 'The ICM website is built to work without tracking. We do not use analytics cookies, advertising cookies or social media tracking, and we do not build profiles of visitors.'),
 ('Cookies on our website', '<b>Our own website.</b> The pages of icm.energy do not set cookies of their own and do not store data in your browser to identify you.<br><b>Third-party content.</b> The forms on our Talk to us page and in the example report pop-up are provided by Fillout. When you load a form, Fillout may set cookies or similar technologies needed to show and submit it. Their use is governed by Fillout’s own policies.'),
 ('Managing cookies', 'You can block or delete cookies in your browser settings. If you do, parts of the website, such as the forms, may not work as intended. If you prefer, you can also email us at <a href="mailto:info@icm.energy">info@icm.energy</a> instead of using the form.'),
 ('If this changes', 'If we start using analytics or other cookies that need consent, we will ask for your permission first and update this policy.'),
 ('More information', 'See our <a href="/privacy/">privacy statement</a> for how we handle personal data, or contact us at <a href="mailto:info@icm.energy">info@icm.energy</a>.'),
]

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
<meta property="og:image" content="https://icm.energy/assets/og-image.png?v=4">
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

SOLUTIONS = [('BESS Calculator', 'Size and value the right system', '/solutions/#configurator'),
             ('BESS Broker', 'Find a trusted optimizer', '/solutions/#broker'),
             ('BESS Backtest', 'Measure what a battery captures', '/solutions/#backtest')]
TALK = '/talk-to-us/'

def nav(t, other_href):
    b = t['base']
    subs = ''.join(f'<li><a href="{h}"><b>{n}</b><span>{s}</span></a></li>' for n, s, h in SOLUTIONS)
    msubs = ''.join(f'<a class="m-sub" href="{h}">{n}</a>' for n, s, h in SOLUTIONS)
    return f"""    <header class="nav">
      <a class="logo" href="{b}" aria-label="The Independent Capacity Market, home"><img class="logo-full logo-on-dark" src="/assets/logo-header.svg" alt="The Independent Capacity Market" width="796" height="119"><img class="logo-full logo-on-light" src="/assets/logo-header-dark.svg" alt="" width="796" height="119"><img class="logo-icon" src="/assets/favicon.svg" alt="" width="36" height="36"></a>
      <nav aria-label="{t['menu']}">
        <ul class="nav-links nav-main">
          <li class="hide-sm"><a href="/solutions/">Solutions</a></li>
          <li class="hide-sm"><a href="/resources/">Resources</a></li>
          <li class="hide-sm"><a href="/company/">Company</a></li>
        </ul>
        <ul class="nav-links nav-right">
          <li class="hide-sm"><a class="nav-signin" href="https://app.icm.energy/">Sign in</a></li>
          {'' if other_href == TALK else '<li><a class="btn btn-lilac" href="' + TALK + '">Get started</a></li>'}
          <li class="show-sm"><button type="button" class="menu-btn" aria-expanded="false" aria-label="Open menu"><span></span><span></span><span></span></button></li>
        </ul>
      </nav>
      <div class="m-menu" hidden><a href="/solutions/">Solutions</a><a href="/resources/">Resources</a><a href="/company/">Company</a><a href="https://app.icm.energy/">Sign in</a><a class="js-gate-open" data-gate="demo" href="/solutions/#backtest">See an example report</a></div>
    </header>
"""

def footer(t, other_href):
    b = t['base']
    return GATE + f"""<footer>
  <div class="wrap foot2">
    <div class="f-about">
      <p class="f-name">The Independent Capacity Market</p>
      <p class="f-tag">The ICM brings clarity, trusted partners and continuity to those adding capacity to the grid.</p>
    </div>
    <a class="f-logo" href="/" aria-label="The ICM, home"><img src="/assets/submark.png" alt="The ICM" width="302" height="449" loading="lazy"></a>
    <nav class="f-links" aria-label="Footer">
      <a href="/solutions/">Solutions</a>
      <a href="/company/">Company</a>
      <a href="/resources/">Resources</a>
      <a href="{TALK}">Talk to us</a>
    </nav>
    <div class="f-mail"><p><a href="mailto:info@icm.energy">info@icm.energy</a></p><p class="f-copy">© 2026 Independent Capacity Market B.V.<span class="f-kvk">KvK 99958775</span></p></div>
    <div class="f-legal">
      <p>Website designed by <a href="https://www.saltandchalk.co.uk" target="_blank" rel="noopener">Salt &amp; Chalk</a></p>
      <p><a href="{b}terms/">{t['terms']}</a> | <a href="{b}privacy/">{t['privacy']}</a> | <a href="{b}cookies/">{t['cookie']}</a></p>
    </div>
  </div>
</footer>
"""

def chart(t):
    m = t['months']
    return f'''      <figure class="chart-card" aria-labelledby="chart-title">
        <h2 id="chart-title">{t['chart_title']}</h2>
        <p class="sub">{t['chart_sub']}</p>
        <svg viewBox="0 0 520 260" role="img" aria-label="{t['chart_aria']}">
          <g stroke="#DDE6E8" stroke-width="1"><line x1="44" x2="508" y1="30" y2="30"/><line x1="44" x2="508" y1="90" y2="90"/><line x1="44" x2="508" y1="150" y2="150"/><line x1="44" x2="508" y1="210" y2="210"/></g>
          <g fill="#4E6167" font-size="11" text-anchor="end"><text x="38" y="34">300k</text><text x="38" y="94">200k</text><text x="38" y="154">100k</text><text x="38" y="214">0</text></g>
          <g fill="#274A51"><rect x="54" y="98" width="22" height="112" rx="3"/><rect x="92" y="110" width="22" height="100" rx="3"/><rect x="130" y="86" width="22" height="124" rx="3"/><rect x="168" y="104" width="22" height="106" rx="3"/><rect x="206" y="128" width="22" height="82" rx="3"/><rect x="244" y="80" width="22" height="130" rx="3"/><rect x="282" y="92" width="22" height="118" rx="3"/><rect x="320" y="74" width="22" height="136" rx="3"/><rect x="358" y="118" width="22" height="92" rx="3"/><rect x="396" y="100" width="22" height="110" rx="3"/><rect x="434" y="88" width="22" height="122" rx="3"/><rect x="472" y="96" width="22" height="114" rx="3"/></g>
          <polyline fill="none" stroke="#D392EB" stroke-width="3" stroke-linejoin="round" points="65,86 103,92 141,80 179,84 217,90 255,70 293,78 331,62 369,82 407,86 445,74 483,80"/>
          <g fill="#4E6167" font-size="11" text-anchor="middle"><text x="65" y="230">{m[0]}</text><text x="141" y="230">{m[1]}</text><text x="217" y="230">{m[2]}</text><text x="293" y="230">{m[3]}</text><text x="369" y="230">{m[4]}</text><text x="445" y="230">{m[5]}</text></g>
          <g font-size="12"><rect x="54" y="244" width="12" height="12" rx="2" fill="#274A51"/><text x="72" y="254" fill="#040D1F">{t['chart_you']}</text><line x1="170" x2="190" y1="250" y2="250" stroke="#D392EB" stroke-width="3"/><text x="196" y="254" fill="#040D1F">{t['chart_peer']}</text></g>
        </svg>
        <p class="chart-note">{t['chart_note']}</p>
      </figure>
'''

def simple_page(t, path, other_path, title, desc, h1, lead, body, jsonld=None):
    return head(t, title, desc, path, other_path, jsonld) + f'''
<div class="hero-shell">
  <div class="wrap">
{nav(t, other_path)}
    <div class="page-hero" id="main">
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
<script src="/main.js?v={V_JS}" defer></script>
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
    return simple_page(t, t['base'] + 'terms/', t['other'] + 'terms/', t['terms_title'], 'How to receive the Terms & Conditions of the Independent Capacity Market.', t['terms_h'], '', body)

def cookies(t):
    secs = ''.join(f'<h2>{h}</h2><p>{p}</p>' for h, p in COOKIES_EN)
    body = f'    <div class="prose">{secs}<p style="color:var(--muted);font-size:14px">Last updated: 16 October 2026</p></div>'
    return simple_page(t, t['base'] + 'cookies/', t['other'] + 'cookies/', 'Cookie policy | The ICM', 'How the Independent Capacity Market website uses cookies and similar technologies.', 'Cookie policy', '', body)

def privacy(t):
    secs = ''.join(f'<h2>{h}</h2><p>{p}</p>' for h, p in PRIVACY[t['lang']])
    body = f'    <div class="prose">{secs}<p style="color:var(--muted);font-size:14px">Last updated: 16 October 2026</p></div>'
    return simple_page(t, t['base'] + 'privacy/', t['other'] + 'privacy/', t['privacy_title'], 'How the Independent Capacity Market handles personal data from its website and contact form.', t['privacy_h'], '', body)


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
<script src="/main.js?v={V_JS}" defer></script>
</body>
</html>
'''

def nl_report_chart():
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep']
    med=[172,165,181,158,149,176,190,184,197]
    p25=[141,137,150,129,121,144,158,150,163]
    p75=[203,196,214,189,178,207,224,219,231]
    W,H,L,R,T,B=560,260,44,16,16,34
    lo,hi=100,250
    x=lambda i: L+i*(W-L-R)/(len(months)-1)
    y=lambda v: T+(hi-v)*(H-T-B)/(hi-lo)
    band=' '.join(f'{x(i):.1f},{y(v):.1f}' for i,v in enumerate(p75))+' '+' '.join(f'{x(i):.1f},{y(v):.1f}' for i,v in reversed(list(enumerate(p25))))
    line=' '.join(f'{x(i):.1f},{y(v):.1f}' for i,v in enumerate(med))
    grid=''.join(f'<line x1="{L}" x2="{W-R}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="nlr-grid"/><text x="{L-8}" y="{y(v)+4:.1f}" text-anchor="end" class="nlr-ax">{v}</text>' for v in (100,150,200,250))
    xl=''.join(f'<text x="{x(i):.1f}" y="{H-12}" text-anchor="middle" class="nlr-ax">{m}</text>' for i,m in enumerate(months))
    pts=''.join(f'<g class="nlr-pt"><rect x="{x(i)-24:.1f}" y="{T}" width="48" height="{H-T-B}" fill="transparent"/><circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="4"/><title>{m} 2026: median EUR {v}k per MW per year (middle half EUR {a}k to {b}k). Illustrative.</title></g>' for i,(m,v,a,b) in enumerate(zip(months,med,p25,p75)))
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Illustrative chart: median revenue per MW per year of Dutch batteries, January to September 2026, with the range of the middle half of assets">{grid}<polygon points="{band}" class="nlr-band"/><polyline points="{line}" class="nlr-line"/>{xl}{pts}</svg>'

# Resources extras (BESS Calculator, NL BESS Revenue Report): built, hidden until launch. Set True to show.
RES_EXTRAS = os.environ.get('ICM_PREVIEW') == '1'  # shown only in the Claude preview until launch
COMPANY_STORY = True  # Our story + Supported by: live
NL_REPORT = False  # NL BESS Revenue Report signup: parked (built, not shown anywhere)
FILLOUT_JS = '\n<script src="https://server.fillout.com/embed/v1/" defer></script>'

def resources(t):
    RES_EXTRAS_HTML = f'''  <div class="wrap">
    <section class="calc-sec res-cols" id="calculator" aria-labelledby="calc-h">
      <div class="res-sec calc-left">
        <h2 id="calc-h">BESS Calculator <span class="calc-beta">Beta</span></h2>
        <p class="res-lead">Stop not knowing. See what your battery could have earned. No one has the perfect 2-hour BESS with a full grid connection that delivered EUR 305k per MW per year. Your battery has its own limits. See what it could have earned within them.</p>
        <div><a class="btn btn-outline-dark" href="/talk-to-us/">Talk to us</a></div>
      </div>
      <div class="res-sec">
        <div class="res-card res-thumb calc-card">
          <button type="button" class="calc-shot-btn js-gate-open" data-gate="calc" aria-label="Open the BESS Calculator"><img src="/assets/img/calculator-preview.jpg" alt="BESS Calculator: full potential and expected revenues per month (fictional example)" width="1440" height="900" loading="lazy"></button>
          <div><span>BESS Calculator</span><small>Subject to change, methodology to be refined.</small></div>
          <button type="button" class="btn btn-dark js-gate-open" data-gate="calc">Open</button>
        </div>
      </div>
    </section>
  </div>
  <div class="wrap">
    <section class="nlr-block" id="nl-report" aria-labelledby="nlr-h">
      <div class="nlr-copy">
        <div class="calc-tags"><span>Coming soon</span></div>
        <h2 id="nlr-h">NL BESS Revenue Report</h2>
        <p class="calc-lead">A periodic, anonymised view of what batteries in the Netherlands earn per MW, based on aggregated data. No asset, owner or optimizer is ever named.</p>
        <ul class="calc-points">
          <li><b>Aggregated and anonymised.</b> Results are only shown for groups of assets, never for a single battery.</li>
          <li><b>Like for like.</b> Revenues are compared per MW and per duration, so a 1-hour and a 2-hour battery are not lumped together.</li>
          <li><b>In your inbox.</b> Free, with each new edition.</li>
        </ul>
        <div class="nlr-form"><div data-fillout-id="3xLzpWnKW7us" data-fillout-embed-type="standard" data-fillout-inherit-parameters data-fillout-dynamic-resize style="width:100%;min-height:200px"></div><noscript><a href="https://forms.fillout.com/t/3xLzpWnKW7us">Sign up for the report</a></noscript></div>
      </div>
      <figure class="nlr-fig">
        <figcaption><b>Revenue per MW per year, NL batteries</b><span>EUR thousand · median and middle half of assets · 2026</span></figcaption>
        {nl_report_chart()}
        <div class="nlr-legend"><span><i class="nlr-k-line"></i>Median</span><span><i class="nlr-k-band"></i>Middle half of assets</span></div>
        <p class="nlr-note">Illustrative data. Shows the format of the report, not real results.</p>
      </figure>
    </section>
  </div>
'''
    if not NL_REPORT:
        RES_EXTRAS_HTML = re.sub(r'\n    <section class="nlr-block".*?</section>', '', RES_EXTRAS_HTML, flags=re.S)
    hero = f'''    <div class="page-hero" id="main">
      <h1>Resources</h1>
      <p>{('A free BESS Calculator, a periodic NL revenue report, API documents and brand assets of the Independent Capacity Market.' if NL_REPORT else 'A free BESS Calculator, API documents and brand assets of the Independent Capacity Market.') if RES_EXTRAS else 'API documents and brand assets of the Independent Capacity Market.'}</p>
    </div>'''
    body = f'''<main class="res">
{RES_EXTRAS_HTML if RES_EXTRAS else ''}  <div class="wrap res-cols">
    <section class="res-sec">
      <h2>Documents</h2>
      <p class="res-lead">Read our API documents. Anything missing? Just ask.</p>
      <div class="res-card res-thumb"><img src="/assets/brand/thumb-api.jpg" alt="" width="1400" height="612" loading="lazy"><div><span>API documents</span><small>Guides and reference for the ICM Platform API</small></div><a class="btn btn-dark" href="https://docs.icm.energy/" target="_blank" rel="noopener">Access</a></div>
    </section>
    <section class="res-sec">
      <h2>Brand assets</h2>
      <p class="res-lead">Download the official logos of the ICM.</p>
      <div class="res-card res-thumb"><img src="/assets/brand/thumb-logos.jpg" alt="" width="640" height="360" loading="lazy"><div><span>Logos</span><small>PNG and SVG, header and footer versions</small></div><a class="btn btn-dark" href="/assets/brand/ICM-logos.zip" download>Download</a></div>
    </section>
  </div>
</main>{FILLOUT_JS if (RES_EXTRAS and NL_REPORT) else ''}'''
    return page_shell(t, '/resources/', 'Resources | The ICM' if not RES_EXTRAS else 'Resources: BESS Calculator, API documents and brand assets | The ICM', 'API documents and brand assets of the Independent Capacity Market.' if not RES_EXTRAS else 'A free BESS Calculator, the NL BESS Revenue Report, API documents and brand assets of the Independent Capacity Market.', hero, body)

ROLES = [
  ('Commercial Lead', 'Amsterdam',
   'Sell our solutions to BESS owners and the installers who work with them. You own the pipeline, from first call to signed contract and beyond.',
   ['Be the connector: build lasting relationships with the installers and developers who bring us BESS owners (3–30 MW)',
    'Run discovery calls and present Calculator, Backtest and Broker results',
    'Guide clients from first call through onboarding, and make sure they get lasting value',
    'Turn successfully served clients into case examples'],
   ['3–6 years in B2B consultative sales (SaaS, energy or finance)',
    'Explains technical topics clearly',
    'Fluent in Dutch and English',
    'Knows BRP and aFRR, or learns fast']),
  ('BESS Analyst', 'Amsterdam',
   'Improve the revenue models, the BESS Backtest and the data pipelines behind every ICM result, and discuss the outcomes with clients.',
   ['Improve and extend the revenue models for imbalance, FCR, aFRR and day-ahead',
    'Speed up the BESS Backtest back-end and automate battery and market data',
    'Follow market design and regulation (TenneT, ACM, grid congestion) and translate it into our methodology',
    'Talk with clients about their results and what they mean for them'],
   ['MSc in econometrics, physics, energy or similar, with Python and SQL',
    '2–5 years at a trader, optimizer or consultancy',
    'Knowledge of the Dutch and European power markets',
    'Able to explain results clearly to people who are not analysts']),
]


def company(t):
    def li(items): return ''.join(f'<li>{i}</li>' for i in items)
    rows = '\n'.join(f'''      <details class="co-role" name="roles"><summary><b>{r}</b><em>{c}</em><i class="co-pm" aria-hidden="true"></i></summary><div class="co-body"><div><p>{m}</p><a class="btn btn-dark" href="mailto:ideles@icm.energy?subject=Application%3A%20{r.replace(" ", "%20")}">Apply</a></div><div><h4>What you will do</h4><ul>{li(do)}</ul></div><div><h4>Who you are</h4><ul>{li(you)}</ul></div></div></details>''' for r, c, m, do, you in ROLES)

    hero = '''    <div class="page-hero" id="main">
      <h1>About The Independent Capacity Market</h1>
      <img class="co-img" src="/assets/img/company-grid.jpg" alt="High-voltage substation against the evening sky" width="1920" height="1080">
    </div>'''
    body = f'''<section class="dark co-who">
  <div class="wrap co-grid">
    <p class="co-label">Who we are</p>
    <div>
      <p>The ICM serves those who add capacity to the grid, but are in the dark about their potential.</p>
      <p>By bringing transparency, we contribute to a stronger grid: one that rewards optimizers that perform, makes batteries easier to finance and gives system operators access to more reliable flexible capacity.</p>
      <p>We value our independence. We don't own, install or optimize, which keeps our intentions pure and our heads clear. For our clients, that means securing the true value of their battery, backed by reliable numbers.</p>
      <a class="btn btn-lilac" href="/talk-to-us/">Talk to us</a>
    </div>
  </div>
</section>
<section class="dark co-team">
  <div class="wrap">
    <p class="co-label">The team</p>
    <div class="team">
      <a class="member" href="https://www.linkedin.com/in/idel%C3%A8s-kaandorp/" target="_blank" rel="noopener"><img class="ph" src="/assets/team-ideles.jpg" alt="Idelès Kaandorp" width="600" height="600" loading="lazy"><b>Idelès Kaandorp</b><span class="m-bio">Founder. Leads the push for transparency in the BESS market. Trained as a mathematician, holds an MBA from Harvard Business School and served energy clients as a manager at McKinsey.</span></a>
      <a class="member" href="https://www.linkedin.com/in/edo-rivai-78b66a17/" target="_blank" rel="noopener"><img class="ph" src="/assets/team-edo.jpg" alt="Edo Rivai" width="512" height="512" loading="lazy"><b>Edo Rivai</b><span class="m-bio">Senior Software Developer. Owns platform design, integrations and infrastructure. Built and scaled software, most recently as Staff Software Engineer at Spot AI (a network of intelligent security cameras).</span></a>
      <a class="member" href="https://www.linkedin.com/in/jesse-h-willis/" target="_blank" rel="noopener"><img class="ph" src="/assets/team-jesse.jpg" alt="Jesse Willis" width="600" height="720" loading="lazy"><b>Jesse Willis</b><span class="m-bio">Project Engineer. Translates your dispatch constraints into custom insights that drive decisions. Studied Industrial Design Engineering in Delft and started Everlab to build meaningful products from scratch.</span></a>
    </div>
    <div class="team-cta"><a class="btn btn-lilac" href="/talk-to-us/">Talk to us</a></div>
  </div>
</section>
{'<section class="co-story" id="story"><div class="wrap"><div class="co-story-grid"><div><span class="eyebrow">Our story</span><h2>How the ICM started</h2><div class="story-txt"><p>Batteries are becoming the backbone of a flexible grid. Europe already has more than 100 GWh of battery storage installed, and the Netherlands is expected to reach around 25 GWh by 2030.</p><p>Batteries strengthen the grid. They store surplus solar and wind power, relieve congested grids and help keep the frequency at 50 Hz.</p><p>Yet most battery owners are flying blind. They have no overview of the optimizers on the market or how they compare, and no reference for what their own site could deliver.</p><p>The ICM was founded in Amsterdam in March 2026 to close this information gap. We serve those who add capacity to the grid, but are in the dark about the potential of their assets.</p><p class="story-src-line">Sources: <a href="https://www.ees-europe.com/publications/european-market-outlook-for-battery-storage-2026" target="_blank" rel="noopener">SolarPower Europe, European Market Outlook for Battery Storage</a>; <a href="https://taiyangnews.info/storage/europe-battery-storage-capacity-exceeds-100-gwh" target="_blank" rel="noopener">TaiyangNews, Europe’s battery storage capacity exceeds 100 GWh</a>.</p></div></div><div><span class="eyebrow">Supported by</span><div class="sup-card"><img src="/assets/img/provincie-noord-holland.png" alt="Province of Noord-Holland" width="1188" height="236" loading="lazy"><p><a href="https://www.noord-holland.nl/Producten_op_alfabet/MKB_innovatiestimulering_topsectoren_MIT_Noord_Holland_Haalbaarheidsproject_subsidie" target="_blank" rel="noopener">MIT feasibility grant</a> from the Province of Noord-Holland.</p></div></div></div></div></section>' if COMPANY_STORY else ''}
<section class="co-careers" id="careers">
  <div class="wrap">
    <p class="co-label dark-t">Open roles</p>
    <h2 class="co-big">A more equitable grid.<span>Do work that matters with people who care.</span></h2>
    <hr>
    <div class="co-acc">
{rows}
    </div>
    <p class="co-note">If no position suits you, you're welcome to submit an open application with your CV and what you'd want to achieve at the ICM to <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>.</p>
  </div>
</section>'''
    ld = {"@context": "https://schema.org", "@type": "AboutPage", "url": "https://icm.energy/company/", "mainEntity": {"@type": "Organization", "@id": "https://icm.energy/#org", "name": "Independent Capacity Market B.V.", "alternateName": "The ICM", "logo": "https://icm.energy/assets/logo-header.png", "url": "https://icm.energy/",
          "founder": {"@type": "Person", "name": "Idelès Kaandorp", "sameAs": "https://www.linkedin.com/in/idel%C3%A8s-kaandorp/"},
          "employee": [{"@type": "Person", "name": "Idelès Kaandorp", "sameAs": "https://www.linkedin.com/in/idel%C3%A8s-kaandorp/"}, {"@type": "Person", "name": "Edo Rivai", "sameAs": "https://www.linkedin.com/in/edo-rivai-78b66a17/"}]}}
    return page_shell(t, '/company/', 'Company: our story and the team behind the Independent Capacity Market | The ICM', 'About the Independent Capacity Market: who we are, our team and open roles in Amsterdam.', hero, body, ld)

ICONS = {
  'configurator': '<path d="M4 7h9M17 7h3M4 17h3M11 17h9"/><circle cx="15" cy="7" r="2"/><circle cx="9" cy="17" r="2"/><path d="M4 12h5M13 12h7"/><circle cx="11" cy="12" r="2"/>',
  'backtest': '<path d="M3.5 12a8.5 8.5 0 1 0 2.6-6.1"/><path d="M3.5 4.5v4h4"/><path d="M12 7.5V12l3 2"/>',
  'broker': '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/><path d="M8 10.5l2 2 3.5-4"/>',
}
def icon_svg(k):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="#97F2F5" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg>'

PROPS = [
  ('configurator', 'BESS Calculator', '/solutions/#configurator', 'Find the optimal system for your context.',
   'We simulate the revenues of different MW/MWh configurations within your site\'s dispatch constraints and show which one delivers the highest returns.'),
  ('broker', 'BESS Broker', '/solutions/#broker', 'Outsource the search for a trusted optimizer.',
   'We run a standardised process to source, compare and contract optimizers, and oversee the switch so your battery keeps earning without interruption.'),
  ('backtest', 'BESS Backtest', '/solutions/#backtest', 'Monitor your performance proactively.',
   'We compare your realised revenues with what can be reasonably achieved within your dispatch constraints, and alert you when performance consistently falls short.'),
]

NEWFAQS = [
 ('Why do battery owners work with the ICM?', 'To know what their battery could earn, and whether it earns that. We compare your revenue with the full potential of your site, and when there is more to earn we help you find a better optimizer. Because we own no batteries and are not an optimizer, you can share our numbers with your bank, installer and insurer.'),
 ('Why do installers offer the BESS Backtest to their customers?', 'It is a gift that builds trust. Installers can include a BESS Backtest at delivery, so every customer gets an independent view of what the battery earns. It shows you stand behind your system.'),
 ('Why can I trust the ICM\'s numbers?', 'We do not own BESS assets. We are not an optimizer. Nor will we ever be.'),
('What is the BESS Backtest?', 'The BESS Backtest compares what your battery earned with the most it could have earned on your site. The result is a capture rate: the share of the full potential that was realised. It shows whether a battery earns what it should, and what holds it back.'),
('What data do I need to provide?', 'The optimizer report, quarter-hour meter data, data from the energy management system for downtime, and the documents on your grid connection and optimizer mandate. We guide you through the list, and your installer or metering service provider can often deliver most of it.'),
('Who orders a BESS Backtest, me or my installer?', 'Installers can include a BESS Backtest at delivery, so every customer gets an independent view of what the battery earns. Owners can also order one directly. Talk to us about how this works for you.'),
('How can my installer work with the ICM?', 'Installers can use the ICM in three ways: size a system with the BESS Calculator before the sale, include a BESS Backtest at delivery so every customer gets an independent view of what the battery earns, and refer owners who want a better optimizer to the BESS Broker. Talk to us to see what fits your way of working.'),
('What if my battery earns less than it could?', 'You decide what happens next. If the result objectively falls short, the BESS Broker can help you request and compare quotes from other optimizers, test what they would have earned, and guide the switch.'),
]

SOL_FAQS = [
 ('Why do battery owners use the ICM?', 'To know what their battery could earn, and whether it earns that. We compare your revenue with the full potential of your site, and when there is more to earn we help you find a better optimizer. Because we own no batteries and are not an optimizer, you can share our numbers with your bank, installer and insurer.'),
 ('Is the ICM for my battery?', 'The ICM serves owners and developers of batteries of roughly 3 to 30 MW, and the installers who work with them. You do not need to be an expert in power markets.'),
 ("I don't know if my optimizer is any good. Can the ICM tell me?", 'Yes. The BESS Backtest compares what your battery earned with the most it could have earned on your site. The result is a capture rate: the share of the full potential that was realised, and what holds it back.'),
 ('What if my battery earns less than it could?', 'You decide what happens next. If the result objectively falls short, the BESS Broker can help you compare optimizers, test what they would have earned and guide the switch.'),
 ('Is the ICM really independent?', 'Yes. We do not own BESS assets. We are not an optimizer. Nor will we ever be.'),
 ('What do I need to get approved?', 'Your work email and a few project details. After approval we ask for read access to your optimizer, or three months of settlements, plus an authorisation to read your meter data from your metering company.'),
 ('When does it make sense to start with the ICM?', 'Before you build, to size the right system with the BESS Calculator. After your battery is running, to see whether it earns what it should with the BESS Backtest. And whenever the numbers say there is more to earn, to find a better optimizer with the BESS Broker.'),
 ('How do installers work with the ICM?', 'Installers can size a system with the BESS Calculator before the sale, include a BESS Backtest at delivery so every customer gets an independent view of what the battery earns, and refer owners who want a better optimizer to the BESS Broker.'),
]

def faq_block(items, title=None):
    rows = '\n'.join(f'      <details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    h = f'<h2>{title}</h2>' if title else ''
    return f"""<section class="faq-sec" id="faq">
  <div class="wrap">
    <div class="section-head center">{h}</div>
    <div class="faq">
{rows}
    </div>
  </div>
</section>"""

def cta_band(t, h="Secure your battery's full potential", p='Tell us about your project. We guide you through the rest.', topic=None):
    q = f'?topic={topic}' if topic else ''
    return f"""<section class="cta-band">
  <div class="wrap">
    <h2>{h}</h2>
    <p>{p}</p>
    <div class="cta-row"><a class="btn btn-lilac" href="{TALK}{q}">Get started</a><a class="btn btn-outline" href="/solutions/">Learn more</a></div>
  </div>
</section>"""

def expect_cards():
    return """<div class="expect">
      <div><b>1</b><h3>A 45-minute call</h3><p>An expert from the ICM team talks you through the options. Booking the call already takes work off your plate.</p></div>
      <div><b>2</b><h3>Context and objectives</h3><p>We use the time to understand your asset, your optimizer set-up and what you are looking for.</p></div>
      <div><b>3</b><h3>A full proposal</h3><p>Afterwards we share a full proposal, so the next steps are clear and nothing comes as a surprise.</p></div>
    </div>"""

def home(t):
    b = t['base']
    other = t['other']
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": "https://icm.energy/#org", "name": "Independent Capacity Market B.V.", "alternateName": "The ICM", "logo": "https://icm.energy/assets/logo-header.png",
         "url": "https://icm.energy/", "email": EMAIL, "address": {"@type": "PostalAddress", "addressLocality": "Amsterdam", "addressCountry": "NL"},
         "founder": {"@type": "Person", "name": "Idelès Kaandorp", "sameAs": LINKEDIN}}]}
    cards = ''.join(f"""      <article class="prop{' featured' if k == 'backtest' else ''}">{CALLOUT if k == 'backtest' else ''}
        <span class="sol-icon" aria-hidden="true">{icon_svg(k)}</span>
        <h3>{n}</h3>
        <p class="prop-lead">{lead}</p>
        <p>{body}</p>
        <div class="prop-actions"><a class="prop-link" href="{h}">Learn more →</a>{'<button type="button" class="btn btn-lilac js-gate-open prop-demo" data-gate="demo">See an example report</button>' if k == 'backtest' else ''}</div>
      </article>
""" for k, n, h, lead, body in PROPS)
    title = 'BESS performance and optimizer insight: secure the true value of your BESS asset | The ICM'
    desc = 'The ICM helps BESS owners in the Netherlands size the right battery, backtest its performance and find a trusted optimizer. Independent: we own no batteries and are not an optimizer.'
    return head(t, title, desc, b, None, ld, 'Secure the true value of your BESS asset') + f'''
<div class="hero-shell hero-photo">
  <img class="hero-img" src="/assets/img/hero-bulb.jpg" alt="" width="1920" height="1080" fetchpriority="high">
  <div class="wrap">
{nav(t, other)}
    <div class="hero" id="main">
      <div>
        <h1>Secure the true value <br>of your BESS asset</h1>
        <p class="lead">For those with a nagging sense their battery could earn more. Find the optimal system for your context, outsource the search for a trusted optimizer and monitor your performance proactively.</p>
        <div class="hero-ctas">
          <a class="btn btn-lilac" href="{TALK}">Get started</a>
          <a class="btn btn-outline" href="/solutions/">Learn more</a>
        </div>
      </div>
    </div>
  </div>
</div>

{why_section(os.environ.get('WHY_VARIANT', '13'))}

<section class="props-sec props-light" id="how">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow why-eyebrow">How we can work together</span>
      <h2>An independent perspective</h2>
    </div>
    <div class="props">
{cards}    </div>
  </div>
</section>




<section class="about-sec about-light" id="about">
  <div class="wrap about-grid2">
    <div class="about-card">
      <span class="eyebrow why-eyebrow">About us</span>
      <h2>Why an Independent Capacity Market matters</h2>
      <p>We are not owners. We are not optimizers. Nor will we ever be. We are an energy tech company.</p>
      <p>We serve those who add capacity to the grid, but are in the dark about the potential of their assets.</p>
      <div class="cta-row" style="justify-content:flex-start"><a class="btn btn-dark" href="{TALK}">{t['talk']}</a><a class="btn btn-outline" href="/company/">Our story</a></div>
    </div>
    <div class="about-visual"><img class="about-img" src="/assets/img/about-pylon.jpg" alt="High-voltage pylon against the evening sky" width="960" height="1080" loading="lazy"></div>
  </div>
</section>


{cta_band(t)}

{footer(t, other)}
<script src="/main.js?v={V_JS}" defer></script>
</body>
</html>
'''

CALLOUT = '<span class="callout">Understand where it leaks</span>'

SOL_IMG = {'configurator': ('/assets/img/sol-owner.jpg', 'Wind turbine against a blue sky'),
           'broker': ('/assets/img/sol-optimizer.jpg', 'Abstract grid of glowing data points'),
           'backtest': ('/assets/img/sol-partner.jpg', 'High-voltage substation against the evening sky')}

def sol_card(k, n, href, lead, body, extra):
    return f"""<article class="sol{' featured' if k == 'backtest' else ''}" id="{k}">{CALLOUT if k == 'backtest' else ''}
        <span class="sol-icon" aria-hidden="true">{icon_svg(k)}</span>
        <div class="sol-body">
          <h2>{n}</h2>
          <p class="sol-lead">{lead}</p>
          <p>{body}</p>
          <p>{extra}</p>
          <div class="cta-row" style="justify-content:flex-start;margin-top:22px">{'<button type="button" class="btn btn-lilac js-gate-open" data-gate="demo">See an example report</button>' if k == 'backtest' else '<a class="btn btn-dark" href="' + TALK + '?topic=' + k + '">Learn more</a>'}</div>
        </div>
      </article>"""

def sol_block(i, k, n, href, lead, body, extra):
    img = f'<div class="sol-img sol-flat sol-flat-{k}" aria-hidden="true">{icon_svg(k)}</div>'
    card = sol_card(k, n, href, lead, body, extra)
    return f'    <div class="sol-row sol-r{i % 2}">\n      {card}\n      {img}\n    </div>\n'

PARTNER_STRIP = '''<section class="dark partner-wrap" id="partners">
  <div class="wrap">
    <div class="partner-strip js-partner">
      <div class="ps-q">
        <p class="eyebrow-w">Partners</p>
        <h2>Know an owner who <em>earns too little?</em></h2>
      </div>
      <div class="ps-slide">
        <label for="ps-mw"><span>Battery size of your referral</span><output class="js-ps-mw" for="ps-mw">10 MW</output></label>
        <input id="ps-mw" class="js-ps-range" type="range" min="0.25" max="50" step="0.25" value="10">
      </div>
      <div class="ps-out">
        <p class="ps-sm">Your reward</p>
        <p class="ps-pay js-ps-pay">EUR 5,000</p>
        <a class="btn btn-lilac" href="/talk-to-us/?topic=partner">Refer an owner</a>
      </div>
    </div>
    <p class="ps-fine">For metering parties, EMS providers, financial advisors and BESS financiers. EUR 500 per MW, one time per client, paid after the client's first invoice has been paid in full.</p>
    <details class="ps-terms">
      <summary>Referral terms</summary>
      <ul>
        <li><b>The fee.</b> EUR 500 per MW of the client's nameplate capacity, paid once the client's first invoice has been paid in full, within 6 months of your introduction.</li>
        <li><b>The referral.</b> Made in writing, to a named decision-maker at the client. It is valid only if the ICM has not already engaged that person in the preceding 6 months.</li>
        <li><b>The payout.</b> We pay by self-billing within 30 days. The fee includes BTW and is repayable if the client is refunded within 180 days.</li>
        <li><b>Advisers.</b> If you also advise the client, tell them you receive a referral fee. No fee is paid to parties with a conflict of interest, such as optimizers.</li>
        <li><b>One fee per client.</b> It applies to the first engagement only, with no top-up when the client later engages the ICM for another asset.</li>
        <li><b>Changes.</b> The ICM may decline a referral without giving reasons. Terms can change for future referrals, not for referrals already made.</li>
      </ul>
    </details>
  </div>
</section>'''

GS_FORM = '''<div class="gs-cta">
  <a class="btn btn-lilac" href="/talk-to-us/">Get started</a>
  <button type="button" class="btn btn-outline js-gate-open" data-gate="demo">See an example report</button>
</div>'''

def gs_form(i):
    return GS_FORM.replace('ID', i)

GS_ICONS = {
  'mail': '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="7" width="24" height="18" rx="2.5"/><path d="m5 9 11 9 11-9"/></svg>',
  'form': '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="4" width="20" height="25" rx="2.5"/><path d="M11 4v3h10V4M11 14h10M11 19h10M11 24h5"/></svg>',
  'key': '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="16" cy="16" r="12"/><path d="m10.5 16.5 4 4 7-8"/></svg>',
}


CR_H = '<h2>The best capture rate, at all times.</h2>'
CR_P = '<p class="cr-p">The ICM proactively monitors your performance and switches optimizers when there is more to earn. Together, we secure the true value of your battery.</p>'

def _cr_ui():
    bars = [88, 87, 85, 82, 78, 75]
    bh = ''.join(f'<i style="height:{(v-60)*2.2:.0f}px" class="{"lo" if v < 80 else ""}"></i>' for v in bars)
    return f"""<div class="cr-ui">
      <div class="cu-card cu-kpi"><div class="cu-top"><span class="cu-dot"></span>Your battery <em>10 MW / 20 MWh</em></div>
        <p class="cu-l">Capture rate, last 6 months</p><p class="cu-big">75%<small>Expected 80%</small></p>
        <div class="cu-bars">{bh}<span class="cu-exp"></span></div><div class="cu-m"><span>Jan</span><span>Jun</span></div></div>
      <div class="cu-card cu-note"><span class="cu-bell"><svg viewBox="0 0 24 24"><path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4zM10 20a2 2 0 0 0 4 0"/></svg></span>
        <div><b>Capture rate below expected for 3 months</b><p>We asked 4 trusted optimizers for a quote.</p></div><time>Today</time></div>
      <div class="cu-card cu-quotes"><p class="cu-l">Quotes, side by side</p>
        <div class="cu-row cu-sel"><span>Optimizer B</span><span>Expected 93%</span><button type="button" tabindex="-1">Switch</button></div>
        <div class="cu-row"><span>Optimizer C</span><span>Expected 89%</span><span></span></div>
        <div class="cu-row"><span>Optimizer D</span><span>Expected 86%</span><span></span></div></div>
    </div>"""

def _cr_feed():
    items = [('Jan', 'Monthly check', 'Capture rate 88%. On track.', ''),
             ('Apr', 'Alert', 'Capture rate 78%, below the expected 80%.', 'v'),
             ('May', 'Quotes compared', 'Four trusted optimizers, side by side.', ''),
             ('Jun', 'Optimizer switched', 'Your battery keeps earning during the move.', ''),
             ('Sep', 'Monthly check', 'Capture rate 94%.', 'c')]
    li = ''.join(f'<li class="cf-{k or "n"}"><time>{m}</time><div><b>{t}</b><span>{d}</span></div></li>' for m, t, d, k in items)
    return f'<div class="cr-feed"><p class="cf-head"><span class="cf-live"></span>The ICM at work for your battery</p><ol>{li}</ol></div>'

def _cr_split():
    return """<div class="cr-split">
      <div class="cs-card cs-off"><p class="cs-tag">Without the ICM</p><p class="cs-big">EUR 1,850,000</p><p class="cs-cap">revenue last year</p>
        <ul><li><span>Full potential</span><b>Unknown</b></li><li><span>Missed</span><b>Unknown</b></li><li><span>Other optimizers</span><b>Unknown</b></li></ul></div>
      <div class="cs-card cs-on"><p class="cs-tag">With the ICM</p><p class="cs-big">94%</p><p class="cs-cap">capture rate</p>
        <ul><li><span>Full potential</span><b>EUR 2,405,000</b></li><li><span>Missed</span><b class="v">EUR 145,000</b></li><li><span>Other optimizers</span><b>Compared</b></li></ul></div>
    </div>"""

def _cr_dots():
    real = [7, 7, 7, 7, 7, 7, 9, 9, 10, 9, 10, 10]
    X = lambda i: 40 + i * 78 + (24 if i >= 6 else 0)
    out = ''
    for i, r in enumerate(real):
        for j in range(10):
            y = 290 - j * 24
            out += f'<circle cx="{X(i)}" cy="{y}" r="8" class="{"cd-d" if j < r else "cd-m"}"/>'
        out += f'<text x="{X(i)}" y="322" class="cr-ax" text-anchor="middle">{"JFMAMJJASOND"[i]}</text>'
    sx = (X(5) + X(6)) / 2
    return f"""<svg viewBox="0 0 1000 335" class="cr-svg" role="img" aria-label="Each column is a month; violet dots are revenue missed, which shrink after the switch">
      {out}<line x1="{sx}" x2="{sx}" y1="44" y2="300" class="cr-switch"/>
      <rect x="{sx-78}" y="8" width="156" height="32" rx="16" class="cr-pill"/><text x="{sx}" y="29" class="cr-pill-t" text-anchor="middle">Switch optimizer</text>
    </svg>
    <div class="cr-leg"><span><i class="cr-k-real" style="border-radius:50%"></i>Delivered</span><span><i class="cd-k-m"></i>Missed</span><span>1 dot = 10% of the full potential that month</span></div>"""

def _cr_anim():
    return """<div class="crx js-crx" data-from="46" data-to="83">
      <div class="crx-card">
        <div class="crx-top"><span class="crx-dot"></span>Your battery <em>10 MW / 20 MWh</em></div>
        <div class="crx-opt"><span class="crx-o crx-oa">Optimizer A</span><span class="crx-o crx-ob">Optimizer B</span></div>
        <div class="crx-gw"><svg viewBox="0 0 400 215" class="crx-g" aria-hidden="true">
          <path d="M40,200 A160,160 0 0 1 360,200" class="crx-g-bg" pathLength="100"/>
          <path d="M40,200 A160,160 0 0 1 360,200" class="crx-g-fg js-crx-arc" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"/>
          <line x1="311.6" y1="118.9" x2="347.2" y2="93.0" class="crx-g-exp"/>
        </svg>
        <div class="crx-num"><b class="js-crx-num">0%</b><span>capture rate</span></div>
        <span class="crx-explab">Expected 80%</span></div>
        <div class="crx-status"><span class="crx-s crx-slo">Below expected</span><span class="crx-s crx-sok">On track</span></div>
      </div>
      <ol class="crx-log">
        <li class="crx-e1"><i></i><div><b>Alert</b><span>Capture rate 46%, below the expected 80%.</span></div></li>
        <li class="crx-e2"><i></i><div><b>Quotes compared</b><span>Trusted optimizers, side by side.</span></div></li>
        <li class="crx-e3"><i></i><div><b>Optimizer switched</b><span>Capture rate up to 83%.</span></div></li>
      </ol>
      <button type="button" class="crx-replay js-crx-replay">Replay</button>
    </div>"""

def _cr_film():
    # All figures are for one illustrative battery. Expected revenues are known only after each month.
    ex = [228, 223, 222, 229, 236, 240, 240, 235, 230, 225, 234, 233]          # expected revenues, EUR k per MW per year (annualised)
    CA, CB, CE = 64, 83, 80                                                     # capture rate with A, with B, expected (83/64 = +30%)
    ra = [e * CA / CE for e in ex]; rb = [e * CB / CE for e in ex]
    before, gain = 185000, 55500                                                # same battery as the home page: EUR 185k, +30% = EUR 55.5k
    fmt = lambda v: f'{v:,.0f}'
    W, H, L, R, T, B = 520, 300, 60, 10, 14, 30
    X = lambda i: L + i * (W - L - R) / 11
    Y = lambda v: T + (270 - v) / (270 - 150) * (H - T - B)
    pl = lambda pts, idx: ' '.join(('M' if k == 0 else 'L') + f'{X(i):.1f},{Y(v):.1f}' for k, (i, v) in enumerate(zip(idx, pts)))
    band = 'M' + ' L'.join(f'{X(i):.1f},{Y(e*1.1):.1f}' for i, e in enumerate(ex)) + ' L' + ' L'.join(f'{X(i):.1f},{Y(e*0.9):.1f}' for i, e in reversed(list(enumerate(ex)))) + ' Z'
    grid = ''.join(f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" class="ax-grid"/><text x="{L-7}" y="{Y(v)+4:.1f}" text-anchor="end" class="ax-ax">{v}k</text>' for v in (150, 175, 200, 225, 250))
    months = ''.join(f'<text x="{X(i):.1f}" y="{H-8}" text-anchor="middle" class="ax-ax">{m}</text>' for i, m in enumerate('JFMAMJJASOND'))
    x1, x2 = X(5) + 2, W
    chart = f"""<svg viewBox="0 0 {W} {H}" class="ax-chart" aria-hidden="true" data-x0="{L}" data-x1="{x1:.1f}" data-x2="{x2}">
          <defs><clipPath id="ax-clip"><rect class="js-ax-clip" x="0" y="0" width="{L}" height="{H}"/></clipPath></defs>{grid}{months}
          <g clip-path="url(#ax-clip)"><path d="{band}" class="ax-band"/><path d="{pl(ex, range(12))}" class="ax-ex"/>
          <path d="{pl(ra[:6], range(6))}" class="ax-ra"/><path d="{pl([ra[5]] + rb[6:], range(5, 12))}" class="ax-rb"/>
          <line x1="{(X(5)+X(6))/2:.1f}" x2="{(X(5)+X(6))/2:.1f}" y1="{T}" y2="{H-B}" class="ax-sw"/></g></svg>"""
    quotes = [('Optimizer B', 84, True), ('Optimizer C', 81, False), ('Optimizer D', 79, False), ('Optimizer E', 76, False)]
    qr = ''.join(f'<div class="ax-q{" ax-qsel" if sel else ""}" style="--k:{k}"><b>{n}</b><span class="ax-qe">Expected <strong>{e}%</strong></span>' + ('<span class="ax-btn">Switch</span>' if sel else '<span></span>') + '</div>' for k, (n, e, sel) in enumerate(quotes))
    nav = [('0', 'Monitor', f'Capture rate at {CA}%, below the expected {CE}%. Owner alerted.'),
           ('6000', 'Compare', 'Trusted optimizers, quotes compared side by side.'),
           ('9800', 'Switch', f'Optimizer B takes over. Capture rate up to {CB}%.'),
           ('13600', 'Result', f'Your battery earns an extra EUR {fmt(gain)} per MW per year.')]
    navh = ''.join(f'<li><button type="button" data-t="{t}"><span>{k+1}</span>{h}</button><p>{d}</p></li>' for k, (t, h, d) in enumerate(nav))
    return f"""<div class="film ax js-film" data-from="{CA}" data-to="{CB}" data-base="{before}" data-gain="{gain}">
      <div class="ax-win">
        <aside class="ax-side"><ol class="fm-ch ax-nav">{navh}</ol></aside>
        <div class="ax-main">
          <img class="ax-mark" src="/assets/icm-mark.svg" alt="The Independent Capacity Market" width="40" height="40">
          <p class="ax-cap js-fm-cap"></p>
          <div class="ax-grid2">
            <div class="ax-card ax-kpi">
              <div class="ax-kh"><b>Capture rate, %</b></div>
              <div class="ax-opt"><span class="ax-o ax-oa">Optimizer A</span><span class="ax-o ax-ob">Optimizer B</span></div>
              <div class="ax-gw"><svg viewBox="0 0 400 210" class="ax-g" aria-hidden="true">
                <path d="M44,196 A156,156 0 0 1 356,196" class="ax-g-bg" pathLength="100"/>
                <path d="M44,196 A156,156 0 0 1 356,196" class="ax-g-fg js-fm-arc" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"/>
                <line x1="311.6" y1="114.9" x2="342.4" y2="92.5" class="ax-g-exp"/><text x="355.3" y="83.1" class="ax-g-el">80%</text>
              </svg><div class="ax-num"><b class="js-fm-num">0%</b></div></div>
              <div class="ax-status"><span class="ax-s ax-slo">Below expected</span><span class="ax-s ax-sok">On track</span></div>
            </div>
            <div class="ax-right">
              <div class="ax-card ax-pchart"><p class="ax-ct">Revenue per MW per year <em>monthly, annualised</em></p>{chart}
                <div class="ax-leg"><span class="ax-l-ra"><i></i>Realised, A</span><span class="ax-l-rb"><i></i>Realised, B</span><span class="ax-l-ex"><i></i>Expected revenues</span><span class="ax-l-band"><i></i>±10%</span></div></div>
              <div class="ax-card ax-pq"><p class="ax-ct">Quotes, side by side <em>4 offers from trusted optimizers</em></p>{qr}
                <p class="ax-note">Expected capture rate on your site, from a backtest of each optimizer. Optimizer A is your current optimizer.</p></div>
            </div>
            <div class="ax-toast ax-t1"><span class="ax-bell"><svg viewBox="0 0 24 24"><path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4zM10 20a2 2 0 0 0 4 0"/></svg></span>
              <div><b>Capture rate below expected for 6 months</b><span class="ax-t1b">Owner alerted. We ask trusted optimizers for a quote.</span></div></div>
            <div class="ax-res">
              <div class="ax-rc ax-off"><p class="cs-tag">Without the ICM</p><p class="ax-big">EUR {fmt(before)}</p><p class="ax-rcap">per MW per year</p>
                <ul><li><span>Missed opportunity</span><b>Unknown</b></li><li><span>Other optimizers</span><b>Unknown</b></li></ul><div class="ax-mg"><svg viewBox="0 0 400 215" aria-hidden="true"><path d="M44,196 A156,156 0 0 1 356,196" class="ax-mg-bg" pathLength="100"/><path d="M44,196 A156,156 0 0 1 356,196" class="ax-mg-fg ax-mg-a" pathLength="100" stroke-dasharray="100" stroke-dashoffset="{100-CA}"/></svg><b>{CA}%</b><span>capture rate</span></div></div>
              <div class="ax-rc ax-on"><p class="cs-tag">With the ICM</p><p class="ax-big"><span class="js-fm-gain">EUR {fmt(before)}</span></p><p class="ax-rcap">per MW per year</p>
                <ul><li><span>Extra revenue</span><b class="js-fm-plus">+EUR 0</b></li><li><span>Offers compared</span><b>4</b></li></ul><div class="ax-mg"><svg viewBox="0 0 400 215" aria-hidden="true"><path d="M44,196 A156,156 0 0 1 356,196" class="ax-mg-bg" pathLength="100"/><path d="M44,196 A156,156 0 0 1 356,196" class="ax-mg-fg ax-mg-b" pathLength="100" stroke-dasharray="100" stroke-dashoffset="{100-CB}"/></svg><b>{CB}%</b><span>capture rate</span></div></div>
            </div>
          </div>
        </div>
      </div>
      <div class="fm-ctrl"><button type="button" class="fm-play js-fm-play" aria-label="Pause">Pause</button>
        <div class="fm-speed" role="group" aria-label="Playback speed"><button type="button" data-s="0.5">0.5×</button><button type="button" data-s="0.75">0.75×</button><button type="button" data-s="1" class="on">1×</button><button type="button" data-s="1.5">1.5×</button><button type="button" data-s="2">2×</button></div></div>
    </div>"""

CR_VARIANTS = {'J': ('Film: I, E and G combined', _cr_film), 'I': ('Animated: 46% to 83% after the switch', _cr_anim), 'E': ('Product cards, Ramp style', _cr_ui),
               'G': ('Without vs with the ICM', _cr_split), 'H': ('Dots per month, like the home page', _cr_dots)}

def cr_section(v, label=False):
    tag = f'<span class="cr-var">Variant {v}: {CR_VARIANTS[v][0]}</span>' if label else ''
    return f"""<section class="dark cr-sec cr-{v}">{tag}<div class="wrap">{CR_H}{CR_P}<p class="cr-note-ill">Illustrative example.</p><div class="cr-vis">{CR_VARIANTS[v][1]()}</div></div></section>"""

CR_CHOICE = os.environ.get('CR_VARIANT', '')
FILM_LIVE = False  # set True once approved to show the film on the live site

GS_STEPS = f'''<section class="dark gs-steps" id="steps">
  <div class="wrap">
    <h2>Get started in three easy steps</h2>
    <div class="gs-grid">
      <div>{GS_ICONS['mail']}<p><b>Step 1: Enter your work email.</b> <span>Enter your business email to begin. You'll be prompted to answer a few questions about your context and objectives.</span></p></div>
      <div>{GS_ICONS['form']}<p><b>Step 2: Provide your details.</b> <span>We'll ask for basic information such as the battery size (MW/MWh) and your dispatch constraints (GTV).</span></p></div>
      <div>{GS_ICONS['key']}<p><b>Step 3: Navigate your reality.</b> <span>Most businesses receive a custom view of their potential earnings within one working day. It's the draft we start from.</span></p></div>
    </div>
  </div>
</section>'''

GS_SECURE = f'''<section class="dark gs-secure" id="get-started">
  <div class="wrap">
    {gs_form('b')}
  </div>
</section>'''

PROTO_URL = 'https://claude.ai/artifact/4JJ9cpLm8pJMx9ZwknDKti'
GATE = f'''<div class="gate" id="gate" hidden data-target="{PROTO_URL}">
  <img class="gate-bg" src="/assets/img/backtest-example.jpg" alt="" width="1440" height="900">
  <div class="gate-card" role="dialog" aria-modal="true" aria-labelledby="gate-h">
    <button type="button" class="gate-x js-gate-close" aria-label="Close">&times;</button>
    <h2 id="gate-h" class="sr-only">Welcome to the ICM</h2>
    <div class="gate-frame" data-form="4W7Pk7S5YTus"></div>
    <a class="gate-go js-gate-go" href="/bess-backtest/example/">Entered your email? Open the example report</a>
  </div>
</div>'''

def solutions(t):
    extras = {
      'configurator': 'For owners and developers who plan a battery, stand-alone or co-located with solar, wind or other assets, and for installers who size systems for customers.',
      'backtest': 'For owners of operating batteries, and for installers who want to give every customer an independent view of what the battery earns.',
      'broker': 'For owners who are keen to understand which high-performing optimizers exist and what they offer to optimize their battery.',
    }
    blocks = ''.join(sol_block(i, k, n, h, lead, body, extras[k]) for i, (k, n, h, lead, body) in enumerate(PROPS))
    hero = f"""    <div class="page-hero sol-hero2" id="main">
      <div class="sh-l">
        <h1>See how the ICM works</h1>
        <p>The ICM brings clarity, trusted partners and continuity to those adding capacity to the grid. Together, we secure the true value of your BESS asset.</p>
        {gs_form('a')}
      </div>
      <div class="sh-r"><img src="/assets/img/solutions-veins-bright.jpg" alt="" width="1600" height="900"></div>
    </div>"""
    body = f"""{cr_section('J') if (RES_EXTRAS or FILM_LIVE) else ''}<section class="sol-light sol-wrap sol-noicon" id="solutions">
  <div class="wrap">
{blocks}  </div>
</section>
{GS_STEPS}
{GS_SECURE}
{faq_block(NEWFAQS, 'Frequently asked questions')}"""
    return page_shell(t, '/solutions/', 'Solutions: BESS Calculator, BESS Backtest and BESS Broker | The ICM',
        'How the ICM helps BESS owners: size the right battery system, backtest its performance against its full potential and find a trusted optimizer.', hero, body)

def prop_page(t, k, path, name, title, desc, lead, what, steps, who, extra_top='', faq=None):
    cards = ''.join(f'<div class="rule"><h3>{h}</h3><p>{p}</p></div>' for h, p in steps)
    whatl = ''.join(f'<li>{x}</li>' for x in what)
    hero = f"""    <div class="page-hero" id="main">
      <span class="eyebrow">{name}</span>
      <h1>{lead[0]}</h1>
      <p>{lead[1]}</p>
      <div class="hero-ctas"><a class="btn btn-lilac" href="{TALK}?topic={k}">{t['talk']}</a></div>
    </div>"""
    body = f"""{extra_top}<section class="prop-what">
  <div class="wrap two">
    <div class="section-head"><span class="eyebrow">What you get</span><h2>{what[0] if False else name + ' in short'}</h2></div>
    <ul class="check">{whatl}</ul>
  </div>
</section>
<section class="rules-wrap">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">How it works</span><h2>Simple steps, from first call to result</h2></div>
    <div class="rules-row">{cards}</div>
    <p class="prop-who"><b>Who it is for.</b> {who}</p>
  </div>
</section>
{faq_block(faq, 'Frequently asked questions') if faq else ''}
{cta_band(t, topic=k)}"""
    return page_shell(t, path, title, desc, hero, body)

def configurator_page(t):
    return prop_page(t, 'configurator', '/solutions/#configurator', 'BESS Calculator',
      'BESS Calculator: size a battery and value the business case | The ICM',
      'Find the optimal battery storage system for your site: size power and capacity, simulate revenue streams and degradation, and see payback and return.',
      ('Find the optimal system for your context', 'A BESS configurator and calculator that sizes the battery for your site and shows whether the investment is technically and financially feasible.'),
      ['Size: how many MW of power and MWh of storage fit your site, your load and your PV or wind profile.',
       'Business case: payback period, net present value and return on investment of the project.',
       'Revenue streams: energy arbitrage, peak shaving, and the imbalance and ancillary service markets.',
       'Lifetime: degradation from cycling and ageing, so you know when capacity declines over 10 to 15 years.'],
      [('Share your context', 'Your site, grid connection and load or generation profile, and what you want from the battery.'),
       ('We size and simulate', 'We test system sizes against your profile and the revenue streams that apply to your site.'),
       ('You see the business case', 'A clear comparison of options, with the assumptions written down, ready for your bank, partner or board.')],
      'Owners and developers planning a battery next to solar, wind or a large energy user, and installers who size systems for customers.')

FLOWER = 'https://www.flower.se/insights/case/ra-energy-switch-optimizer/'
PEN = '<svg class="pen" viewBox="0 0 16 16" aria-hidden="true"><path d="M11.5 2.5l2 2L6 12l-2.8.8L4 10z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>'

def w_pill(cls, label, val, mx=''):
    return f'<label class="pill"><input class="in fit {cls}" type="number" min="1" {mx} step="1" value="{val}" aria-label="{label}">{PEN}</label>'

def w_sentence():
    return f"""<span class="ws1"><b>Same battery, same site, 30% more revenue.</b> <a class="story-src" href="{FLOWER}" target="_blank" rel="noopener">Source: Flower case</a></span><span class="ws1b">Many have a nagging sense that they are leaving money on the table, fed by anecdotes of businesses realising 30% higher revenues.</span><span class="ws2">A 30% gap adds up to <b class="out js-gap">EUR 55.5k</b> per MW per year for a {w_pill('js-mw','Battery size in MW',10,'max="500"')} MW battery that delivered EUR {w_pill('js-rev','Revenue in thousand EUR per MW per year',185)}k per MW per year.</span>"""

def w_hint():
    return f'<p class="hint">{PEN}Enter figures to adjust. Illustrative example.</p>'

WLEG = """<span><i class="d"></i>Delivered <b class="js-del">EUR 1,850,000</b></span><span><i class="m"></i>Missed <b class="js-mis">EUR 555,000</b></span><span class="unit js-unit">1 dot = EUR 10,000 a year</span>"""

def w_dots(rows=10, legend=True):
    cap = f'<figcaption class="why-legend">{WLEG}</figcaption>' if legend else ''
    return f"""<figure class="why-fig" aria-hidden="true"><svg class="js-dots" data-rows="{rows}" role="presentation"></svg>{cap}</figure>"""

WCAUSES = [('The wrong configuration', 'The battery is not sized or set up for what your site allows.', '/solutions/#configurator', 'BESS Calculator'),
           ('The wrong optimizer', 'Another optimizer would earn more with the same battery.', '/solutions/#broker', 'BESS Broker'),
           ('Too little monitoring', 'Underperformance goes unnoticed, so it carries on.', '/solutions/#backtest', 'BESS Backtest')]

def w_can():
    return ''

def w_head(tag='h2'):
    return '<%s class="story-h">It\'s a waste to miss out on <b class="out js-missed">EUR 555,000</b> a year.</%s>' % (tag, tag)

BL1, BL2, BL3 = ('<b>Suboptimal configuration.</b> The MW/MWh installed directly affects your return on investment. A poor set-up can cost you from day one.', '<b>Underperforming optimizer.</b> New players with better algorithms keep entering the market. Staying with yours can pose a risk.', '<b>Too little monitoring.</b> Without knowing how far you are from your full potential, your BESS revenue is a black box. Underperformance can go unnoticed for years.')

def why_section(v='1'):
    cs = WCAUSES
    if v == '1':   # sentence + dots left, causes right
        causes = ''.join(f'<li><b>{a}</b><span>{b}</span><a href="{h}">{n} →</a></li>' for a, b, h, n in cs)
        inner = f"""<div class="wy-head">{w_head()}</div>
    <div class="wy-grid">
      <div class="story"><p class="story-p">{w_sentence()}</p>{w_hint()}{w_dots()}</div>
      <div class="wy-card"><h3>Where revenue leaks</h3><ul class="wy-causes">{causes}</ul></div>
    </div>
    {w_can()}"""
    elif v == '2':  # dots hero, compact input bar, three columns
        causes = ''.join(f'<div><b>{a}</b><p>{b}</p><a href="{h}">{n} →</a></div>' for a, b, h, n in cs)
        inner = f"""<div class="wy-head">{w_head()}</div>
    <div class="wy-bar"><span>My battery</span><label>{w_pill('js-mw','Project size in MW',10,'max="500"')} MW</label><label>{w_pill('js-rev','Revenue in thousand EUR per MW per year',185)} EUR k per MW per year</label><span class="wy-bar-r">A similar asset can deliver <a class="story-link" href="{FLOWER}" target="_blank" rel="noopener">30% more</a>: <b class="out js-gap">EUR 55.5k</b> per MW</span></div>
    <div class="story wy-wide">{w_dots(8)}</div>
    <div class="wy-cols">{causes}</div>
    {w_can()}"""
    elif v == '3':  # big number + light form card
        causes = ''.join(f'<a class="wy-chip" href="{h}"><b>{a}</b><span>{n} →</span></a>' for a, b, h, n in cs)
        inner = f"""<div class="wy-splitR">
      <div><p class="wy-k">Missed a year</p><p class="wy-big out js-missed">EUR 555,000</p><p class="wy-lead">It's a waste to miss out. A similar BESS asset, same size and setup, can deliver <a class="story-link" href="{FLOWER}" target="_blank" rel="noopener">30% more revenue</a>.</p>{w_can()}</div>
      <div class="wy-form"><h3>Your battery</h3>
        <label>Project size<span>{w_pill('js-mw','Project size in MW',10,'max="500"')} MW</span></label>
        <label>Revenue delivered<span>{w_pill('js-rev','Revenue in thousand EUR per MW per year',185)} EUR k per MW per year</span></label>
        <p class="wy-res">A similar asset could earn <b class="js-should">EUR 240.5k</b> per MW per year, <b class="js-gap">EUR 55.5k</b> more.</p>
        <p class="hint">{PEN}Enter figures to adjust. Illustrative example.</p></div>
    </div>
    <p class="wy-k wy-k2">Where it leaks, and what fixes it</p><div class="wy-chips">{causes}</div>"""
    elif v == '4':  # dark dots card left, light card right
        causes = ''.join(f'<li><b>{a}.</b> {b} <a href="{h}">{n} →</a></li>' for a, b, h, n in cs)
        inner = f"""<div class="wy-split wy-split4">
      <div class="wy-dark">{w_head('h2')}{w_dots()}</div>
      <div class="wy-light"><p class="wy-k">What is missing</p><p class="story-p story">{w_sentence()}</p>{w_hint()}<h3>Three places it leaks</h3><ol class="wy-causes">{causes}</ol></div>
    </div>
    {w_can()}"""
    elif v == '13':
        bl = ''.join(f'<li>{x}</li>' for x in (BL1, BL2, BL3))
        inner = f"""<div class="story wy-wide wy-v13">
      <div class="wy-panel"><div class="wy-top"><div class="wy-top-l">{w_head()}</div></div>
      <div class="wy-dotsrow">{w_dots(9, legend=False)}<div class="wy-side"><div class="why-legend wy-legr">{WLEG}</div>{w_hint()}</div></div></div>
      <div class="wy-two wy-plain wy-cards">
        <div><p class="wy-k">What is missing</p><p class="story-p story">{w_sentence()}</p></div>
        <div><p class="wy-k">Where it leaks</p><ul class="wy-bul">{bl}</ul></div>
      </div>
    </div>"""
    elif v in ('10', '11', '12'):
        lk = lambda h, n: f'<a class="story-link" href="{h}">{n}</a>'
        leaks = (f'Revenue leaks in three places. <b>The wrong configuration:</b> the battery is not sized or set up for what your site allows ({lk("/solutions/#configurator", "BESS Calculator")}). '
                 f'<b>The wrong optimizer:</b> another optimizer would earn more with the same battery ({lk("/solutions/#broker", "BESS Broker")}). '
                 f'<b>Too little monitoring:</b> underperformance goes unnoticed, so it carries on ({lk("/solutions/#backtest", "BESS Backtest")}).')
        check = f"""<p class="wy-k">What is missing</p><p class="story-p story">{w_sentence()}</p>{w_hint()}"""
        leaksb = f"""<p class="wy-k">Where it leaks</p><p class="story-p story">{leaks}</p>"""
        if v == '10':   # two equal light cards, dots below
            inner = f"""<div class="wy-head">{w_head()}</div>
    <div class="wy-two"><div class="wy-light">{check}</div><div class="wy-light">{leaksb}</div></div>
    <div class="story wy-wide">{w_dots(8)}</div>"""
        elif v == '11': # two plain columns separated by a rule, same type
            inner = f"""<div class="wy-head">{w_head()}</div>
    <div class="wy-two wy-plain"><div>{check}</div><div>{leaksb}</div></div>
    <div class="story wy-wide">{w_dots(8)}</div>"""
        else:           # one light card, two halves, dots inside
            inner = f"""<div class="wy-head">{w_head()}</div>
    <div class="wy-light wy-one"><div class="wy-two wy-halves"><div>{check}</div><div>{leaksb}</div></div>{w_dots(6)}</div>"""
    elif v in ('6', '7', '8', '9'):
        cols = ''.join(f'<div><b>{a}</b><p>{b}</p><a href="{h}">{n} →</a></div>' for a, b, h, n in cs)
        check = f"""<p class="wy-k">What is missing</p><p class="story-p story">{w_sentence()}</p>{w_hint()}"""
        if v == '6':    # 4's split with 2's clean columns below
            inner = f"""<div class="wy-split wy-split4">
      <div class="wy-dark">{w_head('h2')}{w_dots()}</div>
      <div class="wy-light">{check}</div>
    </div>
    <p class="wy-k wy-k2">Where it leaks</p><div class="wy-cols">{cols}</div>"""
        elif v == '7':  # check card left, dots right, columns below
            inner = f"""<div class="wy-head">{w_head()}</div>
    <div class="wy-split wy-split7">
      <div class="wy-light">{check}</div>
      <div class="story">{w_dots()}</div>
    </div>
    <p class="wy-k wy-k2">Where it leaks</p><div class="wy-cols">{cols}</div>"""
        elif v == '8':  # dark left: headline + clean leaks, light right: check + dots on light
            leaks = ''.join(f'<div><b>{a}</b><p>{b}</p><a href="{h}">{n} →</a></div>' for a, b, h, n in cs)
            inner = f"""<div class="wy-split wy-split4 wy-split8">
      <div class="wy-dark">{w_head('h2')}<div class="wy-colL wy-two wy-plain">{leaks}</div></div>
      <div class="wy-light wy-ondots">{check}{w_dots()}</div>
    </div>"""
        else:           # 9: headline, light strip with the check, full-width dots, columns
            inner = f"""<div class="wy-head">{w_head()}</div>
    <div class="wy-light wy-strip">{check}</div>
    <div class="story wy-wide">{w_dots(8)}</div>
    <p class="wy-k wy-k2">Where it leaks</p><div class="wy-cols">{cols}</div>"""
    else:           # '5' editorial, no dots, big numerals
        causes = ''.join(f'<li><span class="wy-n">{i+1:02d}</span><div><b>{a}</b><p>{b}</p><a href="{h}">{n} →</a></div></li>' for i, (a, b, h, n) in enumerate(cs))
        inner = f"""<div class="wy-head">{w_head()}</div>
    <div class="story wy-center"><p class="story-p">{w_sentence()}</p>{w_hint()}</div>
    <ol class="wy-num">{causes}</ol>
    {w_can()}"""
    return f"""<section class="dark why-sec wy-{v}" id="why"><div class="wrap why-calc"><span class="eyebrow why-eyebrow">Our why</span>
    {inner}
  </div></section>"""


def backtest_page(t):
    example = '''<section class="example-sec">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">See it for yourself</span><h2>An example BESS Backtest report</h2><p>Open an interactive report with fictional data: the capture rate, what drives it and the downtime, with the method written underneath.</p></div>
    <a class="example-card" href="/bess-backtest/example/" aria-label="Open the example BESS Backtest report">
      <img src="/assets/img/backtest-example.jpg" alt="Screenshot of an example BESS Backtest report showing revenue, capture rate and drivers" width="1440" height="900" loading="lazy">
      <span class="btn btn-lilac">Open the example report</span>
    </a>
  </div>
</section>
'''
    return prop_page(t, 'backtest', '/solutions/#backtest', 'BESS Backtest',
      'BESS Backtest: how much of its full potential does your battery capture? | The ICM',
      'The BESS Backtest compares what a battery earned with the most it could have earned on its site. An independent view on BESS performance, optimizer results and downtime.',
      ('Monitor the performance of your BESS', 'An independent view on what a trader with perfect foresight could have reasonably earned, and the share of that your battery captured.'),
      ['Capture rate: realised results compared with the full potential of your site, within its grid, warranty and dispatch limits.',
       'Clear expectations: expected results are set at 80% of the full potential, so you know what good looks like.',
       'Downtime apart: hardware faults are reported as their own driver and are not held against your optimizer.',
       'Checked by people: every result is quality controlled before it reaches you, and final after three months.'],
      [('Share your data', 'Your optimizer report and quarter-hour meter data, plus the documents on your connection. We give you the list.'),
       ('We calculate the full potential', 'We model the best result your site could achieve, hour by hour, and compare it with what the battery earned.'),
       ('You see the result and its drivers', 'The capture rate, split into trading, downtime and site limits. If it falls short, you choose what to do next.')],
      'Owners of operating batteries, and installers who deliver a BESS Backtest with each installation to give customers an independent verdict.',
      extra_top=example, faq=NEWFAQS)

def broker_page(t):
    return prop_page(t, 'broker', '/solutions/#broker', 'BESS Broker',
      'BESS Broker: find and compare a trusted optimizer for your BESS | The ICM',
      'Outsource the search for a trusted BESS optimizer: fill in one form, compare offers side by side and get help moving to the optimizer you choose.',
      ('Outsource the research for a trusted optimizer', 'Fill in one form. We ask trusted optimizers for a quote and show you the offers side by side, so you do not have to run the search yourself.'),
      ['One form that captures what optimizers need to know to make you an offer.',
       'Offers side by side, written to the same format, so you can compare them on the terms that matter.',
       'Optionally, a backtest of what the other optimizers would have earned on your site.',
       'Help with the move to your new optimizer, so your battery keeps earning while it changes hands.'],
      [('Complete one form', 'Your asset, your set-up and what you need from an optimizer, captured once.'),
       ('Compare the quotes', 'We request quotes from trusted optimizers, put them side by side and help you assess them.'),
       ('Move with confidence', 'We help you agree the contract and stay with you until the first month of trading with your new optimizer.')],
      'Owners whose battery objectively earns less than it could, and who want a trusted partner without running the search themselves.')

def talk_proof(v):
    """Block under the form (where the Canva design has a review). Variants A-E for review."""
    if v == 'A':
        inner = '''<img class="tp-logo" src="/assets/img/provincie-noord-holland.png" alt="Province of Noord-Holland" width="1200" height="233" loading="lazy">
      <div><h2>Supported by the Province of Noord-Holland</h2><p>The ICM received early-phase funding (Vroegefasefinanciering) from the Province of Noord-Holland.</p></div>'''
    elif v == 'B':
        inner = '''<img class="tp-photo" src="/assets/img/about-pylon.jpg" alt="Electricity pylon against the sky" width="1200" height="900" loading="lazy">
      <div><h2>An independent view at every stage of a battery's life</h2><p>Size the right system before you build, monitor its performance while it operates and find a trusted optimizer when there is more to earn.</p></div>'''
    elif v == 'C':
        inner = '''<div class="tp-stat"><b>30%</b><span>more revenue</span></div>
      <div><h2>Comparable batteries can earn very different amounts</h2><p>A similar BESS asset, same size and setup, delivered 30% more revenue after switching optimizer. We help you find out where your battery stands.</p><p class="tp-src"><a href="https://www.flower.se/insights/case/ra-energy-switch-optimizer/" target="_blank" rel="noopener">Source: Flower and RA Energy case →</a></p></div>'''
    elif v == 'D':
        inner = '''<div><h2>What you can expect from us</h2><ul class="tp-list"><li><b>Independent.</b> We do not own, install or optimize.</li><li><b>No obligation.</b> A 45-minute call about your context and objectives.</li><li><b>Then a full proposal.</b> You decide what to do next.</li></ul></div>'''
    else:
        inner = '''<img class="tp-face" src="/assets/team-ideles.jpg" alt="Idelès Kaandorp" width="600" height="600" loading="lazy">
      <div><h2>You talk to the founder</h2><p>Idelès Kaandorp, founder of the ICM, walks through your context and objectives with you. Afterwards you receive a full proposal.</p></div>'''
    return f'''<section class="dark talk-proof"><div class="wrap"><div class="tp-card tp-{v}">
      {inner}
    </div></div></section>'''

def talk(t, variant=None):
    variant = variant or os.environ.get('TALK_VARIANT', 'A')
    hero = """    <div class="talk-hero" id="main">
      <div class="talk-copy">
        <span class="eyebrow">Talk to us</span>
        <h1><span class="nw">Secure the true value</span><br><span class="nw">of your BESS asset</span></h1>
        <p>Ready to learn more? Use the form to give us a bit more information about your context and objectives.</p>
        <p>Alternatively, you can email us directly at <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>.</p>
      </div>
      <div class="form fillout">
        <div style="width:100%;height:640px" data-fillout-id="icWpPN8hsgus" data-fillout-embed-type="standard" data-fillout-inherit-parameters data-fillout-dynamic-resize></div>
        <script src="https://server.fillout.com/embed/v1/" defer></script>
        <noscript><a href="https://forms.fillout.com/t/icWpPN8hsgus">Open the form</a></noscript>
      </div>
    </div>"""
    body = f"""{GS_STEPS.replace('class="dark gs-steps"', 'class="dark gs-steps talk-expect"')}
"""
    return page_shell(t, TALK, 'Talk to us: get started with your BESS | The ICM',
        'Get started with the ICM in three steps: enter a work email, share the basic details of your battery and receive a custom report with expected revenues within one working day.', hero, body)


SOL_REDIRECT = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Solutions | The ICM</title><meta name="robots" content="noindex"><link rel="canonical" href="https://icm.energy/solutions/#KEY"><meta http-equiv="refresh" content="0; url=/solutions/#KEY"></head><body><a href="/solutions/#KEY">All solutions are on one page.</a></body></html>'''
REDIRECT = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Careers | The ICM</title><meta name="robots" content="noindex"><link rel="canonical" href="https://icm.energy/company/#careers"><meta http-equiv="refresh" content="0; url=/company/#careers"></head><body><a href="/company/#careers">Careers have moved to our company page.</a></body></html>'''

def write(rel, html):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(html)

for lang in LANGS:
    t = T[lang]
    pre = '' if lang == 'en' else 'nl/'
    write(pre + 'index.html', home(t))
    if os.environ.get('WHY_OPTIONS'):
        opts = ''.join(f'<div class="dark"><p class="tp-label">Version {v}</p></div>' + why_section(v) for v in ('10','11','12'))
        write('why-options/index.html', page_shell(t, '/why-options/', 'Options', '', '<div class="page-hero" id="main"><h1>Our why: 5 versions</h1><p>Choose one for the homepage. All figures can be changed.</p></div>', opts))
    write(pre + 'terms/index.html', terms(t))
    write(pre + 'privacy/index.html', privacy(t))
    if lang == 'en': write('cookies/index.html', cookies(t))
    if lang == 'en':
        write('careers/index.html', REDIRECT)
        write('register/index.html', '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Get started | The ICM</title><meta name="robots" content="noindex"><link rel="canonical" href="https://icm.energy/talk-to-us/"><meta http-equiv="refresh" content="0; url=/talk-to-us/"></head><body><a href="/talk-to-us/">Get started</a></body></html>')
        write('resources/index.html', resources(t))
        write('company/index.html', company(t))
        write('solutions/index.html', solutions(t))
        for k in ('configurator', 'backtest', 'broker'):
            write(f'bess-{k}/index.html', SOL_REDIRECT.replace('KEY', k))
        write('talk-to-us/index.html', talk(t))
        if os.environ.get('TALK_OPTIONS'):
            opts = ''.join(f'<div class="dark"><p class="tp-label">Option {v}</p></div>' + talk_proof(v) for v in 'ABCDE')
            write('talk-to-us/options/index.html', page_shell(t, '/talk-to-us/options/', 'Options', '', '<div class="page-hero" id="main"><h1>Proof block: 5 options</h1><p>Choose one for under the form on Talk to us.</p></div>', opts))
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
<script src="/main.js?v={V_JS}" defer></script>
</body>
</html>
"""
write('methodology/index.html', '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Solutions | The ICM</title><meta name="robots" content="noindex"><link rel="canonical" href="https://icm.energy/solutions/"><meta http-equiv="refresh" content="0; url=/solutions/"></head><body><a href="/solutions/">Go to our solutions</a></body></html>')
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
write('demo/index.html', '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Example report | The ICM</title><meta name="robots" content="noindex"><link rel="canonical" href="https://icm.energy/bess-backtest/example/"><meta http-equiv="refresh" content="0; url=/bess-backtest/example/"></head><body><a href="/bess-backtest/example/">See an example report</a></body></html>')

# BESS Backtest example report (fictional data), served at /bess-backtest/example/ with a way back to the site.
write('bess-backtest/example/index.html', open(os.path.join(ROOT, '_build', 'backtest-example.html'), encoding='utf-8').read())
import shutil
if RES_EXTRAS:
    write('bess-calculator/index.html', open(os.path.join(ROOT, '_build', 'bess-calculator.html'), encoding='utf-8').read())
elif os.path.isdir(os.path.join(ROOT, 'bess-calculator')):
    shutil.rmtree(os.path.join(ROOT, 'bess-calculator'))
print('demo built')
