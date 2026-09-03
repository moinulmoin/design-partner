# Verification protocol

Use the strongest checks the repository supports. Never install or add a large toolchain just to satisfy this protocol without user authorization.

## Static checks

- Run formatter, typecheck, lint, and relevant unit/component tests.
- Search for duplicated raw values introduced where tokens should be used.
- Check semantic elements, labels, alt text, heading order, focus styles, reduced-motion handling, and logical CSS properties.
- Check for fixed dimensions, absolute positioning, clipped text, and hidden overflow that may fail under zoom or localization.

## Runtime checks

- Start the documented dev server and use the configured browser or device tool when available.
- Exercise the primary task and every changed control.
- Inspect at representative narrow, medium, and wide widths; choose breakpoints from the layout, not device names.
- Test 200% browser zoom, keyboard-only navigation, visible focus, long content, empty/loading/error states, and reduced motion.
- Check reflow at 320 CSS px; allow local scrolling for genuinely two-dimensional content. For access-sensitive changes, use [accessibility.md](accessibility.md) and test the entire affected task path.
- Inspect accessible names, roles, and states with available accessibility tooling. An accessibility-tree inspection is not a screen-reader test; name which was actually performed.
- Where relevant, test touch targets, on-screen keyboard behavior, dark mode, RTL, and permissions.
- Inspect the console and network panel for errors, broken assets, layout shift, and slow or oversized resources.

## Visual comparison

- Capture before/after screenshots when they materially support judgment.
- Compare hierarchy, wrapping, alignment, density, and states—not only overall attractiveness.
- Review the whole surface after local changes to catch new inconsistency.

## Completion language

State exactly what ran and passed. If only static inspection was possible, say so. Do not claim cross-browser, accessibility, responsive, or performance completion beyond the evidence collected.

Separate executed checks (exact command or interaction, environment, observed result) from checks not run. Automated scans and source review supplement, but do not replace, keyboard and assistive-technology checks. Use [findings.md](findings.md) for audit verdicts; no findings with incomplete verification does not establish approval.
