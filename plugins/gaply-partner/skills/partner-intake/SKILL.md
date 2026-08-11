---
name: partner-intake
description: >-
  Verzamelt na een getekende Gaply-offerte de projectcontext die Gaply nodig
  heeft om het klantproject in te richten: haalt de actuele vragenlijst live
  op bij Gaply, vult die in via de projectcontext-tools en toont het
  validatierapport dat direct terugkomt. Gebruik bij "intake voor [klant]",
  "nieuwe klant aanmelden", "overdracht naar Gaply", "wat heeft Gaply nodig"
  of direct na een akkoord op een offerte.
---

# Partner-intake (overdracht naar Gaply)

Dit is het formele overdrachtsmoment van partner naar Gaply. Gaply richt op
basis van de projectcontext de omgeving in: project en environments, de
bronnen (datasources), de zoek- en AI-instellingen en de kwaliteitsbewaking.
Dat is bewust werk van Gaply; de partner levert de input en neemt daarna de
inrichting van focusgebieden en content over.

De intake loopt via de projectcontext-tools op de `gaply` MCP-server, niet
meer via een document dat je zelf naar Gaply mailt. Voordeel: de vragenlijst
komt live uit Gaply zelf, dus die kan nooit meer uit de pas lopen met wat
Gaply werkelijk verwacht — en je krijgt na elke keer wegschrijven direct een
validatierapport terug, in plaats van dat pas te horen als iemand bij Gaply
het document leest.

## Werkwijze

### 1. Vragenlijst ophalen

Haal de actuele vragenlijst op met `get_project_context_template`. Lees niet
een lijst uit dit skill-bestand — die staat hier bewust niet meer (zie
hieronder). Elk veld komt terug met `id`, `label`, `sectie`, `type`,
`verplicht` (bool) en `laag` (1 = vóór de demo, 2 = vóór livegang), plus een
`hulptekst`. Dit template ís de bron van waarheid voor wat er gevraagd moet
worden, en dus ook voor welke velden verplicht zijn: dat staat voortaan
uitsluitend in het `verplicht`- en `laag`-veld van elk templateveld zelf, niet
in een aparte lijst in deze skill.

Is er al eerder ingevuld voor dit project, haal dan ook `get_project_context`
op zodat je niet opnieuw vraagt wat al bevestigd is.

### 2. Invullen, sectie voor sectie

Loop de secties uit het template langs. Haal antwoorden uit de offerte en de
gespreksnotities, en bevraag de gebruiker gericht op wat daar niet uit blijkt
— vooral bij "Vragen die bezoekers écht stellen" en "Focusgebied-kandidaten"
moet je actief doorvragen; die vul je niet uit een offerte-PDF.

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

### 3. Wegschrijven

Schrijf de velden weg met `set_project_context`. Partieel schrijven mag en is
normaal — de partner hoeft niet alles in één sessie te hebben; vul aan
naarmate er meer bekend wordt. Het antwoord bevat het bijgewerkte
compleetheidsrapport, dus je hoeft niet apart te pollen.

### 4. Validatierapport tonen

Laat het compleetheidsrapport zien zoals het terugkomt: ontbrekende
verplichte velden, velden die wel gevuld zijn maar te mager (voldoen niet aan
de minimale inhoudseis), en de suggesties. Vertaal de `status` naar wat het
voor de partner betekent:

- `leeg` / `in_bewerking` — er ontbreekt nog verplichte input; Gaply kan nog
  niet starten.
- `compleet_voor_demo` — Gaply kan nu de omgeving inrichten en de demo
  klaarzetten.
- `compleet_voor_livegang` — ook de laag-2-velden zijn binnen; niets houdt
  livegang meer tegen vanuit de intake.

### 5. Afronden

Zolang de status nog niet `compleet_voor_demo` is, is de uitkomst van de
sessie een concreet aanleverlijstje voor de klant: precies de resterende
ontbrekende en te magere velden uit het validatierapport — niet de hele
vragenlijst opnieuw.

Is de status `compleet_voor_demo` of hoger: meld dat aan de gebruiker en
verwijs door naar de skill `partner-focusgebieden` als volgende stap.

## Als de tool niet lukt

Krijg je geen toegang (bijvoorbeeld een 403) of is de MCP-koppeling niet
bereikbaar: meld dat expliciet aan de gebruiker. Val dan terug op het oude
document: bouw op basis van de sectiestructuur in
`references/intake-template.md` een `intake_gaply_[klant].md` en laat de
gebruiker dat naar Gaply (info@gaply.nl) sturen. Vermeld daarbij nadrukkelijk
dat dit document **handmatig verwerkt** moet worden — het gaat buiten de
tool-validatie om, dus Gaply krijgt geen automatisch compleetheidsrapport.

## Grenzen

- Vraag Gaply nooit om toegang tot broninrichting of zoekinstellingen; dat
  blijft bij Gaply.
- Doe geen toezeggingen over de inrichtingsduur namens Gaply; vraag het na.
