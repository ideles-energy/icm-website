"""Builds the icm.energy pages (EN + NL) from one template.

Run from the repo root:  python3 _build/build.py
Edit texts in the T dictionary below, then rebuild. Methodology is edited directly in methodology/index.html.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANGS = ['en']  # add 'nl' once the Dutch texts are proofread
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
  book='Talk to us →', how_link='How it works →',
  chart_title='Project score: 87% of the peer benchmark', chart_sub='EUR per MW per year, by month · gross revenue',
  chart_aria="Illustrative chart: a project's monthly revenue per MW compared with the peer benchmark",
  months=['Oct','Dec','Feb','Apr','Jun','Aug'], chart_you='Your project', chart_peer='Peer benchmark (≥ 5 assets, ≥ 3 organisations)',
  chart_note='Illustrative example with fictional data.',
  why_eyebrow='Why it matters', why_h='BESS assets deliver vastly different results',
  why_p='Independent information on what batteries earn is missing. Some discovered they\'re missing out on 30,000 to 70,000 euro per MW per year. Are you? Without a BESS Benchmark, there is no way of knowing.',
  stats=['EUR 145k', 'EUR 185k', 'EUR 240k'], per='per MW per year', stats_note='Illustrative example: gross market revenues of three BESS assets.',
  learn='How it works →',
  which='Which one is yours?',
  how_eyebrow='How it works', how_h='Our membership model',
  rules=[
   ('Registration', 'We ask new members to share 6 months of BESS performance data and stay a member for at least 3 months. After that, membership can be cancelled monthly.'),
   ('Contribution', 'Members pay 0.5% of what their battery earned that month. At €15,000 per MW, that is €75 per MW. After referring 5 members, the contribution drops to 0.1% for 6 months.'),
   ('Give-to-get', 'Members\' data is anonymised and added to the BESS Benchmark; members only see the BESS Benchmark for the months to which they have contributed. The same "give-to-get" principle applies to financiers, installers and advisers who want access.'),
  ],
  shot_alt='The BESS Benchmark app: project score, revenue per MW and the benchmark over the last 12 months (fictional example data)',
  story_note='Illustrative. Change the numbers in cyan to see your own missed opportunity.',
  calc_eyebrow='Calculator', calc_h='What is your missed opportunity?',
  calc_p='Enter your battery and what it earns today. See what you could have earned if it had matched comparable batteries.',
  calc_mw='Battery size', calc_months='Period', calc_months_unit='months', calc_rev='Your revenue today',
  calc_assume='Assumption: comparable batteries earned 30% more per MW. Illustrative – the BESS Benchmark shows your real gap.',
  calc_you='Your battery', calc_bench='Comparable batteries', calc_missed='Missed opportunity over 6 months', calc_cta='Find out your real gap →',
  demo_eyebrow='See it in action', demo_h='Your EUR per MW per year, next to the BESS Benchmark', demo_p='The BESS Benchmark is a dynamic view on the EUR per MW per year of your assets and those of our other members.', demo_note='Fictional example data.',
  demo_btn='Try the interactive demo →', demo_title='BESS Benchmark – interactive demo (fictional data)', demo_new='Open in a new tab',
  shot_cap='The BESS Benchmark is a dynamic view on the EUR per MW per year of your assets and those of our other members. Fictional example data.',
  faq_link='Read the FAQ →',
  real_eyebrow='Real data, not a model', real_h='Why real revenues beat a simulated index',
  idx_h='A simulated revenue index', idx=['Models a theoretical battery with fixed assumptions','Assumes a full grid connection and no downtime','Cannot tell you how your optimizer performs comparatively'],
  ours_h='The BESS Benchmark', ours=['Is based on realised revenues, as members received them from their optimizers','Anticipates restrictions such as CSC terms, TDTR limits and downtime','Compares your battery with batteries set up like yours'],
  about_eyebrow='About the ICM', about_h='Why an Independent Capacity Market matters',
  about_p='We are not owners. We are not optimizers. Nor will we ever be. We are an energy tech company, serving those who add capacity to the grid, but are in the dark on the potential of their assets. We compare BESS-to-BESS, introduce owners to optimizers and oversee the switch, so your battery keeps earning.',
  open_now='Open now', waitlist='Join the waitlist',
  p1=('BESS Benchmark','Compare your earnings BESS-to-BESS to understand the true value of your asset.'),
  p2=('BESS Broker','Outsource the search for a trusted optimizer. One form, a standardised process and terms banks appreciate.'),
  p3=('BESS Integration','Embed a new project into the portfolio. Our API platform derisks a switch by connecting optimizers with local infra.'),
  contact_eyebrow='Talk to us', contact_h='Book time with us', contact_p='',
  prefer='Prefer email?', subject='BESS Benchmark intake request',
  f_name='Name', f_company='Company', f_email='Email', f_mw='Portfolio or project size in MW',
  f_msg='Tell us a little bit about your context and objectives', f_ph='E.g., asset of 3-30 MW, trading revenues below expectations, interested in the BESS Benchmark',
  f_submit='Send →', f_fine='We use your details only to contact you about the ICM.', f_ok='Thank you – we will be in touch.',
  foot_tag='The Independent Capacity Market (“the ICM”) brings clarity, trusted partners and continuity to those adding capacity to the grid.',
  founded='Founded by', foot_bench='Learn more', methodology='Methodology', contact='Contact',
  terms='Terms & Conditions', privacy='Privacy statement', disclaimer='Benchmark figures are outcome data as reported by optimizers, not advice.',
  faq_title='Frequently asked questions – BESS Benchmark | The ICM', faq_desc='Answers to common questions about the BESS Benchmark: data, costs, privacy and who can join.',
  faq_h='Frequently asked questions', faq_lead='Short answers about the BESS Benchmark. Missing something? Just ask us.', faq_more='Still have a question?',
  faqs=[
   ('How does the BESS Benchmark help me?', '<ul><li><b>Are we doing well?</b> See at a glance how much more or less your batteries earn than comparable batteries. Apples with apples, pears with pears. All data is anonymised.</li><li><b>What does an outage cost?</b> Insurance and warranty claims stand stronger with independent figures on what comparable batteries earned in the meantime.</li><li><b>Who pays for an optimizer that disappoints?</b> A benchmark lets you negotiate a floor with your optimizer, such as "at least 80% of the benchmark".</li><li><b>Is the business case realistic?</b> What comparable batteries really earned is a check on bankable forecasts, and a basis for sizing your next project and for performance warranties.</li></ul>'),
   ('How is this different from backtests, forecasts and battery indices?', 'Backtests, bankable forecasts and indices model what a battery could earn, with fixed assumptions. The BESS Benchmark shows what batteries actually earned: real revenues from optimizers\' statements, including grid restrictions, downtime and degradation. That makes it the reality check for those models.'),
   ('Which batteries can join?', 'Batteries in the Netherlands that an optimizer trades under a merchant contract. We focus on assets of 3 to 30 MW and decide per project in the intake.'),
   ('How does it work?', '<ol><li>A 45-minute intake, in which we go through your projects together.</li><li>You sign the membership form online and confirm the project form.</li><li>You share 6 months of history, then every month your optimizer\'s statement, for example by asking your optimizer to copy bessbenchmark@icm.energy.</li><li>Every month you see your project score online.</li></ol>'),
   ('What data do I share?', 'Per battery and per month: the revenue on your optimizer\'s statement (credit invoice, settlement or report), the optimizer fee, and the hours the battery was out of service. We never ask for bids, prices or trading strategies.'),
   ('Am I allowed to share this under my optimizer contract?', 'Usually yes. If your contract limits sharing with third parties, you and your optimizer first sign a short mandate. Your optimizer then sends the statements to us directly.'),
   ('Who sees my data?', 'Only you see your own figures. Before your data enters the benchmark, we remove your name, the asset name, EAN, location and optimizer. A benchmark is only shown for at least 5 batteries of other companies. We never share your data with optimizers, other members or our investors, and never publish results per optimizer.'),
   ('What do I get in return?', 'Every month, your project score: your revenue per MW divided by the benchmark. You see it per project and per battery, by month, quarter or year, and can filter by duration, project type, market qualifications and congestion contract. You can print it all as a report.'),
   ('What does it cost?', '0.5% of your battery\'s gross revenue for each month you are a member, excluding VAT. The historical months you share at the start are free, and so is any month with negative revenue. There are no other fees. After referring 5 members, you pay 0.1% for 6 months.'),
   ('How long do I commit?', 'The month you join plus two months. After that, membership renews monthly and you can cancel by email at the end of any month.'),
   ('Why do batteries with the same duration earn different amounts?', 'Revenue depends on more than duration: the markets a battery is active in, its grid connection and congestion contract, how often it is available, its state of health, and how well the optimizer trades it. That is why you can filter the benchmark by these characteristics, so you compare like with like.'),
   ('Can I share my results with my bank or optimizer?', 'Yes. You may share your benchmark results and project score with your advisers, financiers and optimizer, for example to negotiate contract terms.'),
   ('Will the ICM try to sell me something?', 'No. We only contact you if your project scored below 80% of the benchmark in at least 6 of the last 12 months, to discuss the option of another optimizer. Otherwise we leave you alone.'),
   ('Can I see which optimizer performs best?', 'No. The BESS Benchmark never shows results per optimizer or rankings of optimizers. If you want to explore other optimizers, our BESS Broker service runs that search for you.'),
   ('Is the ICM independent?', 'Yes. We do not own batteries and are not an optimizer, nor will we ever be. The same rules apply to every member, whatever their optimizer.'),
   ('How is the benchmark calculated?', 'We add up the revenue of all comparable batteries and divide it by their MW and the hours they were available, shown in euro per MW per year. Results are preliminary until no correction has come in for 3 months. All rules are in the <a href="/methodology/">methodology</a>.'),
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
  ('What we collect', 'When you use the contact form: your name, company, email address, portfolio or project size and message. When you visit the site: anonymous usage statistics through Google Analytics.'),
  ('Why', 'To answer your request and plan an intake, and to understand how the website is used. We do not sell your data or use it for other purposes.'),
  ('Who processes it for us', 'Fillout receives the contact form on our behalf and stores it in the United States. Google provides Google Analytics.'),
  ('How long we keep it', 'Contact details are kept as long as needed to follow up on your request, and at most two years after our last contact, unless you become a member.'),
  ('Your rights', 'You can ask to see, correct or delete your data, or object to its use, by emailing <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>. You can also file a complaint with the Dutch Data Protection Authority (Autoriteit Persoonsgegevens).'),
 ],
 'nl': [
  ('Wie we zijn', 'Independent Capacity Market B.V. (“de ICM”), Amsterdam, is verantwoordelijk voor de persoonsgegevens die hier worden beschreven. Contact: <a href="mailto:ideles@icm.energy">ideles@icm.energy</a>.'),
  ('Wat we verzamelen', 'Via het contactformulier: je naam, bedrijf, e-mailadres, omvang van je portefeuille en je bericht. Bij een bezoek aan de site: anonieme gebruiksstatistieken via Google Analytics.'),
  ('Waarom', 'Om je verzoek te beantwoorden en een intake te plannen, en om te begrijpen hoe de website wordt gebruikt. We verkopen je gegevens niet en gebruiken ze niet voor andere doelen.'),
  ('Wie ze voor ons verwerkt', 'Fillout ontvangt het contactformulier namens ons en slaat het op in de Verenigde Staten. Google levert Google Analytics.'),
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
          <li class="hide-sm"><a href="{b}#about">{t['nav_about']}</a></li>
{f'          <li><a class="lang" href="{other_href}" hreflang="{t["other_lang"]}" lang="{t["other_lang"]}">{t["other_label"]}</a></li>' + chr(10) if len(LANGS) > 1 else ''}          <li><a class="btn btn-lilac" href="{b}#contact">{t['talk']}</a></li>
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
          <li><a href="{b}faq/">{t['nav_faq']}</a></li>
          <li><a href="/methodology/">{t['methodology']}</a></li>
        </ul>
      </div>
      <div>
        <h3>{t['contact']}</h3>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
{f'          <li><a href="{other_href}" hreflang="{t["other_lang"]}" lang="{t["other_lang"]}">{t["other_name"]}</a></li>' + chr(10) if len(LANGS) > 1 else ''}
        </ul>
      </div>
    </div>
    <p class="legal"><span>© 2026 Independent Capacity Market B.V. · KvK 99958775</span><span><a href="{b}terms/">{t['terms']}</a></span><span><a href="{b}privacy/">{t['privacy']}</a></span></p>
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
    rules = '\n'.join(f'        <div class="rule"><h3>{h}</h3><p>{p}</p></div>' for h, p in t['rules'])
    def icon(n):
        bars = ''.join(f'<rect x="{7 + 11*k}" y="8" width="8" height="12" rx="1.5" fill="#0E1B2B"' + ('' if k < n else ' fill-opacity="0.18"') + '/>' for k in range(3))
        return f'<span class="stat-icon" aria-hidden="true"><svg viewBox="0 0 48 28"><rect x="2" y="3" width="38" height="22" rx="4" fill="none" stroke="#0E1B2B" stroke-width="3"/><rect x="41" y="10" width="5" height="8" rx="1.5" fill="#0E1B2B"/>{bars}</svg></span>'
    stats = '\n'.join(f'      <div class="stat">{icon(k + 1)}<p><b>{v}</b><span>{t["per"]}</span></p></div>' for k, v in enumerate(t['stats']))
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
    </div>
  </div>
</div>

<section class="dark" style="border-top:1px solid rgba(255,255,255,.08)">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">{t['why_eyebrow']}</span>
      <h2>{t['why_h']}</h2>
      <p>{t['why_p']}</p>
    </div>
    <div class="stats">
{stats}
    </div>
    <p class="stats-note">{t['stats_note']}</p>
    <div class="story" id="calculator" aria-live="polite">
      <p class="story-h">We missed out on <b class="out" id="s-missed">EUR 277,500</b>.</p>
      <p class="story-p">Our <input class="in" id="s-mw" type="number" min="1" max="500" step="1" value="10" aria-label="Project size in MW"> MW project earned EUR <input class="in in-w" id="s-rev" type="number" min="1" max="1000" step="1" value="185" aria-label="Revenue in thousand euro per MW per year">k per MW per year based on the last <input class="in" id="s-m" type="number" min="1" max="36" step="1" value="6" aria-label="Number of months"> months. Yet, a similar asset, same size and set-up, delivered 30% more over the same period: <b class="out" id="s-peer">EUR 240.5k</b> per MW per year.</p>
      <p class="story-note">{t['story_note']}</p>
    </div>
    <p class="which">{t['which']}</p>
    <div class="cta-row"><a class="btn btn-lilac" href="#contact">{t['book']}</a><a class="btn btn-outline" href="#how">{t['learn']}</a></div>
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
      <a class="demo-open" href="/demo/" data-demo><img src="/assets/benchmark-preview.jpg" width="1600" height="1016" alt="{t['shot_alt']}" loading="lazy"><span class="demo-badge">{t['demo_btn']}</span></a>
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
    </div>
    <div class="rules-row">
{rules}
    </div>
    <div class="cta-row" style="justify-content:flex-start;margin-top:36px">
      <a class="btn btn-lilac" href="#contact">{t['book']}</a>
      <a class="btn btn-outline teal" href="{b}faq/">{t['faq_link']}</a>
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
    return simple_page(t, t['base'] + 'terms/', t['other'] + 'terms/', t['terms_title'], t['terms_title'], t['terms_h'], '', body)

def privacy(t):
    secs = ''.join(f'<h2>{h}</h2><p>{p}</p>' for h, p in PRIVACY[t['lang']])
    body = f'    <div class="prose">{secs}<p style="color:var(--muted);font-size:14px">28-09-2026</p></div>'
    return simple_page(t, t['base'] + 'privacy/', t['other'] + 'privacy/', t['privacy_title'], t['privacy_title'], t['privacy_h'], '', body)

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
print('built')

# Methodology page, generated from _build/methodology.md (same text as the Methodology doc).
import markdown
FORMULAS = [
 '<div class="formula" role="math" aria-label="B sub m equals the sum over peers of revenue, divided by the sum over peers of MW times active hours, times 8760">B<sub>m</sub> = <span class="frac"><span>Σ<sub>i∈P</sub> R<sub>i,m</sub></span><span>Σ<sub>i∈P</sub> MW<sub>i</sub> × H<sub>i,m</sub></span></span> × 8,760</div>',
 '<div class="formula" role="math" aria-label="Score equals the project revenue per MW-hour over the period divided by the peer revenue per MW-hour over the same months, times 100 percent">Score<sub>T</sub> = <span class="frac"><span>Σ<sub>m∈T</sub> Σ<sub>i∈A</sub> R<sub>i,m</sub> ÷ Σ<sub>m∈T</sub> Σ<sub>i∈A</sub> MW<sub>i</sub> × H<sub>i,m</sub></span><span>Σ<sub>m∈T</sub> Σ<sub>j∈P<sub>m</sub></sub> R<sub>j,m</sub> ÷ Σ<sub>m∈T</sub> Σ<sub>j∈P<sub>m</sub></sub> MW<sub>j</sub> × H<sub>j,m</sub></span></span> × 100%</div>',
]
md = open(os.path.join(ROOT, '_build', 'methodology.md'), encoding='utf-8').read()
md = re.sub(r'^# .*\n', '', md, count=1)
version = re.search(r'Methodology version ([\d.]+) of ([^,]+),', md)
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
page = head(te, 'BESS Benchmark methodology – how we calculate revenue per MW | The ICM',
            f'How the ICM calculates the BESS Benchmark and the Project Score: data, quality control, active hours, duration bands, filters, anonymity thresholds and corrections. Version {version.group(1)}.',
            '/methodology/', None, ld, f'BESS Benchmark methodology, version {version.group(1)}') + f"""
