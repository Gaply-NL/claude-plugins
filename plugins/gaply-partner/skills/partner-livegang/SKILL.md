---
name: partner-livegang
description: >-
  Livegang van een Gaply-klantproject: synchronisatie van test naar productie,
  widget-installatie op de klantsite met API-keys, en verificatie na livegang.
  Gebruik bij "live zetten", "livegang [klant]", "naar productie", "widget
  installeren" of "de zoekfunctie op de site zetten".
---

# Partner-livegang

De partner mag zelfstandig live zetten. Live zetten betekent: de op de
testomgeving ingerichte focusgebieden en instellingen naar de
productieomgeving synchroniseren en de widget op de klantsite activeren.
Direct wijzigen op productie is platformbreed geblokkeerd; alles loopt via de
sync vanaf test. Dat is normaal gedrag, geen rechtenprobleem.

## Checklist vóór livegang

Loop deze punten na en benoem expliciet wat nog openstaat:

1. Focusgebieden staan op test, zijn doorgerekend (`list_lenses`:
   lastRefreshedAt gevuld) en met de klant besproken.
2. De grootste contentgaten van de startfase zijn geadresseerd of bewust
   geaccepteerd door de klant.
3. Proefondervindelijk getest: stel via `ask_chat` en `search_knowledge_base`
   de tien belangrijkste klantvragen en beoordeel de antwoorden samen met de
   klant.
4. De klant heeft akkoord gegeven op livegang (datum vastleggen).
5. Widgetconfiguratie klaar: huisstijl en teksten via `get_widget_settings` /
   `set_widget_settings`.

## Livegang

1. **Synchroniseer naar productie**: `sync_environment` naar de
   productie-environment. Schrijfacties op productie vereisen
   `allowProduction: true`; destructieve of kostenbare acties ondersteunen
   `dryRun: true` voor een preview — gebruik die eerst.
2. **API-key voor de widget**: `create_api_key` op environment-scope. Bewaar
   de secret veilig; die wordt maar één keer getoond. Beperk de key direct tot
   de domeinen van de klant met `update_api_key_allowed_origins` (uit de
   intake).
3. **Widget op de site**: gebruik `get_widget_bookmarklet` om de plaatsing te
   demonstreren of te testen; de definitieve embed plaatst de webbouwer van de
   klant (vaak de partner zelf) volgens de widgetconfiguratie.
4. **Standalone agent** (indien afgesproken): aanmaken en configureren op de
   testomgeving (`create_standalone_agent`, branding, welkomstbericht); het
   live zetten op productie en een eventueel custom domain lopen via Gaply —
   meld het verzoek bij Gaply met de gewenste domeinnaam.

## Verificatie na livegang

- `get_sync_status` en `get_ingest_status`: synchronisatie afgerond zonder
  fouten.
- Stel op de live site enkele kernvragen en controleer de antwoorden.
- Controleer na de eerste dagen `list_interaction_logs` op verkeer en
  `get_gap_sources` of de bronnen data leveren.
- Meld de livegang aan Gaply (info@gaply.nl), zodat de kwaliteitsbewaking en
  signalering aan Gaply-kant meelopen.

Plan direct de eerste maandrapportage in (skill `partner-rapportage`), één
volle kalendermaand na livegang.

## Grenzen

- Geen wijzigingen aan bronnen, zoek- of AI-instellingen; storingen of gekke
  antwoorden meld je bij Gaply.
- API-keys nooit in chat of documentatie laten slingeren; origins altijd
  direct beperken.
- Custom domains en certificaten lopen via Gaply.
