# Design foundations

Use these as decision tools, not immutable style laws. Product evidence and existing brand rules win.

## Choose composition from the job

- `Monitor`: prioritize status, change, alerts, recency, and drill-down.
- `Operate`: keep tools, selection, context, and feedback close to the work surface.
- `Compare`: maintain stable rows/columns, aligned measures, and consistent scanning lanes.
- `Configure`: group dependent choices, show consequences, and provide a clear commit/revert area.
- `Learn`: optimize sequence, orientation, readable measure, and progressive disclosure.
- `Decide`: focus attention on evidence, risk, alternatives, and one dominant next action.
- `Explore`: make search, filters, previews, history, and reversible navigation prominent.

Mixed products may combine patterns, but one should dominate each surface.

## Establish hierarchy

- Make the first meaningful viewport explain what this is, what matters now, and what the user can do.
- Use position, size, contrast, density, and whitespace together; do not rely on font weight alone.
- Give one action primary emphasis per decision region.
- Prefer grouped relationships over a collection of equal cards.
- Keep dense work surfaces compact enough to scan while preserving touch and focus access.

## Build typography as a system

- Define semantic roles before assigning sizes.
- Keep body text comfortably readable and line length appropriate to the content and viewport; roughly 45–80 characters is a useful starting range, not a mandate.
- Use obvious hierarchy steps and consistent vertical rhythm.
- Test long words, dynamic numbers, mixed scripts, user zoom, and fallback fonts.
- Avoid decorative font choices that compromise UI clarity; avoid defaulting to a fashionable font without a product reason.

## Build color as roles

- Start with semantic tokens for canvases, surfaces, text, borders, actions, and statuses.
- Reserve the strongest chroma or contrast for information that deserves attention.
- Meet WCAG contrast requirements appropriate to the text or UI element. Provide icons, labels, patterns, or position so color is never the only signal.
- Test light/dark themes independently; inversion is rarely sufficient.
- Use perceptual color spaces when generating scales, then inspect real rendered output.

## Make components complete

- Define variants and states from product behavior, not from a component-gallery checklist.
- Every interactive component needs visible focus and a coherent default, hover, active, disabled, loading, success/error, and selected state when applicable.
- Use border, radius, and elevation to express grouping, containment, interactivity, or depth. Avoid decoration with no information role.
- Prefer familiar controls when novelty would increase interaction cost.

## Treat motion as behavior

- Animate state change, spatial continuity, direct feedback, or deliberate attention.
- Keep frequent interactions fast; allow larger navigational transitions more time.
- Avoid bounce or elastic easing unless the brand and interaction genuinely support playfulness.
- Keep animations interruptible, avoid layout-heavy properties, and honor `prefers-reduced-motion`.

## Write specific interfaces

- Name the actual artifact and action. Prefer “Send invoice” to “Continue” when that is the operation.
- Use realistic domain content in examples and previews.
- Explain errors with cause, preserved state, and a recovery path.
- Avoid unsupported superlatives, invented metrics, and vague “AI-powered” filler.

## Design for varied contexts

- Use semantic HTML and logical CSS properties where possible.
- Verify keyboard order follows the visual and task order.
- Preserve 200% zoom, long localization, RTL/bidirectional text, safe areas, and mobile software keyboards.
- Keep narrow-screen form controls at 16px or larger to prevent iOS focus zoom.
- Prefer at least 24×24 CSS px targets with adequate spacing; enlarge important or mobile controls beyond the minimum.
