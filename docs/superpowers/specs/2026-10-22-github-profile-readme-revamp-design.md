# GitHub profile README revamp — design

## Intent and scope

Redesign **`lalitmee/lalitmee`**, the GitHub profile README repository, so a visitor can quickly see Lalit Kumar's engineering judgment, useful shipped tools, open-source contributions, and a way to contact him. Serve engineering hiring managers, open-source collaborators, and potential product/client partners from one readable GitHub profile. The existing website at `https://www.lalitmee.com` is a destination linked from the README, **not** a codebase to redesign or modify in this effort.

The user chose a **maker workbench** character, three featured apps (Markdown Previewer, JSON Assistant, Jira Assistant), a safely sanitized professional-work mention, and the contribution snake **on the GitHub profile only**. The README is an entry point, not a second portfolio site or an unsupported collection of counters.

## Visitor flow and presentation

1. Start with the name and a short, specific introduction: senior software engineer building product experiences and developer tools. A compact code/workbench-inspired accent and clear type hierarchy communicate the selected visual direction, but text must remain legible in both GitHub light and dark themes. Replace the current blue `header.png` hero rather than letting it conflict with the new direction. Avoid layout-dependent HTML, large animated headers, or a separate rendering stack.
2. Present three direct paths as short links or labels: engineering experience, open-source work, and apps/product work. Link the canonical portfolio, GitHub repositories, and contact information. No new portfolio pages are needed.
3. Show **Markdown Previewer**, **JSON Assistant**, and **Jira Assistant** first, with a concise grounded description for each and links to verified public source and/or working demos. Verify exact repo names, destinations, and claims before writing copy. Do not invent feature descriptions, usage counts, or testimonials.
4. Show selected open-source repositories as a smaller secondary group. Prefer links to directly relevant maintained work over a long skills-icon grid. Add one brief professional-work note using only publicly shareable facts; do not publish employer-sensitive architecture, private screenshots, unconfirmed metrics, or inferred business outcomes.
5. End with the generated contribution snake and a compact contact/footer area. The graphic is supporting context, not evidence that substitutes for completed work; it must not dominate the page and must have useful alternative text. Contact links and canonical portfolio URL must be current.

Use plain Markdown and minimal GitHub-compatible HTML, with no new dependency for layout or visual effects. Readability, keyboard-accessible links, reasonable image sizing, mobile wrapping, and meaningful link names take priority over a simulated terminal UI. Respect reduced motion by keeping the core content independent of the snake animation; if a static fallback is needed, generate it from the same workflow rather than loading an unrelated service.

## Content and tool boundaries

- Remove the obsolete 2024 goals, stale learning claims, noisy social icon row, broad skill icon strip, quotes, visitor counter, and hosted stats/language/WakaTime cards from the README. Avoid replacing them with trophy cards or a 3D activity graph. Preserve the user-selected snake.
- Update the profile's website link from `https://lalitmee.github.io/portfolio` to `https://www.lalitmee.com`. Only include selected social/contact links whose destination has been checked. Do not change the separate canonical portfolio application.
- Retain the existing `Platane/snk`-generated contribution visual in principle, but **do not reuse the present output as-is**: the published SVG currently has a 48×96 view box and rendered as purple blocks during review. Diagnose the generator/workflow and validate the new published SVG has a complete contribution grid and sensible dimensions before linking it as the final asset. Use an actively supported action invocation and minimal permissions; do not assume the specific failure cause without checking. Preserve the output branch approach if it works rather than adding a hosting service. Keep workflow run frequency modest.
- Stop scheduling README-mutating actions for sections no longer displayed: remove the recent-activity updater and the Waka stats updater if their content is removed. Leave unrelated automation outside scope. Do not add a live API or new secret to the README.
- The earlier discussion of portfolio case-study routes, Next.js layouts, and app data files belonged to a different repository and is **not part of this change**. The three selected apps need succinct verified links and descriptions here, not new case-study routes.

## Changes and boundaries

Expected edits are `README.md`, `.github/workflows/contribution-snake.yml`, and removal of `.github/workflows/update-readme.yml` and `.github/workflows/update-stats.yml` if their generated sections are dropped. `header.png` can remain as an unused tracked asset unless deleting it is clearly safe and valuable. No product dependencies, external portfolio files, analytics, deployment, or work on `master`.

Implementation must happen in the sibling worktree `/home/lalitmee/Projects/Personal/Github/lalitmee-worktrees/github-profile-revamp` on `feat/github-profile-revamp`. Commit this specification separately from any later implementation. No push or merge without a separate request.

## Failure handling and verification

- If a featured repository/demo URL is inaccessible, do not publish a broken link: use its verified counterpart or omit that destination while preserving the app name only if it is verifiable.
- If generating a healthy snake asset requires a workflow run unavailable locally, review the action version/configuration and test what can be checked locally; report the remote SVG as unverified until an actual successful generation and render check. The rest of the README must remain useful if the image fails to load.
- Preview the README in a GitHub-compatible renderer or on GitHub when possible. Check heading order, links, image alt text, desktop/mobile wrapping, and light/dark legibility. Verify that no unsupported metrics or confidential professional details were introduced, the old portfolio URL and 2024 goal are gone, and no surviving workflow edits removed content. Check workflow syntax and `git diff --check`; verify the resulting SVG visually once generated.

## Acceptance criteria

The GitHub profile leads with a clear maker-workbench introduction and all three selected apps, presents three audience paths and selected open-source/professional evidence without unverified claims, links to the canonical website, and includes one working contribution snake below the primary work. Removed widgets no longer trigger README-update automation. All changes stay in `lalitmee/lalitmee` on the dedicated feature branch; the separate `portfolio` project and `master` remain untouched.
