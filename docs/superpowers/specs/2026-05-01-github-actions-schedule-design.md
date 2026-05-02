# GitHub Actions Schedule Design

**Date:** 2026-05-01  
**Project:** chipotle-scrape-pipeline  
**Scope:** Automate `scrape_pipeline.py` on a schedule via GitHub Actions (Step 10)

---

## Architecture

A single workflow file (`.github/workflows/scrape-pipeline.yml`) with two triggers:
- `workflow_dispatch` — manual run from the GitHub Actions tab
- `schedule` — cron at `0 6 * * 1` (every Monday 6am UTC)

The workflow runs on `ubuntu-latest`, installs only the two packages the script actually needs (`requests`, `python-dotenv`), executes the script, then commits any new files added to `knowledge/raw/` back to `main`.

## Credentials

`FIRECRAWL_API_KEY` is injected as a GitHub Actions secret (`secrets.FIRECRAWL_API_KEY`) and exposed to the script via the `env:` block. The script already reads it via `os.getenv("FIRECRAWL_API_KEY")` — no code change needed.

## Commit-back step

Uses `github-actions[bot]` identity. Stages only `knowledge/raw/`. Uses `git diff --staged --quiet || git commit` so it skips the commit if the scrape produced no new files (idempotent on duplicate runs).

## Schedule rationale

Weekly (Monday 6am UTC) is the right cadence for Chipotle investor relations press releases: new releases are infrequent, and daily would burn API credits for no new content. Weekly keeps data reasonably fresh with minimal cost.

## Required repo setup

Add `FIRECRAWL_API_KEY` as a repository secret:  
**Settings → Secrets and variables → Actions → New repository secret**

Name must match exactly: `FIRECRAWL_API_KEY`
