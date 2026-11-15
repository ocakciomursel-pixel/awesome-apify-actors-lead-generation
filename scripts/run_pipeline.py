#!/usr/bin/env python3
"""Zero-dependency Apify B2B Lead Generation & Enrichment runner."""
import argparse
import json
import os
import sys
import urllib.request

ACTORS = {
    "gmaps": "lucacelli~google-maps-scraper-places-emails-contacts-reviews",
    "enrich": "lucacelli~b2b-domain-contact-tech-enricher",
    "dossier": "lucacelli~master-360-b2b-company-deep-dossier-enricher",
    "verify": "lucacelli~bulk-email-syntax-mx-disposable-role-verifier",
    "pixels": "lucacelli~pixel-tag-manager-ad-spend-signal-detector",
    "icebreakers": "lucacelli~cold-email-personalization-first-line-icebreaker-miner",
}


def run_actor_sync(actor_id: str, payload: dict, token: str) -> list:
    url = f"https://api.apify.com/v2/acts/{actor_id}/run-sync-get-dataset-items?token={token}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Apify B2B Lead Generation pipelines")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_gm = sub.add_parser("gmaps", help="Scrape Google Maps leads with contacts")
    p_gm.add_argument("--query", required=True, help="Business search term")
    p_gm.add_argument("--location", default="", help="City/State/Country filter")
    p_gm.add_argument("--limit", type=int, default=20, help="Max results")

    p_en = sub.add_parser("enrich", help="Enrich company domains with emails, phones & tech stack")
    p_en.add_argument("--domains", nargs="+", required=True, help="Company domains")

    p_ve = sub.add_parser("verify", help="Verify bulk emails via syntax & DNS MX")
    p_ve.add_argument("--emails", nargs="+", required=True, help="Email addresses")

    p_px = sub.add_parser("pixels", help="Detect Meta, Google Ads & TikTok ad pixels")
    p_px.add_argument("--domains", nargs="+", required=True, help="Company domains")

    p_ic = sub.add_parser("icebreakers", help="Generate personalized cold-email icebreakers")
    p_ic.add_argument("--domains", nargs="+", required=True, help="Company domains")

    args = parser.parse_args()
    token = os.environ.get("APIFY_TOKEN", "").strip()
    if not token:
        print("Error: APIFY_TOKEN environment variable is required for direct CLI mode.", file=sys.stderr)
        return 1

    if args.cmd == "gmaps":
        payload = {
            "searchStringsArray": [args.query],
            "maxCrawledPlacesPerSearch": args.limit,
            "scrapeContacts": True,
            "scrapeSocialMediaProfiles": True,
        }
        if args.location:
            payload["locationQuery"] = args.location
    elif args.cmd in ("enrich", "pixels", "icebreakers"):
        payload = {"domains": args.domains}
    elif args.cmd == "verify":
        payload = {"emails": args.emails}
    else:
        return 1

    items = run_actor_sync(ACTORS[args.cmd], payload, token)
    print(json.dumps(items, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
