---
name: partner-rapportage
description: >-
  Maandelijkse zoek- of chatrapportage per Gaply-eindklant, met contentroadmap
  per focusgebied en verbruik op projectniveau, als HTML in de huisstijl van
  de eindklant met de partner als afzender. Gebruik bij "maandrapportage",
  "rapportage voor [klant]", "hoe presteert de zoekfunctie" of "maandelijkse
  update naar de klant".
---

# Partner-rapportage (maandelijks)

De eindklant ziet elke maand hoe de zoekfunctie of chat presteert, waar
bezoekers naar vragen en welke content er ontbreekt op de focusgebieden. De
partner is afzender; het rapport vermeldt "in samenwerking met Gaply".

## Twee harde regels (lees eerst)

1. **KB-dekking, contentgaten, AI-zichtbaarheid en voortgang meet je
   UITSLUITEND per focusgebied (lensId).** Nooit op het omgevingsbrede
   alle-vragen-cijfer. Alleen **bereik** mag over al het verkeer: aantal
   zoekopdrachten of chatgesprekken, aandeel met en zonder resultaat. Heeft
   een focusgebied nog geen meting, meld dat; vul het nooit aan met het
   omgevingscijfer. De contentroadmap bevat alleen clusters die aan een
   bestaand focusgebied hangen.
2. **Geen cijfer dat niet uit een tool-respons komt, en alleen werkelijk
   gestelde bezoekersvragen.** Een leeg of misleidend rapport is schadelijker
   dan geen rapport.

## Stap 0 — Klant, kanaal en huisstijl

1. Los de id's op (`resolve_path` of lijst-tools); gebruik volledige
   environment-UUID's.
2. Kanaal bepalen met `get_gap_sources`: draait `site_search` met verkeer,
   dan een zoekrapportage; draait alleen `chat`, dan een chatrapportage.
   Rapporteer nooit een leeg kanaal.
3. Huisstijl van de EINDklant (merkkleur hex, logo-URL): van de website van de
   klant of uit eerdere rapportages; verzin geen kleuren. De afzenderbranding
   van de partner komt uit `config/branding.md`.

## Stap 1 — Weigeren bij te weinig data

Controleer verkeer (`list_interaction_logs`, aggregates.total) en of er
minstens één gemeten focusgebied is (`list_lenses` + `get_metrics_trend` met
lensId). Geen verkeer: geen rapport, meld wat er ontbreekt. Wel verkeer maar
geen gemeten focusgebied: overleg of een bereik-only rapport zin heeft.

## Stap 2 — De cijfers

Periode: de volledige vorige kalendermaand, vergeleken met de maand ervoor
(of "eerste volledige maand").

- **Bereik** (mag omgevingsbreed): `list_interaction_logs(channel, dateFrom,
  dateTo, limit=1)` → aggregates `total` en `empty`; aandeel zonder resultaat
  is `empty / total`. Per week voor de verloopgrafiek; het maandtotaal is het
  kerncijfer.
- **Topvragen**: `get_interaction_frequency` — alleen werkelijk gestelde
  vragen.
- **Dekking en kwaliteit, per focusgebied**: per lens `get_metrics_trend`
  (bucket week) voor dekking, gaten en AI-zichtbaarheid, en
  `get_metrics_compare` (altijd mét lensId) voor opgeloste en nieuwe gaten.
  Het omgevingsbrede `get_metrics_trend` alleen voor de operationele markers
  (doorgevoerde verbeteringen), nooit als klantdekkingscijfer.
- **Wat er is gedaan**: doorgevoerde contentvoorstellen en bijgekomen of
  doorgerekende focusgebieden (`list_lenses`: createdAt, lastRefreshedAt).
- **Verbruik (projectniveau)**: `get_cost_overview` voor het
  verbruiksoverzicht van het project; neem dit beknopt op als de afspraak met
  de klant dat vraagt, zonder interne kostendetails.

## Stap 3 — De contentroadmap

`list_missing_content(environmentId, from, to, limit=20)`. Alleen clusters met
een `topic` dat bij een ingericht focusgebied hoort. Rangschik op askedCount,
maal 2 bij label "gap", maal 1 bij "partial"; neem de tien hoogste. Gebruik
het `improvement`-veld als aanbeveling; is dat leeg, beschrijf dan alleen wat
er gezocht wordt. Verzin geen aanbevelingen.

## Stap 4 — Bouw het rapport

HTML, print-klaar op A4, in de huisstijl van de eindklant; bovenaan de CSS één
blok met de klantvariabelen (kleuren, logo). Bestandsnaam
`<klant>-zoekrapportage-<maand>-<jaar>.html` (of `-chatrapportage-`).

Secties, in volgorde: kop (klantlogo, "door [partner], in samenwerking met
Gaply", periode); in het kort (vier of vijf zinnen, verhalend); vier
kerncijfers (bereikcijfers plus één dekkingscijfer dat expliciet per
focusgebied is, met naam); wat er sinds vorige maand is gedaan (met datums);
verloop over de maand (volume per week mag omgevingsbreed, dekking alleen per
focusgebied); waar bezoekers naar zoeken (top 20 echte vragen); focusgebieden
(per gebied dekking, open gaten, AI-zichtbaarheid en beweging; niet-gemeten
expliciet benoemen); wat niets opleverde (uitgesplitst naar type);
contentroadmap (tien onderwerpen); wat ons opviel (één observatie); wat wij
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
- Dekkingscijfers alleen per focusgebied; roadmap alleen binnen de
  focusgebieden.
- Interne Gaply-kosten of prijsafspraken horen niet in een klantrapport;
  alleen het verbruiksoverzicht op projectniveau, indien afgesproken.
