---
name: partner-intake
description: >-
  Verzamelt na een getekende Gaply-offerte de projectcontext die Gaply nodig
  heeft om het klantproject in te richten: haalt de actuele vragenlijst live
  op bij Gaply, vult die in via de projectcontext-tools, toont het
  validatierapport dat direct terugkomt en geeft daarna het seintje waarmee
  Gaply de volledige inrichting start. Gebruik bij "intake voor [klant]",
  "nieuwe klant aanmelden", "overdracht naar Gaply", "wat heeft Gaply nodig"
  of direct na een akkoord op een offerte.
---

# Partner-intake (overdracht naar Gaply)

Dit is het formele overdrachtsmoment van partner naar Gaply. Gaply richt op
basis van de projectcontext de omgeving in: project en environments, de
bronnen (datasources), de zoek- en AI-instellingen en de kwaliteitsbewaking.
Dat is bewust werk van Gaply; de partner levert de input en activeert daarna
bij de klant.

De intake loopt via de projectcontext-tools op de `gaply` MCP-server, niet
meer via een document dat je zelf naar Gaply mailt. Voordeel: de vragenlijst
komt live uit Gaply zelf, dus die kan nooit meer uit de pas lopen met wat
Gaply werkelijk verwacht — en je krijgt na elke keer wegschrijven direct een
validatierapport terug, in plaats van dat pas te horen als iemand bij Gaply
het document leest.

## Het proces: één run van A tot Z

**De intake start pas als de offerte getekend is.** De klant ís dan al klant,
dus er is geen demo-drempel meer: het onderscheid tussen "compleet voor de
demo" en "compleet voor livegang" is vervallen. Er is één drempel — de
context is compleet — en daarna één ononderbroken inrichtingsrun.

1. **Getekende offerte** → jij begint de intake.
2. Je vult de projectcontext in tot het validatierapport niets verplichts
   meer mist.
3. **Het seintje.** Je meldt bij Gaply (info@gaply.nl) dat de vragenlijst
   volledig is ingevuld. Er is geen automatische melding: zonder dit bericht
   weet Gaply niet dat je klaar bent.
4. Gaply controleert de context. Ontbreekt er toch iets, dan hoor je precies
   wat — anders start de inrichting.
5. **Gaply draait de volledige run van A tot Z**: bronnen en crawl,
   afstelling van zoeken en chat, contentvoorstellen en inzichten, widget en
   vulling, promotie naar productie. Zonder tussenstops en zonder aparte
   livegang-aanvraag. De livegangsdatum van de klant is hierbij niet leidend;
   Gaply rolt door tot alles technisch live staat.
6. **Het eind-seintje.** Gaply meldt je: alles staat live. Dan ben jij aan
   zet.
7. **Jouw activatiewerk**, ná het eind-seintje:
   - Gaply implementeren op de front-end van de klant (widget of API);
   - klantaccounts aanmaken en de klant onboarden;
   - tijdens of na de partnertraining: Search Console koppelen,
     focusgebieden aanmaken (skill `partner-focusgebieden`) en eventueel de
     kantoor-IP's van de klant laten whitelisten. **Koppel Search Console bij
     voorkeur vóór je de focusgebieden aanmaakt**, dan zitten de
     GSC-zoekwoorden er meteen in. Later koppelen kan ook — de queries komen
     dan alsnog automatisch mee — maar vooraf is beter.
   - **controleren of het juridische akkoord van jóúw organisatie staat.** Dat
     akkoord hangt aan je organisatie, niet aan deze klant: heb je het al eens
     gegeven en is er sindsdien geen nieuwe documentversie gepubliceerd, dan
     is dit alleen een controle. Is dit je eerste klant, dan moet de
     tekenbevoegde het daadwerkelijk nog zetten — skill `partner-juridisch`.
8. Vanaf het eind-seintje loopt het beheer door: skill `partner-beheer`.

Beloof de klant dus geen inrichtingsdatum op basis van zijn eigen
livegangswens, en wacht na het seintje op Gaply in plaats van alvast te
beginnen aan focusgebieden of accounts.

## Werkwijze

### 0. Zorg dat het project bestaat

