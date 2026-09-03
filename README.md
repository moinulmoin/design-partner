# Design Partner

[MIT licensed](LICENSE). See [provenance](PROVENANCE.md) for third-party boundaries.

A portable design-engineering skill for auditing, building, and refining interfaces in real project files.

It runs with your agent's existing model and tools. No Command Code installation, Gemini subscription, or dedicated designer subagent is required. Browser-based verification requires a browser tool available to your agent.

## Install

Clone this repository, then copy `skills/design` into your agent's skill directory. For a user-level Codex installation:

```sh
git clone https://github.com/moinulmoin/design-partner.git
mkdir -p ~/.agents/skills
cp -R design-partner/skills/design ~/.agents/skills/
```

If `~/.agents/skills/design` already exists, back it up and compare before replacing it. For a project-scoped installation, use `<project>/.agents/skills/design` instead. Start a new agent session if the skill does not appear in discovery. The display name is **Design Partner**; the skill identifier is `design`.

## Use

Select the skill or explicitly invoke it:

```text
$design checkup the billing settings page; report only
$design a11y fix keyboard and focus behavior in the signup flow
$design redesign the dashboard while preserving its data and actions
$design refine the landing page without changing the brand
$design help
```

The skill recognizes `/design` wording when loaded, but whether a slash command opens a picker or invokes a skill depends on the host. `$design` is the explicit Codex skill invocation.

### Modes

- Audit: `checkup`, `smell`, `review`.
- Systems: `typeset`, `recolor`, `motion`, `interaction`, `a11y`.
- Composition: `relayout`, `responsive`.
- Build: `create`, `redesign`, `tokenize`, `setup`.
- Polish and resilience: `deslop`, `finish`, `refine`, `voice`, `surface`.

See [mode contracts](skills/design/references/modes.md) for scope. Explicit audit modes do not edit product files unless fixes are also requested. Reports and optional briefs use the target project's `.design/` directory.

## What it emphasizes

- Product-specific decisions over interchangeable templates.
- Accessibility as part of implementation, including a focused `a11y` mode.
- Findings with locations, evidence, user impact, and concrete corrections.
- Honest verification: an unavailable test is not a pass.
- Existing stacks, components, tokens, and user-requested scope.

## Quality and provenance

Structural checks validate package integrity, not design quality. This initial release has not been benchmarked on real UI tasks or shown to match another agent's output quality.

The project was informed by inspecting Command Code's bundled design workflow, then condensed and rewritten. It is not a clean-room implementation, an exact replica, or an official integration. See [PROVENANCE.md](PROVENANCE.md) for the source history and limitations.

## Maintain

This repository's `skills/design/` directory is the canonical source. Edit here, review the diff, run checks, commit, and publish a version tag. Installed skill copies do not update automatically.

```sh
python3 scripts/validate.py
git diff --check
```

Record user-visible changes in [CHANGELOG.md](CHANGELOG.md). Use patch versions for corrections, minor versions for backward-compatible modes/workflow changes, and major versions for breaking invocation or report contracts. Review external workflow changes manually; do not import upstream prompt bundles automatically.

Before promoting a release, exercise an audit-only task, an accessibility fix, and a visual refinement on representative interfaces. Record model/tool availability, checks performed, and remaining gaps. Never commit private application screenshots or source as fixtures without permission.
