---
name: partner-nulmeting
description: >-
  Nulmeting aan het begin van een Gaply-klantproject, in twee delen: een
  SEO-technische nulmeting van de website (staat alles in de sitemap, kan
  alles gelezen en geïndexeerd worden, klopt de paginastructuur) terwijl de
  site voor Gaply wordt geanalyseerd, en een vraag-nulmeting uit Inzichten
  (onderwerpen en vraagclusters met hun dekking) zodra de omgeving staat en
  Search Console gekoppeld is. Levert één startrapport dat de partner aan
  zijn eigen verhaal richting de klant hangt. Gebruik bij "nulmeting voor
  [klant]", "technische check van de site", "staat alles in de sitemap",
  "startrapport", "waar staan we nu" of direct aan het begin van de intake.
---

# Partner-nulmeting

Een nulmeting legt vast waar de klant staat vóórdat er iets verandert. Zonder
dat startpunt kun je later niet laten zien wat jouw werk en Gaply hebben
opgeleverd. De nulmeting heeft twee delen, omdat ze twee verschillende vragen
beantwoorden:

| Deel | Vraag | Wanneer | Waarop |
|---|---|---|---|
| **A. Techniek** | Kunnen zoekmachines, AI-assistenten en Gaply de site goed lezen? | Aan het begin, tijdens de intake (kan al in de offertefase) | De openbare website |
| **B. Vragen** | Welke vragen stellen mensen, en beantwoordt de site ze? | Na het eind-seintje, zodra Search Console gekoppeld is | Inzichten in Gaply |

Doe deel A tegelijk met de analyse van de site die je voor de intake toch al
maakt. Je hebt het rapport dan klaar op het moment dat de klant nog aan het
begin staat, en je kunt de bevindingen direct meenemen in je eigen advies.

## Waarom de techniek bij Gaply hoort

Gaply leest de site in via de sitemap; daarom vraagt de intake om de
sitemap-URL's. Wat niet in de sitemap staat, komt niet vanzelf in de
kennisbank. Een vraag waarop de site wel een antwoord heeft, komt dan toch
als contentgat uit de meting. Een voorbeeld uit de praktijk: een keten met
een eigen pagina per vestiging, waarvan die vestigingspagina's niet in de
sitemap stonden.

Wie zo'n bevinding pas ná de inrichting doet, repareert achteraf. Wie hem
vooraf doet, lost hem op vóór de eerste meting en heeft meteen een concreet
SEO-punt voor de klant. Daarom hoort deel A vóór het seintje aan Gaply.

## Deel A — SEO-technische nulmeting

Werk op de openbare site. Een Gaply-omgeving heb je hiervoor niet nodig.
Heb je een eigen crawltool of eigen toegang tot Search Console, gebruik die
dan als bron en noem dat in het rapport; anders werk je met een steekproef
zoals hieronder.

### A1. Sitemap ophalen en tellen

- Haal `https://[domein]/sitemap.xml` op. Is het een sitemap-index, haal dan
  ook de deel-sitemaps op (WordPress: `page-sitemap.xml`,
  `post-sitemap.xml`). Kijk in `robots.txt` of daar een andere sitemap wordt
  genoemd.
- Tel de URL's per eerste padsegment. Dit is dezelfde telling als het veld
  `scope.sitemap_overzicht` in de intake en de sitemap-analyse in
  `partner-offerte`; doe het één keer en gebruik het op alle drie de plekken.
- Noteer of de sitemap wijzigingsdatums (`lastmod`) heeft. Gaply gebruikt die
  om gewijzigde pagina's op te pikken.
- Staat de Gaply-omgeving al, dan geeft `preview_sitemap` hetzelfde beeld,
  inclusief waarschuwingen bij een sitemap die niet goed te lezen is.

### A2. Is de sitemap volledig?

Dit is de belangrijkste controle. Zoek naar pagina's die wel bestaan maar
niet in de sitemap staan.

- **Via de navigatie.** Loop het hoofdmenu, de voettekst en de
  overzichtspagina's na en controleer of de pagina's waar ze naar linken in
  de sitemap staan. Let vooral op paginatypen met veel soortgenoten:
  vestigingen of locaties, producten, behandelingen, diensten, teamleden,
  kennisbankartikelen.
- **Via Search Console.** Pagina's die in Google vertoond worden maar niet
  in de sitemap staan, zijn het sterkste bewijs. Heb je zelf toegang, kijk
  dan nu. Anders komt deze controle terug in deel B met
  `get_gsc_query_pages`.
- **Andersom.** Staan er URL's in de sitemap die er niet horen: doorverwijzingen,
  pagina's die niet meer bestaan, testpagina's, URL's met parameters?

