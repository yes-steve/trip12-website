# Trip 12 Future Foundation — Website

Official website of Trip 12 Future Foundation Inc., a 501(c)(3) public charity (EIN 41-2611886) providing financial assistance, service animal support, and education for individuals and families affected by TRIP12-related disorders.

## Structure

- `site/` — the deployable static site (HTML/CSS, self-hosted fonts). Netlify publishes this folder (see `netlify.toml`).
- `build_site.py` — Python generator that produces the pages in `site/` from shared templates. Edit this, then run `python3 build_site.py` to regenerate.

## Updating the site

Content updates are made via Claude (Cowork / Claude Code): describe the change, Claude edits the generator or CSS, regenerates, commits, and pushes. Netlify auto-deploys from `main`.
