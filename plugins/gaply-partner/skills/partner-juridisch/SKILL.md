---
name: partner-juridisch
description: >-
  De juridische documenten van Gaply: lezen, als PDF downloaden, namens je
  organisatie accepteren met de bevoegdheidsverklaring, en het
  acceptatiebewijs terugvinden om aan je eindklant te overleggen. Gebruik bij
  "juridische documenten", "verwerkersovereenkomst", "DPA", "algemene
  voorwaarden", "security-bijlage", "ik moet iets accepteren", "er staat een
  melding dat ik akkoord moet geven", "mijn klant vraagt om de
  verwerkersovereenkomst" of "er is een nieuwe versie gepubliceerd".
---

# Juridische documenten

Gaply publiceert drie documenten waar elke partnerorganisatie akkoord op geeft:
de **algemene voorwaarden**, de **verwerkersovereenkomst** (DPA) en de
**security-bijlage**. Zonder dat akkoord loopt de dienst niet — en je eindklant
kan er bovendien naar vragen, want zijn eigen verwerkersovereenkomst met jou
verplicht hem te weten wie er verderop in de keten met de gegevens werkt.

Deze skill dekt vier dingen: **wat er ligt**, **wie tekent**, **hoe je tekent**,
en **hoe je het bewijs terugvindt** als je klant erom vraagt.

## Waar jij staat in de keten

Twee rollen, en welke van de twee geldt hangt af van wie de klant is:

- **Directe klant van Gaply** — de klant sluit zelf met Gaply. Gaply is dan
  **verwerker**, de klant is verwerkingsverantwoordelijke.
- **Klant via jou** — jij hebt het contract met de eindklant, Gaply levert aan
  jou. Dan is jouw organisatie de verwerker richting die klant, en is Gaply
  **subverwerker**. Dit is de normale situatie in dit pakket.

Dat onderscheid is geen formaliteit: het bepaalt wie tekent (jij, niet je
klant) en waarom je klant het bewijs mag opvragen (hij moet kunnen zien welke
subverwerkers jij inzet). De verwerkersovereenkomst die je accepteert, is de
overeenkomst tússen jouw organisatie en Gaply — niet die tussen jou en je
klant. Die tweede blijft jouw eigen document.

## Wat er ligt

| Document | Waar het over gaat |
|---|---|
| Algemene voorwaarden | de dienst zelf: wat Gaply levert, onder welke condities |
| Verwerkersovereenkomst (DPA) | de persoonsgegevens: wat Gaply ermee doet, hoe lang, met welke subverwerkers, en welke rol Gaply heeft (verwerker of subverwerker) |
| Security-bijlage | de technische en organisatorische maatregelen die daaronder hangen |

Je vindt ze op de pagina **Juridisch** in het Gaply-dashboard. Daar kun je ze
lezen, downloaden als PDF (via de printdialoog van je browser — in de voettekst
staan de versie, de datum en een contenthash, zodat aantoonbaar is welke tekst
je in handen hebt) en, als er iets openstaat, accepteren.

Via MCP kun je de stand van je eigen organisatie opvragen met
**`get_legal_acceptance_status`** (`organisationId` van je partnerorganisatie).
Die geeft je de huidige gepubliceerde documenten plus of er nog iets openstaat.

> **Eén leesvalkuil, en het is een stille.** `requiresAcceptance: false`
> betekent "**jij** hoeft niets te accepteren" — niet automatisch "de
> organisatie is akkoord". Wie geen beheerder van die organisatie is, krijgt
> namelijk `false` in plaats van een foutmelding, simpelweg omdat alleen een
> organisatiebeheerder kán accepteren. Vraag je de stand op voor een
> organisatie waar jij die rol niet hebt, dan zegt het antwoord dus niets.
> Controleer bij twijfel in het dashboard of vraag het na bij Gaply.

## Wie tekent

Acceptatie gaat op **organisatie**-niveau, niet per project of per omgeving.
Eén keer akkoord dekt al je projecten onder die organisatie. Bij een nieuwe
klant hoef je dus niets opnieuw te doen — bij een **nieuw gepubliceerde
versie** wél: dan komt de gate terug en moet er opnieuw getekend worden.

De acceptatiepagina is zichtbaar voor wie de capability **`legal.accept`**
heeft. Die zit in de Partner-rol. **Lezen** en de PDF downloaden kan iedereen
(`legal.read_documents` zit in zowel de Klanten- als de Partner-rol) — alleen
het akkoord zelf is afgeschermd.

