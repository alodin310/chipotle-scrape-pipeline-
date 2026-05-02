# Step 02: Save Firecrawl Results to knowledge/raw/

**Date:** 2026-04-15
**File:** scrape_pipeline.py (inline Step 02 block)

## Goal

Extend `scrape_pipeline.py` to loop over the 5 Firecrawl search results from Step 01 and write each one as a markdown file in `knowledge/raw/`.

## Approach

Inline `# --- Step 02 ---` block added directly after the Step 01 loop in `scrape_pipeline.py`. No new files, no helper functions.

## Filename Format

Derived from today's date + the result URL.

- Strip scheme (`https://`, `http://`)
- Replace all non-alphanumeric characters with hyphens
- Collapse consecutive hyphens into one
- Prepend `YYYY-MM-DD-`
- Append `.md`

Example: `https://ir.chipotle.com/news-releases` → `2026-04-15-ir-chipotle-com-news-releases.md`

## Output Directory

`knowledge/raw/` — created automatically with `Path.mkdir(parents=True, exist_ok=True)` if it does not exist.

## File Contents

Each file begins with a provenance header, then the scraped markdown:

```
Source: <url>
Title: <title>
Scraped: <YYYY-MM-DD>

---

<markdown content>
```

## Empty Result Handling

If `r.get("markdown")` is `None` or an empty string:
- Print: `Skipping <url> — no markdown content`
- Do not write a file

## Console Output

- On successful write: `Saved: knowledge/raw/<filename>`
- On skip: `Skipping <url> — no markdown content`

## Imports Already Available

`re`, `Path` (from `pathlib`), and `datetime` (stdlib, not yet imported — must be added) cover all filename and date logic.
