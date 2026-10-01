# PROJECT EXPRESStoration

**An independent, open-source retail turnaround proposal for Express, published by ImperiumGroup.**

[Live site](https://project-expresstoration.pages.dev/)

> **Unofficial:** This project is independent and is not affiliated with, endorsed by, sponsored by, or commissioned by Express, Inc. or WHP Global. It is a public strategy proposal, not an internal or leaked corporate document. Quantitative claims are explicitly labeled by confidence tier and documented in the methodology ledger.

## What this project is

PROJECT EXPRESStoration is a static, boardroom-style strategy site covering three operational pillars:

1. **Sensory Theater & Utility Overhaul**: store atmosphere, lighting, and audio concepts
2. **Product Purge & Nightlife Heritage**: assortment, inventory velocity, and rapid-response product validation
3. **Frictionless Logistics & Conversion**: checkout and returns workflow improvements

The repository is intentionally simple: there is no application backend, database, authentication system, or server-side API. The deliverable is the published static proposal and its supporting research, methodology, and pilot model.

## Repository structure

```text
/
├── index.html                # Main proposal
├── methodology.html          # Sourcing standard and figure ledger
├── precedents.html           # Comparable-retailer case studies
├── pilot-program.html        # Phased pilot plan and KPI gates
├── faq.html                  # Status, sourcing, and licensing FAQ
├── license.html              # Human-readable license page
├── 404.html                  # Branded not-found page
├── _headers                  # Cloudflare Pages security headers
├── robots.txt                # Crawler directives
├── sitemap.xml               # Search-engine sitemap
├── LICENSE                   # CC BY 4.0 project license notice
├── SECURITY.md               # Security reporting and scope
├── CONTRIBUTING.md           # Contribution and validation workflow
├── tests/
│   └── validate_site.py      # Dependency-free repository checks
└── .github/
    └── workflows/
        └── validate.yml      # CI for repository validation
```

## Design and implementation

This is a no-build static site. Each HTML document contains its page-specific markup and styling, with shared conventions for navigation, disclosure, typography, responsive behavior, and source labeling.

The visual system uses a black, white, cyan, and red palette with Space Grotesk, Inter, and monospace labels. The design is intentionally editorial and technical rather than imitating an Express brand asset.

## Methodology

Every quantitative claim is assigned one of three confidence tiers:

- **SOURCED**: tied to a named public source
- **MODELED**: calculated from public benchmarks or assumptions
- **DIRECTIONAL**: a reasoned estimate where no clean benchmark is available

The full figure ledger and sourcing rules live in [`methodology.html`](methodology.html). Modeled and directional figures are not Express internal data.

## Security

This repository publishes static content only. It does not store application credentials, process user accounts, or expose a private API.

The deployment includes a Cloudflare Pages `_headers` policy covering common browser hardening controls, including a Content Security Policy, clickjacking protection, MIME sniffing protection, a restrictive permissions policy, and referrer controls.

Third-party resources are intentionally limited to the Google Fonts stylesheet and the SoundCloud reference embed used on the proposal page. See [`SECURITY.md`](SECURITY.md) for scope and reporting guidance.

## Quick start

Clone the repository and open `index.html` in a browser, or serve the directory with any static HTTP server.

Example:

```bash
python -m http.server 8000
```

Then open `http://127.0.0.1:8000/`.

No package manager, build step, or runtime service is required.

## Testing

The repository has a dependency-free validation suite that checks document structure, required disclosures, internal links, fragment targets, required files, sitemap coverage, and common placeholder markers.

Run:

```bash
python tests/validate_site.py
```

GitHub Actions runs the same validation on pushes and pull requests.

## Deployment

The current live URL is a Cloudflare Pages deployment. The repository is already structured as a static publish directory, so no build command is required.

For another static host, publish the repository root as the site output directory. Keep `_headers` when deploying to Cloudflare Pages because that file is interpreted by Pages as response-header configuration.

## Configuration

There are no application secrets or required environment variables.

The external URLs that matter to the site are visible in the HTML and can be reviewed directly:

- Live site canonical URL: `https://project-expresstoration.pages.dev/`
- Creative Commons license: `https://creativecommons.org/licenses/by/4.0/`
- Reference audio embed: SoundCloud

## Usage notes

The “Print / Save as PDF” control uses the browser's print dialog. It does not upload or generate a server-side PDF.

The public site contains third-party references and embeds. Those services remain subject to their own terms and licenses. This repository's CC BY 4.0 grant applies to the project material covered by that license, not to third-party assets.

## Licensing

Unless otherwise noted, project content and original design/code in this repository are published under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

CC BY 4.0 permits reuse, adaptation, and commercial use, provided the required attribution and license notice are retained. It does not mean attribution is optional.

See [`LICENSE`](LICENSE) and [`license.html`](license.html) for the project notice and a plain-language explanation. Third-party fonts, embeds, trademarks, and source materials retain their own applicable rights and licenses.

## Contributing

Corrections are welcome, especially for sourcing, figures, broken links, accessibility, and factual clarity.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting a change. Contributors should update documentation when behavior or published claims change and should run the validation suite before opening a pull request.

## Scope and limitations

This repository is a public strategy proposal, not a consulting engagement, operating plan, investment recommendation, or official corporate communication. It is not based on confidential Express or WHP Global information.

The proposal does not establish that any initiative will produce a particular financial result. Pilot gates and modeled figures are intended for discussion and validation, not as guarantees.

## Status

The site is maintained as a living public research and design artifact. Changes should leave the implementation, documentation, and sourcing disclosures in agreement with each other.
