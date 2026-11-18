---
name: partner-rapportage
description: >-
  Maandelijkse zoek- of chatrapportage per Gaply-eindklant, met het vraagbeeld
  en de contentroadmap per onderwerp uit Inzichten (en per focusgebied waar
  die er zijn) en verbruik op projectniveau, als HTML in de huisstijl van
  de eindklant met de partner als afzender. Gebruik bij "maandrapportage",
  "rapportage voor [klant]", "hoe presteert de zoekfunctie" of "maandelijkse
  update naar de klant".
---

# Partner-rapportage (maandelijks)

De eindklant ziet elke maand hoe de zoekfunctie of chat presteert, waar
bezoekers naar vragen en welke content er per onderwerp ontbreekt. De
partner is afzender. Of het rapport "in samenwerking met Gaply" vermeldt,
staat in `config/branding.md` (veld Vermelding van Gaply).

## Twee harde regels (lees eerst)

1. **Dekking, contentgaten en voortgang rapporteer je per onderwerp uit
   Inzichten en, waar ze er zijn, per focusgebied. Nooit als één cijfer over
   de hele omgeving.** Een klant begint met Inzichten en heeft dan nog geen
   focusgebieden; het beeld per onderwerp is dan de basis van het rapport.
   Komt er later een focusgebied als verdieping bij, dan rapporteer je dat
   apart, met zijn eigen cijfers (lensId). Tel onderwerpen en focusgebieden
   niet bij elkaar op en vul het ene niet aan met het andere. Alleen
   **bereik** mag over al het verkeer: aantal zoekopdrachten of
   chatgesprekken, aandeel met en zonder resultaat. AI-zichtbaarheid noem
   je alleen waar die gemeten is.
2. **Geen cijfer dat niet uit een tool-respons komt, en alleen werkelijk
   gestelde bezoekersvragen.** Een leeg of misleidend rapport is schadelijker
   dan geen rapport.

## Stap 0 — Klant, kanaal en huisstijl

1. Los de id's op (`resolve_path` of lijst-tools); gebruik volledige
   environment-UUID's.
2. Kanaal bepalen met `get_gap_sources`: draait `site_search` met verkeer,
   dan een zoekrapportage; draait alleen `chat`, dan een chatrapportage.
   Rapporteer nooit een leeg kanaal.
3. Huisstijl van de EINDklant (merkkleur hex, logo-URL): dit zijn sinds de
   intake verplichte velden in de projectcontext — haal ze eerst op met
   `get_project_context`. Ontbreken ze daar (een oudere intake, van vóór ze
   verplicht werden), val dan terug op de website van de klant of eerdere
   rapportages; verzin geen kleuren. De afzenderbranding van de partner komt
   uit `config/branding.md`.

## Stap 1 — Weigeren bij te weinig data

Controleer verkeer (`list_interaction_logs`, aggregates.total) en of er een
vraagbeeld is: beoordeelde vraagclusters in Inzichten
(`get_insights_summary`, `list_insight_topics`). Focusgebieden zijn niet
nodig voor een rapport. Geen verkeer: geen rapport, meld wat er ontbreekt.
Wel verkeer maar nog geen beoordeelde clusters: overleg of een bereik-only
rapport zin heeft.

## Stap 2 — De cijfers

Periode: de volledige vorige kalendermaand, vergeleken met de maand ervoor
(of "eerste volledige maand"). Bij de eerste rapportage is de nulmeting
(skill `partner-nulmeting`) het vergelijkingspunt: noem wat er sinds dat
startpunt is veranderd, in plaats van een vorige maand die er niet is.

- **Bereik** (mag omgevingsbreed): `list_interaction_logs(channel, dateFrom,
  dateTo, limit=1)` → aggregates `total` en `empty`; aandeel zonder resultaat
  is `empty / total`. Per week voor de verloopgrafiek; het maandtotaal is het
  kerncijfer.
- **Topvragen**: `get_interaction_frequency` — alleen werkelijk gestelde
  vragen.
