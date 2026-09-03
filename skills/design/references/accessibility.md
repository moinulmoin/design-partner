# Accessibility implementation

Use for `a11y` and relevant portions of changes to interactive controls, forms, overlays, or motion. Keep fixes within the requested surface. Start with existing reports and the primary task, not a global search-and-replace of ARIA attributes.

## Inspect the task, then repair

Identify entry point, actions, feedback, recovery, and completion. Walk that path with keyboard input; separately inspect accessible names, roles, and states. Use a screen reader when available and record exactly what was tested. If unavailable, say so rather than claiming equivalent coverage from an accessibility-tree snapshot.

Prioritize barriers according to [findings.md](findings.md). Preserve working library primitives and established brand tokens; fix their usage before replacing them.

## Controls and navigation

- Prefer native links for navigation and buttons for actions. A custom role requires implementing its keyboard behavior, states, and naming, not just adding a role attribute.
- Keep focus order consistent with the task and DOM order. Avoid positive tabindex. Use 0 to include a necessary custom focus target and -1 for programmatic focus or inactive items in a managed widget.
- Preserve a visible focus indicator. Test custom rings across actual adjacent colors, selected states, clipping containers, and forced-color settings; do not remove outlines without a verified replacement.
- Use established keyboard patterns for composite controls such as tabs, menus, comboboxes, and listboxes. Match the actual widget pattern; do not apply application-menu semantics to ordinary site navigation.
- Provide keyboard alternatives to dragging, hover-only content, and pointer gestures. Escape should close the relevant dismissible layer without unexpectedly dismissing its parents.

## Names and structure

- Prefer names derived from visible labels. Icon-only actions need an accessible name describing the action; hide decorative icons from assistive technology.
- Keep visible control wording within its accessible name, including after localization. Verify referenced label/description IDs exist and are unique.
- Do not hide focusable controls or their ancestors from the accessibility tree. Use semantic headings, landmarks, and a skip path around repeated navigation where appropriate.
- Give informative images purpose-appropriate alternatives, decorative images empty alt text, and complex charts an accessible explanation or data representation. Check media captions/transcripts where relevant.
- After client-side navigation, keep document title, focus, and reading context useful; verify back/forward behavior rather than forcing the same reset for every navigation.

## Overlays

Prefer the project's tested accessible dialog primitive or native modal dialog when appropriate. A modal needs a name, logical initial focus, background interaction suppression, focus containment, a way to close, and sensible focus restoration. Initial focus depends on content and risk; destructive confirmations should not default to the destructive action.

Test nested overlays, long content, Escape, Tab/Shift+Tab, and closing after the original trigger disappears. A tooltip or nonmodal popover does not automatically need a modal focus trap.

## Forms and feedback

- Associate persistent visible labels with inputs. Placeholders can illustrate values but cannot replace labels. Use appropriate input types, input modes, autocomplete, and password-manager-compatible fields.
- Connect errors to their fields, expose invalid state, explain recovery, and retain entered data. On submission, direct users to errors through a suitable summary or focus target without redundant announcements.
- Prefer allowing submission to explain validation failures over an unexplained disabled submit. Distinguish invalid input from an in-flight request or genuine permission restriction.
- Native disabled controls supply behavior; aria-disabled only communicates state. If using aria-disabled to retain discoverability, prevent activation in code and explain availability.
- Announce relevant asynchronous changes with an appropriate status/live region when focus or a field description does not already communicate them. Reserve interruptive alerts for urgent information; avoid duplicate speech and excessive live updates.
- Keep paste and password managers working. Loading states should retain the action's identity. Errors or actionable messages should remain available long enough to use, not vanish on a short timer.

## Visual access and adaptation

- Check contrast on rendered foreground/background pairs, including interaction states. Record the measured pair and applicable threshold for a contrast finding; preserve brand identity through targeted token corrections.
- Give status and distinctions redundant cues beyond hue alone.
- Inspect usable target size and separation; enlarge important touch controls where feasible without overlapping neighboring hit areas. Apply the project's accessibility target and relevant exceptions instead of treating every small inline link as an automatic failure.
- Verify content and function at 200% zoom and reflow at 320 CSS px. Allow local two-dimensional scrolling where necessary, rather than clipping content or forcing whole-page horizontal scrolling.
- Check text expansion, long labels, sticky chrome, and focus obscured by fixed elements. Preserve user scaling and let text containers grow.

## Motion

Respect reduced-motion preferences in CSS and scripted behavior. Replace unnecessary spatial movement with static or lower-motion feedback while retaining understandable state changes. Provide appropriate controls for autoplaying or persistent moving content.

Test both preference states. Do not blindly remove animation events when application logic depends on them; make completion logic reliable with and without animation. Do not assume every spinner needs removal or every animation is safe merely because it is brief.

## Finish with evidence

Rewalk the affected task after fixes. Use automated checks where already available, plus manual keyboard, focus, state, zoom, and motion checks. Record assistive-technology coverage and remaining gaps separately. For a narrow request, claim only that narrow coverage—not a comprehensive accessibility audit or certification.