De vragenlijst ophalen kan altijd, maar de ingevulde context hangt aan een
project. Bestaat er nog geen project voor deze klant (check met
`list_projects` in je eigen organisatie), maak het dan zelf aan met
`create_project`: projectnaam = de klantnaam zoals die in de offerte staat
(bijv. "Bakkerij Jansen"), binnen je eigen partner-organisatie. Meer dan een
naam is niet nodig — omgevingen, bronnen en de crawl richt Gaply in tijdens
de inrichtingsrun. Een leeg project kost niets; maak er wel maar één per
klant aan en hergebruik het bestaande project bij een tweede sessie.
Verwijderen van een verkeerd aangemaakt project kan alleen Gaply — meld een
misser via info@gaply.nl in plaats van een nieuw project met bijna dezelfde
naam te beginnen.

### 1. Vragenlijst ophalen

Haal de actuele vragenlijst op met `get_project_context_template`. Lees niet
een lijst uit dit skill-bestand — die staat hier bewust niet meer (zie
hieronder). Elk veld komt terug met `id`, `label`, `sectie`, `type`,
`verplicht` (bool) en `laag`, plus een `hulptekst`. Dit template ís de bron
van waarheid voor wat er gevraagd moet worden, en dus ook voor welke velden
verplicht zijn: dat staat voortaan uitsluitend in het `verplicht`-veld van
elk templateveld zelf, niet in een aparte lijst in deze skill.

Het `laag`-veld splitste de vragenlijst vroeger in "vóór de demo" en "vóór
livegang". Dat onderscheid is vervallen: behandel álle verplichte velden als
nodig vóór het seintje, ongeacht hun laag.

Is er al eerder ingevuld voor dit project, haal dan ook `get_project_context`
op zodat je niet opnieuw vraagt wat al bevestigd is.

### 2. Invullen, sectie voor sectie

Loop de secties uit het template langs. Haal antwoorden uit de offerte en de
gespreksnotities, en bevraag de gebruiker gericht op wat daar niet uit blijkt
— vooral bij "Vragen die bezoekers écht stellen" moet je actief doorvragen;
die vul je niet uit een offerte-PDF.

Twee velden vragen om een eigen aanpak: het **woordgebruik** en de velden
waar Gaply de **topics** uit afleidt. Beide staan verderop uitgewerkt.

Verzin niets; markeer wat echt onbekend is. Dat is nu concreet, per veld:

- **Echt onbekend**: stuur het veld niet mee, of geef het `status: 'leeg'`
  mee.
- **Afgeleid** — je haalt het antwoord uit de offerte of de website, maar het
  is niet expliciet gehoord of bevestigd: `status: 'afgeleid'`, en leg het
  daarna expliciet aan de klant of de partner voor ter bevestiging. Dit is
  bewust — een afgeleid antwoord telt NIET mee als compleet voor een
  verplicht veld, ook niet ná het wegschrijven. Een afgeleid veld is een
  aanbod om te corrigeren, geen feit; alleen een bevestigd antwoord telt.
- **Bevestigd** — de klant of partner heeft het letterlijk zo gezegd of
  goedgekeurd: `status: 'bevestigd'`.

Geef bij elk veld ook `herkomst` mee (`bron` + `datum`).

De datum waarop de klant akkoord gaf op de offerte
(`herkomst.offerte_datum_akkoord`) is **verplicht**. Dat is geen
administratieve formaliteit: die datum is de start van het traject, en zonder
getekende offerte hoort de intake niet te lopen. Je weet 'm altijd — vul 'm
als `bevestigd`.

### 3. Wegschrijven

Schrijf de velden weg met `set_project_context`. Partieel schrijven mag en is
normaal — de partner hoeft niet alles in één sessie te hebben; vul aan
naarmate er meer bekend wordt. Het antwoord bevat het bijgewerkte
compleetheidsrapport, dus je hoeft niet apart te pollen.

### 4. Validatierapport tonen

Laat het compleetheidsrapport zien zoals het terugkomt: ontbrekende
verplichte velden, velden die wel gevuld zijn maar te mager (voldoen niet aan
de minimale inhoudseis), en de suggesties.

