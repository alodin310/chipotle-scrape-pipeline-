# Step 02: Loop and Save Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend `scrape_pipeline.py` to save each Firecrawl result as a `NN-slug.md` file in `knowledge/raw/`.

**Architecture:** Clean up duplicate parsing blocks from Step 01, then add a save loop directly below the existing results list. No new files or functions needed — everything stays in `scrape_pipeline.py`.

**Tech Stack:** Python stdlib (`re`, `pathlib.Path`), already imported

---

### Task 1: Clean up duplicate parsing blocks

**Files:**
- Modify: `scrape_pipeline.py`

- [ ] **Step 1: Remove the two extra copies of the parsing block**

The file currently has this block three times. Keep only the first occurrence and delete the other two:

```python
data = response.json()
results = data["data"]["web"]
print(f"Firecrawl returned {len(results)} results")

for r in results:
    print(f"  - {r['title']}")
    print(f"    {r['url']}")
    print(f"    markdown length: {len(r.get('markdown') or '')} chars")
```

- [ ] **Step 2: Verify the file looks clean**

`scrape_pipeline.py` should now have exactly one parsing block after `response = requests.post(...)`.

---

### Task 2: Add save loop to scrape_pipeline.py

**Files:**
- Modify: `scrape_pipeline.py`

- [ ] **Step 1: Add directory creation and save loop after the print loop**

Append this block immediately after the existing print loop:

```python
# --- Step 02: Save results to knowledge/raw/ ---

out_dir = Path("knowledge/raw")
out_dir.mkdir(parents=True, exist_ok=True)

for i, r in enumerate(results):
    if not r.get("markdown"):
        continue

    slug = re.sub(r'[^a-z0-9]+', '-', r['title'].lower()).strip('-')[:40]
    filename = f"{i:02d}-{slug}.md"
    filepath = out_dir / filename

    content = f"Source: {r['url']}\n\n{r['markdown']}"
    filepath.write_text(content, encoding="utf-8")
    print(f"  Saved: {filename}")
```

- [ ] **Step 2: Run the script**

```bash
python scrape_pipeline.py
```

Expected output: five lines like `Saved: 00-chipotle-mexican-grill-investor-re.md`

- [ ] **Step 3: Verify files in knowledge/raw/**

```bash
ls knowledge/raw/
```

Expected: 5 `.md` files named `00-*.md` through `04-*.md`

- [ ] **Step 4: Spot-check one file**

```bash
head -3 knowledge/raw/00-*.md
```

Expected: first line is `Source: https://...`, second line blank, third line starts markdown content.

- [ ] **Step 5: Commit**

```bash
git add scrape_pipeline.py knowledge/raw/
git commit -m "feat: step 02 - loop and save results to knowledge/raw/"
```
