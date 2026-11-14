# Nbooks

A single-file reading list: ratings (Goodreads → Amazon → Aladin), categories, read status, last read date,
long notes with Vim keys, rankings by category, and a fully keyboard-driven UI (`f` hints, `:` palette, `?` help).

- **App:** `docs/nbooks.html`, published with GitHub Pages.
- **Data:** never in this repo. Each device keeps a copy in the browser, and syncs through a secret GitHub Gist
  (⋯ → Sync across devices, using a token that only has the `gist` scope).

## Updating the published app

The private working copy `nbooks.html` (git-ignored) holds the built-in book list. After changing it:

```
python tools/build_public.py   # writes docs/nbooks.html without the book list
git add docs && git commit -m "Update app" && git push
```
