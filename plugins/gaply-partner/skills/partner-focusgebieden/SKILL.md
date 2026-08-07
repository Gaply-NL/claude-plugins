---
name: partner-focusgebieden
description: >-
  Focusgebieden (lenses) opzetten, doorrekenen en duiden voor een
  Gaply-klantproject, samen met de eindklant. Gebruik bij "focusgebieden
  zetten voor [klant]", "gap-analyse bekijken", "welke gaten zijn er",
  "query-boom", "nieuwe gaps" of na de melding van Gaply dat de testomgeving
  klaarstaat.
---

# Partner-focusgebieden (GAP-analyse)

Een focusgebied (lens) is een afgebakend thema waarbinnen Gaply meet of de
website de vragen van bezoekers beantwoordt: dekking, contentgaten en
AI-zichtbaarheid. Focusgebieden zetten en duiden is kernwerk van de partner,
in samenspraak met de eindklant.

## Voorbereiding (elke sessie)

1. Los eerst de juiste id's op: `resolve_path` met de klantreferentie, of
   `list_organisations` → `list_projects` → `list_environments`. Vrijwel alle
   tools willen een volledige environment-UUID; een prefix geeft stilzwijgend
   lege data.
2. Werk op de **testomgeving**. Focusgebieden aanmaken en wijzigen is op een
   productie-environment platformbreed geblokkeerd; dat is normaal gedrag,
   geen rechtenprobleem. Livegang loopt via de skill `partner-livegang`.
3. Onzeker over je rechten: `get_my_access` toont wat je token kan.

## Werkwijze

### 1. Bepaal de focusgebieden met de klant

Vertrekpunt is de intake: doelgroepen en vraagtypen. Goede focusgebieden zijn
onderwerpen waar bezoekersvragen over bestaan, niet de menustructuur van de
site. Gebruik als input wat bezoekers werkelijk doen: `get_interaction_frequency`
en `list_interaction_logs` (echte zoekopdrachten en chatvragen),
`get_gsc_queries` (Google-zoekwoorden als GSC gekoppeld is) en
`get_insights_summary` / `list_insight_topics` voor de vraagclusters. Stel per
focusgebied vast: naam, afbakening (wat hoort er wel en niet bij) en de
doelgroep.

### 2. Maak aan en reken door

- `create_lens` per focusgebied op de testomgeving.
- Bekijk vóór het doorrekenen de kosten: `preview_lens_cost`. Meld de
  inschatting aan de gebruiker bij grote aantallen.
- `refresh_lens` om membership, PAA, dekkingsjudge en AI-zichtbaarheid te
  laten draaien; volg de run via `get_run` / `wait_for_run_completion`.
- Stuur bij met handmatige includes/excludes
  (`add_lens_manual_include` / `add_lens_manual_exclude`) als de automatische
  afbakening pagina's mist of ten onrechte meeneemt.

### 3. Duid de uitkomst

- `get_lens_query_tree` toont de vraagstructuur van het focusgebied.
- `get_lens_new_gaps` en `list_query_universe` tonen waar de dekking
  tekortschiet: vragen zonder goed antwoord.
- Zet per gap-query de status met `set_gap_query_status` (nieuw, afgehandeld,
  genegeerd) zodat het overzicht schoon blijft; her-toets twijfelgevallen met
  `recheck_query_coverage`.

Bespreek de uitkomst met de klant in klanttaal: welke thema's staan er goed
voor, waar zitten de grootste gaten, en wat pakken we als eerste op. De
logische vervolgstap voor de grootste gaten is de skill
`partner-contentvoorstellen`.

## Grenzen

- Alleen op de testomgeving aanmaken en wijzigen; productie alleen lezen.
- Broninrichting, zoekinstellingen en AI-instellingen zijn van Gaply. Zie je
  daar iets geks (bron valt stil, vreemde antwoorden), meld het aan Gaply in
  plaats van zelf te sleutelen — die tools heb je bewust niet.
- Verwijder geen focusgebieden van andere projecten of zonder overleg met de
  klant; `delete_lens` is onomkeerbaar voor de meetgeschiedenis.