**Ziet de persoon die moet tekenen de gate niet?** Dat is bijna altijd
hetzelfde geval: de tekenbevoegde binnen jouw organisatie is niet dezelfde
persoon als de dagelijkse beheerder, en heeft daarom een smallere rol. De
oplossing is níét die persoon een bredere rol geven, maar Gaply vragen om de
rol **`Tekenbevoegd`** toe te kennen. Dat is een aparte rol die uitsluitend de
juridische rechten draagt en die je *naast* een bestaande rol krijgt — rollen
stapelen, dus de betrokkene houdt precies de toegang die hij al had en krijgt
alleen deze knop erbij. Vraag hem aan bij Gaply (info@gaply.nl) met naam en
e-mailadres van de tekenbevoegde.

## Hoe je tekent

1. **Lees het document eerst echt.** Klinkt overbodig; is het niet. Wat je
   accepteert is de overeenkomst waar jij je eindklanten op gaat aanspreken —
   en die klanten stellen er vragen over.
2. **Ga naar Juridisch in het dashboard** en open het document dat openstaat.
3. **Verklaar dat je bevoegd bent.** Bij de acceptatie bevestig je dat je
   namens je organisatie mag tekenen. Dat is geen vinkje voor de vorm: er wordt
   vastgelegd wie het zette, wanneer, op welke versie en met welke contenthash.
   Zet het akkoord dus niet namens een collega en niet "even snel" vanaf
   iemand anders' account.
4. **Controleer daarna de stand** — de gate hoort weg te zijn en de pagina toont
   het akkoord met datum.

**Een agent zet dit akkoord nooit.** Ook niet als het het laatste is wat een
livegang tegenhoudt: het is een rechtshandeling met een bevoegdheidsverklaring
eronder, en die kan alleen een mens afleggen. Loop je hier tegenaan in een
geautomatiseerde run, dan is de juiste uitkomst een melding aan de
tekenbevoegde — nooit een klik.

## Het acceptatiebewijs

Na acceptatie kun je op dezelfde pagina het **acceptatiebewijs** downloaden. Dat
bevat: het documenttype, de versie, de contenthash van de geaccepteerde tekst,
de naam en het e-mailadres van degene die accepteerde, en het tijdstip. Er staat
bewust **geen IP-adres** in — een bewijsstuk hoort te bewijzen wie tekende, niet
waar iemand zat.

**Dit is wat je aan je eindklant overlegt.** Vraagt hij op grond van artikel 7.3
van jullie verwerkersovereenkomst om aan te tonen dat je subverwerkers onder een
gelijkwaardige overeenkomst werken, dan stuur je twee dingen: de
verwerkersovereenkomst zelf (de PDF, mét versie en hash in de voettekst) en het
acceptatiebewijs dat laat zien dat jouw organisatie die versie heeft aanvaard.
Samen dekken die de vraag. Schrijf er geen eigen verklaring omheen en vat de
inhoud niet samen als toezegging — het document is de toezegging.

## Als er een nieuwe versie komt

Gaply publiceert af en toe een nieuwe versie van een document. Dan:

1. **Verschijnt de gate opnieuw** voor wie `legal.accept` heeft. Dat is geen
   fout en geen dubbele vraag — het akkoord hoort bij een specifieke versie.
2. **Lees wat er veranderd is** vóór je opnieuw accepteert.
3. **Waarschuw je eindklanten waar dat relevant is.** Wijzigt er iets aan de
   subverwerkers, de bewaartermijnen of de beveiligingsmaatregelen, dan is dat
   informatie die zij op grond van hun eigen overeenkomst willen hebben. Jij
   bent hun aanspreekpunt, niet Gaply.
4. **Vervang het bewijsstuk** dat je eerder aan klanten hebt verstrekt door het
   nieuwe, zodat wat er bij hen ligt bij de geldende versie hoort.

Het oude akkoord blijft overigens gewoon bestaan als historisch feit — een
nieuwe versie accepteren wist niet wat je eerder tekende.

## Grenzen

- **Je accepteert nooit namens een eindklant**, en een eindklant accepteert
  nooit jouw partnerovereenkomst. Twee organisaties, twee akkoorden.
- **Onderhandelen over de tekst loopt via Gaply** (info@gaply.nl), niet via
  een aantekening bij de acceptatie. Wat je accepteert is de gepubliceerde
  tekst, ongewijzigd.
- **Krijg je een 403** bij het lezen of accepteren: dat is correct gedrag, geen
  defect. Meld het bij Gaply met de exacte foutmelding — dan wordt de rol
  bijgewerkt. Zoek er geen omweg omheen; dat geldt in dit hele pakket.
- **Publiceren, wijzigen of terugdraaien van documenten is Gaply-werk.** Zie je
  daar tools voor, dan zijn ze niet voor jou bedoeld.
