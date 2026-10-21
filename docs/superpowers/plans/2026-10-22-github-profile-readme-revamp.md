# GitHub Profile README Revamp Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `lalitmee/lalitmee` into a readable maker-workbench GitHub profile that leads with three shipped apps and displays a healthy contribution snake.

**Architecture:** Keep the README as the only presentation surface. Generate light/dark snake SVGs using the existing GitHub Action and `output` branch; link those assets from a compact Markdown README. Remove automation tied to deleted README sections; do not modify the separate `portfolio` repo.

**Tech Stack:** GitHub-flavored Markdown, GitHub Actions YAML, `Platane/snk/svg-only@v3`, Python 3 standard-library `unittest` for static checks.

**Spec:** `docs/superpowers/specs/2026-10-22-github-profile-readme-revamp-design.md`

## Global Constraints

- Work only on `feat/github-profile-revamp` in `/home/lalitmee/Projects/Personal/Github/lalitmee-worktrees/github-profile-revamp`; leave `master` and the separate `portfolio` application untouched. Do not push or merge.
- Lead with Markdown Previewer, JSON Assistant, and Jira Assistant; link only verified public destinations. No invented metrics, testimonials, private details, or guessed demos.
- Offer paths for engineering experience, open-source work, and apps/product work. The canonical website is `https://www.lalitmee.com`.
- Keep a single contribution-snake presentation on the GitHub README only. Validate the actual generated asset; a green Action run alone is insufficient.
- Use plain Markdown/minimal GitHub-compatible HTML; readable on mobile and light/dark themes; content must stand on its own for reduced-motion visitors.
- No new app dependencies, hosted badge/stats APIs, live GitHub API integration, or additional secrets.

## Review Focus

1. A missing or mistyped featured-app link must not be published: Task 2 tests all three names with Markdown link syntax and checks each destination manually before use.
2. A malformed snake must not count as success: Task 1 tests workflow output paths and checks generated SVG dimensions/grid after a permitted remote run.
3. Dark-mode viewers must not see invisible artwork: Task 1 tests distinct light/dark outputs; Task 2 tests both `<picture>` sources and checks rendering on GitHub when possible.
4. Old goals and portfolio links must not survive: Task 2 tests for the canonical URL and absence of the old URL, 2024 goal, and removed widgets.
5. Scheduled updaters must not churn removed sections: Task 2 tests that the activity/Waka updater workflow files and activity markers are absent.

## File map

- `.github/workflows/contribution-snake.yml`: generate and publish the two snake variants. It does not edit `README.md`.
- `README.md`: complete GitHub profile content and one responsive light/dark snake presentation.
- `.github/workflows/update-readme.yml`, `.github/workflows/update-stats.yml`: delete after removing their generated content.
- `tests/test_profile.py`: minimal dependency-free structural checks for workflow/README integration; no network calls. Keep `header.png` tracked but unused.

---

### Task 1: Repair and validate snake generation

**Files:**
- Modify: `.github/workflows/contribution-snake.yml:1-39`
- Create: `tests/test_profile.py`

**Interfaces:**
- Consumes: existing `output` branch publishing convention and GitHub's `${{ github.repository_owner }}`.
- Produces: `output/github-contribution-grid-snake.svg` and `output/github-contribution-grid-snake-dark.svg` with both names unchanged for Task 2's `<picture>` sources.

- [ ] **Step 1: Add a failing `unittest`** in `tests/test_profile.py`: `test_snake_workflow` reads the YAML text and asserts it uses `Platane/snk/svg-only@v3`, an `outputs: |` list containing both `dist/github-contribution-grid-snake.svg` and `dist/github-contribution-grid-snake-dark.svg?palette=github-dark`, `target_branch: output`, `build_dir: dist`, and `contents: write`; assert the legacy `svg_out_path:` input is absent. Run `python3 -m unittest discover -s tests -v`; expect failure on the current workflow.
- [ ] **Step 2: Update `.github/workflows/contribution-snake.yml`** to use the documented v3 SVG-only `outputs` interface and `crazy-max/ghaction-github-pages@v3.1.0`. Give only the generate job `contents: write`, retain `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}`, keep the `output` branch and path names above, and change the six-hour cron to daily `0 0 * * *`; preserve `workflow_dispatch` and the existing `master` push trigger so a later merge triggers initial generation. The source example is `https://raw.githubusercontent.com/Platane/Platane/master/.github/workflows/main.yml`.
- [ ] **Step 3: Run** `python3 -m unittest discover -s tests -v` and `git diff --check`; expect PASS and no whitespace errors. Inspect YAML as text and, if an installed YAML parser exists, parse it without adding a dependency.
- [ ] **Step 4: Check the real artifact when a run is authorized and available.** GitHub may not expose a newly changed workflow for dispatch until it exists on the default branch. After a permitted remote run (normally after a later merge/push), inspect both URLs under `https://raw.githubusercontent.com/lalitmee/lalitmee/output/`. Confirm HTTP success, a contribution-grid-scale SVG (not 48×96), non-empty cells, and readable light/dark rendering. Until then, mark remote image repair as pending; do not claim it works. If output is still bad after a run, investigate the generator inputs/artifact before calling it fixed.
- [ ] **Step 5: Commit** `git add .github/workflows/contribution-snake.yml tests/test_profile.py && git commit -m "fix: regenerate profile snake with supported action"`.

