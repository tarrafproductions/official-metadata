# Website integration contract

This document defines how the official TARRAF PRODUCTIONS metadata is used on
the public Vite/React website deployed through Netlify.

The current source-of-truth snapshot is
[`v1.0.0`](https://github.com/tarrafproductions/official-metadata/releases/tag/v1.0.0).
The website must consume a reviewed build-time snapshot pinned to a release tag
or commit; it must not depend on a runtime request to GitHub or silently track
mutable `main` data.

## Stable entity identifiers

These identifiers are language-neutral and must remain unchanged across every
localized page:

| Entity | Stable `@id` |
| --- | --- |
| TARRAF PRODUCTIONS | `https://aliktarraf.com/#tarraf-productions` |
| Alik Tarraf | `https://aliktarraf.com/#alik-tarraf` |
| Marina Tarraf | `https://aliktarraf.com/#marina-tarraf` |
| Epic Evolution Music | `https://aliktarraf.com/#epic-evolution-music` |
| TARRAF LIVE SHOW | `https://aliktarraf.com/#tarraf-live-show` |
| TARRAF PRODUCTIONS LIVE | `https://aliktarraf.com/#tarraf-productions-live` |
| TARRAF EPIC CHOIR | `https://aliktarraf.com/#tarraf-epic-choir` |
| OBARABO | `https://aliktarraf.com/obarabo#obarabo` |

Localized pages may have different canonical URLs, but they must identify the
same entity with the same `@id`.

## Language URL contract

- Existing English URLs remain the default and must not be broken.
- Russian pages use `/ru/`.
- Ukrainian pages use `/uk/`, not `/ua/`.
- Arabic pages use `/ar/` and render with `lang="ar"` and `dir="rtl"`.
- Every localized page has a self-referencing canonical URL.
- Every language variant lists reciprocal `hreflang` links for `en`, `ru`,
  `uk`, and `ar`.
- `x-default` points to the English/default version.
- Language switching changes the URL; it must not only replace client-side text.

Example for one localized route:

```html
<link rel="canonical" href="https://aliktarraf.com/ru/example" />
<link rel="alternate" hreflang="en" href="https://aliktarraf.com/example" />
<link rel="alternate" hreflang="ru" href="https://aliktarraf.com/ru/example" />
<link rel="alternate" hreflang="uk" href="https://aliktarraf.com/uk/example" />
<link rel="alternate" hreflang="ar" href="https://aliktarraf.com/ar/example" />
<link rel="alternate" hreflang="x-default" href="https://aliktarraf.com/example" />
```

Replace `example` with the final route. Canonical and alternate URLs must be
absolute production URLs, not Netlify preview URLs.

## Raw HTML requirements

The following must be present in the server-delivered or pre-rendered HTML,
before React executes:

- the correct `<html lang>` value and Arabic text direction;
- a unique `<title>` and meta description;
- one self-referencing canonical link;
- the complete reciprocal `hreflang` set;
- route-specific Open Graph and Twitter metadata;
- route-relevant JSON-LD in `<script type="application/ld+json">`;
- meaningful visible page content.

Client-side injection alone is not the acceptance criterion. Search engines and
other consumers must be able to read the core identity and metadata without
executing JavaScript.

## JSON-LD rules

1. Reuse the stable `@id` values from this repository.
2. Keep the visible page text and structured claims consistent.
3. Use the localized page URL for `WebPage` or `mainEntityOfPage`; do not create
   a new entity identifier for each language.
4. Include only the graph nodes relevant to the current page.
5. Do not invent dates, venues, participants, awards, or publication status.
6. TARRAF LIVE SHOW remains described as being in active preparation until an
   official public announcement changes that status.
7. Apply metadata changes in this repository first, pass validation, publish a
   versioned release, and then update the website snapshot.

## Vite and Netlify delivery

The production build must pre-render the important entity, project, and release
routes. Generated route files must be deployed before the general SPA fallback
rule. Opening or refreshing any localized URL directly must return its own
pre-rendered HTML with HTTP 200.

The general Netlify fallback may still serve application-only routes, but it
must not replace the pre-rendered entity pages with one shared `index.html`.

## Release gate

Before a production deployment, verify the Netlify Deploy Preview by checking:

1. page source with JavaScript disabled;
2. unique title, description, canonical, `hreflang`, and JSON-LD;
3. Schema.org validation;
4. Google Rich Results Test by URL where the selected schema type is supported;
5. mobile and desktop rendering;
6. direct opening and refresh of every language URL;
7. one unique self-canonical per language page;
8. no fallback-generated duplicate pages or redirect loops.

Only after these checks pass should the production deployment be released and
the canonical URLs submitted for re-indexing in Google Search Console.
