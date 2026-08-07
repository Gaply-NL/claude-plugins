---
name: partner-offerte
description: >-
  Genereert een beknopte, professionele Gaply-offerte-PDF (max 3 A4) in de
  huisstijl van de partner, op de vaste Gaply-prijslijst: sitemap-analyse,
  scope-varianten A/B/C en investeringstabel. Gebruik deze skill ALTIJD bij een
  offerte, prijsvoorstel, voorstel of "plan voor [klant]" voor een
  Gaply-implementatie — ook als het woord "offerte" niet valt, bijvoorbeeld
  "maak een voorstel voor [domein] op basis van deze gesprekken" of "maak er
  iets stuurbaars van".
---

# Partner-offerte (Gaply)

Maakt van gespreksnotities en een klantdomein een offerte-PDF die een nieuwe
lezer zonder context begrijpt. De vaste structuur zit in
`scripts/generate_offerte.py`; lever onderzoek en inhoud aan via een
config-JSON. Een compleet ingevuld voorbeeld staat in
`references/voorbeeld-config.json` — lees dat eerst als referentie voor toon,
lengte en detailniveau.

## Twee harde regels

1. **Prijzen komen UITSLUITEND uit `config/prijslijst.md`** (in de map config
   van deze plugin). Dit is de vaste Gaply-prijslijst; wijk niet af en geef
   geen korting zonder schriftelijk akkoord van Gaply. Laat de gebruiker de
   definitieve bedragen altijd bevestigen voordat je genereert.
2. **Branding komt uit `config/branding.md`.** De offerte gaat uit onder de
   naam van de partner; vul het `branding`-blok van de config-JSON met de
   kleuren en het logo uit dat bestand. Staat daar "INVULLEN", vraag de
   gebruiker eerst om de ontbrekende waarden.

## Werkwijze

### 1. Verzamel input

Nodig: klantdomein, gespreksnotities of transcripten, contactgegevens. Lees de
notities volledig: daar staan de echte wensen, zorgen (verouderde content,
weinig eigen tijd, meerdere doelgroepen), toezeggingen en vaak een genoemde
prijsrange. De offerte moet aantoonbaar op het gesprek aansluiten. Vraag wat
niet uit het gesprek blijkt — meestal: welke variant aanbevolen wordt en aan
wie de offerte gericht is. Sprekerlabels in transcripten zijn vaak
onbetrouwbaar; neem geen persoonsnamen over zonder bevestiging.

### 2. Analyseer de sitemap

Haal `https://[domein]/sitemap.xml` op en categoriseer alle URL's op het
eerste padsegment, met aantallen. Probeer bij een sitemap-index ook de
sub-sitemaps (WordPress: `sitemap_index.xml`, `page-sitemap.xml`,
`post-sitemap.xml`). Beoordeel per categorie de fit met Gaply:
kennis-/servicecontent met langetermijnwaarde is hoog; tijdelijke of dubbel
gepubliceerde content is laag. Nieuws krijgt standaard een 12-maandenfilter
(ouder nieuws bevat verouderde informatie en schaadt de betrouwbaarheid van
antwoorden).

### 3. Bepaal varianten en prijzen

Drie varianten, oplopend in scope. A = kern (aanbevolen: laagdrempelig starten
met de content waar de gebruikersvraag ligt), B = kern plus één logische
uitbreiding, C = volledig. Prijs elke variant volgens de staffels in
`config/prijslijst.md` op basis van het aantal URL's in scope. Prijzen moeten
identiek zijn in sectie 6 (tabel) en sectie 7 (akkoord-bullets); het script
leidt sectie 7 automatisch af, dus vul ze op één plek in.

### 4. Schrijf de config en genereer

Kopieer `references/voorbeeld-config.json` als startpunt en vervang alle
inhoud. Schrijfregels:

- Nederlands, zakelijk maar toegankelijk; geen jargon zonder uitleg (leg
  "gap-analyse" en "structured data" uit in gewone woorden).
- Geen gedachtestrepen (—) in lopende tekst; gebruik een punt of komma.
- Gebruik `&amp;` voor &-tekens; `<b>`-tags zijn toegestaan in tekstvelden.
- Noem bewezen resultaten: Juridisch Loket, Milieu Centraal, NPO (32.000
  zoekinteracties in 90 dagen; ±70% minder telefonische contactaanvragen).
- Sectie 2 ("Wat lost dit op") spiegelt de zorgen uit het gesprek in 3-5
  bullets, elk beginnend met een vetgedrukte kernbelofte.
- Sectie 5 (aanpak) in 4-6 korte subsecties; benoem daarin dat de technische
  inrichting (bronnen, zoek- en AI-instellingen) door Gaply wordt gedaan en
  dat de partner de implementatie begeleidt.
- Het veld `meta.van` is de partner (uit `config/branding.md`), met de
  toevoeging "in samenwerking met Gaply".

Genereer daarna:

```bash
pip install reportlab --break-system-packages  # indien nodig
python3 scripts/generate_offerte.py config.json offerte_[partner]_[klant].pdf
```

Optioneel klantlogo: zet een PNG (liefst transparant) naast de config en vul
`meta.klant_logo`, `klant_logo_breedte_mm` en `klant_logo_ratio`
(hoogte/breedte) in; het komt rechtsboven op elke pagina naast het
partnerlogo.

### 5. Controleer vóór oplevering

Render pagina's als PNG (`pdftoppm -png -r 60`) en bekijk ze: maximaal 3
pagina's, geen verweesde koppen onderaan een pagina, tabellen netjes, beide
logo's zichtbaar. Check dat de URL-aantallen optellen tot het sitemaptotaal en
dat de prijzen exact uit de prijslijst-staffels komen. Lever de PDF op aan de
gebruiker.

## Na akkoord

Wijs de gebruiker op de volgende stap: de intake met de klant via de skill
`partner-intake`, zodat Gaply de omgeving kan inrichten.
