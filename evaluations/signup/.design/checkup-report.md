# Signup checkup

Scope: original `before.html`, inspected in Chromium using agent-browser on 2026-09-06. Report-only pass; the original HTML is preserved for comparison.

The invitation task is clear, but keyboard users cannot reach its action. The fixed-width surface also prevents narrow-screen reflow.

Preserve the plain-language task, green action color, and administrator-approval explanation. Product clarity scores 3/4; keyboard completion scores 0/4. The task description works, while its only completion control is absent from the Tab sequence.

| ID | Severity | Area | Location / evidence | Current behavior | Proposed correction | User impact |
|---|---|---|---|---|---|---|
| A1 | HIGH | Keyboard | before.html:4; Tab moves input → body | Clickable div cannot receive normal keyboard focus | Use a native submit button inside a form | Keyboard users cannot complete the task |
| A2 | HIGH | Focus | before.html:3; global outline removal | Input focus has no outline replacement | Restore visible focus styling | Keyboard location is hard to track |
| A3 | HIGH | Forms | before.html:4 | Placeholder supplies the only field label | Associate a visible label with the input | Field purpose disappears while typing |
| A4 | HIGH | Reflow | before.html:3; 700px width plus 80px padding | Surface exceeds a 320px viewport | Use bounded fluid sizing and wrapping | Content and action extend outside the narrow viewport |

Now: repair A1–A4 together. Next: inspect form feedback after repair. Later: refine type hierarchy without changing the product identity.

Rejected candidate: replacing the green brand color; no evidence gathered here justifies a brand change. Screen-reader speech, native browser zoom, and cross-browser behavior remain unverified. The local fixture simulates an invitation; no backend exists.

Verdict: Block.
