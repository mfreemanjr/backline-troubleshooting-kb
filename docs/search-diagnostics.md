# Ensure docs directory exists (it should)
New-Item -ItemType Directory -Path .\docs -Force | Out-Null

@'
# 🔎 Search Diagnostics

This page helps verify whether the Material for MkDocs search engine is functioning correctly on this site.

---

## ✅ 1. Check if the search index is reachable

Click the link below:

**View search_index.json**

Expected results:
- If it downloads or opens a large JSON blob → **Good**
- If it shows 404 / Cannot load / HTML error → **Search cannot work**

---

## ✅ 2. Real-time browser diagnostics

Open your browser’s Developer Tools:
- **Chrome / Edge** → F12 → “Network” tab  
- Refresh the page
- In the filter box, type: **search**

You should see requests for:

- `search_index.json`
- `search.js`
- `worker/search.worker.js` (depending on theme version)

If any are **red / 404 / blocked**, search will return zero results.

---

## ✅ 3. JavaScript console errors

Open DevTools → “Console”.

Common failure messages include:
- `Failed to fetch search_index.json`
- `Cannot read property 'config' of undefined`
- `Uncaught ReferenceError: lunr is not defined`
- `Failed to load resource: the server responded with a status of 404`

If you see any of these, search is broken due to missing/inaccessible JS assets.

---

## ✅ 4. Verify theme configuration

Make sure `mkdocs.yml` includes:

```yaml
theme:
  name: material