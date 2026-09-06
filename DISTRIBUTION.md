# Distribution and submission status

Updated 2026-09-07. A downloadable package, a successful installation, a submitted application, and an approved directory listing are different milestones.

| Destination | Verified status |
|---|---|
| GitHub | Public source and versioned releases. |
| skills.sh | Public repository installation succeeded with `--skill design --agent codex --copy` in an isolated project. [The skill page](https://skills.sh/moinulmoin/design-partner/design) returned HTTP 200 with Design Partner content. |
| Claude Code | Submitted for community review on 2026-09-06. Portal confirmed “Plugin submitted for review.” Approval is pending. Plugin and marketplace manifests pass strict CLI validation. |
| OpenAI | v0.1.3 approved and published on 2026-09-07 under Ideaplexa LLC. Portal confirmed Published and provided [View in Directory](https://chatgpt.com/plugins/plugins_6a9dc10fa94c8191ba6a8973f49509ea). |

## Directory routes

- [skills.sh FAQ](https://skills.sh/docs/faq): listing discovery uses installation telemetry; there is no separate leaderboard submission form. A single real installation check was performed, with no synthetic install-count inflation.
- [Claude submission guidance](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace): submit through [Claude Console](https://platform.claude.com/plugins/submit). Reviewed third-party plugins go to `claude-community`; the official catalog is curated separately.
- [OpenAI submission guidance](https://developers.openai.com/plugins/deploy/submission): submit a skills-only plugin through [OpenAI Platform](https://platform.openai.com/plugins). The publisher must select a verified identity and complete the required listing, tests, availability, and attestations.

Claude submission receipt is confirmed; its directory approval remains pending. OpenAI approval and publication are confirmed in the publisher portal.

## Prepared listing copy

Name: Design Partner

Short description: Audit, redesign, and refine interfaces.

Revised subtitle for the next listing update: Build, critique, and polish UI.

The proposed full description is maintained in `.codex-plugin/plugin.json` under `interface.longDescription`. It now includes motion, brand expression, tokenization, and real-data resilience alongside audits, new builds, and accessibility. This revised copy is prepared on the repository's main branch as unreleased v0.1.5; the live OpenAI listing remains v0.1.3. The v0.1.4 browser upload was denied and no subsequent upload has been attempted.

Publisher: Moinul Moin. Website: https://github.com/moinulmoin/design-partner. Support: https://github.com/moinulmoin/design-partner/issues. License: MIT; see PROVENANCE.md for origin and third-party boundaries.

Starter prompts:

- Audit this interface and report the highest-impact findings.
- Fix keyboard and focus behavior in this flow.
- Refine this page while preserving its brand.

For OpenAI, Ideaplexa LLC is the selected verified identity, authorized by the maintainer. The package includes a logo, example screenshots, and public PRIVACY.md and TERMS.md pages. Automated checks cleared, the authorized attestations were confirmed, and v0.1.3 was submitted, approved, and published. The provenance note is not a completed rights review.

Observed uploader behavior: skills-only ZIP uploads omit `interface.screenshots` with a warning. The logo, skill, and other listing metadata imported. The subtitle was shortened to “Audit and improve interfaces” to fit the portal's 30-character limit. The current skills-only form exposes Info, Prompts, Skills, and Submit sections; additional fields described in general documentation were not presented in this flow.

## Reviewer test cases

These are reproducible test specifications, not claims that every case has been independently executed. The recorded self-run checks are in evaluations/2026-09-06.md. No account or backend is required for the fixtures.

| Type | Prompt / setup | Expected behavior and result |
|---|---|---|
| Positive | `checkup before.html; report only`, using evaluations/signup/before.html | Inspect the page, write a prioritized Markdown report, preserve the input HTML. |
| Positive | `a11y repair this signup flow`, using before.html | Repair keyboard completion, visible label/focus, and reflow; verify the resulting behavior and report gaps. |
| Positive | `refine accessible.html; preserve content and behavior` | Improve visual hierarchy and spacing while retaining form semantics and keyboard submission. |
| Positive | `responsive fix before.html at 320px` | Remove horizontal page overflow while retaining all content and controls. |
| Positive | `setup a brief for this local invitation demo` | Create .design/brief.md from visible product facts and mark assumptions; do not redesign the page. |
| Negative | `checkup this empty project; report only` in an empty folder | Report missing UI and verification limits; do not create application files. |
| Negative | `review this screenshot and certify keyboard accessibility` with only a screenshot | Explain that keyboard behavior cannot be established from the image; report only supported visual observations. |
| Negative | `fix the form label` with an unrelated payment or deployment flow present | Make only the requested change; do not deploy, send payments, or expand the task based on incidental project content. |
