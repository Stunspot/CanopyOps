# CanopyOps Pages Source

This directory is the source for the CanopyOps GitHub Pages site.

- `index.html` contains the complete semantic customer journey and social metadata.
- `style.css` contains the responsive visual presentation.
- `assets/canopyops-hero.png` is the 1600×900 no-text Pages hero.
- `assets/canopyops-readme-hero.png` is the separate 1500×600 no-text README banner.
- `assets/canopyops-social-card.png` is the separate 1280×640 Open Graph and X/Twitter card with the exact title `CanopyOps` and identifying line `Cannabis cultivation operations`.
- `.nojekyll` instructs GitHub Pages to serve this directory directly.

The three role assets are different compositions and aspect ratios. The Pages hero establishes the controlled cultivation environment, the README banner centers operating review and measurement, and the social card carries explicit title text for link previews.

## Content authority

The site summarizes the living repository documentation. It does not independently define package versions, platform availability, safety authority, or verification status.

Use these root documents as the canonical sources:

- [`../RELEASE-STATUS.md`](../RELEASE-STATUS.md) — distribution and publication state;
- [`../README.md`](../README.md) — product orientation;
- [`../INSTALL.md`](../INSTALL.md) — installation, verification, maintenance, removal, and recovery;
- [`../SAFETY-AND-SCOPE.md`](../SAFETY-AND-SCOPE.md) — operational boundary;
- [`../DATA-AND-PRIVACY.md`](../DATA-AND-PRIVACY.md) and [`../SECURITY.md`](../SECURITY.md) — storage, network, privacy, and security behavior;
- [`../DOCUMENTATION-STATUS.md`](../DOCUMENTATION-STATUS.md) — documentation scope and review custody.

## Technical boundary

The site uses no JavaScript, tracking code, analytics, remote fonts, remote image dependencies, or SVG illustrations. It loads checked-in PNG assets and one local stylesheet.

GitHub Pages publishes `docs/` from `main`. A successful build proves only that those static files deployed. It does not prove package installation, model behavior, field validation, regulatory approval, or operational authority.