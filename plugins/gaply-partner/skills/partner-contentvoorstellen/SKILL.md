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

### 1. Kies de queries

Vertrek vanuit de focusgebieden: `get_lens_new_gaps` en `list_query_universe`
tonen de vragen zonder goed antwoord. Kies maximaal 10 samenhangende queries
per voorstel-run, bij voorkeur binnen één focusgebied. Rangschik op wat
bezoekers werkelijk vragen (askedCount), zwaarst wegend bij label "gap".

### 2. Start en beantwoord de discovery

- `start_content_proposal` met de gekozen queries; Gaply genereert
  discovery-vragen.
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
- controleer daarna met `get_lens_new_gaps` of het gat inderdaad dicht is en
  werk de gap-status bij met `set_gap_query_status`.

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
