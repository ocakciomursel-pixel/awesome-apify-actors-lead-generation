---
name: apify-b2b-lead-generation
description: Extract verified Google Maps business leads, enrich B2B company domains with emails/phones/38+ tech stack signatures, verify bulk email deliverability via DNS MX/SPF/DMARC, spy on Meta/Google/TikTok ad pixels, and generate personalized cold outreach icebreakers using Apify Cloud Actors.
version: 1.0.0
category: sales-lead-gen
tags:
  - apify
  - lead-generation
  - b2b-sales
  - google-maps-scraper
  - email-verification
  - competitive-intelligence
license: MIT
---

# Apify B2B Lead Generation, Enrichment & Outbound Intelligence

Use this skill whenever the user needs to build targeted B2B lead lists, scrape local businesses from Google Maps, enrich company domains with verified decision-maker/role emails and phone numbers, validate bulk email deliverability (MX, SPF, DMARC, disposable traps), audit competitor ad spend pixels, or generate personalized cold-email icebreakers.

## Capabilities & Chained Workflows

1. **Local Business Lead Discovery (`lucacelli/google-maps-scraper-places-emails-contacts-reviews`)**
   - Extract business names, websites, verified emails, phone numbers, ratings, review counts, and social handles (LinkedIn, Instagram, Facebook, X) for any niche + city/state query.
2. **360° B2B Domain Enrichment (`lucacelli/b2b-domain-contact-tech-enricher` & `lucacelli/master-360-b2b-company-deep-dossier-enricher`)**
   - Enrich raw company domains with verified contact emails, phone numbers, social links, DNS MX/SPF/DMARC posture, and 38+ SaaS/CRM/analytics tech stack signatures (`$0.90 / 1,000` records).
3. **Bulk Email Hygiene & Deliverability (`lucacelli/bulk-email-syntax-mx-disposable-role-verifier`)**
   - Filter out invalid syntax, dead MX domains, disposable inboxes, and high-bounce traps before launching cold email sequences.
4. **Paid-Media & Funnel Qualification (`lucacelli/pixel-tag-manager-ad-spend-signal-detector` & `lucacelli/calendly-hubspot-booking-funnel-sales-stack-detector`)**
   - Identify companies actively spending on Meta Pixel, Google Ads, TikTok Pixel, or LinkedIn Insight Tag, and detect embedded Calendly, HubSpot, Chili Piper, or Intercom funnels.
5. **Cold Outreach Personalization (`lucacelli/cold-email-personalization-first-line-icebreaker-miner`)**
   - Extract live homepage value propositions, case studies, and hiring signals to draft natural, non-generic first-line icebreakers.

## Execution Modes

### Mode A: Via Agensi Managed Apify Tool / Apify MCP Server (Zero Setup)
When running inside an Agensi-connected agent or with the Apify MCP tool active, invoke the Actor directly by ID:
- `lucacelli/google-maps-scraper-places-emails-contacts-reviews` — `{"searchStringsArray": ["medspa", "dental clinic"], "locationQuery": "Austin, TX", "maxCrawledPlacesPerSearch": 25, "scrapeContacts": true}`
- `lucacelli/b2b-domain-contact-tech-enricher` — `{"domains": ["stripe.com", "linear.app", "resend.com"]}`
- `lucacelli/bulk-email-syntax-mx-disposable-role-verifier` — `{"emails": ["hello@vercel.com", "sales@supabase.com"]}`
- `lucacelli/pixel-tag-manager-ad-spend-signal-detector` — `{"domains": ["gymshark.com", "allbirds.com"]}`
- `lucacelli/cold-email-personalization-first-line-icebreaker-miner` — `{"domains": ["linear.app", "posthog.com"]}`

### Mode B: Via Bundled Python Script (`scripts/run_pipeline.py`)
If `APIFY_TOKEN` is set in the environment, run the zero-dependency Python helper in `scripts/run_pipeline.py`:
```bash
python scripts/run_pipeline.py enrich --domains stripe.com linear.app
python scripts/run_pipeline.py gmaps --query "roofing contractor" --location "Dallas, TX" --limit 25
python scripts/run_pipeline.py verify --emails founders@linear.app info@stripe.com
```

## Output Standards
- Always deduplicate leads by normalized root domain before enrichment so the user never pays twice for the same company.
- Always verify extracted emails with `bulk-email-syntax-mx-disposable-role-verifier` before exporting outreach-ready CSV/JSON tables.
- Present results in a clean table with: `Company`, `Domain`, `Verified Email`, `Phone`, `MX Valid`, `Tech Stack / Ad Pixels`, and `Suggested Icebreaker`.
- Consult `reference/actors_catalog.md` for full input/output schemas across 20+ vertical B2B scrapers.
