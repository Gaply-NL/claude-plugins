# Gaply Partner-plugin

Werkpakket voor Gaply-implementatiepartners (zoals Webbio, Leadrs en Sterk).
De partner doet de sales en de implementatie richting de eindklant; Gaply
draait het systeem. Deze plugin geeft de agent van de partner precies de
werkstromen die daarbij horen.

## De zeven skills

**Start hier:** weet je niet welke skill je nodig hebt, zeg dan gewoon
"nieuwe klant" of "wat is de volgende stap voor [klant]" — de skill
`partner-start` bepaalt waar de klant staat en wijst de weg, inclusief de
momenten waarop je op Gaply wacht.

| Skill | Wanneer |
|---|---|
| partner-start | Wegwijzer: waar staat de klant, welke skill is nu aan zet |
| partner-offerte | Offerte-PDF in partnerhuisstijl op de vaste Gaply-prijslijst |
| partner-intake | Na akkoord: de klantcontext invullen in de projectcontext van Gaply — live vragenlijst, validatie- en compleetheidsrapport in de respons |
| partner-focusgebieden | Focusgebieden opzetten, doorrekenen en duiden met de klant |
| partner-contentvoorstellen | Van contentgat naar geplaatste, geverifieerde content |
| partner-rapportage | Maandrapportage per eindklant, met roadmap per focusgebied |
| partner-livegang | Livegang voorbereiden en aanvragen — de uitvoering (sync, keys, widget) doet Gaply |

## Installatie (door Gaply, per partner)

1. **MCP-koppeling**: vervang in `.mcp.json` de placeholder-URL door de echte
   Gaply MCP-server-URL. Partnergebruikers loggen in met hun eigen
   Gaply-account; hun Partnerrol bepaalt automatisch wat de agent kan.
2. **Branding**: vul `config/branding.md` in met naam, kleuren, logo en
   afzender van de partner. Leg het partnerlogo als PNG naast dat bestand.
3. **Prijslijst**: `config/prijslijst.md` is de vaste Gaply-prijslijst en
   wordt door Gaply beheerd; de partner past die niet aan.

## Rolverdeling (belangrijk voor de agent)

De Partnerrol kan bewust NIET bij de broninrichting (datasources), de zoek- en
AI-instellingen, de golden set en het platformbeheer. Dat is de motorkap van
Gaply. Loopt een skill daar tegenaan (403 of ontbrekende tool), dan is dat
correct gedrag: meld het bij Gaply (info@gaply.nl) in plaats van een omweg te
zoeken. Focusgebieden wijzig je op de testomgeving. **De livegang zelf —
synchronisatie naar productie, API-keys, widget-configuratie — voert Gaply
uit, nooit de partner**; de skill partner-livegang bereidt voor en dient de
aanvraag in.
