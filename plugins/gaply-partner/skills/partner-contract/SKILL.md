---
name: partner-contract
description: >-
  Regelt na een akkoord op de offerte de contractstap met Gaply: per project
  een aanvraagformulier plus de verplichte verwerkersovereenkomst, en éénmalig
  per partner de geheimhoudingsovereenkomst. Verzamelt de gegevens die Gaply
  nodig heeft om de documenten in PandaDoc klaar te zetten, dient de aanvraag
  in en bewaakt de tekenronde. Gebruik bij "contract voor [klant]",
  "aanvraagformulier", "verwerkersovereenkomst", "[klant] is akkoord, wat
  nu", "tekenronde" of direct na een akkoord op een offerte — vóór de intake.
---

# Partner-contract (aanvraagformulier + verwerkersovereenkomst)

Tussen het akkoord op de offerte en de intake zit één verplichte stap: de
overeenkomst voor het project. Zonder getekend aanvraagformulier én getekende
verwerkersovereenkomst start Gaply geen inrichting en verleent Gaply geen
toegang tot een omgeving. Deze skill zorgt dat die stap snel en compleet
verloopt.

## Wat er getekend wordt

Gaply werkt met drie sjablonen in PandaDoc. Ze zijn hetzelfde voor een
partner en voor een eindklant die rechtstreeks afneemt; het aanvraagformulier
en de verwerkersovereenkomst kennen daarvoor een keuze "directe afname" of
"afname via een partner".

| Document | Hoe vaak | Wie tekent |
|---|---|---|
| **Aanvraagformulier** (order form) — scope, maandlicentie, setup, voorwaarden | **per project** (identifier `GAPLY-[jaar]-[KLANTCODE]-01`) | Gaply en de Afnemer (de partner; bij directe afname de eindklant) |
| **Verwerkersovereenkomst** (DPA) — verplicht, onlosmakelijk onderdeel van het aanvraagformulier | **per project**, samen met het aanvraagformulier | Gaply en de Afnemer |
| **Geheimhoudingsovereenkomst** (NDA) — dekt de hele samenwerking | **éénmalig per partner** (of per direct afnemende eindklant) | Gaply en de Afnemer |

De verwerkersovereenkomst is geen optie en geen bijlage-op-verzoek: het
aanvraagformulier verklaart haar tot onlosmakelijk onderdeel van de
overeenkomst, en het abonnement gaat pas in als beide zijn getekend. Bij
afname via een partner is de partner Verwerker van de eindklant en Gaply
Subverwerker van de partner (artikel 3 van de DPA); de partner moet dan
zelf een verwerkersovereenkomst met de eindklant hebben die het inschakelen
van Gaply toestaat. Kent die overeenkomst strengere termijnen (bijvoorbeeld
een kortere meldtermijn bij een datalek), meld die dan bij de aanvraag — ze
gelden dan ook voor Gaply.

De partner tekent; de eindklant is bij afname via een partner geen partij.
De partner factureert de eindklant, Gaply factureert de partner.

## Werkwijze

### 1. Verzamel de gegevens voor de aanvraag

Haal uit de offerte en het akkoord:

- eindklant: naam, website/domein, klantcode-voorstel (kort, hoofdletters);
- offertereferentie (kenmerk, titel, datum) en de **datum van het akkoord**;
- gekozen scope-variant met korte omschrijving, URL-omvang (bijv. "±600"),
  focusgebieden voor zover al bekend (anders "n.t.b. bij intake");
- maandlicentie en setupbedrag exact zoals in de offerte (uit de vaste
  prijslijst; nooit zelf afronden of "corrigeren");
- gewenste startdatum (default: eerste van de komende maand, "of eerder bij
  toegang");
- de tekenbevoegde van de partner (naam, functie, e-mail) en KvK-nummer en
  vestigingsadres van de partner, tenzij Gaply die al heeft;
- voor de verwerkersovereenkomst: wie bij de eindklant de
  Eindverantwoordelijke is (organisatienaam) en eventuele strengere
  termijnen uit jullie eigen verwerkersovereenkomst met die klant.

Ontbreekt iets, vraag het de gebruiker gericht in één ronde. Verzin niets.

### 2. Dien de aanvraag in bij Gaply

Mail de gegevens uit stap 1 naar info@gaply.nl met als onderwerp
"Aanvraag contract [eindklant] — [partner]". Gaply zet daarop in PandaDoc
het aanvraagformulier en de verwerkersovereenkomst klaar (en, als die er
voor de partner nog niet is, de geheimhoudingsovereenkomst) en stuurt ze
ter ondertekening naar de tekenbevoegde. Er is geen automatische
aanmelding: zonder deze mail gebeurt er niets.

### 3. Tekenronde

De tekenbevoegde ontvangt de documenten uit PandaDoc. Zorg dat beide
projectdocumenten (aanvraagformulier én verwerkersovereenkomst) getekend
worden; een half getekende set telt niet. Vragen over de inhoud gaan naar
info@gaply.nl; onderhandel niet zelf over voorwaarden namens Gaply.

### 4. Daarna: de intake

Zodra Gaply de getekende set heeft bevestigd, begint de intake via
`partner-intake`. De datum van het offerte-akkoord uit stap 1 heb je daar
meteen nodig (`herkomst.offerte_datum_akkoord`).

## Grenzen

- Geen toezeggingen over prijzen, voorwaarden of termijnen buiten het
  sjabloon om; afwijkingen alleen via Gaply.
- Geen intake, projectaanmaak of activatiewerk voordat de set getekend is.
- De documenten zelf worden door Gaply aangemaakt en verstuurd; de partner
  heeft geen toegang tot PandaDoc en bouwt geen eigen versie.
