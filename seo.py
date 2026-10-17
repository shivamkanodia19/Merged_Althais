"""
seo.py: robots.txt, sitemap.xml and a noindex header for everything that is not a public marketing page.

The sitemap is built from the pages registered with platform_pages.register (Platform, For Your Practice, Solutions,
Resources, Company, Guides) plus the home page and the two sign-up pages. A page that sets "noindex": True stays out of the
sitemap and is served with a noindex tag. Every other path (the app, the API, sign-in, admin) gets an X-Robots-Tag header.
"""

from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse, Response

import platform_pages

SITE = "https://althais.com"
router = APIRouter()

ALWAYS_PUBLIC = ("/", "/pilot", "/demo", "/legal/privacy", "/legal/terms")
STATIC_PREFIXES = ("/static/", "/videos/")


def _pages():
    return platform_pages.REGISTRY


def public_paths():
    """Paths that may be indexed: the sitemap list."""
    out = list(ALWAYS_PUBLIC)
    out += [href for href, p in _pages().items() if not p.get("noindex")]
    seen, uniq = set(), []
    for h in out:
        if h not in seen:
            seen.add(h)
            uniq.append(h)
    return uniq


@router.get("/robots.txt", include_in_schema=False)
async def robots_txt():
    body = "\n".join([
        "User-agent: *",
        "Allow: /",
        "Disallow: /api/",
        "Disallow: /admin",
        "Disallow: /login",
        "Disallow: /logout",
        "Disallow: /emr",
        "Disallow: /portal",
        "Disallow: /settings",
        "Disallow: /onboarding",
        "Disallow: /invite/",
        "Disallow: /set-password",
        "Disallow: /reset-password",
        "Disallow: /forgot-password",
        "Disallow: /overview",
        "Disallow: /revenue",
        "Disallow: /practice",
        "Disallow: /team",
        "Disallow: /manager",
        "Disallow: /clinic-admin",
        "Disallow: /no-access",
        "",
        f"Sitemap: {SITE}/sitemap.xml",
        "",
    ])
    return PlainTextResponse(body)


@router.get("/sitemap.xml", include_in_schema=False)
async def sitemap_xml():
    urls = "".join(f"  <url><loc>{SITE}{p if p != '/' else '/'}</loc></url>\n" for p in public_paths())
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    return Response(content=xml, media_type="application/xml")


async def robots_header(request: Request, call_next):
    """Ask search engines not to index anything that is not a public marketing page."""
    response = await call_next(request)
    path = request.url.path
    if path in ("/robots.txt", "/sitemap.xml") or path.startswith(STATIC_PREFIXES):
        return response
    page = _pages().get(path)
    if path in ALWAYS_PUBLIC or (page is not None and not page.get("noindex")):
        return response
    response.headers["X-Robots-Tag"] = "noindex, nofollow"
    return response
