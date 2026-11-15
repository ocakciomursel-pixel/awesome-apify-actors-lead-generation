# Apify B2B Lead Generation Actors Reference (`@lucacelli`)

All Actors below use predictable Pay-Per-Event pricing (`$0.90 / 1,000` records on enrichment & verification tools) and return clean JSON arrays ready for CRM, Clay, or CSV export.

| Actor Slug | Primary Use Case | Required Input |
| :--- | :--- | :--- |
| `lucacelli/google-maps-scraper-places-emails-contacts-reviews` | Local business discovery + website contact extraction | `{"searchStringsArray": ["dental clinic"], "locationQuery": "Miami, FL", "maxCrawledPlacesPerSearch": 25}` |
| `lucacelli/b2b-domain-contact-tech-enricher` | Fast domain -> email, phone, social handles & 38+ tech signatures | `{"domains": ["stripe.com", "linear.app"]}` |
| `lucacelli/master-360-b2b-company-deep-dossier-enricher` | Full 360° B2B dossier (contacts, DNS SPF/DMARC, social, tech stack) | `{"domains": ["supabase.com"]}` |
| `lucacelli/bulk-email-syntax-mx-disposable-role-verifier` | Bulk email syntax, DNS MX & disposable domain verification | `{"emails": ["founders@linear.app"]}` |
| `lucacelli/pixel-tag-manager-ad-spend-signal-detector` | Detect active Meta, Google Ads, TikTok & LinkedIn ad pixels | `{"domains": ["gymshark.com"]}` |
| `lucacelli/calendly-hubspot-booking-funnel-sales-stack-detector` | Detect Calendly, HubSpot, Chili Piper & Intercom sales funnels | `{"domains": ["deel.com"]}` |
| `lucacelli/cold-email-personalization-first-line-icebreaker-miner` | Extract live copy & signals for cold-email first-line icebreakers | `{"domains": ["resend.com"]}` |
| `lucacelli/ats-job-board-hiring-signal-scraper` | Scrape Greenhouse, Lever & Ashby open roles for hiring intent | `{"companySlugs": ["stripe", "linear"]}` |
| `lucacelli/dental-medical-clinic-patient-booking-software-spy` | Identify dental/medical clinics & patient booking platforms | `{"domains": ["aspendental.com"]}` |
| `lucacelli/wordpress-woocommerce-site-spy` | Enrich WordPress & WooCommerce stores with plugins & contacts | `{"domains": ["woocommerce.com"]}` |
