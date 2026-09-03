# Gaply Partner-plugin

Werkpakket voor Gaply-implementatiepartners (zoals Webbio, Leadrs en Sterk).
De partner doet de sales en de implementatie richting de eindklant; Gaply
draait het systeem. Deze plugin geeft de agent van de partner precies de
werkstromen die daarbij horen.

## De negen skills

**Start hier:** weet je niet welke skill je nodig hebt, zeg dan gewoon
"nieuwe klant" of "wat is de volgende stap voor [klant]" — de skill
`partner-start` bepaalt waar de klant staat en wijst de weg, inclusief de
momenten waarop je op Gaply wacht.

| Skill | Wanneer |
|---|---|
| partner-start | Wegwijzer: waar staat de klant, welke skill is nu aan zet |
| partner-offerte | Offerte-PDF in partnerhuisstijl op de vaste Gaply-prijslijst |
| partner-contract | Na akkoord, vóór de intake: aanvraagformulier + verplichte verwerkersovereenkomst per project (en NDA per partner) aanvragen bij Gaply en de tekenronde bewaken |
| partner-intake | Na de getekende contractset: de klantcontext invullen in de projectcontext van Gaply — live vragenlijst, validatierapport in de respons, seintje aan Gaply |
| partner-focusgebieden | Focusgebieden opzetten, doorrekenen en duiden met de klant |
| partner-contentvoorstellen | Van contentgat naar geplaatste, geverifieerde content |
| partner-rapportage | Maandrapportage per eindklant, met roadmap per focusgebied |
| partner-livegang | Livegang voorbereiden en aanvragen — de uitvoering (sync, keys, widget) doet Gaply |
| partner-beheer | Na livegang: golden set reviewen en voorstellen indienen, beheerinstructie voor de klant, verbetercadans |
| partner-juridisch | De juridische documenten: lezen, PDF, akkoord namens je organisatie, acceptatiebewijs voor je eindklant |

## Installatie (door Gaply, per partner)

1. **MCP-koppeling**: vervang in `.mcp.json` de placeholder-URL door de echte
   Gaply MCP-server-URL. Partnergebruikers loggen in met hun eigen
   Gaply-account; hun Partnerrol bepaalt automatisch wat de agent kan.
2. **Branding**: vul `config/branding.md` in met naam, kleuren, logo en
   afzender van de partner. Leg het partnerlogo als PNG naast dat bestand.
3. **Prijslijst**: `config/prijslijst.md` is de vaste Gaply-prijslijst en
   wordt door Gaply beheerd; de partner past die niet aan.

## Rolverdeling (belangrijk voor de agent)

Elk klantproject begint met een getekende contractset: het aanvraagformulier
en de verwerkersovereenkomst (verplicht, onlosmakelijk onderdeel), naast de
geheimhoudingsovereenkomst die per partner één keer wordt getekend. Gaply
zet die documenten in PandaDoc klaar; de partner levert de gegevens aan
(skill `partner-contract`). Zonder getekende set geen intake, geen project
en geen toegang.

De Partnerrol kan bewust NIET bij de broninrichting (datasources), de zoek- en
AI-instellingen en het platformbeheer. Dat is de motorkap van Gaply. Loopt een
skill daar tegenaan (403 of ontbrekende tool), dan is dat correct gedrag: meld
het bij Gaply (info@gaply.nl) in plaats van een omweg te zoeken.

### Verwerker of subverwerker — waar jij staat

Wie welke rol heeft in de privacywetgeving hangt af van wie het contract met de
eindklant heeft, en dat verschilt per traject. Sluit de klant **rechtstreeks**
met Gaply, dan is Gaply verwerker en is de klant verwerkingsverantwoordelijke.
Loopt de klant **via jou** — de normale situatie in dit pakket — dan heb jij het
contract met de eindklant, ben jij zijn verwerker, en is Gaply **subverwerker**
in die keten.

Praktisch betekent dat drie dingen. De verwerkersovereenkomst die jij accepteert
is die tussen jouw organisatie en Gaply, niet die tussen jou en je klant; die
tweede blijft jouw eigen document. Jouw eindklant mag van jou verlangen dat je
aantoont onder welke voorwaarden je subverwerkers werken — daarvoor bestaat het
acceptatiebewijs. En jij bent het aanspreekpunt van die klant, ook over deze
documenten: vragen over de inhoud stel je aan Gaply, maar het antwoord geef je
zelf. De skill `partner-juridisch` beschrijft het hele pad, inclusief wie mag
tekenen en wat er in het bewijsstuk staat.

Voor de **golden set** ligt het genuanceerder: *bewerken* blijft Gaply-werk
(`golden_set.manage` is super-admin-only — de set is de antwoordsleutel),
maar *lezen en wijzigingen voorstellen* is partnerwerk, want daar is
klantkennis voor nodig. Dat loopt via de skill `partner-beheer` en de
capabilities `golden_set.read` en `golden_set.suggest`, die Gaply nog uitrolt
en per partner moet toekennen; tot die tijd gaat het via een export en een
mail. Focusgebieden wijzig je op de testomgeving. **De livegang zelf —
synchronisatie naar productie, API-keys, widget-configuratie — voert Gaply
uit, nooit de partner**; de skill partner-livegang bereidt voor en dient de
aanvraag in.
