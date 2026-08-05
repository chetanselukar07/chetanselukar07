# GitHub Profile Setup Guide

Green / Blue Cloud Cyberpunk profile for **chetanselukar07**.

## Folder structure

```text
chetanselukar07/
??? README.md
??? SETUP.md
??? .github/
?   ??? workflows/
?       ??? snake.yml
??? assets/
    ??? banner.svg
    ??? developer-card.svg
    ??? background.svg
    ??? cloud.svg
    ??? footer.svg
    ??? logo.svg
    ??? images/
    ?   ??? profile.png
    ??? animations/          # created by GitHub Actions
        ??? github-contribution-grid-snake.svg
        ??? github-contribution-grid-snake-dark.svg
```

## 1. Enable GitHub Actions

1. Open the repository on GitHub
2. Go to **Actions**
3. Click **I understand my workflows, go ahead and enable them** (if prompted)
4. Open **Generate Snake** ? **Run workflow**

The contribution snake SVGs appear under `assets/animations/` after the first successful run.

## 2. Push to your default branch

This repo’s default branch is currently `development`. The profile README is shown from the **default branch** of `chetanselukar07/chetanselukar07`.

```bash
git add .
git commit -m "Initial GitHub profile"
git push origin development
```

If you later switch the default branch to `main`:

```bash
git checkout -b main
git push -u origin main
```

Then set **Settings ? General ? Default branch** to `main`.

## 3. Private contributions (optional)

1. Open https://github.com/settings/profile
2. Enable **Include private contributions on my profile**
3. Actions ? **Generate Snake** ? Run workflow

## 4. What updates automatically

| Widget | Source |
|--------|--------|
| GitHub Stats | gitstats.vercel.app |
| GitHub Streak | github-readme-streak-stats |
| Top Languages | gitstats.vercel.app |
| Activity Graph | github-readme-activity-graph |
| Contribution Snake | `.github/workflows/snake.yml` |
| Profile Views | komarev.com/ghpvc |

## 5. Optional tweaks

- Replace LinkedIn / email / location in `README.md`
- Swap `assets/images/profile.png` (keep the same path)
- Re-color SVG accents in `assets/*.svg` (`#39FF14` green, `#00F0FF` cyan)

## 6. Clean README HTML link (GitHub Pages)

Short HTML view (no GitHub chrome):

**https://chetanselukar07.github.io/chetanselukar07/**

Enable once:

1. Repo ? **Settings** ? **Pages**
2. Source: **GitHub Actions**
3. Run workflow **Deploy README HTML** (or push to `development`)

Files live in `docs/index.html`.

## Theme tokens

| Token        | Hex       |
|--------------|-----------|
| Neon green   | `#39FF14` |
| Cyan         | `#00F0FF` |
| Deep navy    | `#0A0E17` |
| Panel blue   | `#071525` |
