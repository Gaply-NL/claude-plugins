# Changelog — gaply-partner

Alle wijzigingen aan deze plugin worden hier bijgehouden. Versies volgen
[semver](https://semver.org/lang/nl/): MAJOR bij wijzigingen waardoor partners
hun werkwijze moeten aanpassen, MINOR bij nieuwe of gewijzigde skills en
prijslijst-/beleidswijzigingen, PATCH bij tekstuele fixes.

## [1.1.0] — 2026-09-03

### Toegevoegd
- Nieuwe skill **`partner-contract`**: de contractstap tussen offerte-akkoord
  en intake. Per project wordt een **aanvraagformulier** getekend met de
  **verwerkersovereenkomst als verplicht, onlosmakelijk onderdeel**; per
  partner éénmalig de geheimhoudingsovereenkomst. De skill verzamelt de
  gegevens die Gaply nodig heeft, dient de aanvraag in bij info@gaply.nl en
  bewaakt de tekenronde. De documenten zelf maakt en verstuurt Gaply vanuit
  PandaDoc.

### Gewijzigd
- De PandaDoc-sjablonen van Gaply gelden nu voor **partners én direct
  afnemende eindklanten** (keuze "directe afname" of "afname via een
  partner" in aanvraagformulier en verwerkersovereenkomst). Voor de partner
  verandert de werkwijze niet, behalve dat de verwerkersovereenkomst niet
  langer "waar nodig" maar altijd wordt gesloten.
- `partner-start` kent een extra stap in de route (contractset getekend?)
  en een tweede wachtmoment (na de contractaanvraag).
- `partner-intake` start pas na bevestiging van Gaply dat de contractset
  getekend is; stap 0 checkt dat expliciet.
- `partner-offerte` verwijst na akkoord naar `partner-contract` in plaats
  van rechtstreeks naar de intake.

## [1.0.0] — 2026-09-03

**Eerste stabiele release.** Het werkproces is uitontwikkeld: van offerte en
intake tot focusgebieden, contentvoorstellen, rapportage en beheer na livegang
zit de hele keten in dit pakket, en met deze versie komt het laatste stuk erbij
dat er nog buiten viel — het juridische. Een 0.x-nummer straalt "nog in
ontwikkeling" uit, en dat past niet bij iets waar partners hun klantafspraken
op baseren.

Nieuw in deze release is het juridische deel, dat tot nu toe per mail werd
geregeld.

### Toegevoegd
- Nieuwe skill **`partner-juridisch`**: de drie documenten (algemene
  voorwaarden, verwerkersovereenkomst, security-bijlage), waar ze staan, wie
  ze mag accepteren en hoe je het akkoord zet. Reden om er een eigen skill van
  te maken in plaats van een alinea in `partner-intake`: het akkoord hangt aan
  je **organisatie**, niet aan een klant, en kan dus op elk moment opkomen —
  bij je eerste klant, of jaren later bij een nieuwe documentversie.
- **Acceptatie is een organisatiestap, geen projectstap.** Eén keer akkoord
  dekt al je projecten; bij een nieuw gepubliceerde documentversie komt de
  gate terug. `partner-intake` en `partner-beheer` verwijzen er allebei naar
  op het moment ná het eind-seintje, zodat het bij de eerste klant niet
  vergeten wordt en bij de volgende alleen nog een controle is.
- **Het acceptatiebewijs** staat beschreven als wat het is: het stuk waarmee
  je richting je eindklant aantoont dat je subverwerkers onder een
  gelijkwaardige overeenkomst werken (art. 7.3). Het bevat documenttype,
  versie, contenthash, naam en e-mailadres van de accepteerder en het
  tijdstip — bewust géén IP-adres.
- **De rol `Tekenbevoegd`** is uitgelegd als de oplossing voor het geval dat
  in de praktijk het vaakst voorkomt: de tekenbevoegde is niet de dagelijkse
  beheerder en ziet de acceptatiepagina daarom niet. Die rol draagt alleen de
  juridische rechten en komt *naast* een bestaande rol, zodat niemand een
  bredere toegang krijgt dan nodig. Aan te vragen bij Gaply.
- **Verwerker versus subverwerker** staat nu in de README-rolverdeling: bij een
  directe klant is Gaply verwerker, bij een klant via de partner is de partner
  verwerker en Gaply subverwerker. Dat onderscheid bepaalt wie tekent en
  waarom de eindklant het bewijs mag opvragen — zonder die twee alinea's
  belandde die vraag steeds bij Gaply in plaats van bij de partner.

### Gewijzigd
- **`partner-intake`: "juridische bijzonderheden" is uit de vervallen-lijst
  gehaald en vervangen door drie gerichte velden** —
  `juridisch.verwerkersrol` (`direct` of `partner`),
  `juridisch.tekenbevoegde` (naam + e-mailadres) en
  `juridisch.bewaartermijn_dagen`. Het oude verzamelveld werd niet gebruikt en
  is daarom in 0.4.0 geschrapt; deze drie sturen wél iets aan. Zonder de
  tekenbevoegde kan Gaply de juiste rol niet toekennen, en dan ziet die
  persoon het akkoord straks simpelweg niet staan.
- **De bewaartermijn is uitgelegd in plaats van alleen gevraagd.** Leeg laten
  betekent de standaard van 365 dagen, en dat is een keuze, geen ontbrekend
  antwoord. Ná de termijn verdwijnen de rúwe vragen en gesprekken terwijl de
  tellingen blijven staan — die nuance staat er expliciet bij, omdat "dan zien
  we toch niets meer?" anders de eerste vraag van elke klant is.
- **`partner-start`** routeert een openstaand akkoord, een nieuwe
  documentversie en een klant die om de verwerkersovereenkomst vraagt naar
  `partner-juridisch`, met de aantekening dat die route naast het traject
  loopt en geen fase is.
- **`partner-beheer`** noemt de akkoordcontrole in de overname-checklist en
  neemt de juridische verhouding op in de beheerinstructie voor de eindklant —
  uit jezelf vertellen is goedkoper dan het antwoord schuldig blijven als de
  privacy-officer van de klant erom vraagt.

## [0.4.0] — 2026-08-14

### Gewijzigd
- **`partner-intake`: het onderscheid demo/livegang is vervallen.** De intake
  start pas na een getekende offerte, dus er is nog maar één drempel
  (compleet) en daarna één ononderbroken inrichtingsrun. De skill beschrijft
  nu het volledige proces: de partner seint dat de vragenlijst vol is, Gaply
  controleert en draait de inrichting van A tot Z tot en met promotie naar
  productie, en geeft een eind-seintje terug. Pas dán activeert de partner —
  front-end (widget of API), klantaccounts, en tijdens of na de
  partnertraining Search Console koppelen, focusgebieden aanmaken en
  eventueel kantoor-IP's laten whitelisten. Search Console gaat bij voorkeur
  vóór de focusgebieden.
- **Tien besluiten over de vragenlijst verwerkt.** Eruit: CMS/technische
  stack, de twee Search Console-velden, demo-deelnemers,
  focusgebied-kandidaten, demo-datum, kantoor-IP's van de klant en
  juridische bijzonderheden; de livegangsdatum stuurt niets meer. Verplicht
  geworden: de datum van het offerte-akkoord
  (`herkomst.offerte_datum_akkoord`) en het woordgebruik
  (`toon.voorkeurswoorden`) — dat laatste mét een suggestieflow, waarin de
  skill op basis van een sitescan zelf woorden voorstelt die de klant alleen
  nog goed- of afkeurt.
- **Topics expliciet gemaakt in `partner-intake`:** er is geen apart
  topics-veld; Gaply leidt de project-topics af uit `scope.categorieen_in`,
  `doelgroep.matrix`, `bezoekersvragen.lijst` en de sitemapstructuur. De
  skill legt nu uit hoe de partner daaraan bijdraagt.
- `partner-start` volgt de nieuwe route: één wachtmoment in plaats van twee,
  en na het eind-seintje door naar `partner-beheer`.
- `partner-livegang` geldt alleen nog voor trajecten die onder de oude flow
  zijn gestart; bij nieuwe klanten zit de livegang in de A-Z-run van Gaply.
- **README-uitsluiting genuanceerd:** de golden set *bewerken* blijft
  Gaply-werk (`golden_set.manage` is super-admin-only), maar *lezen en
  wijzigingen voorstellen* is partnerwerk.

### Toegevoegd
- Nieuwe skill **`partner-beheer`** (beheer en onderhoud na livegang):
  - de golden set van de klant lezen, per entry reviewen (klopt de vraag; is
    dít de pagina waarmee de klant beantwoord wíl worden; kloppen antwoord,
    terugvalgedrag en serviceverwachting met de klantintentie) en aanvullen
    vanuit klantkennis. De partner keurt en levert aan, Gaply voert door;
  - de beheerinstructie voor de eindklant — die taak ligt vanaf nu
    expliciet bij de partner, Gaply levert hem niet meer;
  - een verbetercadans met terugkerend naloopwerk: golden-set-review, het
    menselijke deel van de judge-ijkronde, nieuwe bezoekersvragen,
    focusgebieden en gaten;
  - een handoff-sectie met wat de partner bij het eind-seintje overneemt.
- **Let op de permissies:** het lezen van de golden set en het indienen van
  voorstellen loopt via de nieuwe capabilities `golden_set.read` en
  `golden_set.suggest`. Die zijn bij het uitkomen van deze versie nog niet
  uitgerold; tot dan levert Gaply de set als export bij het eind-seintje en
  gaan voorstellen per mail. Zodra ze live zijn, moet Gaply ze aan de
  Partnerrol toekennen — anders volgt een 403.

## [0.3.1] — 2026-08-12

### Toegevoegd
- Nieuwe skill **`partner-start`**: wegwijzer door het hele traject —
  bepaalt via `get_my_access`/`get_project_context` waar een klant staat en
  verwijst naar de juiste skill, inclusief de twee wachtmomenten waarop de
  bal bij Gaply ligt. README kreeg een "Start hier"-sectie.
- `partner-intake` stap 0: de partner maakt het klantproject zélf aan
  (`create_project` in de eigen organisatie) als het nog niet bestaat — de
  Partnerrol heeft daarvoor sinds 12-08 de capability `project.create`.
  Omgevingen, bronnen en crawl blijven Gaply-werk.

## [0.3.0] — 2026-08-11

### Gewijzigd
- `partner-intake` werkt niet langer met een markdown-document dat je naar
  info@gaply.nl mailt. De vragenlijst wordt live opgehaald bij Gaply
  (`get_project_context_template`), ingevuld en weggeschreven via
  `set_project_context`, met een validatierapport direct in de respons. De
  vragenlijst kan zo nooit meer uit de pas lopen met wat Gaply verwacht — het
  oude document blijft alleen nog als terugvaloptie als de tool niet
  beschikbaar is.
- De verplichte-veldenlijst in `partner-intake/SKILL.md` is verwijderd:
  `verplicht` is nu een eigenschap van het templateveld zelf, niet van de
  skill-tekst.
- `references/intake-template.md` is **verwijderd**. De uitleg per veld
  (waarom Gaply het vraagt, met voorbeelden) zit voortaan als `helpText` ín
  de template zelf en komt mee met `get_project_context_template` — één bron
  van waarheid, geen lokaal document dat kan verouderen. Ook de papieren
  terugvaloptie (intake-document mailen bij een niet-werkende koppeling) is
  vervallen: bij een 403 of onbereikbare MCP meld je het bij Gaply en wordt
  de koppeling hersteld — een intake buiten de validatie om bestaat niet
  meer.
- Nieuwe sectie in `partner-intake`: **de partner koppelt Search Console
  zelf** via de Gaply-webinterface (browser-login vereist; MCP kan de status
  wel checken via `get_gsc_status`, de koppeling niet leggen). Gaply zit hier
  bewust niet tussen.
- `partner-focusgebieden` en `partner-rapportage` verwijzen nu naar de
  projectcontext (`get_project_context`) voor respectievelijk
  focusgebied-kandidaten en de verplichte huisstijlvelden (merkkleur,
  logo-URL), in plaats van die los te laten zoeken.
- **`partner-livegang` voert de livegang niet meer zelf uit.** De uitvoering
  (synchronisatie naar productie, API-keys, widget-configuratie, standalone
  agents) ligt volledig bij Gaply; de skill bereidt voor (gereedheids-check
  incl. `compleet_voor_livegang` op de projectcontext, klant-akkoord), dient
  de aanvraag in bij Gaply en coördineert de klant-acties (tag-plaatsing door
  de tagmanager-beheerder uit de projectcontext). Alle prod-schrijfacties
  (`sync_environment` met `allowProduction`, `create_api_key`,
  `update_api_key_allowed_origins`, `set_widget_settings`,
  `create_standalone_agent`) zijn uit de skill verwijderd.
- Plugin-README bijgewerkt: intake- en livegang-omschrijvingen kloppen weer
  met de werkelijke flow; rolverdeling benoemt expliciet dat livegang
  Gaply-werk is.

### Toegevoegd
- Nieuwe verplichte/uitgebreide velden in de projectcontext-vragenlijst:
  "Vragen die bezoekers écht stellen" (minimaal tien),
  "Focusgebied-kandidaten", taal/talen van site en demo, een eigen
  sitemap-overzicht-veld, no-go-onderwerpen, kantoor-IP's van de klant,
  aparte contactrollen voor dagelijks beheerder en tagmanager-beheerder,
  demo-datum en doel met Gaply. Merkkleur(en) hex en logo-URL zijn verplicht
  geworden — dit repareert de inconsistentie waarbij `partner-rapportage` ze
  al hard eiste terwijl de intake ze niet opvroeg.

## [0.2.0] — 2026-08-07

### Gewijzigd
- Prijslijst gecorrigeerd naar de juiste staffel: € 500 (tot ±600 URL's),
  € 750 (±600–1.600 URL's), € 1.000 (±1.600–3.500 URL's). Setup blijft € 2.500.
- Voorbeeldconfiguratie van de offerte-skill in lijn gebracht met de nieuwe staffel.
- Repository-verwijzing toegevoegd: de plugin wordt beheerd en uitgegeven via
  GitHub (gaply/claude-plugins).

## [0.1.0] — 2026-08

- Eerste versie: zes partner-skills (offerte, intake, focusgebieden,
  contentvoorstellen, rapportage, livegang), Gaply MCP-koppeling,
  partnerbranding- en prijslijstconfiguratie.
