# Audit protocol

Use this protocol for `checkup`, `smell`, and `review`, together with [findings.md](findings.md). Audit-only means no product-file edits unless the user explicitly requests fixes too. Scores describe quality; findings determine action priority.

## Evidence order

1. Run the interface when feasible and inspect representative routes and states.
2. Capture viewport-specific behavior rather than judging a single screenshot.
3. Trace visible problems to components, styles, tokens, or content.
4. Cite file and line when code evidence exists. Mark runtime-only observations clearly.
5. Put unconfirmed hypotheses in verification gaps, not actionable findings. Explain what evidence would resolve them.

## Severity

Use the shared HIGH / MEDIUM / LOW scale and escalation rules in [findings.md](findings.md). For older reports, map P0 and P1 to HIGH, P2 to MEDIUM, and P3 to LOW, then revalidate the actual impact; do not rewrite old reports solely to change labels.

## Scoring

Score each applicable dimension from 0–4:

- `0 Broken`: primary behavior or access fails.
- `1 Weak`: frequent serious problems.
- `2 Mixed`: usable but inconsistent or fragile.
- `3 Strong`: clear and dependable with minor issues.
- `4 Excellent`: intentional, resilient, and verified across relevant states.

Do not average scores into false precision. Explain the two dimensions that most affect the user.

## Dimensions

- Product clarity and prompt fidelity.
- Information hierarchy and composition.
- Task flow, affordance, and feedback.
- Typography and content readability.
- Color roles, contrast, and non-color cues.
- Component and token consistency.
- Responsive recomposition, zoom, localization, and RTL.
- Keyboard, semantics, labels, focus, reduced motion, and target sizing.
- Real-data resilience: empty, long, loading, error, permission, and stale states.
- Performance feel: layout shift, delayed response, oversized assets, and jank.
- Credibility: real evidence, specific copy, and domain-appropriate artifacts.

## Markdown report structure

Write `.design/<mode>-report.md` with:

1. Scope and verification method.
2. Two-sentence executive read.
3. What works and should be preserved.
4. Scorecard for applicable dimensions.
5. Findings table using the shared evidence and severity contract.
6. Prioritized action plan grouped into now, next, and later.
7. Verification gaps and assumptions.
8. Genuine candidates considered but rejected, with reasons; omit rather than invent filler.
9. Scoped verdict: Block, Needs changes, or Approve. If checks needed to support approval remain unavailable, state Verdict pending verification instead.

Keep `checkup` brief. Make `review` comprehensive. For `smell`, group repeated symptoms under one root decision rather than listing every instance.

## HTML mirror

When creating `.design/<mode>-report.html`, mirror the Markdown content exactly. Use semantic headings, landmarks, tables with headers, visible focus styles, responsive CSS, print styles, and no external dependency. The report's visual theme must not leak into the product UI.
