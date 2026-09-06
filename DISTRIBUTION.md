# Distribution and submission status

Updated 2026-09-06. A downloadable package, a successful installation, a submitted application, and an approved directory listing are different milestones.

| Destination | Verified status |
|---|---|
| GitHub | Public source and versioned releases. |
| skills.sh | Public repository installation succeeded with `--skill design --agent codex --copy` in an isolated project. [The skill page](https://skills.sh/moinulmoin/design-partner/design) returned HTTP 200 with Design Partner content. |
| Claude Code | Submitted for community review on 2026-09-06. Portal confirmed “Plugin submitted for review.” Approval is pending. Plugin and marketplace manifests pass strict CLI validation. |
| OpenAI | Signed in; Ideaplexa LLC publisher identity authorized. Package upload is blocked by browser-extension file access. Submission has not been completed. |

## Directory routes

- [skills.sh FAQ](https://skills.sh/docs/faq): listing discovery uses installation telemetry; there is no separate leaderboard submission form. A single real installation check was performed, with no synthetic install-count inflation.
- [Claude submission guidance](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace): submit through [Claude Console](https://platform.claude.com/plugins/submit). Reviewed third-party plugins go to `claude-community`; the official catalog is curated separately.
- [OpenAI submission guidance](https://developers.openai.com/plugins/deploy/submission): submit a skills-only plugin through [OpenAI Platform](https://platform.openai.com/plugins). The publisher must select a verified identity and complete the required listing, tests, availability, and attestations.

Claude submission receipt is confirmed; directory approval remains pending. OpenAI submission is incomplete. Do not advertise catalog acceptance until its status is confirmed.

## Prepared listing copy

Name: Design Partner

Short description: Audit, redesign, and refine interfaces.

Long description: Design Partner supplies 19 focused workflows for interface design in existing project files. It covers report-only audits, accessibility repairs, typography, responsive layout, visual refinement, and new screens. Findings include evidence and concrete corrections; verification reports distinguish checked behavior from remaining gaps. It uses the host agent's model and tools and requires no MCP service or separate account.

Publisher: Moinul Moin. Website: https://github.com/moinulmoin/design-partner. Support: https://github.com/moinulmoin/design-partner/issues. License: MIT; see PROVENANCE.md for origin and third-party boundaries.

Starter prompts:

- Audit this interface and report the highest-impact findings.
- Fix keyboard and focus behavior in this flow.
- Refine this page while preserving its brand.

For OpenAI, verified identity, final logo, privacy and terms URLs, supported regions, and policy attestations still need completion. Do not invent publisher facts or represent the existing provenance note as a completed rights review.

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
