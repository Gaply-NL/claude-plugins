# Changelog — gaply-partner

Alle wijzigingen aan deze plugin worden hier bijgehouden. Versies volgen
[semver](https://semver.org/lang/nl/): MAJOR bij wijzigingen waardoor partners
hun werkwijze moeten aanpassen, MINOR bij nieuwe of gewijzigde skills en
prijslijst-/beleidswijzigingen, PATCH bij tekstuele fixes.

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
- `references/intake-template.md` is omgezet van invulformulier naar een
  korte toelichting per sectie — achtergrond, geen invullijst.
- `partner-focusgebieden` en `partner-rapportage` verwijzen nu naar de
  projectcontext (`get_project_context`) voor respectievelijk
  focusgebied-kandidaten en de verplichte huisstijlvelden (merkkleur,
  logo-URL), in plaats van die los te laten zoeken.

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
