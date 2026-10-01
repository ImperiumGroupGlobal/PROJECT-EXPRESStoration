#!/usr/bin/env python3
"""Dependency-free checks for the PROJECT EXPRESStoration static site."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))
REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "_headers",
    "robots.txt",
    "sitemap.xml",
    "llms.txt",
]


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.title = False
        self.lang = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "html" and data.get("lang"):
            self.lang = True
        if tag == "title":
            self.title = True
        if "id" in data:
            self.ids.add(data["id"] or "")
        if tag == "a" and data.get("href"):
            self.links.append(data["href"] or "")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    for name in REQUIRED_FILES:
        if not (ROOT / name).exists():
            fail(f"missing required file: {name}")

    if not HTML_FILES:
        fail("no HTML pages found")

    for path in HTML_FILES:
        text = path.read_text(encoding="utf-8")
        parser = DocumentParser()
        parser.feed(text)

        if not parser.title:
            fail(f"{path.name}: missing <title>")
        if not parser.lang:
            fail(f"{path.name}: missing html lang")
        if path.name != "404.html" and "[ UNOFFICIAL ]" not in text:
            fail(f"{path.name}: missing above-the-fold unofficial disclosure")
        if re.search(r"(?i)(lorem ipsum|your name here|coming soon|todo:)", text):
            fail(f"{path.name}: placeholder text detected")

        for href in parser.links:
            if href.startswith(("#", "mailto:", "tel:", "javascript:")):
                if href.startswith("#"):
                    target = href[1:]
                    if target and target not in parser.ids:
                        fail(f"{path.name}: broken fragment #{target}")
                continue

            parsed = urlparse(href)
            if parsed.scheme in {"http", "https"}:
                continue
            if parsed.scheme:
                fail(f"{path.name}: unsupported link scheme {href}")

            target = href.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            target_path = (path.parent / target).resolve()
            if not target_path.exists():
                fail(f"{path.name}: missing internal target {href}")

            if "#" in href:
                fragment = href.split("#", 1)[1]
                target_text = target_path.read_text(encoding="utf-8")
                if f'id="{fragment}"' not in target_text and f"id='{fragment}'" not in target_text:
                    fail(f"{path.name}: broken cross-page fragment {href}")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if "Sitemap: https://project-expresstoration.pages.dev/sitemap.xml" not in robots:
        fail("robots.txt sitemap is missing or incorrect")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for page in ["index.html", "methodology.html", "precedents.html", "pilot-program.html", "faq.html", "license.html"]:
        if page != "index.html" and page not in sitemap:
            fail(f"sitemap.xml missing {page}")

    robots_lines = robots.splitlines()
    if "User-agent: OAI-SearchBot" not in robots_lines or "Allow: /" not in robots_lines:
        fail("robots.txt must allow OAI-SearchBot")
    if "User-agent: PerplexityBot" not in robots_lines:
        fail("robots.txt must declare PerplexityBot access")
    if "Sitemap: https://project-expresstoration.pages.dev/sitemap.xml" not in robots:
        fail("robots.txt sitemap reference is missing")

    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    for required in [
        "https://project-expresstoration.pages.dev/",
        "https://project-expresstoration.pages.dev/methodology.html",
        "https://project-expresstoration.pages.dev/precedents.html",
        "https://project-expresstoration.pages.dev/pilot-program.html",
        "https://project-expresstoration.pages.dev/faq.html",
        "https://project-expresstoration.pages.dev/license.html",
    ]:
        if required not in llms:
            fail(f"llms.txt missing canonical URL: {required}")

    print(f"PASS: validated {len(HTML_FILES)} HTML pages and repository metadata")
    return 0


if __name__ == "__main__":
    sys.exit(main())