Er is nog maar één drempel die telt: **compleet**. Zolang Gaply de engine nog
niet heeft omgebouwd, kan het rapport nog de oude statussen teruggeven —
vertaal ze dan zo:

- `leeg` / `in_bewerking` — er ontbreekt nog verplichte input; het seintje
  kan nog niet.
- `compleet_voor_demo` of `compleet_voor_livegang` — lees dit als
  **compleet**: alles wat Gaply nodig heeft is binnen, geef het seintje.

Ga niet op zoek naar een tweede drempel verderop in het traject; die bestaat
niet meer.

### 5. Afronden

Is de context nog niet compleet, dan is de uitkomst van de sessie een
concreet aanleverlijstje voor de klant: precies de resterende ontbrekende en
te magere velden uit het validatierapport — niet de hele vragenlijst opnieuw.

Is de context compleet: meld dat aan de gebruiker en **geef het seintje aan
Gaply** (info@gaply.nl, met klant en projectnaam). Daarna ligt de bal bij
Gaply tot het eind-seintje; zie "Het proces" hierboven voor wat je dán doet.

## Woordgebruik: jij doet de voorstellen, de klant keurt goed of af

Het veld `toon.voorkeurswoorden` (welke woorden de klant wél gebruikt en
welke bewust niet) is **verplicht**. Een partner die dit veld koud voorlegt,
krijgt zelden een bruikbaar antwoord — dus draai het om:

1. **Scan de site van de klant** op terminologie: een handvol kernpagina's,
   de belangrijkste dienst- of productnamen, hoe de klant zijn doelgroep
   aanspreekt (u of je), welke synoniemen hij consequent vermijdt.
2. **Doe een concreet voorstel**: een korte lijst "deze woorden gebruiken" en
   "deze woorden vermijden", elk met de vindplaats erbij, plus de synoniemen
   waarvan jij vermoedt dat ze juist níét passen.
3. **Laat per woord goedkeuren of afkeuren.** Wat de klant of partner
   goedkeurt gaat weg als `bevestigd`; wat je alleen zelf hebt afgeleid en
   nog niet is goedgekeurd, gaat weg als `afgeleid` en telt dus niet mee als
   compleet. Voeg toe wat de klant zelf noemt.

Deze flow is de reden dat het veld verplicht kón worden: het kost de klant
een paar minuten keuren in plaats van een leeg tekstvak.

## Topics: er is geen apart veld, maar je bepaalt ze wel

De vragenlijst heeft bewust geen topics-vraag. Gaply leidt de project-topics
tijdens de inrichting af uit vier bronnen, en drie daarvan lever jij:

- `scope.categorieen_in` (en de uitgesloten categorieën) — dit is de
  thema-afbakening; wat hier ontbreekt, wordt geen topic;
- `doelgroep.matrix` — wie er vraagt, bepaalt hoe de thema's uiteenvallen;
- `bezoekersvragen.lijst` — de echte vragen; hoe concreter, hoe scherper de
  topics;
- de sitemapstructuur van de site zelf (die haalt Gaply op).

Vul die drie velden dus niet af als vinkje. Vind je dat een bepaald thema
hoe dan ook als eigen onderwerp moet bestaan (of juist niet mag ontstaan),
zet dat er expliciet bij in de toelichting — dan neemt Gaply het mee bij het
afleiden. Topics zelf aanmaken of wijzigen is Gaply-werk.

## Wat er niet meer gevraagd wordt (sinds 0.4.0)

Deze velden zijn uit de vragenlijst gehaald. Vraag er niet meer naar en zoek
ze ook niet alsnog op — ze staan hier alleen zodat je weet dat het weglaten
opzet is en geen omissie:

| Vervallen | Waarom |
|---|---|
| CMS / technische stack | Lastig te achterhalen, meerwaarde voor de inrichting onduidelijk |
| Search Console beschikbaar + wie verleent toegang | GSC hoort ná de inrichting, bij de partnertraining |
| Wie schuift aan bij de demo | Er is geen demo-gate meer |
| Focusgebied-kandidaten | Focusgebieden zijn partnerwerk ná livegang, niet nodig voor de inrichting |
| Demo-datum | Idem: geen demo-gate |
| Kantoor-IP's van de klant | Komt bij de partnertraining, later toe te voegen |

