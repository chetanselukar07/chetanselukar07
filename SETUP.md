# GitHub Profile Setup Guide

Green / Blue Cloud Cyberpunk profile for **chetanselukar07**.

## Folder structure

```text
chetanselukar07/
??? README.md
??? SETUP.md
??? docs/
?   ??? index.html          # clean HTML README viewer
??? .github/workflows/
?   ??? snake.yml
?   ??? pages.yml
??? assets/
    ??? banner-v2.svg
    ??? developer-card-fx.svg
    ??? images/
    ?   ??? profile.png
    ?   ??? profile-glow.png
    ??? animations/
```

## 1. Enable GitHub Actions

1. Open the repository on GitHub
2. Go to **Actions**
3. Click **I understand my workflows, go ahead and enable them** (if prompted)
4. Open **Generate Snake** -> **Run workflow**

## 2. Push to your default branch

This repo default branch is `development`.

```bash
git add .
git commit -m "Update GitHub profile"
git push origin development
```

## 3. Private contributions (optional)

1. Open https://github.com/settings/profile
2. Enable **Include private contributions on my profile**
3. Actions -> **Generate Snake** -> Run workflow

## 4. What updates automatically

| Widget | Source |
|--------|--------|
| GitHub Stats | gitstats.vercel.app |
| GitHub Streak | github-readme-streak-stats |
| Top Languages | gitstats.vercel.app |
| Activity Graph | github-readme-activity-graph |
| Contribution Snake | `.github/workflows/snake.yml` |
| Profile Views | komarev.com/ghpvc |
| README HTML page | `.github/workflows/pages.yml` |

## 5. Clean README HTML link (GitHub Pages)

Short HTML view:

**https://chetanselukar07.github.io/chetanselukar07/**

Pick **one** source (do not leave both fighting):

### Option A (recommended): Deploy from branch

1. Repo -> **Settings** -> **Pages**
2. Source: **Deploy from a branch**
3. Branch: `development` / folder: **/docs** (or `/` root — both have `index.html`)
4. Save

`.nojekyll` is present so Jekyll will not break the static HTML.

### Option B: GitHub Actions

1. Repo -> **Settings** -> **Pages**
2. Source: **GitHub Actions**
3. Run workflow **Deploy README HTML**

If the site returns 404 again, Pages source was switched and the branch publish overwrote Actions (or the reverse). Re-check the setting above.

## 6. Optional tweaks

- Replace LinkedIn / email / location in `README.md`
- Swap `assets/images/profile.png` (then regenerate glow with `python scripts/make_profile_glow.py`)
- Re-color SVG accents (`#39FF14` green, `#00F0FF` cyan)

## Theme tokens

| Token | Hex |
|-------|-----|
| Neon green | `#39FF14` |
| Cyan | `#00F0FF` |
| Deep navy | `#0A0E17` |
| Panel blue | `#071525` |
