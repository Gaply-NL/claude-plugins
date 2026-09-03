# Gaply Claude-plugins

Dit is de officiële bron voor alle Claude-plugins van Gaply. Gaply beheert deze
repository; partners (zoals Webbio, Leadrs en Sterk) installeren en updaten hun
plugin vanaf hier. Zo houdt Gaply controle op afstand: één wijziging hier, en
elke partner draait bij de volgende update hetzelfde, actuele werkproces.

## Plugins in deze repository

| Plugin | Versie | Voor wie |
|---|---|---|
| [gaply-partner](plugins/gaply-partner) | 1.0.0 | Implementatiepartners: offertes, intake, focusgebieden, contentvoorstellen, rapportage, livegang, beheer, juridische documenten |

Nieuwe extensies (bijvoorbeeld een sales- of implementatiepakket) komen als
extra map onder `plugins/` en als extra regel in
`.claude-plugin/marketplace.json`. Alles blijft zo bij elkaar in één
Gaply-organisatie.

## Installatie bij een partner

1. De partner voegt de marketplace toe in Claude:
   `/plugin marketplace add gaply-nl/claude-plugins`
   (bij een private repository moet het GitHub-account van de partner eerst
   read-toegang hebben op deze repo)
2. Daarna: `/plugin install gaply-partner@gaply`
3. Gaply richt per partner de configuratie in: MCP-URL in `.mcp.json`,
   partnerbranding in `config/branding.md` (zie de README van de plugin).

Updaten: `/plugin marketplace update gaply` gevolgd door een herinstallatie of
update van de plugin. Partners die afwijken van de plugin of skills doen dat op
eigen risico.

## Versiebeheer en releases

- Versies volgen **semver** (MAJOR.MINOR.PATCH), bijgehouden in
  `plugins/<naam>/.claude-plugin/plugin.json` én in het `CHANGELOG.md` van de
  plugin.
  - **MAJOR** — partners moeten hun werkwijze aanpassen
  - **MINOR** — nieuwe of gewijzigde skills, prijslijst- of beleidswijzigingen
  - **PATCH** — tekstuele of cosmetische fixes
- Elke release krijgt een git-tag: `gaply-partner-v0.2.0`.
- De `main`-branch is altijd de uitleverbare stand; wijzigingen gaan via een
  branch + pull request, zodat er een reviewmoment is voordat partners iets
  ontvangen.

### Release-flow (voor Gaply)

1. Maak een branch, pas de plugin aan (skills, prijslijst, branding-template).
2. Bump de versie in `plugin.json`, werk `CHANGELOG.md` bij, en werk de
   versie in `.claude-plugin/marketplace.json` bij.
3. Open een pull request, laat meelezen, merge naar `main`.
4. Tag de release: `git tag gaply-partner-vX.Y.Z && git push --tags`.
5. Meld de update aan partners (Slack-koppeling) met de changelog-regels.

## Rolverdeling

- **Gaply** beheert deze repo, de prijslijst en de skill-inhoud.
- **Partners** krijgen read-toegang en nemen de plugin af; aanpassen doen ze
  niet in deze repo. Feedback of wensen gaan naar info@gaply.nl en worden hier
  door Gaply doorgevoerd, zodat elke partner dezelfde verbetering krijgt.
