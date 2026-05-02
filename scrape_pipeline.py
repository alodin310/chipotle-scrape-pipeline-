import os
import re
import time
from pathlib import Path
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("FIRECRAWL_API_KEY")

# --- Step 01: Search + scrape with Firecrawl ---

api_url = "https://api.firecrawl.dev/v2/search"

headers = {
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "query": "Chipotle investor relations press releases",
    "limit": 5,
    "scrapeOptions": {"formats": ["markdown"]}
}

response = requests.post(api_url, headers=headers, json=payload)

data = response.json()
results = data["data"]["web"]
print(f"Firecrawl returned {len(results)} results")

for r in results:
    print(f"  - {r['title']}")
    print(f"    {r['url']}")
    print(f"    markdown length: {len(r.get('markdown') or '')} chars")

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
