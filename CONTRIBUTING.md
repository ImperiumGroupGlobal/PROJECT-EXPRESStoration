# Contributing

Thanks for helping improve PROJECT EXPRESStoration.

## Before you change anything

Keep the project aligned with these rules:

- Preserve the above-the-fold unofficial disclosure.
- Do not make the project appear to be an official Express or WHP Global document.
- Label quantitative claims as SOURCED, MODELED, or DIRECTIONAL and update the methodology ledger when needed.
- Do not add confidential, leaked, or non-public company information.
- Keep internal links working and add new pages to the sitemap.
- Preserve keyboard accessibility and reduced-motion behavior.
- Do not add secrets, tracking scripts, or unnecessary third-party dependencies.
- Do not claim functionality the static site does not actually provide.

## Validation

Run:

```bash
python tests/validate_site.py
```

The check is dependency-free and should pass before a pull request is opened.

## Content changes

If a change alters a published figure, source, methodology rule, legal disclosure, or licensing statement, update the related documentation at the same time.

## Style

Keep the existing editorial direction: high-contrast, technical, restrained, and boardroom-oriented. Avoid unnecessary visual effects that reduce readability or performance.

## Pull requests

Describe:

1. What changed
2. Why it changed
3. Any figures or sources affected
4. How you validated the change

Small, focused pull requests are preferred.
