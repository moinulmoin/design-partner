# Actionable findings

Use this contract across all audit modes and when consuming earlier reports. Keep the report bounded to the requested surface and tested states.

## Evidence and consolidation

A finding needs a demonstrated problem, a location, user impact, and an implementable correction. Cite source paths and lines for code claims; cite route, component, viewport, and interaction for runtime observations. Include the relevant current implementation or observed behavior.

Source alone cannot establish a visual or runtime failure when computed styles, state, or interaction decide the result. A screenshot alone cannot establish which code caused it. Put unresolved suspicions in a separate verification-gaps section with the next check needed.

Group repeated symptoms caused by one shared component or token into one finding with affected locations. Rank shared fixes ahead of isolated fixes of equal severity. Distinguish defects from optional taste preferences; do not present a preferred aesthetic as a blocker.

## Severity

- **HIGH:** prevents or materially compromises a task, excludes users from essential content or controls, misleads consequential decisions, or exposes users to unrecoverable loss.
- **MEDIUM:** demonstrably increases effort or confusion, or causes meaningful inconsistency without blocking the task.
- **LOW:** localized polish with limited practical impact.

Escalate confirmed failures involving inaccessible control names, absent visible keyboard focus, pointer-only task paths, inadequate contrast, color-only meaning, placeholder-only field labels, clipped or unreachable content at zoom/narrow widths, unmitigated vestibular motion, and unsafe irreversible actions to HIGH. Establish that the failure actually exists and check relevant exceptions before assigning severity. Do not dilute a confirmed access barrier because neighboring visuals score well.

## Report shape

Use a compact table:

| ID | Severity | Area | Location / evidence | Current behavior | Proposed correction | User impact |
|---|---|---|---|---|---|---|

Give each finding a stable ID for follow-up work. Corrections should name what changes, not say merely “improve accessibility” or “make it cleaner.” Mark a suspected root cause as suspected even when the observed failure is confirmed.

Mention genuine borderline candidates rejected during inspection and why: existing behavior is valid, the proposal adds cost without benefit, or evidence is insufficient. Do not invent a quota of rejected candidates. Evidence-insufficient candidates also belong in verification gaps when they affect coverage.

## Verification and verdict

Record checks actually executed separately from checks not run. Include the command or interaction, relevant environment, and observed outcome. Do not treat tool availability, a planned test, or successful compilation as proof of UI behavior.

End with a verdict scoped to the inspected surface:

- **Block:** one or more confirmed HIGH findings remain.
- **Needs changes:** actionable MEDIUM or LOW findings remain, but no confirmed HIGH findings.
- **Approve:** no actionable findings remain and the checks necessary for the claimed scope were actually completed.

When there are no confirmed findings but missing checks prevent an honest approval, use **Verdict pending verification** and name the missing evidence. This is uncertainty, not a product defect. Never imply whole-product or formal accessibility certification from a bounded design pass.

Audit modes deliver findings, not implicit authorization to fix them. Implementation modes should consume the IDs and proposed corrections, recheck stale evidence, and report resolved versus outstanding work.
