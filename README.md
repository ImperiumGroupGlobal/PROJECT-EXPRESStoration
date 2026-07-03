# PROJECT EXPRESStoration

**An independent, open-source retail turnaround proposal for Express, published by ImperiumGroup.**

🔗 Live site: [project-expresstoration.pages.dev](https://project-expresstoration.pages.dev/)

---

## ⚠️ Disclosure

ImperiumGroup is an independent, pseudonymous collective. This repository and the site it publishes are **not affiliated with, endorsed by, or commissioned by Express, Inc. or WHP Global.** Nothing here is a leaked or official corporate document — it's an unsolicited, speculative strategy proposal, published openly.

Every quantitative claim on the site is labeled by confidence tier (`SOURCED` / `MODELED` / `DIRECTIONAL`) and logged in the [Methodology & Figure Ledger](https://project-expresstoration.pages.dev/methodology.html). See that page before citing any number from this project elsewhere.

---

## What this is

PROJECT EXPRESStoration is a boardroom-style memorandum — three core strategic pillars, a phased pilot rollout, comparable-retailer precedent, and a sourcing standard — built to demonstrate retail strategy and store-design thinking in public. It's structured and written the way a real capital-allocation proposal would be, on the theory that a well-argued idea deserves a well-produced container.

**Core pillars:**
1. **Sensory Theater & Utility Overhaul** — lighting and audio redesign framed in operating-cost terms
2. **Product Purge & Nightlife Heritage** — inventory velocity and assortment strategy
3. **Frictionless Logistics & Conversion** — checkout/return flow redesign

---

## Site structure

```
/
├── index.html            # Landing page — overview, three pillars, chapters 01–03
├── methodology.html       # Sourcing standard + full figure ledger
├── precedents.html        # Comparable-retailer case studies + Express's own bankruptcy record
├── pilot-program.html     # Full phased rollout plan + KPIs
├── faq.html                # "Is this official," licensing, etc.        [planned]
├── license.html            # Plain-language CC BY 4.0 explainer          [planned]
├── sitemap.xml             # Crawl map
├── robots.txt               # Crawler directives, points to sitemap.xml
└── README.md                 # This file
```

Every page shares one design system (see below) and cross-links to the others via a consistent nav/footer, so the site reads as a single body of work rather than disconnected pages.

---

## Design system

- **Palette:** pitch black (`#000000`), white (`#ffffff`), neon cyan (`#00f3ff`), neon red (`#ff003c`)
- **Type:** [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) (headers, uppercase, brutalist), [Inter](https://fonts.google.com/specimen/Inter) (body), `Courier New` (terminal labels, mono data)
- **Motif:** "Corporate Executive Terminal" — liquid-metal gradients, architectural grids, status badges (`[ CAPEX: ZERO ]`), data-readout callouts
- **Copy register:** every design or creative decision is translated into financial/operational language (e.g. "Mitigating Checkout-Line Abandonment," not "shorter lines")

No build step — each page is a self-contained `.html` file with inline `<style>` and `<script>`.

---

## Adding a new page

To keep the site coherent and crawlable, every new page should:

1. Reuse the shared design tokens (colors, fonts) from `index.html`'s `<style>` block.
2. Include the **independence strip** at the top of `<body>` — non-negotiable, this is what keeps the project unambiguous about its status.
3. Include the same `nav` and `footer` structure, with the current page marked via a `.current` class in `.nav-links`.
4. Add an entry to `sitemap.xml`.
5. Link to and from at least one existing page (no orphan pages).
6. Tag any new quantitative claims by confidence tier and add them to the ledger in `methodology.html`.

---

## License

All content, copy, and design in this repository is published under **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)**.

In plain terms: anyone — including Express, Inc. or WHP Global — may use, adapt, or ignore any part of this proposal, with or without credit, for any purpose. This is a good-faith declaration, not a legal filing or binding instrument.

---

## Contributing

This is currently maintained as a single-collective project rather than an open contribution pipeline. If you want to propose a correction to a figure in the ledger, or flag something that reads as misrepresenting itself as an official document, please open an issue.
