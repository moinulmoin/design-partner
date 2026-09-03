# Mode contracts

Load only the requested mode plus any linked foundation or verification sections.

| Mode | Group | Contract |
|---|---|---|
| `checkup` | Audit | Fast health scan with evidence, severity, and prescriptions. Report only. |
| `smell` | Audit | Identify formulaic, generic, or internally inconsistent visual decisions. Report only. |
| `review` | Audit | Thorough critique with scores, walkthrough, strengths, risks, and prioritized recommendations. Report only. |
| `deslop` | Fix | Remove confirmed generic patterns and replace them with product-specific decisions. |
| `typeset` | System | Repair font loading, scale, weight, rhythm, measure, wrapping, and hierarchy. |
| `recolor` | System | Define semantic roles, palette, contrast, themes, and state color. |
| `motion` | System | Establish purposeful timing, easing, choreography, interruption, and reduced-motion behavior. |
| `interaction` | System | Complete control states, feedback, keyboard paths, focus, forms, overlays, and recovery. |
| `a11y` | System | Repair accessibility across the requested task flow: semantics, keyboard, focus, names, forms, announcements, motion, and reflow. |
| `relayout` | Compose | Change information architecture and spatial composition, not just margins. |
| `responsive` | Compose | Recompose content and controls across width, zoom, input mode, orientation, and text direction. |
| `create` | Build | Build a new surface from the brief in the existing stack; create a minimal stack only if the project is empty. |
| `redesign` | Build | Change the visual direction of an existing interface while preserving required behavior and content. |
| `tokenize` | Build | Extract repeated decisions into semantic tokens and reusable components without erasing meaningful variation. |
| `setup` | Build | Create or update `.design/brief.md`; do not redesign unless explicitly requested. |
| `finish` | Ship | Pre-ship pass over states, copy, metadata, responsive behavior, accessibility, assets, and visible defects. |
| `refine` | Ship | Strengthen character through subtraction, hierarchy, rhythm, and precision without a full redesign. |
| `voice` | Ship | Sharpen brand expression, art direction, copy tone, imagery, and memorable product-specific cues. |
| `surface` | Ship | Harden application UI for real data, density, roles, permissions, latency, failure, and operator workflows. |

## Audit modes

Use [audit.md](audit.md). Base every finding on rendered behavior or code evidence. Separate defects from taste preferences. Preserve what already works.

- `checkup`: score intentionality, readability, usability, responsiveness, accessibility, performance feel, and product credibility. Keep it concise.
- `smell`: detect default-template composition, interchangeable copy, weak proof, arbitrary tokens, overused effects, repetitive cards, unnecessary ornament, and motion without meaning.
- `review`: include first impression, task walkthrough, system consistency, content and hierarchy, responsive/accessibility risks, and a prioritized improvement plan.

## Implementation modes

- `deslop`: consume existing audit reports first. Fix identity and composition before cosmetics. Remove unjustified effects; keep useful conventional patterns.
- `typeset`: define roles before sizes. Verify fallback fonts, loading, line breaks, numeric alignment, dense labels, and user-scaled text.
- `recolor`: begin with semantic tokens (`canvas`, `surface`, `text`, `muted`, `action`, `danger`, etc.). Test states, charts, themes, and common color-vision deficiencies.
- `motion`: map motion to state change, spatial continuity, feedback, or attention. Make interactions interruptible and provide an equivalent reduced-motion path.
- `interaction`: enumerate each control's state machine. Ensure clear affordance, immediate feedback, safe destructive actions, focus restoration, and recoverable errors.
- `a11y`: read [accessibility.md](accessibility.md). Trace a complete user task, repair confirmed barriers, and verify changed behavior. Read existing reports first; do not substitute a few ARIA attributes for a flow-level pass. Save a new report only when requested or needed for continuity.
- `relayout`: choose the dominant work pattern and rebuild the information hierarchy. Validate scanning order before styling.
- `responsive`: decide what wraps, stacks, scrolls, collapses, becomes a drawer, changes density, or remains fixed. Test long content and on-screen keyboards.
- `create`: build the smallest complete vertical slice around the primary job and real artifact. Include credible content and the essential states.
- `redesign`: name a coherent direction and define what remains invariant. Change composition, type, color, and component language together; avoid a cosmetic reskin.
- `tokenize`: inventory repetition, introduce semantic—not purely numeric—tokens, extract components with clear variants, and test for visual regression.
- `finish`: fix visible incompleteness and edge states. Remove dead styles, broken assets, placeholder copy, layout shift, and unsupported completion claims.
- `refine`: subtract noise first, then improve alignment, rhythm, density, hierarchy, and small interaction details.
- `voice`: connect visual and verbal choices to product character. Replace category clichés with a repeatable, credible lane.
- `surface`: verify dense and sparse data, sorting/filtering, bulk actions, permissions, time zones, destructive flows, stale data, and latency.

## Suggested continuations

Offer no more than two:

- After `checkup` or `review`: `finish`, `relayout`, or `redesign`, based on severity.
- When confirmed access barriers dominate: `a11y` before visual polish.
- After `smell`: `deslop` and then `finish`.
- After `redesign`: `checkup` or `responsive`.
- After `typeset` or `recolor`: `responsive` and then `finish`.
- After `motion`: `interaction` or `responsive`.
- After `surface`: `interaction` or `finish`.
- After `tokenize`: `responsive` or `finish`.
