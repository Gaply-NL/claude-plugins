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
- `references/intake-template.md` is **verwijderd**. De uitleg per veld
  (waarom Gaply het vraagt, met voorbeelden) zit voortaan als `helpText` ín
  de template zelf en komt mee met `get_project_context_template` — één bron
  van waarheid, geen lokaal document dat kan verouderen. Ook de papieren
  terugvaloptie (intake-document mailen bij een niet-werkende koppeling) is
  vervallen: bij een 403 of onbereikbare MCP meld je het bij Gaply en wordt
  de koppeling hersteld — een intake buiten de validatie om bestaat niet
  meer.
- Nieuwe sectie in `partner-intake`: **de partner koppelt Search Console
  zelf** via de Gaply-webinterface (browser-login vereist; MCP kan de status
  wel checken via `get_gsc_status`, de koppeling niet leggen). Gaply zit hier
  bewust niet tussen.
- `partner-focusgebieden` en `partner-rapportage` verwijzen nu naar de
  projectcontext (`get_project_context`) voor respectievelijk
  focusgebied-kandidaten en de verplichte huisstijlvelden (merkkleur,
  logo-URL), in plaats van die los te laten zoeken.
- **`partner-livegang` voert de livegang niet meer zelf uit.** De uitvoering
  (synchronisatie naar productie, API-keys, widget-configuratie, standalone
  agents) ligt volledig bij Gaply; de skill bereidt voor (gereedheids-check
  incl. `compleet_voor_livegang` op de projectcontext, klant-akkoord), dient
  de aanvraag in bij Gaply en coördineert de klant-acties (tag-plaatsing door
  de tagmanager-beheerder uit de projectcontext). Alle prod-schrijfacties
  (`sync_environment` met `allowProduction`, `create_api_key`,
  `update_api_key_allowed_origins`, `set_widget_settings`,
  `create_standalone_agent`) zijn uit de skill verwijderd.
- Plugin-README bijgewerkt: intake- en livegang-omschrijvingen kloppen weer
  met de werkelijke flow; rolverdeling benoemt expliciet dat livegang
  Gaply-werk is.

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
