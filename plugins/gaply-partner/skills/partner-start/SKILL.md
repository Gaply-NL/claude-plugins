---
name: partner-start
description: >-
  Wegwijzer door het hele partnertraject: bepaalt waar een klant stáát en
  verwijst naar de juiste skill, inclusief de momenten waarop je op Gaply
  wacht. Gebruik bij "nieuwe klant", "waar begin ik", "wat is de volgende
  stap voor [klant]", "hoe ver zijn we met [klant]" of als je niet zeker
  weet welke skill van dit pakket je nodig hebt. Doet zelf geen
  inrichtingswerk — alleen routeren.
---

# Partner-start

Dit pakket heeft tien werk-skills. Deze elfde vertelt je welke je nodig
hebt. Stel eerst vast waar de klant staat, verwijs dan door — en begin niet
zelf alvast aan werk dat bij een andere skill (of bij Gaply) hoort.

## Zo bepaal je waar de klant staat

1. **Toegang checken** — `get_my_access`. Zie je je partner-organisatie
   niet, of krijg je een 403: stop en meld het bij Gaply (info@gaply.nl).
   Een 403 is in dit pakket nooit iets om omheen te werken.
2. **Bestaat het project al?** — `list_projects` in je eigen organisatie.
   - **Nee** → is de offerte getekend? Zo nee: `partner-offerte`. Zo ja:
     is de contractset getekend (aanvraagformulier én verwerkersovereenkomst
     voor dit project, plus de geheimhoudingsovereenkomst van de partner)?
     Zo nee: `partner-contract`. Zo ja: `partner-intake` (die begint met het
     aanmaken van het project, stap 0).
   - **Ja** → lees `get_project_context` en kijk naar
     `completeness.status`; de tabel hieronder wijst de weg.
   - **Ja, en het draait al, maar de projectcontext is leeg** → dit is een
     project van vóór de intake via de projectcontext. Je herkent het aan
     een productie-omgeving met vragen (`get_gap_sources`) of focusgebieden
     (`list_lenses`). Stuur het niet terug naar de intake: het loopt door
     via `partner-beheer` en `partner-rapportage`. Vul de context alleen aan
     als Gaply erom vraagt.

## De route

| Waar de klant staat | Signaal | Skill / actie |
|---|---|---|
| Nog geen getekende offerte | — | `partner-offerte` |
| Begin van het traject: de site wordt geanalyseerd | de sitemap-analyse voor de offerte of de intake loopt | `partner-nulmeting`, deel A (SEO-technische nulmeting). Kan al in de offertefase en hoort klaar te zijn vóór het seintje aan Gaply |
| Offerte akkoord, contractset nog niet getekend | geen bevestiging van Gaply dat aanvraagformulier + verwerkersovereenkomst getekend zijn | `partner-contract` — **verplicht vóór de intake**; de verwerkersovereenkomst is onlosmakelijk onderdeel |
| Contractset getekend, nog geen of onvolledige intake | geen project, of status `leeg` / `in_bewerking` | `partner-intake` — het compleetheidsrapport vertelt precies wat er nog mist |
| Intake compleet, seintje gegeven, Gaply richt in | status compleet (`compleet_voor_demo` of hoger), maar er is nog geen eind-seintje | **Wachtmoment** — zie hieronder |
| Eind-seintje binnen: alles staat live | Gaply heeft gemeld dat de omgeving op productie draait | `partner-beheer` — activatie, beheerinstructie en de eerste golden-set-review |
| Search Console gekoppeld, nog geen vraag-nulmeting | `get_gsc_status` staat, `get_gap_sources` toont vragen uit Search Console | `partner-nulmeting`, deel B (Inzichten over de hele site) |
| Nulmeting klaar | het startrapport is compleet | Werk vanuit Inzichten: `partner-contentvoorstellen` voor de grootste gaten per onderwerp. Zet nu geen focusgebieden op |
| Een onderwerp vraagt om verdieping | een onderwerp uit Inzichten is groot of belangrijk genoeg voor een eigen, vaste meting | `partner-focusgebieden` — de verdiepende gap-analyse, later en alleen waar het iets toevoegt |
| Draait een maand | — | `partner-rapportage`, één volle kalendermaand na livegang; daarna de cadans uit `partner-beheer` |
| Er staat een juridisch akkoord open, er is een nieuwe documentversie gepubliceerd, of een klant vraagt om de verwerkersovereenkomst of het acceptatiebewijs | melding in het dashboard, of `get_legal_acceptance_status` op je eigen organisatie meldt iets openstaands | `partner-juridisch` |

## Het wachtmoment

Er zijn twee punten waarop de bal bij Gaply ligt en de juiste actie melden
en wachten is, niet doorduwen: **na de contractaanvraag** (Gaply zet de
documenten klaar en verstuurt ze; jij bewaakt alleen dat ze getekend
worden) en **na de intake**.

Zodra het compleetheidsrapport niets verplichts meer mist, meld je dat bij
Gaply (info@gaply.nl) — er is geen automatische melding, dus zonder dit
bericht weet Gaply niet dat je klaar bent. Gaply controleert de context en
draait daarna de volledige inrichting van A tot Z, tot en met promotie naar
productie, zonder tussenstops. Er is geen demo-gate en geen aparte
livegang-aanvraag meer. Je hoort het als alles live staat (het
**eind-seintje**); pas dán begint jouw activatiewerk — front-end, Search
Console, de vraag-nulmeting uit Inzichten en, als de klant zelf meekijkt,
klantaccounts — en loopt het beheer door via `partner-beheer`.

Die route loopt **naast** het traject, niet erin: het juridische akkoord hangt
aan je organisatie en niet aan een klant, dus het kan op elk moment opkomen —
bij de eerste klant, of jaren later bij een nieuwe documentversie. Zie het als
een eigen ingang, geen fase.

## Inzichten eerst, focusgebieden later

Een traject begint met Inzichten: het beeld over de hele site, per onderwerp
en per vraagcluster. Daar stuur je op, daar komen de contentvoorstellen uit
en daar rapporteer je over. Een focusgebied is een verdieping op één
onderwerp en komt pas als dat onderwerp erom vraagt. Begin er dus niet mee,
ook niet als de klant de term kent.

## Grenzen

- Deze skill routeert alleen; hij maakt niets aan en wijzigt niets.
- Sla geen stap over omdat de klant haast heeft — de gates bestaan omdat
  een demo op een halve intake of een livegang op een halve inrichting
  méér tijd kost, niet minder.
