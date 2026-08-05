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

Enable once:

1. Repo -> **Settings** -> **Pages**
2. Source: **GitHub Actions** (not "Deploy from a branch")
3. Run workflow **Deploy README HTML**

Do not use Jekyll / branch deploy for this repo. The HTML viewer is in `docs/index.html` and is published by Actions.

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