### Task 2: Rebuild README and retire unused updaters

**Files:**
- Modify: `README.md:1-96`
- Delete: `.github/workflows/update-readme.yml`, `.github/workflows/update-stats.yml`
- Modify: `tests/test_profile.py`

**Interfaces:**
- Consumes: Task 1's exact `output` branch SVG paths; the public repository and demo destinations verified during this task.
- Produces: standalone GitHub profile README. No generated README markers, API-backed widgets, or scheduled README rewrite jobs remain.

- [ ] **Step 1: Verify featured-project destinations and copy.** Check the public repositories and optional live demos for Markdown Previewer, JSON Assistant, and Jira Assistant by fetching their README/project pages or HTTP responses. Confirm each description against public source. Check `https://www.lalitmee.com`, selected open-source repositories, LinkedIn/email/resume links if used. Exclude any destination that cannot be verified; never guess a URL or invent a feature. Use a concise Nykaa professional-work line only if it can be stated from shareable facts without metrics.
- [ ] **Step 2: Extend `tests/test_profile.py` with failing tests:** `test_profile_structure` asserts `README.md` contains Markdown links labeled `Markdown Previewer`, `JSON Assistant`, and `Jira Assistant` (regex matching a non-empty `https://` destination), headings/labels for engineering, open source, and apps, `https://www.lalitmee.com`, and `<picture>` with the exact Task 1 light/dark URLs and `alt="Animated snake tracing Lalit's GitHub contributions"`; `test_no_stale_or_generated_content` asserts old GitHub Pages portfolio URL, `2024 Goals`, `<!--START_SECTION:activity-->`, hosted stats/quotes/visitor widgets, and references to `header.png` are absent, and asserts the two updater workflow files do not exist. Run `python3 -m unittest discover -s tests -v`; expect failure on the current README.
- [ ] **Step 3: Replace `README.md`** with: short name/engineering introduction and restrained workbench/code accent; three navigation paths; featured apps in user-selected order, with brief verified descriptions and direct links; a short selected open-source section; a safely shareable professional note; `<picture>` containing light/dark raw `output` snake SVGs with one descriptive `img alt`; and concise contact/canonical website links. Use Markdown first and avoid layout tables that break on narrow viewports. Remove the obsolete skills icon grid, badges/stats, recent activity block, quotes, visitors, stale year/copy, and blue header reference. Delete the two updater workflow files when their sections are gone. Keep the README useful even before SVG generation completes by retaining text and project links independently of the image.
- [ ] **Step 4: Run** `python3 -m unittest discover -s tests -v`, `git diff --check`, and a read-through of README headings/URLs; expect PASS. Check every selected external URL (e.g. `curl -IL --max-time 15 <url>`), allowing for services that reject HEAD by checking GET instead; treat failed or restricted endpoints as unverified, not healthy. Preview in GitHub-compatible rendering where possible and inspect light/dark, mobile wrapping, link names, image alt text, and reduced-motion readability. Do not claim the SVG works without Task 1's artifact check.
- [ ] **Step 5: Commit** `git add README.md .github/workflows/update-readme.yml .github/workflows/update-stats.yml tests/test_profile.py && git commit -m "feat: refresh GitHub profile around shipped work"`.

## Final gate

Re-run `python3 -m unittest discover -s tests -v` and `git diff --check`; inspect `git status --short --branch`, verify `master` and the separate portfolio repo remain unchanged, and explicitly distinguish local workflow validation from verified remote SVG output. Do not push, merge, or claim a repaired image until generated output is inspected.