- **Vraagbeeld per onderwerp (Inzichten)**: `list_insight_topics` over de
  rapportagemaand en over de maand ervoor (`from`, `to`), met dezelfde
  drempels als de nulmeting. Per onderwerp: het aantal vraagclusters dat
  beantwoord is (covered), deels beantwoord (partial) en niet beantwoord
  (gap). Clusters die nog niet beoordeeld zijn (none) noem je apart en tel
  je nergens bij op. `get_insights_summary` geeft het aantal gaten dat sinds
  de vorige periode is gedicht.
- **Verdieping per focusgebied, alleen als er focusgebieden zijn**: per lens
  `get_metrics_trend` (bucket week) voor dekking, gaten en AI-zichtbaarheid,
  en `get_metrics_compare` (altijd mét lensId) voor opgeloste en nieuwe
  gaten. Het omgevingsbrede `get_metrics_trend` alleen voor de operationele
  markers (doorgevoerde verbeteringen), nooit als klantdekkingscijfer.
- **Wat er is gedaan**: doorgevoerde contentvoorstellen en, als die er zijn,
  bijgekomen of doorgerekende focusgebieden (`list_lenses`: createdAt,
  lastRefreshedAt).
- **Verbruik (projectniveau)**: `get_cost_overview` voor het
  verbruiksoverzicht van het project; neem dit beknopt op als de afspraak met
  de klant dat vraagt, zonder interne kostendetails.

## Stap 3 — De contentroadmap

`list_missing_content(environmentId, from, to, limit=20)` geeft de
vraagclusters zonder goed antwoord, de meest gestelde eerst. Neem de tien
hoogste en groepeer ze per onderwerp (`topic`). Gebruik het
`improvement`-veld als aanbeveling; is dat leeg, beschrijf dan alleen wat
er gezocht wordt. Verzin geen aanbevelingen. Is er een focusgebied, geef dan
aan welke van deze tien daarbinnen vallen.

## Stap 4 — Bouw het rapport

HTML, print-klaar op A4, in de huisstijl van de eindklant; bovenaan de CSS één
blok met de klantvariabelen (kleuren, logo). Bestandsnaam
`<klant>-zoekrapportage-<maand>-<jaar>.html` (of `-chatrapportage-`).

Secties, in volgorde: kop (klantlogo, "door [partner]" met de vermelding
van Gaply volgens `config/branding.md`, periode); in het kort (vier of vijf zinnen, verhalend); vier
kerncijfers (bereikcijfers plus één dekkingscijfer dat expliciet bij één
onderwerp of focusgebied hoort, met naam); wat er sinds vorige maand is
gedaan (met datums); verloop over de maand (volume per week mag
omgevingsbreed, dekking alleen per onderwerp of focusgebied); waar bezoekers
naar zoeken (top 20 echte vragen); onderwerpen (per onderwerp hoeveel
vraagclusters beantwoord, deels en niet beantwoord zijn, en de beweging
sinds vorige maand; nog niet beoordeeld expliciet benoemen); focusgebieden,
alleen als ze er zijn (per gebied dekking, open gaten, AI-zichtbaarheid en
beweging); wat niets opleverde (uitgesplitst naar type); contentroadmap
(tien clusters, per onderwerp); wat ons opviel (één observatie); wat wij
van jullie nodig hebben (alleen indien echt nodig); over deze rapportage
(bron en meetbeperkingen).

Voeg geen extra cijfers toe: het rapport werkt omdat het weinig getallen
heeft en die goed uitlegt. Toon: zakelijk Nederlands, geen marketingtaal,
tegenvallers gewoon benoemen met verklaring, geen gedachtestrepen, datums als
"1 t/m 5 juli".

## Stap 5 — Oplevering

Lever het HTML-bestand op aan de gebruiker, met een concept-begeleidmail van
zes tot tien regels (belangrijkste ontwikkeling plus het belangrijkste
roadmap-punt) die de partner zelf verstuurt. Verstuur nooit zelf iets naar de
eindklant.

## Grenzen

- Nooit zelf versturen; de partner verstuurt.
- Dekkingscijfers alleen per onderwerp of per focusgebied, nooit over de
  hele omgeving; onderwerpen en focusgebieden niet optellen.
- Interne Gaply-kosten of prijsafspraken horen niet in een klantrapport;
  alleen het verbruiksoverzicht op projectniveau, indien afgesproken.
