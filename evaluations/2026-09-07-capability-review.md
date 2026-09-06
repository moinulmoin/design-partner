# Design workflow coverage review

Reviewed against installed Command Code v1.50.0 on 2026-09-07. Its official updater reported that version current during this check. This is a documentation and routing review, not a comparison of generated designs.

## Evidence and scope

Inspected the actual help-mode registry and working-rules implementation in the installed CLI, the bundled design entrypoint, the complete reference-file/section inventory, and selected mode-contract sections. Examined audit/report contracts, creation, redesign, layout, refinement, tokenization, setup, typography, color, responsive behavior, motion, interaction, voice, and product-surface guidance against Design Partner's entrypoint and mode contracts. The terminal help is a fixed guide; inspecting its implementation did not require starting an agent session or exposing a user's project to it.

The bundle contains 27 reference files totaling 5,323 lines. That volume describes instruction depth, not measured quality. The comparison below does not claim every line of every reference was independently evaluated.

## Capability coverage

The CLI registry exposes 18 named modes. All 18 have matching mode names in Design Partner. Design Partner also exposes `create` explicitly, for 19 modes; Command Code routes new-build requests to an internal create reference.

| Work | Command Code modes | Design Partner coverage |
|---|---|---|
| Diagnose | checkup, smell, review | Fast scan, generic-pattern critique, deeper review; evidence and prioritized corrections |
| Remove generic design | deslop | Product-specific replacements for confirmed generic choices |
| Visual systems | typeset, recolor | Type hierarchy, font behavior, palette roles, contrast, themes |
| Behavior | motion, interaction, a11y | Animation, control states, keyboard/focus, feedback, access barriers |
| Composition | relayout, responsive | Structural layout changes and adaptation across contexts |
| Build and organize | redesign, tokenize, setup; inferred creation | New UI, visual transformation, reusable components/tokens, durable brief |
| Refine and finish | finish, refine | Edge states, polish, hierarchy, subtraction, verified completion |
| Brand expression | voice | Brand character, art direction, copy tone, imagery, product-specific proof |
| Operational UI | surface | Data density, permissions, loading, failure, recovery, realistic content |

## Where our listing fell short

The previous copy overemphasized critique, accessibility, and modest polish. It underrepresented new builds, structural redesign, motion, brand direction, tokenization, and operator-facing resilience. “Build, critique, and polish UI” is the chosen short subtitle. The longer description should connect those disciplines to useful tasks without reproducing the entire help table.

## Differences in instruction depth

- Command Code gives most modes a dedicated reference and an explicit minimum execution bar. Design Partner condenses most into one-line contracts plus shared foundations. Mode-name coverage does not imply equal execution depth.
- Command Code's broad motion pass explicitly looks for missing transitions and feedback across the surface. Our mode covers purpose, interruption, and reduced motion but leaves more of the inventory to the model.
- Command Code separates expressive brand work from repeat-use operational UI more strongly. Our voice and surface modes cover both categories, with less specific decision guidance.
- Command Code's refinement reference describes several diagnosis-dependent directions, including stronger expression, reduced intensity, simplification, resilience, and first-use improvements. Ours emphasizes subtraction, hierarchy, and precision.
- Both require implementation evidence for completion claims and carry reports into later work. That agreement is an instruction-level observation; it does not establish reliable behavior in every run.

## Differences we should preserve

- Our explicit audits preserve product files in empty projects. The inspected source simultaneously mandates report-only audits and creating HTML for any mode in an empty project; we should not import that conflict.
- Our HTML reports are optional. The source mandates Markdown and HTML templates and distinct numerical scoring systems. More artifacts do not automatically improve an audit.
- Our deslop mode consumes available reports without mandating all three full audits first. The source requires generating every missing report, which adds work even for a narrow request.
- Our foundations frame visual choices as contextual decisions. The source contains rigid aesthetic formulas and some conflicts, including scope around palette/type changes in relayout. Those should not be treated as universal requirements.

## Follow-up priorities

1. Test broad motion, brand-expression, and dense-product tasks before expanding the skill. The current signup smoke fixture does not cover them.
2. If those tests show incomplete work, add concise mode-specific acceptance guidance based on the demonstrated gaps.
3. Keep the public listing's claims within the skill's documented scope and measured evidence. Do not claim quality parity or an improvement percentage without a comparison.

No original Command Code prompt bundle was copied into this repository. See PROVENANCE.md for the inspection history and licensing boundary. This review changed listing copy only.