De **livegangsdatum** is eveneens vervallen als sturend veld: Gaply plant er
niets meer op. Staat hij nog in het template, vul 'm dan hoogstens
informatief in en hang er geen verwachting aan.

## Drie juridische velden — nieuw, en wél gevraagd

Het oude verzamelveld "juridische bijzonderheden" is vervangen door drie
gerichte vragen. Ze zijn kort te beantwoorden, maar ze sturen echt iets aan:
zonder deze drie loopt de inrichting later vast op iets wat niemand meer snel
kan oplossen.

| Veld | Wat je invult |
|---|---|
| `juridisch.verwerkersrol` | `direct` als de klant rechtstreeks met Gaply contracteert, `partner` als de klant via jou loopt. In dit pakket is `partner` de normale waarde: jij bent dan de verwerker en Gaply de subverwerker. Zie de skill `partner-juridisch`. |
| `juridisch.tekenbevoegde` | Naam **en** e-mailadres van de persoon die namens de organisatie mag tekenen. Gaply gebruikt dit om die persoon de juiste rol te geven; zonder naam en adres kan dat niet, en dan ziet hij het akkoord straks niet staan. |
| `juridisch.bewaartermijn_dagen` | Hoe lang de zoek- en chatvragen van bezoekers bewaard mogen blijven, in dagen. **Laat het leeg als de klant geen eis heeft** — dan geldt de standaard van 365 dagen. Dat is geen ontbrekend antwoord maar een keuze. |

Over die derde: ná de bewaartermijn verdwijnen de **rúwe** vragen en
gesprekken, terwijl de **tellingen** blijven staan (hoe vaak iets gevraagd
werd, welke vervolgvragen er waren, waar de gaten zaten). Een klant die om een
korte termijn vraagt, verliest dus niet zijn rapportage — hij verliest de
mogelijkheid om een individuele vraag van lang geleden terug te lezen. Leg dat
zo uit; het antwoord op de vraag "maar dan zien we toch niets meer?" is nee.

Wat je er meteen bij kunt zeggen als de klant doorvraagt: van bezoekers wordt
géén IP-adres bewaard (alleen een dag-wisselende code, zodat de bezoekerstelling
klopt zonder iemand te kunnen volgen), en contactgegevens die iemand in de
zoekbalk typt — e-mailadres, telefoonnummer, BSN-vormige reeks — worden bij het
opslaan gemaskeerd.

## Search Console: ná de inrichting, door de partner zelf

De koppeling met Google Search Console legt de partner zélf, via de
Gaply-webinterface (inloggen met je eigen Gaply-account → omgeving →
instellingen → Search Console). De Google-koppeling vereist een browser-login
en kan dus niet via MCP; controleren of hij staat kan wél via
`get_gsc_status`. Gebruik het Google-account dat toegang heeft tot de
property van de klant.

Doe dit **niet tijdens de intake** maar ná het eind-seintje, tijdens of na de
partnertraining — en bij voorkeur vóór je de focusgebieden aanmaakt. Gaply
zit hier bewust niet tussen.

## Als de tool niet lukt

Krijg je geen toegang (bijvoorbeeld een 403) of is de MCP-koppeling niet
bereikbaar: **stop en meld het bij Gaply** (info@gaply.nl), met de exacte
foutmelding en het moment. Er is bewust géén papieren terugvaloptie — een
intake buiten de tool om krijgt geen validatie en geen compleetheidsrapport,
en dat is precies wat deze flow moet garanderen. Gaply herstelt de koppeling;
daarna ga je gewoon verder waar je was (partieel wegschrijven mag altijd).

## Grenzen

- Vraag Gaply nooit om toegang tot broninrichting of zoekinstellingen; dat
  blijft bij Gaply.
- Doe geen toezeggingen over de inrichtingsduur namens Gaply; vraag het na.
- Begin geen activatiewerk (front-end, klantaccounts, Search Console,
  focusgebieden) vóór het eind-seintje binnen is.