<div class="hero-shell">
  <div class="wrap">
{nav(te, '/nl/')}
    <div class="page-hero" id="main">
      <span class="eyebrow">BESS Benchmark · Methodology v{version.group(1)} · {version.group(2)}</span>
      <h1>How we calculate the benchmark</h1>
      <p>Every rule that determines a Benchmark or a Project Score – from the data we collect to how we keep peers anonymous.</p>
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
write('methodology/index.html', page)
print('methodology built, v' + version.group(1), len(toc), 'sections')


# Interactive demo: the prototype (fictional data) served at /demo/, embedded on the homepage.
demo = open(os.path.join(ROOT, '_build', 'prototype.html'), encoding='utf-8').read()
demo = demo.replace('https://app.box.com/s/52dy3lyuocqpj3ss3rf47sdyveq7b1ir', '/methodology/').replace('https://app.box.com/s/3hmk2batlg2l2nv91e59gafzu2p1hek6', '/terms/')
demo = demo.replace('<title>BESS Benchmark Report</title>', '<title>BESS Benchmark – interactive demo | The ICM</title><meta name="robots" content="noindex">')
# no optimizer filter in the public demo (T&C 8.3: no results per optimizer)
demo = demo.replace('<div class="f"><span class="lab">Optimizer</span><div class="seg stack" data-key="opt"></div></div>', '')
demo = demo.replace("document.querySelectorAll('.seg[data-key]').forEach(el=>{\n  const key=el.dataset.key;", "document.querySelectorAll('.seg[data-key]').forEach(el=>{\n  const key=el.dataset.key;if(!OPTS[key])return;")
# a way back to the website (target=_top also works when the demo is shown inside the homepage dialog)
back = ('<div class="no-report" style="background:#061530;border-bottom:1px solid #1C3356;margin:-20px -16px 20px;padding:10px 16px;font:600 14px Figtree,system-ui,sans-serif">'
        '<a href="/#how" target="_top" style="color:#97F2F5;text-decoration:none">← Back to icm.energy</a></div>')
demo = demo.replace('<div class="wrap" id="page1">', back + '\n<div class="wrap" id="page1">', 1)
write('demo/index.html', demo)
print('demo built')
