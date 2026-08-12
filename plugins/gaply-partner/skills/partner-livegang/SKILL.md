---
name: partner-livegang
description: >-
  Livegang van een Gaply-klantproject voorbereiden en aanvragen: gereedheid
  checken, klant-akkoord vastleggen, de aanvraag bij Gaply indienen en de
  klant-acties coördineren. De livegang zelf (sync naar productie, API-keys,
  widget-configuratie) voert Gaply uit — nooit de partner. Gebruik bij "live
  zetten", "livegang [klant]", "naar productie" of "de zoekfunctie op de site
  zetten".
---

# Partner-livegang

**De livegang wordt uitgevoerd door Gaply, nooit door de partner.** Jouw rol
is de voorbereiding: vaststellen dat alles er klaar voor is, het akkoord van
de klant vastleggen, de aanvraag bij Gaply indienen en daarna de acties aan
klantzijde coördineren. Kom je ergens een schrijfactie richting productie
tegen (synchronisatie, API-keys, widget-instellingen) — dan hoort die niet
bij jou; een 403 daarop is correct gedrag, geen rechtenprobleem.

## Checklist vóór de aanvraag

Loop deze punten na en benoem expliciet wat nog openstaat:

1. **Projectcontext op `compleet_voor_livegang`** — check via
   `get_project_context`. Het rapport vertelt precies welke laag-2-velden nog
   ontbreken of onbevestigd zijn (widget-domeinen, merkkleuren/logo,
   beheerder, tagmanager-beheerder, kantoor-IP's, livegang-datum). Gaply
   gebruikt die velden bij de uitvoering; onvolledig betekent dat de
   livegang niet start.
2. Focusgebieden staan op test, zijn doorgerekend (`list_lenses`:
   lastRefreshedAt gevuld) en met de klant besproken.
3. De grootste contentgaten van de startfase zijn geadresseerd of bewust
   geaccepteerd door de klant.
4. Proefondervindelijk getest: stel via `ask_chat` en `search_knowledge_base`
   de tien belangrijkste klantvragen op de testomgeving en beoordeel de
   antwoorden samen met de klant.
5. De klant heeft akkoord gegeven op livegang — leg de datum vast (bevestig
   ook `livegang.datum` in de projectcontext als die afwijkt).

## De aanvraag

Meld de livegang aan bij Gaply (info@gaply.nl) met: klant/project, de
afgesproken livegang-datum en eventuele bijzonderheden. Gaply voert de
livegang uit: de synchronisatie van test naar productie, de origin-gebonden
API-key, de widget-configuratie in de huisstijl uit de projectcontext, de
nulmeting en het aanzetten van de kwaliteitsbewaking. Ook een standalone
agent (indien afgesproken) en custom domains lopen via Gaply.

Gaply levert na uitvoering de embed-instructie of tagmanager-tag terug.

## Coördinatie aan klantzijde

- De **tagmanager-beheerder** (contactpersoon uit de projectcontext) plaatst
  de tag of de webbouwer plaatst de embed — dat is de enige technische
  handeling buiten Gaply, en die ligt bij de klant of bij jou als partner,
  op de klántsite.
- Stem de communicatie rond het livegang-moment af met de dagelijks
  beheerder.

## Verificatie na livegang

- Stel op de live site enkele kernvragen en controleer de antwoorden.
- Controleer na de eerste dagen `list_interaction_logs` op verkeer en
  `get_gap_sources` of de bronnen data leveren.
- Plan direct de eerste maandrapportage in (skill `partner-rapportage`), één
  volle kalendermaand na livegang.

## Grenzen

- **De partner voert de livegang nooit zelf uit**: geen synchronisatie naar
  productie, geen API-keys aanmaken of wijzigen, geen widget-instellingen
  schrijven, geen standalone agents aanmaken. Dat is allemaal Gaply-werk.
- Geen wijzigingen aan bronnen, zoek- of AI-instellingen; storingen of gekke
  antwoorden meld je bij Gaply.
- Custom domains en certificaten lopen via Gaply.
