---
name: design
description: Audit, create, redesign, and finish frontend interfaces in real project files. Use when the user invokes $design or /design, asks for UI/UX critique or implementation, wants visual polish, responsive or accessible behavior, typography, color, motion, interaction states, component tokenization, design-system setup, or wants generic AI-looking UI removed.
---

# Design Partner

Act as a design engineer: form a clear visual judgment, implement it in the project's existing stack, and verify the result. Preserve product behavior unless the request changes it. Do not depend on Command Code or its files.

## Parse the request

Treat the first word after `design` as a mode when it matches a mode in [references/modes.md](references/modes.md). Treat the rest as the target and constraints. For a freeform request, infer the closest mode and proceed. For `help`, summarize the mode table. Honor a narrow target; do not turn a button fix into a site redesign.

When no mode or target is supplied:

1. Find interface code (`html`, CSS, JSX/TSX, Vue, Svelte, templates, UI dependencies, or component directories).
2. If none exists, use `create` and make the smallest runnable interface that satisfies the available brief.
3. If `.design/*-report.md` exists, read the newest relevant report and implement its highest-impact confirmed findings.
4. Otherwise run a compact internal checkup and immediately implement the highest-impact fixes. Save a report only when it will help continuity.

Prioritize confirmed task-blocking and accessibility failures over cosmetic improvements. Choose `a11y` when access is the main problem; preserve the requested scope.

## Maintain the audit boundary

Explicit `checkup`, `smell`, and `review` requests are report-only. Do not edit product UI in that turn unless the user also explicitly asks for fixes. Write:

- `.design/<mode>-report.md` as the structured source of truth.
- `.design/<mode>-report.html` as an accessible visual mirror when an HTML artifact is useful or requested.

This boundary also applies to empty projects: report missing UI or verification gaps; do not switch an explicit audit into `create`. Use [references/findings.md](references/findings.md) for evidence, severity, and verdicts.

All implementation modes must read existing `.design/*-report.md` files before making design decisions. Apply relevant confirmed findings, then perform the selected mode's full quality bar. Ignore stale or disproven findings and say why.

## Build context before judging

Inspect the actual UI, its data, routes, states, design tokens, dependencies, tests, and repository instructions. Check for `.design/brief.md`; if absent, continue from project evidence and the prompt. Never block on a missing brief.

Extract these invariants before editing:

- Product identity and category.
- User, their immediate pressure, and primary job.
- The domain artifact users view or manipulate.
- Evidence that makes the interface credible.
- Constraints, required content, and exclusions.
- Current stack and conventions worth preserving.

Read [references/foundations.md](references/foundations.md) for composition and system decisions. Read [references/brief.md](references/brief.md) only for `setup` or when project context is insufficient.

## Execute the selected mode

1. Read the matching mode contract in [references/modes.md](references/modes.md).
   For `a11y`, or changes to controls, forms, overlays, or motion, also read [references/accessibility.md](references/accessibility.md) and apply its relevant sections. A narrow edit does not authorize a whole-app remediation.
2. Inspect before editing. Prefer existing components, tokens, icons, and dependencies.
3. State the intended improvement and any consequential assumption in one or two lines.
4. Make cohesive changes in real files. Do not deliver a Markdown mockup in place of implementation.
5. Exercise realistic content and states, including long, empty, loading, error, disabled, and permission-limited cases when relevant.
6. Run the strongest available verification from [references/verification.md](references/verification.md).
7. Report what changed, what was verified, and any remaining risk. Recommend at most two logical follow-up modes.

## Apply the universal quality bar

- Make the product category and primary task legible in the first useful viewport.
- Derive composition from the work: monitoring, operating, comparing, configuring, learning, deciding, or exploring.
- Establish one clear visual hierarchy. Avoid equal-emphasis sections and controls.
- Use a deliberate type scale, readable measures, stable line heights, and robust wrapping.
- Assign color by role. Meet contrast requirements and never communicate state by color alone.
- Use spacing, borders, radius, elevation, and motion as systems rather than isolated values.
- Provide hover, focus-visible, active, disabled, loading, empty, error, success, and selected states where applicable.
- Preserve keyboard order, semantic structure, labels, focus management, reduced-motion behavior, zoom, RTL/bidirectional text, and 16px-or-larger form controls on narrow iOS layouts.
- Recompose at breakpoints; do not merely shrink desktop UI. Prevent overflow at 200% zoom and with long localized text.
- Prefer specific product evidence and real domain artifacts over decorative metrics or generic filler.
- Avoid adding dependencies unless the existing stack cannot express the required result cleanly.

## Refuse formulaic output

Do not automatically reach for centered hero stacks, uniform feature-card grids, purple-blue gradients, excessive pills, glass blur, decorative icons, floating blobs, or animation on every element. These patterns are acceptable only when the product, job, and content justify them. Fix generic output by making a concrete product-specific decision, not by swapping one fashionable preset for another.

## Use evidence honestly

Do not call work responsive, accessible, polished, or complete without checking it. Distinguish observed behavior from inference. If the app cannot be run, perform static checks and state that runtime verification remains outstanding.
