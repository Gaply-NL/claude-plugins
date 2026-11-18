---
name: partner-contentvoorstellen
description: >-
  Contentvoorstellen genereren, met de eindklant afronden en de implementatie
  verifiëren voor een Gaply-klantproject. Gebruik bij "contentvoorstel",
  "content maken voor de gaten", "discovery-vragen", "voorstel reviewen" of
  "is het gat nu gedicht".
---

# Partner-contentvoorstellen

Van contentgat naar geplaatste content, samen met de redactie van de
eindklant. De klant schrijft en plaatst zelf (of de partner doet dat in
opdracht); Gaply genereert het voorstel en meet of het gat daarna dicht is.

## Voorbereiding

Los de id's op (`resolve_path` of de lijst-tools) en werk met de volledige
environment-UUID. Contentvoorstellen kunnen ook op productie; dit raakt de
engine-inrichting niet.

## Werkwijze

### 1. Kies waar je content voor maakt

**Vertrek vanuit Inzichten.** `list_missing_content` geeft de vraagclusters
waarvan is vastgesteld dat de inhoud ontbreekt, de meest gestelde eerst, met
het verbeteradvies per cluster. `get_insight_topic_clusters` geeft hetzelfde
per onderwerp, inclusief de clusters die deels beantwoord zijn. Kies per
ronde een handvol clusters binnen één onderwerp, zodat de redactie in één
keer een samenhangend stuk kan schrijven. `get_query_cluster` laat van een
cluster de kernvraag, de formuleringen en de pagina's zien die er nu het
dichtst bij komen.

Controleer vóór je begint of het gat geen technische oorzaak heeft (zie
`partner-nulmeting`, stap B4). Voor een pagina die bestaat maar niet is
ingelezen, schrijf je geen nieuwe content.

**Is er een focusgebied voor dit onderwerp**, dan kun je ook daaruit
vertrekken: `get_content_proposal_seeds` en `get_lens_new_gaps` geven de
vragen zonder goed antwoord binnen dat focusgebied. Kies dan maximaal tien
samenhangende vragen per ronde.

### 2. Start en beantwoord de discovery

- Vanuit een cluster: `start_content_proposal` met `clusterId` en de
  kernvraag van het cluster (`canonicalQueryId`) als enige waarde in
  `queryIds`. Je krijgt één voorstel dat alle formuleringen van het cluster
  dekt.
- Vanuit losse vragen in een focusgebied: `start_content_proposal` met de
  gekozen vragen (en `lensId`).
- Gaply genereert in beide gevallen discovery-vragen.
- Beantwoord de discovery-vragen SAMEN met de klant; daar zit de kennis die
  niet op de site staat. Verzin geen antwoorden namens de klant. Dien ze in
  met `submit_content_proposal_answers`; Gaply genereert dan content plus een
  plaatsingsvoorstel.
- Wil de redactie een andere plek: `set_content_proposal_placement` vóór de
  generatie.

### 3. Review met de klant

- `get_content_proposal` en `get_content_proposal_seeds` voor het voorstel en
  de brondata.
- Akkoord of afwijzen: `set_content_proposal_review`. Bij afwijzing met
  feedback: `regenerate_content_proposal`.
- Opruimen: `archive_content_proposal` (omkeerbaar). Verwijder voorstellen
  niet permanent.

### 4. Na plaatsing: verifieer

Zodra de klant de content heeft geplaatst:

- `set_proposal_implementation` (bevestigd of gecorrigeerd);
- `verify_proposal_implementation` voor een gerichte recrawl plus
  dekkings-hertoets;
- controleer daarna of het gat inderdaad dicht is: in Inzichten met
  `get_query_cluster` (het oordeel over het cluster), binnen een focusgebied
  met `get_lens_new_gaps`. Werk de status van de vraag bij met
  `set_gap_query_status`.

Koppel het resultaat terug aan de klant: welke vragen nu wél beantwoord
worden. Dit is ook de kerninhoud van de maandrapportage
(skill `partner-rapportage`).

## Grenzen

- Nooit content publiceren zonder review van de klant; de klant blijft
  eigenaar van de site.
- Geen queries handmatig in bulk importeren in het universum; dat loopt via
  Gaply.
- Feedback over de kwaliteit van gegenereerde antwoorden of de zoekresultaten
  zelf gaat naar Gaply; de engine-instellingen zijn bewust niet toegankelijk.
