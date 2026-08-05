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

## 3. Dual GitHub accounts (personal + Thinksmart)

Work is split across two GitHub users:

| Account | Role |
|---------|------|
| [chetanselukar07](https://github.com/chetanselukar07) | Personal profile |
| [chetanthinksmart](https://github.com/chetanthinksmart) | Thinksmartin org commits |
| [Thinksmartin](https://github.com/Thinksmartin) | Organization (private repos) |

The README shows **separate** stats / streak / languages / activity / snake for each account (GitHub cannot merge two usernames into one card).

### Required on chetanthinksmart

1. Sign in as **chetanthinksmart**
2. Open https://github.com/settings/profile
3. Enable **Include private contributions on my profile**
4. Confirm Thinksmartin commits are authored as that account

Do the same on **chetanselukar07** for private personal work.

### Optional

- Thinksmartin ? People ? set `chetanthinksmart` membership to **Public**
- Actions ? **Generate Snake** ? Run workflow (regenerates both snakes)

## 4. What updates automatically

| Widget | Source |
|--------|--------|
| Stats / langs (both users) | gitstats.vercel.app |
| Streak (both users) | github-readme-streak-stats |
| Activity graphs (both users) | github-readme-activity-graph |
| Snakes (both users) | `.github/workflows/snake.yml` |
| Profile Views | komarev.com/ghpvc |

## 5. Optional tweaks

- Replace LinkedIn / email / location in `README.md`
- Swap `assets/images/profile.png` (keep the same path)
- Re-color SVG accents in `assets/*.svg` (`#39FF14` green, `#00F0FF` cyan)

## Theme tokens

| Token        | Hex       |
|--------------|-----------|
| Neon green   | `#39FF14` |
| Cyan         | `#00F0FF` |
| Deep navy    | `#0A0E17` |
| Panel blue   | `#071525` |
