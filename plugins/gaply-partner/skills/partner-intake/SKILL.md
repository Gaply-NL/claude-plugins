---
name: partner-intake
description: >-
  Verzamelt na een getekende Gaply-offerte alle input die Gaply nodig heeft om
  het klantproject in te richten, en levert één gestandaardiseerd
  intakedocument op. Gebruik bij "intake voor [klant]", "nieuwe klant
  aanmelden", "overdracht naar Gaply", "wat heeft Gaply nodig" of direct na een
  akkoord op een offerte.
---

# Partner-intake (overdracht naar Gaply)

Dit is het formele overdrachtsmoment van partner naar Gaply. Gaply richt op
basis van dit document de omgeving in: project en environments, de bronnen
(datasources), de zoek- en AI-instellingen en de kwaliteitsbewaking. Dat is
bewust werk van Gaply; de partner levert de input en neemt daarna de
inrichting van focusgebieden en content over. Hoe vollediger de intake, hoe
sneller de omgeving staat — een complete intake voorkomt heen-en-weer.

## Werkwijze

### 1. Vul het intakedocument

Gebruik `references/intake-template.md` als vaste structuur. Verzamel de
gegevens uit de offerte, de gespreksnotities en waar nodig door de gebruiker
gericht te bevragen. Verzin niets; markeer wat echt onbekend is als
"onbekend" met de reden.

Verplichte onderdelen voordat je het document oplevert:

- klantnaam, domein en de gekozen offertevariant met de bijbehorende scope
  (welke contentcategorieën wel en niet, inclusief het 12-maandenfilter voor
  nieuws);
- sitemap-overzicht uit de offerteanalyse (categorieën met aantallen);
- doelgroepen en de belangrijkste vraagtypen per doelgroep;
- toon en taalgebruik van de klant (formeel/informeel, "je" of "u");
- Google Search Console: is er toegang, en wie verleent die;
- gewenste plek van de zoekwidget (bijvoorbeeld header) en de domeinen
  waarop die komt te staan (nodig voor API-key origins);
- contactpersonen: bij de klant (redactie en techniek) en bij de partner;
- juridische randvoorwaarden of gevoeligheden die uit het gesprek bleken;
- gewenste livegang-datum.

### 2. Controleer op volledigheid

Loop het template langs; elk verplicht veld is gevuld of expliciet "onbekend"
met reden. Een intake met stille gaten kost meer tijd dan een intake die
eerlijk zegt wat er nog mist.

### 3. Lever op en draag over

Sla het document op als `intake_gaply_[klant].md` en lever het aan de
gebruiker op met de instructie het naar Gaply (info@gaply.nl) te sturen.
Vermeld in je afronding: Gaply richt de omgeving in en meldt wanneer de
testomgeving klaarstaat; daarna start de partner met de skill
`partner-focusgebieden`.

## Grenzen

- Vraag Gaply nooit om toegang tot broninrichting of zoekinstellingen; dat
  blijft bij Gaply.
- Doe geen toezeggingen over de inrichtingsduur namens Gaply; vraag het na.