Leg per ontbrekend paginatype vast: welk type, hoeveel pagina's ongeveer, en
één of twee voorbeeld-URL's als bewijs.

### A3. Kan alles gelezen en geïndexeerd worden?

Neem een steekproef van tien tot twintig pagina's, verdeeld over de
paginatypen (niet alleen de homepage). Controleer per pagina:

- geeft de pagina een normale respons, zonder doorverwijzing of foutmelding;
- sluit `robots.txt` de pagina of de map uit;
- staat er een `noindex` op, of wijst de canonical naar een andere pagina;
- staat de tekst in de HTML van de pagina zelf. Tekst die pas na het laden
  via JavaScript verschijnt, in een afbeelding staat of achter een inlog zit,
  wordt niet of slecht gelezen. Dat geldt voor Google, voor AI-assistenten
  en voor Gaply.

### A4. Klopt de paginastructuur?

Op dezelfde steekproef:

- precies één hoofdkop (H1) en een logische volgorde van tussenkoppen;
- een eigen titel en meta-omschrijving per pagina, geen kopieën;
- de hoofdinhoud in een herkenbaar hoofdgedeelte, los van menu, voettekst en
  zijbalk. Gaply leest de hoofdinhoud; inhoud in uitklapblokken of tabbladen
  telt alleen mee als de tekst in de HTML staat;
- gestructureerde gegevens (schema.org) waar dat past: organisatie,
  vestiging, product, veelgestelde vragen, artikel;
- dezelfde inhoud onder meer dan één adres (met en zonder www, met en zonder
  schuine streep aan het eind, taalvarianten zonder hreflang).

Laadsnelheid en Core Web Vitals vallen buiten deze nulmeting. Heb je daar
eigen cijfers van, dan kun je ze in je eigen advies opnemen.

### A5. Wat betekent elke bevinding, en voor wie?

Verdeel de bevindingen in twee soorten. Dat onderscheid bepaalt wie er iets
mee doet.

1. **Raakt de inrichting van Gaply.** Pagina's die in de kennisbank horen
   maar niet in de sitemap staan, paginatypen die niet gelezen kunnen worden,
   inhoud die dubbel voorkomt. Zet dit in de intake (bij de sitemap-velden,
   de categorieën binnen en buiten scope, en `bijzonderheden.overig`) en noem
   het in het seintje aan Gaply. De beste oplossing is dat de klant de
   sitemap herstelt. Kan dat niet op korte termijn, dan bepaalt Gaply hoe die
   pagina's toch worden meegenomen; regel dat niet zelf.
2. **SEO-werk voor de klant.** Al het andere. Dit is jouw advies aan de
   klant en hoort in het startrapport, met een prioriteit erbij.

### A6. Vastleggen

Eén tabel, één regel per bevinding:

| Bevinding | Waar gezien | Gevolg | Advies | Voor wie |
|---|---|---|---|---|
| wat er aan de hand is | voorbeeld-URL | wat het kost aan vindbaarheid of aan antwoorden | wat er moet gebeuren | webbouwer van de klant, partner of Gaply |

Regels voor de inhoud:

- Alleen bevindingen met een URL als bewijs.
- Geen score of percentage dat je niet zelf hebt geteld.
- Benoem ook wat goed staat. De klant moet het rapport als meting kunnen
  lezen, niet als verkooplijst.
- Zeg erbij dat het een steekproef is, van welke datum, en hoeveel pagina's
  je hebt bekeken.

## Deel B — Vraag-nulmeting (Inzichten)

Inzichten laat over de hele website zien welke vragen er leven, gegroepeerd
in onderwerpen en vraagclusters, en per cluster of de site het antwoord
heeft. Hiermee begint elk traject. Je zet aan het begin geen focusgebieden
op: je stuurt op de onderwerpen en vraagclusters uit Inzichten. Een
focusgebied komt pas later, en alleen als een onderwerp een verdiepende
gap-analyse verdient.

### B0. Voorwaarden

- Het eind-seintje van Gaply is binnen: de omgeving staat.
- Search Console is gekoppeld (`get_gsc_status`) en de eerste vragen zijn
  binnen (`get_gap_sources`: de bron `gsc` is beschikbaar en heeft vragen).
  Koppel Search Console daarom direct na het eind-seintje.
- Draait er nog geen zoekfunctie of chat op de site, dan komen de vragen
  alleen uit Search Console en uit de verdiepingsvragen van Google. Zonder
  Search Console is er dan te weinig om een nulmeting op te baseren: wacht.

### B1. Het totaalbeeld

`get_insights_summary` geeft het aantal gestelde vragen, de vertoningen in
Google en de verdeling van de vraagclusters:

