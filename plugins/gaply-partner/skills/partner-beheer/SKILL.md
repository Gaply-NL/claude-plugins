---
name: partner-beheer
description: >-
  Beheer en onderhoud van een live Gaply-klantomgeving: de golden set van de
  klant lezen, reviewen en wijzigingsvoorstellen indienen bij Gaply, de
  beheerinstructie voor de eindklant opstellen en onderhouden, en de
  terugkerende verbetercadans draaien. Gebruik na het eind-seintje van Gaply
  en bij "beheer voor [klant]", "golden set nalopen", "antwoorden kloppen
  niet", "beheerinstructie", "onderhoudsronde" of "verbetercadans".
---

# Partner-beheer (na livegang)

Zodra Gaply het eind-seintje heeft gegeven — de omgeving staat live op
productie — is de inrichting klaar en begint het werk dat nooit afloopt: de
zoekfunctie blijft alleen goed als iemand blijft kijken of de antwoorden nog
kloppen met wat de klant wíl uitstralen. Dat is partnerwerk, want het vraagt
klantkennis, geen platformkennis.

Deze skill dekt drie dingen: de golden set van de klant, de beheerinstructie
voor de eindklant, en de cadans waarin je beide blijft nalopen.

## Wat je bij het eind-seintje overneemt

Bij het eind-seintje krijg je van Gaply de stand van zaken van de nieuwe
omgeving: de productie-omgeving, de golden set die tijdens de inrichting is
gebouwd, en de nulmeting die daarop is gedraaid. Vanaf dat moment:

1. **Implementeer Gaply op de front-end** van de klant (widget of API) en
   maak de klantaccounts aan.
2. **Koppel Search Console** en maak daarna de focusgebieden aan (skill
   `partner-focusgebieden`) — tijdens of na de partnertraining. GSC eerst,
   dan de focusgebieden.
3. **Schrijf de beheerinstructie** voor de eindklant (zie hieronder).
4. **Loop de golden set na** — de eerste review hoort bij de overdracht, niet
   pas bij de eerste cadansronde.
5. **Controleer of het juridische akkoord van je organisatie staat** — dat is
   een eenmalige stap per organisatie, geen stap per klant, maar bij je eerste
   klant valt hij hier. Skill `partner-juridisch`.
6. Plan de eerste maandrapportage in (skill `partner-rapportage`), één volle
   kalendermaand na livegang.

### Voorwaarde: de Partnerrol heeft nieuwe permissies nodig

Het lezen van de golden set en het indienen van voorstellen loopt via twee
nieuwe capabilities: **`golden_set.read`** en **`golden_set.suggest`**. Die
worden op dit moment door Gaply gebouwd en zijn bij het uitkomen van deze
versie **nog niet uitgerold**. Twee dingen volgen daaruit:

- **Tot ze live zijn** krijg je de golden set bij het eind-seintje als export
  van Gaply, en dien je je voorstellen in per mail (info@gaply.nl). Ga niet
  zoeken naar een MCP-tool die de set ophaalt; die heb je nu niet.
- **Zodra ze live zijn** moet Gaply ze ook daadwerkelijk aan de Partnerrol
  toekennen. Gebeurt dat niet, dan krijg je een **403** op het moment dat je
  de set probeert te lezen of een voorstel probeert in te dienen. Dat is dan
  geen defect en geen omweg-probleem: meld het bij Gaply met de exacte
  foutmelding, dan wordt de rol bijgewerkt. Gaply meldt bij de uitrol welke
  tools erbij horen — verzin er zelf geen.

## De golden set: jij keurt, Gaply voert door

De golden set is de meetlat van de klantomgeving: een vaste verzameling
vragen met per vraag het verwachte antwoord, de pagina waarmee die vraag
beantwoord hoort te worden, en het gedrag dat Gaply moet vertonen als het
antwoord er niet is. Gaply meet er de kwaliteit mee; als de set niet klopt,
meet Gaply het verkeerde.

**Bewerken kan alleen Gaply.** De capability `golden_set.manage` is en blijft
super-admin-only: de set is de antwoordsleutel, en wie hem kan wijzigen kan
de meetlat naar de uitkomst toe schrijven. Jouw rol is dus: lezen, keuren,
aanvullen en aanleveren. Gaply voert de wijzigingen door en draait de meting
opnieuw.

### Wat je per entry controleert

1. **Klopt de vraag?** Is dit een vraag zoals bezoekers hem werkelijk
   stellen — in hun woorden, niet in die van de organisatie? Vragen die
   niemand zo stelt, vervuilen de meting.
2. **Is dít de pagina waarmee de klant beantwoord wíl worden?** Technisch kan
   een andere pagina het antwoord ook bevatten; de vraag is welke pagina de
   klant vóór wil zetten. Dit is de vraag waar jouw klantkennis het verschil
   maakt en waar Gaply niet aan toe komt.
