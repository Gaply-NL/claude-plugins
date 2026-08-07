# Gaply Partner-plugin

Werkpakket voor Gaply-implementatiepartners (zoals Webbio, Leadrs en Sterk).
De partner doet de sales en de implementatie richting de eindklant; Gaply
draait het systeem. Deze plugin geeft de agent van de partner precies de
werkstromen die daarbij horen.

## De zes skills

| Skill | Wanneer |
|---|---|
| partner-offerte | Offerte-PDF in partnerhuisstijl op de vaste Gaply-prijslijst |
| partner-intake | Na akkoord: gestandaardiseerde overdracht naar Gaply voor de inrichting |
| partner-focusgebieden | Focusgebieden opzetten, doorrekenen en duiden met de klant |
| partner-contentvoorstellen | Van contentgat naar geplaatste, geverifieerde content |
| partner-rapportage | Maandrapportage per eindklant, met roadmap per focusgebied |
| partner-livegang | Sync naar productie, widget en API-keys, verificatie |

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
zoeken. Focusgebieden en instellingen wijzig je op de testomgeving; live
zetten gaat via de environment-sync (skill partner-livegang).
