# Achtergrond bij de projectcontext-vragenlijst

De vragen zelf komen live uit `get_project_context_template` op de `gaply`
MCP-server. **Dit bestand is geen invulformulier** en dupliceert de
vragenlijst niet — gebruik het als achtergrond: wat elke sectie betekent en
waarom Gaply het vraagt, zodat je weet waar je moet doorvragen. Welke velden
verplicht zijn, en voor welke laag (1 = vóór de demo, 2 = vóór livegang),
staat per veld in het template zelf, niet hier.

De secties hieronder volgen de indeling van de bestaande template, aangevuld
met de secties en velden die erbij zijn gekomen.

## 1. Klant en domein

Basisidentificatie: organisatie, website(s), sitemap-URL('s), CMS/technische
stack. Zonder dit kan Gaply niet eens beginnen met crawlen.

## 2. Scope

Wat Gaply wel en niet meeneemt, met de reden — de gekozen offertevariant en
het 12-maandenfilter voor nieuws.

- **Sitemap-overzicht** (categorieën met aantallen) is een eigen veld: Gaply
  gebruikt dit om de crawl-omvang te plannen en achteraf te verifiëren dat de
  crawl klopt met wat er op de site staat.
- **No-go-onderwerpen**: wat absoluut niet in de chat of zoekresultaten mag
  verschijnen. Mag bevestigd leeg zijn — een klant zonder gevoelige
  onderwerpen bestaat — maar sla het nooit ongevraagd over; Gaply wil weten
  dát je het gevraagd hebt, niet aannemen dat het niet van toepassing is.

## 3. Doelgroepen en vraagtypen

Wie bezoekt de site, met welke vragen, via welk kanaal nu (telefoon, mail,
balie). Voedt samen met de sectie hieronder de focusgebied-indeling.

## 4. Vragen die bezoekers écht stellen

De zwaarste eis van de hele lijst: minimaal tien concrete vragen, zoals
bezoekers ze letterlijk zouden stellen — geen onderwerpen, geen
samenvattingen. Deze lijst voedt zowel de demo-vulling als de meetlat
waartegen Gaply de antwoordkwaliteit later beoordeelt. Minder dan tien
levert geen bruikbare demo op; dit is niet onderhandelbaar.

## 5. Focusgebied-kandidaten

Onderwerpen die naar verwachting een eigen focusgebied verdienen: onderwerp,
waarom, en een paar voorbeeldvragen per kandidaat. Focusgebieden zijn
volledig partnerwerk (skill `partner-focusgebieden`) — hier legt de partner
de eerste kandidaten vast, zodat die skill niet blanco hoeft te beginnen.

## 6. Toon en taal

Aanspreekvorm (je/u), toon (zakelijk, warm, neutraal), vermeden of juist
gewenste formuleringen — én de **taal/talen** van de site en van de demo.
Dat laatste stond niet in de oude template en is nodig zodra een klant
meertalig is, of de demo in een andere taal moet dan de hoofdsite.

## 7. Data en koppelingen

Google Search Console-toegang, een eventuele bestaande zoekfunctie op de
site, analytics-gevoeligheden, en de **kantoor-IP's** van de klant — nodig
zodat verkeer van de klant zelf niet meetelt in de metingen
(intern-verkeer-filtering).

## 8. Widget en livegang

Plek van de widget, domeinen waarop die komt (voor API-key origins),
**merkkleur(en) hex en logo-URL**, de gewenste livegang-datum, en de
**demo-datum**. Merkkleur en logo-URL zijn verplicht geworden: de skill
`partner-rapportage` eist ze al hard en verbiedt ze te verzinnen — die kunnen
nu gewoon uit de intake komen, in plaats van dat de rapportage-skill zelf op
zoek moet.

## 9. Contactpersonen

Naast redactie en techniek bij de klant, en de projectlead bij de partner:
de **dagelijks beheerder namens de klant** en de **beheerder van de
tagmanager** zijn eigen contactrollen. De contactpersoon is niet
vanzelfsprekend dezelfde persoon als de beheerder — vraag het apart uit.

## 10. Bijzonderheden

Juridische randvoorwaarden of gevoeligheden, toezeggingen uit het
verkooptraject die Gaply moet kennen, en het **doel met Gaply** — bij
voorkeur een letterlijk citaat van de klant. Dat citaat is waardevoller dan
een samenvatting: het is precies wat Gaply moet waarmaken.
