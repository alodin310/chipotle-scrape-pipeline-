# Step 02: Loop and Save — Design Spec

## Goal
Extend `scrape_pipeline.py` to save each Firecrawl search result as a markdown file in `knowledge/raw/`.

## Changes to `scrape_pipeline.py`
1. Remove duplicate parsing blocks — keep one clean version
2. Create `knowledge/raw/` with `Path("knowledge/raw").mkdir(parents=True, exist_ok=True)`
3. Loop over results; skip any where `r.get("markdown")` is empty
4. Generate slug: lowercase title → `re.sub(r'[^a-z0-9]+', '-', ...)` → strip hyphens → truncate to 40 chars → prefix with zero-padded index (e.g. `00-chipotle-press-releases.md`)
5. Write each file with `Source: <url>` on line 1, blank line, then markdown content

## Requirements satisfied
- `knowledge/raw/` created if missing
- Filenames follow `NN-slug.md` pattern
- Source URL traceable in each file
- Empty markdown results skipped
