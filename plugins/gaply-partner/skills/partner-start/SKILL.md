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

Dit pakket heeft zes werk-skills. Deze zevende vertelt je welke je nodig
hebt. Stel eerst vast waar de klant staat, verwijs dan door — en begin niet
zelf alvast aan werk dat bij een andere skill (of bij Gaply) hoort.

## Zo bepaal je waar de klant staat

1. **Toegang checken** — `get_my_access`. Zie je je partner-organisatie
   niet, of krijg je een 403: stop en meld het bij Gaply (info@gaply.nl).
   Een 403 is in dit pakket nooit iets om omheen te werken.
2. **Bestaat het project al?** — `list_projects` in je eigen organisatie.
   - **Nee** → is de offerte getekend? Zo nee: `partner-offerte`. Zo ja:
     `partner-intake` (die begint met het aanmaken van het project, stap 0).
   - **Ja** → lees `get_project_context` en kijk naar
     `completeness.status`; de tabel hieronder wijst de weg.

## De route

| Waar de klant staat | Signaal | Skill / actie |
|---|---|---|
| Nog geen getekende offerte | — | `partner-offerte` |
| Akkoord, nog geen of onvolledige intake | geen project, of status `leeg` / `in_bewerking` | `partner-intake` — het compleetheidsrapport vertelt precies wat er nog mist |
| Intake compleet, Gaply richt in | status `compleet_voor_demo` of hoger, maar zoeken/chat op de testomgeving levert nog niets op | **Wachtmoment 1** — zie hieronder |
| Omgeving ingericht en testklaar | Gaply heeft testklaar gemeld; `search_knowledge_base` geeft resultaten op de testomgeving | `partner-focusgebieden` |
| Focusgebieden doorgerekend en met de klant besproken | `list_lenses`: lastRefreshedAt gevuld | `partner-contentvoorstellen` |
| Content op orde, klant wil live | check status `compleet_voor_livegang` | `partner-livegang` — voorbereiden en aanvragen; de uitvoering doet Gaply (**wachtmoment 2**) |
| Live | — | `partner-rapportage`, één volle kalendermaand na livegang |

## De twee wachtmomenten

Op twee punten ligt de bal bij Gaply en is de juiste actie: melden en
wachten, niet doorduwen.

1. **Na de intake.** Zodra het rapport `compleet_voor_demo` (of hoger)
   toont, meld je dat bij Gaply (info@gaply.nl) — er is nog geen
   automatische melding, dus zonder dit bericht weet Gaply niet dat je klaar
   bent. Gaply richt daarna de omgeving in (bronnen, crawl, motor) en meldt
   wanneer de testomgeving klaarstaat. Pas dán heeft `partner-focusgebieden`
   iets om op te bouwen.
2. **Na de livegang-aanvraag.** `partner-livegang` dient de aanvraag in;
   Gaply voert uit (synchronisatie, sleutels, widget) en levert de
   tag-/embed-instructie terug. Jij coördineert daarna alleen de plaatsing
   aan klantzijde.

## Grenzen

- Deze skill routeert alleen; hij maakt niets aan en wijzigt niets.
- Sla geen stap over omdat de klant haast heeft — de gates bestaan omdat
  een demo op een halve intake of een livegang op een halve inrichting
  méér tijd kost, niet minder.