| Label | Betekenis |
|---|---|
| covered | de site beantwoordt de vraag |
| partial | de site beantwoordt de vraag deels |
| gap | de site heeft geen goed antwoord |
| none | nog niet beoordeeld |

Rapporteer `none` als "nog niet beoordeeld" en tel het nergens bij op.
Noteer welke drempels zijn toegepast (`appliedMinVisitorOccurrences`,
`appliedMinImpressions`). Een latere meting is alleen vergelijkbaar met
dezelfde drempels.

### B2. Per onderwerp

`list_insight_topics` geeft per onderwerp het aantal clusters, hoe vaak de
vragen gesteld zijn en de verdeling over de labels. Dit is de nulmeting op
onderwerpniveau: waar staat de site er goed voor, en waar zitten de meeste
onbeantwoorde vragen.

### B3. Verdieping

- `get_insight_topic_clusters` voor de twee of drie onderwerpen met de meeste
  gaten (sorteer op `worst`), met de vraagformuleringen erbij.
- `list_missing_content` voor de clusters waarvan is vastgesteld dat de
  inhoud ontbreekt, met het verbeteradvies per cluster.

### B4. Leg de gaten naast deel A

Controleer bij de grootste gaten of de inhoud echt ontbreekt, of dat de
pagina wel bestaat maar niet is gelezen:

- `search_knowledge_base` met de vraag: komt er een pagina terug?
- `list_datasources` en daarna `list_resources` met `urlContains` op het
  paginatype: staat het in de kennisbank?
- `get_gsc_query_pages`: vertoont Google voor die vraag een pagina van de
  klant die niet in de sitemap of niet in de kennisbank staat?

Een gat dat door een technische bevinding uit deel A komt, los je technisch
op en niet met nieuwe content. Meld het bij Gaply en bij de klant, en begin
er geen contentvoorstel voor.

### B5. Vastleggen als startpunt

Noteer de datum, de periode waarover je keek, de drempels en de cijfers per
onderwerp. Dit is het ijkpunt waar de maandrapportage en elke latere meting
naar terugverwijzen.

## Het startrapport

Eén rapport in twee stappen. Je levert het eerst met alleen deel A, zodat je
het direct kunt gebruiken, en vult het na de inrichting aan met deel B.

- **Vorm:** HTML, print-klaar op A4, in de huisstijl van de eindklant met de
  partner als afzender, op dezelfde manier als `partner-rapportage`.
  Bestandsnaam `<klant>-nulmeting-<maand>-<jaar>.html`.
- **Huisstijl:** merkkleur en logo uit de projectcontext
  (`get_project_context`) als die er al zijn, anders van de website van de
  klant. De afzender en de vermelding van Gaply volgen
  `config/branding.md`.
- **Secties, in volgorde:** kop (klantlogo, afzender, datum); in het kort
  (vier of vijf zinnen); de techniek: wat goed staat en wat aandacht vraagt
  (de tabel uit A6); wat dat betekent voor de vindbaarheid en voor de
  antwoorden; het vraagbeeld per onderwerp (deel B, of "volgt na de
  inrichting"); de eerste drie prioriteiten; wat wij van jullie nodig
  hebben; over deze nulmeting (werkwijze, steekproef, datum).
- **Toon:** zakelijk Nederlands, geen marketingtaal, geen gedachtestrepen.
  Schrijf voor iemand die de site beheert, niet voor een ontwikkelaar.

Lever het bestand op aan de gebruiker. De partner verstuurt het zelf; stuur
nooit iets rechtstreeks naar de eindklant.

## Hierna

- Je werkt verder vanuit Inzichten. De grootste gaten per onderwerp gaan
  naar `partner-contentvoorstellen`; de maandrapportage
  (`partner-rapportage`) laat per onderwerp zien wat er sinds de nulmeting
  is veranderd.
- Een focusgebied zet je pas op als een onderwerp om verdieping vraagt:
  skill `partner-focusgebieden`. Dat is geen vaste stap.
- Herhaal deel A na een grote wijziging aan de site (nieuw ontwerp,
  verhuizing, nieuw CMS). De sitemap en de structuur zijn dan niet meer
  dezelfde.

## Grenzen

- Deel A is een steekproef en geen volledige technische audit. Beloof geen
  volledigheid en geen posities in Google.
- Het technische advies is jouw advies aan de klant. Het is geen oplevering
  of garantie van Gaply.
- Pas niets aan op de site van de klant; dat doet de klant of zijn
  webbouwer.
- Bevindingen die de inrichting raken gaan naar Gaply. Bronnen, de crawl en
  de zoek- en AI-instellingen blijven Gaply-werk, ook als je ziet wat er
  anders zou moeten.
- Geen cijfer dat niet uit een telling of een tool-respons komt.