3. **Kloppen antwoord, terugvalgedrag en serviceverwachting met de
   klantintentie?** Klopt de strekking van het verwachte antwoord? Is het
   juist dat Gaply hier doorverwijst in plaats van antwoordt (of andersom)?
   Wil de klant bij deze vraag naar een formulier, de telefoon of de balie?
4. **Wat ontbreekt?** Vul aan vanuit wat je van de klant weet: vragen die aan
   de balie of telefoon binnenkomen, seizoens- en campagnevragen, nieuwe
   diensten, veelgemaakte misverstanden.

### Zo lever je aan

Lever een lijst, niet een verhaal. Per entry één van vier: **houden**,
**wijzigen** (met de nieuwe waarde én de reden), **schrappen** (met reden) of
**toevoegen** (vraag, gewenste pagina, verwacht antwoord). Zet erbij wat de
klant zelf heeft goedgekeurd en wat jouw eigen inschatting is — Gaply
behandelt die twee verschillend.

Doe dit samen met de klant, niet erover. Een set die jij alleen invult, meet
opnieuw een aanname.

## Beheerinstructie voor de eindklant

**De beheerinstructie voor de eindklant is partnerwerk.** Gaply levert die
niet; jij bent de partij die de klant kent en zijn dagelijkse werk begrijpt.
Schrijf hem kort — één of twee pagina's — en houd hem bij als er iets
verandert.

Wat er minimaal in hoort:

- wat Gaply op hun site doet, in klanttaal, en waar het zichtbaar is;
- wie welke rol heeft: wat de klant zelf kan (inloggen, meekijken met wat
  bezoekers vragen, content aanpassen op de eigen site), wat via jou loopt
  (focusgebieden, contentvoorstellen, rapportage) en wat via Gaply loopt
  (bronnen, zoek- en AI-instellingen, de meetlat);
- hoe ze iets melden dat niet klopt — en bij wie: bij jou, niet bij Gaply;
- wat er verandert als hun site verandert (nieuwe pagina's komen mee met de
  crawl, een nieuwe domeinnaam of een verhuizing niet automatisch — dat
  melden ze);
- hoe het juridisch geregeld is: dat jij hun verwerker bent en Gaply
  subverwerker, en dat je op verzoek de verwerkersovereenkomst en het
  acceptatiebewijs kunt overleggen (skill `partner-juridisch`) — noem het uit
  jezelf, want een privacy-officer vraagt er anders later alsnog naar.

Neem de instructie door tijdens de onboarding van de klantaccounts; een
document dat alleen wordt gemaild, wordt niet gelezen.

## Verbetercadans

Beheer is terugkerend naloopwerk, geen incident. Houd één vaste ronde aan
naast de maandrapportage — maandelijks bij veel verkeer, anders per kwartaal:

| Onderdeel | Wat je doet |
|---|---|
| **Golden-set-review** | Loop de set na volgens de vier vragen hierboven, met de klant erbij. Neem in elk geval mee wat er sinds de vorige ronde is veranderd op de site en in het aanbod. |
| **Judge-ijkronde (menselijk deel)** | Gaply ijkt de automatische beoordelaar routinematig met een AI-ronde. Het menselijke deel is naloopwerk: beoordeel een steekproef antwoorden zelf en meld waar jouw oordeel van dat van Gaply afwijkt. Systematische afwijking is een signaal, niet een detail. |
| **Wat de bezoekers deden** | `get_interaction_frequency` en `list_interaction_logs`: welke nieuwe vragen zijn opgekomen, welke leverden niets op. Die horen vaak in de golden set of in een focusgebied. |
| **Focusgebieden en gaten** | `list_lenses` en `get_lens_new_gaps`: zijn de focusgebieden nog de goede, zijn er nieuwe gaten? Grote gaten gaan door naar `partner-contentvoorstellen`. |
| **Beheerinstructie** | Klopt hij nog? Is de contactpersoon nog dezelfde? |

Leg per ronde kort vast wat je hebt bekeken en wat je hebt ingediend, en wie
meekeek. Zonder die notitie weet de volgende ronde niet wat al beoordeeld is.

## Grenzen

- **Je bewerkt de golden set nooit zelf** — ook niet als je toegang lijkt te
  hebben. Voorstellen indienen is het pad; Gaply voert door.
- Bronnen, zoek- en AI-instellingen en de meetlat zelf blijven Gaply-werk.
  Zie je iets geks (een bron valt stil, antwoorden veranderen zonder reden),
  meld het bij Gaply in plaats van te sleutelen.
- Een 403 in dit pakket is nooit iets om omheen te werken; het is een
  melding waard.
- Verstuur niets rechtstreeks naar de eindklant namens Gaply — jij bent de
  afzender richting de klant.
