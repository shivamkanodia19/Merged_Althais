# Althais go-to-market and SEO strategy

Written October 2026 from a multi-agent research pass (61 research agents plus a 15-agent SERP and sales re-run). Read the evidence notes first: some inputs are strong, some are missing, and the numbers that are assumptions are labeled as such.

## Evidence quality

- **Solid:** the audit of what the product does and does not do today; segment definitions and counts from CMS/KFF; channel mechanics (NRHA, state offices, NARHC, public lead lists); what actually ranks today for ten provider-side denied-claim searches (observed in live results).
- **Thin:** sales benchmarks (CAC, ACV, pilot-to-paid for small practices were not found); competitor pricing (mostly search snippets); rural-specific denial rates (none found from a credible source).
- **Missing:** keyword volumes (no keyword tool is connected; use Google Search Console and Keyword Planner), customer interviews, any measured clinic outcome.
- The first research pass ran out of its shared web-search allowance before the SEO and sales phases. Those were re-run with a per-agent cap; the SERP results below come from that re-run.

## 1. What Althais is today (ground truth)

Real: dictate or type a visit and get a SOAP note; ICD-10 and CPT suggestions with confidence scores; a bundling check on about 62 hand-picked NCCI pairs; appeal letters drafted from denial text a user pastes in; every claim held for a person to approve.

Not real yet: no payer or clearinghouse connection (claims are never sent), no automatic denial intake (staff mark denials by hand, stored in the browser only), no EHR integrations, no RHC or CAH-specific billing logic, no recovered-dollar tracking, no measured customer results, no SOC 2.

Everything below is built to sell what exists, and to say so plainly.

## 2. Who to sell to first

**Primary:** Owner-operated or small-group rural primary care practices (1 to 5 providers) that own their billing, including direct primary care and independent clinics, with an administrator or office manager doing coding, claim checks and appeals themselves. Include independent (freestanding) Rural Health Clinics only as a generic 'rural clinic' buyer, with no RHC-specific claims, because RHCs are the most countable rural buyer list (about 5,461 enrolled per CMS data via KFF, Q4 2025).

**Why first:** Best fit with what is real today: SOAP note, ICD-10/CPT suggestions, a 62-pair bundling check, appeal letters from pasted denial text, and human approval on every claim. Standalone copy/paste works with any EHR, which matters because there are no integrations. These buyers decide fast (owner or administrator signs), have thin margins and small staff (Experian 2025: 43% understaffed; 90% of denials get manual rework), and most denials are never appealed, so appeal-drafting time is a believable pain. Hospital-employed clinics (about 75% of rural physicians) and CAHs need EHR/clearinghouse/835 integration, security paperwork and RHC/CAH logic the product lacks, so they would stall in procurement. The sale is a low-risk, time-boxed pilot where the clinic measures its own baseline, not a platform contract.

**Buyer titles:** Practice administrator / office manager; Owner or lead physician (small independent practice); Billing lead / biller / coder; Clinic director (independent or freestanding RHC)

**Triggers:**
- Rising denials or a backlog of unappealed denials; staff stretched thin
- A payer edit or code-set change hitting claims (annual CPT/ICD-10 updates, quarterly NCCI updates, CMS 2026 fee schedule changes)
- Losing a biller or coder, or considering outsourcing billing at 4 to 10% of collections (vendor-stated figure)
- Physician documentation burden and evening charting
- Medicaid or payer-mix pressure from H.R. 1 changes starting 2027 (context, not a promise)

**Size of the prize (honest):** Honestly unquantified. Countable targets: about 5,461 Medicare-certified RHCs (CMS enrollment via KFF) plus an unsized number of 1-to-5-provider rural independents; independents are shrinking (rural independent physicians down 43% 2019 to 2024, advocacy-sourced). Assumption-only software TAM for RHCs is roughly 16M to 82M dollars per year at 3k to 15k per clinic, and the per-clinic spend is unverified. Treat this as a niche beachhead of low tens of millions at best, so success means 10 to 25 paying clinics in year one, not market domination. No rural denial rate or willingness-to-pay figure exists; validate with 10 to 15 administrator interviews.

**Secondary segments (later):**
- Provider-based RHCs and clinics attached to Critical Access Hospitals (about 1,386 CAHs as of Oct 2026), selling to billing leads or the CFO. When: After a consented pilot with measured results, a BAA process, and either EHR-agnostic workflow proof or a real clearinghouse/835 path. Do not claim RHC/CAH billing logic until it is built and verified.
- FQHCs and community health centers (32.7M patients in 2025; Medicaid managed care denials, with about one third of Medicaid appeals overturned per KFF). When: After Medicaid-managed-care payer logic exists and written confirmation that software is an allowable grant cost. Longer cycles and board approval.
- Rural urgent care and freestanding ER operators (Texas/Arizona interest in the repo). When: After the independent-practice pilot proves the E/M and bundling value; they have higher claim volume but no verified rural data and different coding needs.
- State-level channels: state rural health offices and associations, NARHC/NRHA events, Rural Health Transformation Program subawardees. When: In parallel as distribution, not as a buyer. Ask each state in writing whether denial/revenue-cycle software is allowable; do not imply RHTP money pays for Althais. Register on SAM.gov and get a UEI now.
- Medical billers and small outsourced billing shops serving rural clinics. When: Once the appeal-letter workflow is proven; they multiply reach per sale, but they are a different persona and pricing model.

**Avoid for now:**
- Hospital systems and large multi-specialty groups: they need EHR/clearinghouse integration, SOC 2, and a signed BAA, and the old case studies for them are unsourced and must come down.
- CAH-wide or hospital CFO enterprise deals: no RHC/CAH logic, no recovered-dollar tracking, no verified outcomes to put in front of a CFO.
- Anyone who needs claim transmission, payer connectivity, 835/277 denial ingestion or EHR integration to buy.
- Prior-authorization-heavy buyers (post-acute, Medicare Advantage-centered): the product has no prior-auth tracking.
- Grant-funded purchases via HRSA, USDA or Flex: allowability of billing software is unverified.
- Any outreach that names the former pilot or design-partner organizations: no documented consent.

**Messaging by persona:**
- **Practice administrator / office manager.** Catch common claim mistakes before you file, and get a draft appeal letter in minutes from the denial text you paste in. A person on your team approves everything. Honest scope: we check a starting set of about 62 common bundling pairs, we do not send claims for you yet, and you enter denials by hand. Try a 30-day pilot where you measure your own denials and appeal time before and after.
- **Owner / lead physician.** Dictate the visit, get a SOAP note and suggested ICD-10/CPT codes with confidence levels, and nothing is filed until you or your staff approve it. It works alongside your current EHR by copy and paste, with no integration project. We will not promise recovered dollars; we will help you measure yours.
- **Billing lead / coder.** A fast second set of eyes on code pairs before submission, and appeal drafts you edit instead of write from scratch. Clear limits: curated NCCI pair list (not the full CMS file), human sign-off on every claim, denials logged manually. Your judgment stays in charge; the tool saves typing and misses.
- **Clinic director / CFO of a small rural org (secondary).** A low-risk pilot with success metrics agreed in advance and only observed numbers reported. Market context (11.65% initial denial rate in Kodiak 2025 data, most denials never appealed) is shown as industry background, not as our results. We are early, and we will say exactly what is and is not built.
- **Search visitor (insurance claims savings / denied claim appeal).** Lead with the page H1 naming denied claims and rural/small clinics, then show the actual workflow and a plain Today / Not yet list above the fold, one primary CTA (Join the Pilot or a de-identified sample review), and sourced industry context only. No savings percentages, no customer logos, no testimonials until consented.

## 3. How to reach them (channel ranking)

Scores are the strategist's judgment, not measurements.

- **1. Own-site conversion and SEO fix (honest rewrite of title/H1/meta for denied-claim appeals, free appeal-draft sample, fix forms)** (score 9.5). Cost: $0 cash; founder time, about 2 to 3 weeks. First lead: 2 to 8 weeks for organic; immediate for outbound traffic landing on it. First action: Remove unbacked claims (clearinghouse, 65% recovery, case-study numbers/quotes, old pilot names without written consent, 'follow to payment'), fix demo.html lines 51-52, then rewrite title/H1/meta to name denied claims, appeals and small rural clinics. Add canonical tags, a sitemap and robots.txt. Add honeypot/Turnstile, validation and qualification fields (clinic type, state, EHR, monthly claims) to /request-demo and /request-pilot, and route leads to a sheet or CRM.
- **2. Targeted cold outbound to independent rural clinics and CAH-affiliated RHCs (email plus phone) from CMS/HRSA public lists** (score 9). Cost: $0 to $200 per month (domain, sending tool, a verification tool). First lead: 1 to 3 weeks. First action: Download the CMS RHC Enrollments CSV, join NPPES on NPI, and add HRSA Data Explorer and state RHC directories (Wisconsin, Illinois) for phone numbers. Choose 2 or 3 expansion states. Send 50 to 100 compliant emails per week with a no-cost 30-day pilot offer.
- **3. Free tools as lead magnets (CARC/RARC denial code lookup, 'what the 62-pair bundling check covers', appeal draft from pasted denial text, labeled-assumption denial cost calculator)** (score 8.5). Cost: $0 cash; mostly engineering and writing time. First lead: 4 to 10 weeks. First action: Ship a free CARC/RARC lookup page sourced to X12 lists and link it to the real appeal generator. Add a clearly labeled illustrative calculator with visible assumptions instead of the hard-coded 65% recovery.
- **4. Free educational and webinar channels (NARHC RHC technical-assistance webinars, RHIhub Suggest-an-Event, state ORH newsletters)** (score 7.5). Cost: $0. First lead: 3 to 8 weeks. First action: Attend NARHC's Oct 29 2026 webinar 'AI in Rural Health Without the Hype' as a participant to learn buyer language. Submit a speaker/webinar topic through RHIhub on claims prep and appeal drafting with human approval. Contact the NARHC membership line (866-306-1961) about 2027 vendor options.
- **5. Design-partner pilot program with written consent (3 to 5 clinics) that produces consented, measured baselines and later case studies** (score 7.5). Cost: $0 cash; free or discounted pilot plus founder time. First lead: Conversion of first pilots takes 4 to 8 weeks from first call. First action: Write a one-page pilot agreement: 30-day pilot, clinic measures its own denials and appeal time before and after, explicit written consent clause for naming the clinic and quoting results. Offer it in every outbound message and every demo.
- **6. Partners: rural billing consultants/firms, CAH Flex-program coordinators (State Offices of Rural Health), state RHTP offices** (score 6.5). Cost: $0 to low. First lead: 6 to 16 weeks. First action: Email 10 State Offices of Rural Health and 5 rural billing consultants offering a free denial-appeal tool for their clients. Ask each RHTP office in writing whether denial-management software is an eligible technology category, and save written answers. Register on SAM.gov for a UEI. Do not claim that RHTP, Flex or USDA funds will pay for Althais.
- **7. State association and conference presence (SDAHO, Nebraska, Ohio AFP, NRHA May 2027 and Sept 2027 RHC conference)** (score 5). Cost: $500 to $1,000 per state booth; $3,500 per year NRHA supporting membership; sponsorships $1,500 to $10,000. First lead: 6 to 9 months (all 2026 events are past). First action: Email SDAHO, the Nebraska association, NRHA (Larry Bedell for publications; membership line) for 2027 prospectuses. Do not book anything until attendee lists confirm clinic administrators and until at least 2 consented pilots exist.
- **8. Paid search test (tightly capped, exact-match denied-claim and appeal queries)** (score 4.5). Cost: $300 to $600 per month cap; benchmark CPC roughly $2 to $7 is unverified. First lead: 1 to 3 weeks after tracking is live. First action: Wait until Search Console, conversion events and qualification fields are live, and pull Keyword Planner volumes. Then test 3 to 5 exact-match phrases at $10 to $20 per day for 30 days and stop if cost per qualified lead exceeds a pre-set cap.
- **9. EHR marketplaces (NextGen, athenahealth, eClinicalWorks)** (score 2). Cost: Unpublished fees; engineering time. First lead: 6 to 12 months or more. First action: Defer. Althais has no EHR integration and the fee and review terms are unpublished or unverified. Revisit only after paying customers ask for it.
- **10. RCM-vendor-style national events and sponsorships (MGMA national, HFMA national, AAFP FMX at $45,000 solution sessions)** (score 1.5). Cost: Prohibitive for a tiny team; prices gated. First lead: 9 to 12 months or more. First action: Do not spend. Request prospectuses for information only, and consider a local HFMA chapter sponsorship (about $2,000 to $4,750) later, if at all.

### 90-day plan

**Weeks 1-2: Make the site and the offer safe to send traffic to**
- Pull all unbacked claims from live pages: clearinghouse and EHR connections, 'follow it to payment' (demo.html lines 51-52), the 65% recovery calculator, '30 to 60 days live', SOC 2 wording, prior-auth, API and payer-intelligence features, the case-study numbers and quotes, and the old pilot and design-partner names (no documented consent). Say '62 common NCCI pairs, not the full CMS file'.
- Note that templates/pricing.html, resources.html, solutions.html and contact.html are orphaned. Edit the live sources in practice_pages.py, more_pages.py and marketing_data.py instead.
- Add a plain 'what Althais does and does not do' section: claims never transmitted, a person approves every claim, denials entered by hand, no payer connection.
- Rewrite titles, H1s and metas for the landing, pricing, demo and pilot pages around denied claims, appeal letters and small rural clinics. Do not use an 'insurance claims savings' headline promise. Instead, answer that query on the page with the real workflow and an honest scope.
- Add canonical tags, sitemap.xml and robots.txt, and Open Graph tags. Move /pilot and /demo onto self-canonical pages.
- Harden /request-demo and /request-pilot: validation, honeypot or Turnstile, rate limit, no confirmation email to unverified addresses, and a check that RESEND_API_KEY works in production. Move the notification address to a config variable and add an admin view or export of leads.
- Add qualification fields: clinic type, state, EHR, monthly claims, billing staff count.
- Install Search Console and conversion events. Pull Keyword Planner volumes for the target phrases (no volume data exists yet).
- Register on SAM.gov for a UEI. Draft the one-page 30-day pilot agreement with a written consent clause, and have counsel review it.

**Weeks 3-4: Build the list and start a small outbound test**
- Build the first list of 200 clinics in 2 or 3 expansion states from the CMS RHC Enrollments CSV, NPPES, HRSA Data Explorer and state directories. Enrich contacts by hand.
- Send the first 50 to 100 compliant emails per week, with phone follow-up where a public number exists, using the sequence below.
- Publish the free CARC/RARC lookup page (sourced to X12 lists) with a link to the appeal generator, and a 'denied claim appeal letter for small clinics' page with a free sample draft from pasted denial text.
- Interview 10 to 15 clinic administrators (these are calls, not sales) to validate buyer, budget owner, billing staffing, denial mix and whether software is allowable under grants.
- Attend the NARHC webinar on Oct 29 2026 as a participant. Submit a topic suggestion to RHIhub. Call NARHC about 2027 vendor options.

**Weeks 5-8: Run the first pilots and publish what is real**
- Sign 2 to 3 design-partner pilots under the written agreement. Record each clinic's own baseline (denial count, appeals filed, staff minutes per appeal) before turning anything on.
- Sit with each pilot weekly. Log every place the product breaks (manual denial entry, bundling check coverage gaps) and tell the clinic plainly.
- Continue outbound at 50 to 100 emails per week and tune the subject lines and offer from reply data.
- Publish 3 to 4 real, sourced articles whose bodies exist (CMS 2026 fee schedule, RHC telehealth HCPCS change effective Oct 1 2026, G0511/G0512 retirement and care-management codes, bundling edits) with primary-source links. Label them as education unless the product checks the item. Do not claim RHC-specific logic.
- Email State Offices of Rural Health and 5 rural billing consultants about a partnership. Send the written RHTP eligibility question to the target states.
- Request 2027 prospectuses from NRHA, SDAHO and the Nebraska association (information only).

**Weeks 9-13: Convert, prove and decide where to double down**
- Close out pilots with a short results sheet built from the clinic's own measured numbers, and ask for written permission to name them and quote them. Only then publish a case study, and only with measured and consented numbers.
- Convert pilots to paid with a simple starting price (publish a pilot price or range on the pricing page, and fix the Starter/Professional/Enterprise tier lists so they match the product).
- Expand outbound to 3 to 5 more states using whatever worked (state, ownership type, subject line). Add the CAH-affiliated RHC segment only if buyer interviews confirm interest.
- If tracking is live and the pages convert, run the capped paid search test ($300 to $600 for the month) on exact-match denied-claim and appeal queries.
- Decide on 2027 events with real data: book only a low-cost state event that confirmed clinic administrators attend, and only if there is a consented reference.
- Review the 90 days against the metrics and drop the weakest channel.

### Outbound sequence

- Targeting: administrator, billing lead, office manager or owner physician at independent rural clinics and RHCs (including CAH-affiliated ones) in 2 or 3 expansion states. 5 touches over about 21 days, stopping at any reply or opt-out.
- Day 1, email 1 (plain text, under 90 words). Subject: 'Denied claim appeals at [Clinic name]?' Body: one line of context (Experian 2025: 41% of providers report denial rates of 10%+ ... cite year and survey), then what Althais really does: you paste in a denial, it drafts the appeal letter; it also checks a coded visit against about 62 common NCCI bundling pairs; a person approves everything. Say: 'No payer connection, claims are not transmitted.' Offer: a free 30-day pilot where you measure your own denials and staff time before and after. Include physical postal address and an opt-out line.
- Day 4, email 2 (short, new angle). Offer a free sample: 'Send me one denial text (remove patient names) and I'll send back the drafted appeal.' Do not ask for PHI. Tell them to strip identifiers.
- Day 8, phone call where a public number exists (business landline; check do-not-call rules; no prerecorded or autodialed calls). Script: 'Quick question about how your office handles denied claims and appeals. Who does that?' Aim for the right contact and a 15-minute call, not a pitch. Leave no unrequested voicemail promises.
- Day 13, email 3. Hook on a verified, dated rule change relevant to the segment (for example, RHC telehealth billing must use individual codes instead of G2025 from Oct 1 2026), cite the CMS/MAC source, and say plainly that Althais does not check RHC-specific codes. Link the free CARC/RARC lookup page.
- Day 21, break-up email. 'Closing the loop. If appeals are not a priority, no problem. The free sample offer stands.' Remove the contact on any opt-out within 10 business days (do it immediately).
- Rules for every touch: accurate headers, no deceptive subject lines, no fake 'Re:', no recovered-dollar claims, no named customers, no testimonials, no 'AI will fix your denials' language. Log all replies and objections in the sheet and review weekly. Treat vendor reply-rate benchmarks (1.6% to 9.8%) as unreliable and use your own numbers by day 60.

### Lead list from public data

Build the list entirely from public data, in this order.

1. Core file. Download the CMS RHC Enrollments CSV from data.cms.gov (updated 2026-07-27). It has legal name, DBA, organization type, address and a 10-digit NPI. Optionally add the CMS RHC All Owners file (ownership name and type, from PECOS) to split hospital-owned from freestanding clinics. Use about 5,461 enrolled RHCs as the working denominator, dated Q4 2025 (KFF/CMS). Note that other sources say 5,600 or more, so state the date wherever you quote the count.
2. Enrichment. Join the NPPES monthly full file (dated 2026-10-12) on NPI for practice location and taxonomy. NPPES does not give administrator names.
3. Phones and directories. Use HRSA Data Explorer (Health Care Facilities, Site Category = Rural Health Clinic, filtered by state) and state directories that list phones (Wisconsin DHS RHC directory, Illinois IDPH Rural Health Care Center Directory, which may be dated). Check the CMS Provider of Services file on data.cms.gov for the current download URL.
4. Segments. Tag each row by state, Medicaid expansion status (the Chartis data shows 34.9% of rural hospitals in the red in expansion states versus 52.2% in non-expansion states, so start with expansion states for willingness to pay), and ownership type. Treat CAH-affiliated provider-based RHCs as a separate segment and use the RHIhub state profiles for state counts (for example, Minnesota has 76 CAHs and 106 RHCs). Treat independent rural practices and rural direct primary care practices as a secondary segment, because hospital-employed clinics are out of scope.
5. Named contacts. Public CMS and NPPES files do not name administrators. Fill contacts by hand from clinic websites, state association member pages and public listings, and start with the first 200 clinics in 2 or 3 states. Use role inboxes only where they are publicly listed. Do not use any list that did not come from public sources.
6. Compliance. CAN-SPAM applies to B2B email (accurate headers, ad disclosure, a physical postal address, a working opt-out honored within 10 business days). Do not send unsolicited fax ads. Do not use prerecorded or autodialed calls without written consent. Check state rules before calling, and keep a suppression list.
7. Tracking. Log source, state, ownership type, touches and replies for every row in a sheet or CRM from day one.

### Funding angle

Do not sell Althais as something that Rural Health Transformation, Flex or USDA money pays for. No source confirms that revenue-cycle or denial software is an allowable use. RHTP funds reach vendors only through state subawards and procurements, and provider payments can be capped (Oregon, for example, caps them at 15%). Use funding as context and as a research channel. (1) Register on SAM.gov and get a UEI, since state vendor forms such as Montana's require it. (2) Ask each target state's RHTP office in writing whether denial management or revenue-cycle software fits a technology category, and use any answer in sales material only if the state confirms it in writing. (3) Track state procurement portals (Montana eMACS, Maryland and Idaho subaward postings, RHIhub vendor directories). A directory listing is not an endorsement and must not be described as one. (4) Treat Flex awards as small, state-specific line items (North Dakota allows chargemaster and revenue-cycle work, with a $2,500 ceiling and about 4 awards, deadline Oct 30 2026), and verify each state's rules before mentioning them. (5) Position the pilot as low-cost with pre-agreed metrics, because rural margins are thin (median about 2.0% in 2025, with 41.2% of rural hospitals in the red). HRSA FQHC grant funds are program funds, not vendor purchases. Confirm software is an allowable cost before pitching grant-funded budgets.

### Metrics to track

- Clinics on the target list by state and ownership type (CMS RHC Enrollments is the denominator, with its date)
- Emails sent, delivered, opened, replied and positive replies (replace vendor benchmarks of 1.6% to 9.8% reply with Althais's own numbers by day 60)
- Discovery calls booked and held per week
- Pilot offers made, pilots signed (with written consent), and pilots completed
- Per pilot: baseline and post-pilot denial count, appeals drafted, and staff minutes per appeal, as measured by the clinic. Never report recovered dollars, because the product does not track them.
- Pilot-to-paid conversion and price accepted
- Website: organic impressions, clicks and average position in Search Console for denied-claim, appeal-letter and bundling-edit queries
- Website: visits to demo/pilot conversion rate, share of leads that are rural or small-clinic (using the new qualification fields), and spam or junk submission rate
- Lead response time (the pilot page promises one business day, so measure it)
- Cost per qualified lead for any paid test, against a cap set in advance
- Number of consented, citable customer statements

## 4. Sales, pricing and revenue

**First offer:** A 30-day "Denial Appeal Workflow Pilot" for independent rural practices and RHC/CAH-affiliated practices with 1-5 providers. Scope is only what the product does today: (1) clinic uploads or pastes 10-25 of its own past denial letters (de-identified, or under a signed BAA before any PHI); (2) Althais drafts appeal letters, a human on the clinic staff reviews and approves each one, and the clinic's own staff time per appeal is logged before and after; (3) optionally run the clinic's real pre-filing visits through SOAP/ICD-10/CPT suggestions and the 62-pair bundling check, described as a limited starter check with a visible last-updated date. Success is pre-agreed in writing and measured by the clinic: minutes per appeal draft, count of denials worked, count of appeals sent. No promised recovered dollars, no claim transmission, no payer connection, no denial auto-detection (staff enter denials by hand), no RHC/CAH-specific logic. Written consent is required for any later use of results or the clinic's name. Run 3-5 design-partner pilots first, founder-led, before any broad sale.

**Pricing hypothesis:** Flat monthly per-clinic subscription (tiered loosely by provider count), with a low fixed-fee 30-day paid pilot credited toward the first month. No percent-of-recovered-dollars or contingency fee, no per-claim fee tied to payer payment, and no money-back guarantee tied to recovered dollars. Optional refund only for objective product failure (e.g., the tool does not produce a SOAP note or appeal draft).  
Starting range: HYPOTHESIS TO TEST, not sourced: pilot about $0-$500 flat for 30 days (free for the first 3 design partners in exchange for documented consent and metrics access); subscription about $199-$499 per clinic per month, i.e. roughly $2,400-$6,000 per clinic per year. This sits inside the low-thousands ACV assumption from the unit-economics note and the $3k-$15k per clinic per year market-sizing assumption, neither of which was verified against competitor pricing. No competitor, billing-service, or AI-coding price benchmark was retrieved. Replace with pilot data and 10-15 administrator interviews before publishing any price.  
Why: Pricing benchmarks were not obtained, so price must be tested, not asserted. A flat fee is the safest structure because the product has no recovered-dollar tracking, no 835/277 ingestion, and cannot measure outcomes; rural margins are thin (Chartis: median rural hospital operating margin about 2.0% in 2025, 41.2% in the red), so buyers need a small, fast-payback commitment. Publishing a visible starting price on the pricing page is recommended once validated, because the current page shows no price at all.  
Needs counsel: Yes, before launch. Counsel should review (a) the Anti-Kickback and False Claims Act exposure of any fee tied to clinic billing volume, (b) whether any percentage-of-collections arrangement is restricted for Medicare billing (unverified in research), (c) state fee-splitting and billing-company licensing rules, (d) the wording and scope of the free pilot/audit, and (e) HIPAA BAA terms and the de-identification route (Safe Harbor vs expert determination; HHS pages were not retrieved). Do not launch any contingency pricing until counsel signs off.

Observed price points from the re-run (search snippets, unverified): AdvancedMD from about $130 per provider per month; DenialMD from $49.99 per month (single user) to $359.95 per user per month; outsourced billing commonly quoted at about 4 to 8 percent of collections. Percentage-of-collections pricing also raises Medicare reassignment questions (42 CFR 424.80) that counsel must review before use.

**Competitor free-audit norm:** OmniMD and others offer a free audit that asks for no PHI and offers a BAA on request. A de-identified sample review matches that norm.

**Sales process:**
- 0. Pre-work (this week): fix the must-fix items below, get counsel on pricing/pilot wording, draft a BAA and a one-page security/data-handling sheet that states honestly what exists (no SOC 2 claim), register on SAM.gov and obtain a UEI (state RHTP vendor forms require it).
- 1. Build a list of 100-150 targets: independent rural practices, RHCs (about 5,461 Medicare-certified per KFF/CMS data) and small CAH-affiliated clinics (about 1,377 CAHs). Prioritize Medicaid-expansion states first (34.9% of rural hospitals in the red vs 52.2% in non-expansion states, per Chartis), as an untested proxy for willingness to pay.
- 2. Founder-led outreach to administrators, office managers, billing leads and owner physicians via email/phone, state rural health associations, and NRHA events (confirm 2027 dates). Message: staff time on denial appeals and a limited pre-filing check, human approves everything. No dollar-savings or percentage claims.
- 3. 20-minute discovery call: pull the clinic's own monthly claim count, denials per month, how denials are tracked, who writes appeals, hours per appeal, EHR, payer mix. This replaces the missing market benchmarks with the prospect's real numbers. Add qualification fields (clinic type, state, EHR, monthly claims) to the demo/pilot forms.
- 4. Demo using a fictional or de-identified denial letter showing paste-in to appeal draft to human approval; state plainly what is not built (no claim transmission, no automatic denial intake, bundling check covers about 62 pairs, no RHC/CAH logic).
- 5. Pilot agreement: 1-page scope, BAA signed before any PHI, success metrics agreed in writing (minutes per appeal, appeals drafted and sent, staff satisfaction), consent clause for using results and name. 30 days.
- 6. Weekly 15-minute check-in; staff log minutes per appeal before vs after; the clinic computes its own results. Do not compute or claim recovered dollars.
- 7. Day 25-30 readout from the clinic's own logs; convert to flat monthly subscription, credit pilot fee; ask for written testimonial and consent only if results are positive.
- 8. Parallel channel work: write to each target state RHTP office asking whether denial-management/appeal software qualifies under a technology category; track state procurement portals (e.g., Montana eMACS, Maryland and Idaho subaward postings). Never state that RHTP, Flex or USDA money pays for Althais unless a state confirms in writing.
- 9. Gate to scale: only after 3+ consented pilots show measured results and the hand-entered denial workflow is durable (server-side, not localStorage) do you expand outreach, paid search, or sell to CFO/board buyers.

**Objections:**
- **Does it send claims to payers / connect to our clearinghouse or EHR?** No. Today Althais does not transmit claims, connect to a clearinghouse or payer, or integrate with EHRs. It drafts notes, suggests ICD-10/CPT codes, runs a limited bundling check, and drafts appeal letters from denial text you paste in. Every claim is held for a person to approve. Say this up front; it is the honest scope of the pilot.
- **How much money will we get back?** We will not promise a dollar figure; the product has no recovered-dollar tracking and we have no verified customer outcomes yet. What we can measure together in 30 days is staff minutes per appeal and how many denials you actually work. Public context: KFF found fewer than 1% of marketplace denials were appealed and, among Medicare Advantage prior-auth denials that were appealed, a large majority were overturned (80.7% in 2024). That is industry context, not an Althais result.
- **Is it HIPAA compliant / are you SOC 2?** We are not SOC 2 certified and will not say we are. We will sign a BAA before any PHI is loaded (pending counsel-reviewed terms), provide a written data-handling summary, and can run the pilot on de-identified letters first. Do not claim encryption-at-rest or audit status until verified in code.
- **Does the bundling check cover all NCCI edits?** No. It checks about 62 hand-picked NCCI pairs, a small subset of the CMS file that is revised quarterly (Q4 2025 replacement files withdrew some edits). Treat it as a starter check with a visible last-updated date, not a substitute for your coder or the full CMS tables.
- **We are an RHC / CAH with all-inclusive-rate billing. Does it handle that?** Not yet. There is no RHC or CAH-specific billing logic. Be candid and offer the pilot only for appeal drafting and general coding suggestions, or put them on an interest list and learn their requirements.
- **Who else uses it? Can we talk to a reference?** We are recruiting design partners and have no consented references yet. Do not use names from the old site or any case-study figures. Offer a design-partner discount in exchange for documented consent and metrics access.
- **Why pay when our biller or clearinghouse already flags denials?** Do not claim superiority. Position as complementary: it drafts the appeal letter from the denial text your staff already has, reducing writing time. Let the clinic's own minutes-per-appeal log decide.
- **Can you work for a percentage of what you recover?** Not at this stage. We use a flat fee because we cannot yet measure recovered dollars, and contingent fee structures need legal review. Revisit with counsel after tracking exists.
- **We have no budget; maybe grant money can pay for it.** We cannot say RHTP, Flex or USDA funds cover this; no source confirms billing or denial software is allowable. Suggest the clinic ask its state RHTP office in writing, and keep the pilot price low enough to fit an operating budget.

**Must fix before selling:**
- Remove or rewrite fabricated case studies, stats and quotes (marketing_data.py: $4.2M+ recovery, 6-hospital system 11.4% to 3.8%, 66% in four months resource article, $86K average recovery, FQHC/40-provider group numbers). Largest legal and trust risk; no consent or evidence.
- Remove all old pilot/design-partner names and logos from the site and sales material until written consent is documented.
- Remove false integration and transmission claims: clearinghouse/EHR connected in week one, claims sent via clearinghouse, 'follow it to payment' (demo.html step 03), denials returning automatically with payer reason; also stop the legacy Claim.MD 'transmitted to payer' animation in dashboard.html and the Settings clearinghouse dropdown that implies a connection.
- Rewrite the pricing matrix to remove unbuilt features sold as real (payer intelligence engine, prior auth support, benchmarking, SSO/API, custom EHR/clearinghouse integrations, custom-tuned models, BAA workflow) or label them roadmap; fix the Starter tier AI Scribe mismatch and blank provider limits.
- Correct NCCI claims everywhere: say about 62 hand-picked pairs, add a visible last-updated date, stop implying every claim is checked against the full CMS table or showing '0 conflicts' as assurance. Fix the broken quarterly loader (ncci_checker.py splits on whitespace so pipe-delimited CMS files load zero pairs) and consider loading the full table (about 675,157 records in the current practitioner file).
- Remove or relabel the 65% recovery assumption, the 'Est. Recovered With Althais' calculator and the unsourced '30 to 60 day' implementation timeline; if kept, show it as an illustration with visible inputs and no outcome implication.
- Resolve security contradictions: SOC 2 Ready / audit in progress vs 'not SOC 2 certified'; verify encryption-at-rest claims in code (cryptography is pinned but unused) and the BAA claim; publish only what is true.
- Make the denial workflow durable: claim and denial status currently lives in browser localStorage, so a pilot clinic's data is lost on browser change and cannot be measured. Move to server storage and add a basic export so pilot metrics (minutes per appeal, denials worked, appeals sent) are actually capturable.
- Fix lead capture before sending any traffic: route leads to a monitored inbox/CRM instead of one hardcoded personal address, add an admin view or export of demo_requests/pilot_requests (currently write-only), add CAPTCHA/honeypot, validation and rate limits (open forms can email third parties), stop silently failing confirmation emails, and add qualification fields (clinic type, state, EHR, monthly claims).
- Stop promising a one-business-day reply on /pilot unless a staffed process exists; state pilot terms (length, cost, data needs) on the page.
- Counsel review of pilot terms, pricing structure, BAA, and de-identification route before the first PHI or first dollar.
- Fix SEO basics that block the stated goal: add sitemap.xml and robots.txt, replace the /insurance 302 redirect to the login-gated page with a public landing page, give /pilot and /demo self-canonicals, titles naming denials/appeals, Open Graph, and delete orphan templates (pricing.html, contact.html); the live pricing page is in practice_pages.py.
- Do not target or headline 'insurance claims savings' with savings promises; if the phrase is used, pair it with real features and state human approval. Validate keyword volume with Search Console or a keyword tool first (no volume data was obtained).
- Update docs/SITE_STRATEGY.md, which is stale on rural positioning, and keep a single source of truth for pricing copy.

### Revenue model (assumptions, not forecasts)

- All figures below are ASSUMPTIONS for planning, not forecasts and not sourced benchmarks; ARPA and conversion rates were not obtained from any source and must be replaced with pilot data.
- Price assumption: $199-$499 per clinic per month; scenarios use $250, $350 and $450 per month ARPA. No competitor pricing was retrieved.
- Sourced market anchors (for scale only): about 5,461 Medicare-certified RHCs (KFF/CMS, 2025) and about 1,377 CAHs (secondary source, April 2025). Industry initial denial rate about 11.65% for 2025 through November per Kodiak/HFMA (vendor data; 2024 baseline conflicts at 11.41% vs 11.81%). These are context, not Althais results.
- Product constraint: no RHC/CAH-specific logic, so the addressable base today is independent rural practices more than RHC-specific buyers; RHCs and CAHs are an interest-list segment until logic exists. No sourced count of independent rural practices exists.
- Market-sizing note (low confidence, derived): at $3k-$15k per RHC per year the RHC software pool would be about $16M-$82M, and with CAHs at $5k-$25k about $23M-$116M combined; per-clinic spend is unverified.
- Sales-cycle and pilot-to-paid conversion are unknown; assume 30-day pilot plus 30-60 days to contract, roughly 3 months from first call to paid, and test it.
- Churn, CAC and gross margin are unmeasured; AI inference plus human support may make margin lower than classic SaaS. ARR below is gross subscription revenue, not profit.
- Annual figures: ARR = clinics x ARPA x 12. No revenue from percent-of-recovery fees is included.

| Scenario | Clinics | $/clinic/month | ARR | Note |
|---|---|---|---|---|
| Design-partner proof (first 90 days) | 3 | 0 | $0 | 3 free or heavily discounted pilots in exchange for documented consent and metrics. Goal is evidence and references, not revenue. |
| Conservative (month 12) | 10 | 250 | $30,000 | Assumes 10 paying clinics from founder-led outreach; 10 x $250 x 12 = $30,000. |
| Base (month 12) | 25 | 350 | $105,000 | Assumes 25 paying clinics; 25 x $350 x 12 = $105,000. Requires the must-fix list done, durable denial tracking and at least 3 consented references. |
| Stretch (month 18-24) | 75 | 450 | $405,000 | Assumes 75 clinics; 75 x $450 x 12 = $405,000; would be roughly 1.4% of about 5,461 RHCs plus 1,377 CAHs (about 6,838) if all were from that pool, but this is not a validated conversion rate and RHC/CAH logic is not built. |

## 5. Search strategy (SEO)

### What the search results showed

- **"insurance claims savings"** returns consumer premium-discount and insurer claims-cost pages (including UK sources), not clinic billing content. The phrase alone does not reach a clinic administrator, and a new site will not win it. It is used on one dedicated clinic page, in the landing page description and in an FAQ answer, always paired with "clinic" and "billing team".
- **Broad provider head terms** ("reduce claim denials small practice", "denial management software small practice", "recover denied insurance claims medical practice") are held by billing-company blogs, trade publications and software review sites. Not winnable soon.
- **Open long-tail ground:** plain-language guidance on bundling (NCCI/CO-97) denials; provider-side appeal letter help (most results are consumer or legal-services pages); CO-50 steps tied to the policy and the note; sourced, honest explainers (top results cite unsourced denial statistics and unverified 90 percent-plus success claims).
- **Rural clinic billing denials** results are led by payer PDFs, MAC and state Medicaid bulletins. A plain-language RHC remittance-code guide is a gap, but it needs RHC billing expertise Althais does not yet have, so it is not built.

### Built in this change

- `/robots.txt` and `/sitemap.xml` (none existed). The sitemap lists only public marketing pages; every other path gets an `X-Robots-Tag: noindex` header.
- Canonical, Open Graph and Twitter tags on the landing page and on every page that uses the shared page template; Organization and WebSite JSON-LD on the home page; BreadcrumbList JSON-LD on inner pages.
- Five guides, each answering one real search in its first paragraph: `/insurance-claims-savings-for-clinics`, `/denial-appeal-letter-help`, `/ncci-bundling-check`, `/co-97-denial-bundled-service`, `/co-50-medical-necessity-denial`. Titles are 54 characters or fewer, descriptions 157 or fewer.
- Home page: a guides section with internal links, an FAQ answer that handles the phrase "insurance claims savings", a corrected title and description.
- Footer and Resources page link to the guides; the Resources page no longer lists articles that were never written.
- Removed unsourced proof: customer quotes, before/after figures, ROI numbers, and the fake article cards. Case Studies is now an honest placeholder and is `noindex`. Removed the footer HIPAA badge.

### Not built, with reasons

- Pages on appeal deadlines, timely filing, or Medicaid rules by state: every figure needs a primary-source check first.
- Rural Health Clinic and Critical Access Hospital billing pages: the product has no RHC or CAH logic.
- Savings calculators using the $165 claim value or 65 percent recovery assumption: unsourced.
- Competitor comparison pages: competitor facts are not verified.
- FAQPage structured data: the research reported Google dropped FAQ rich results in 2026 and this was not re-verified, so FAQs stay as visible text only.

### Still to do for search

- Connect Google Search Console and submit the sitemap. Verify the real search volume for the guide phrases before writing more.
- Add a free, honest "cost to rework a denied claim" worksheet where the clinic enters its own numbers (the SERP showed a gap: the most cited figure is a decade-old $25 MGMA number, and no top result gives a calculator).
- Fix the remaining pages that still carry unbacked claims (see section 6) before sending traffic to them.
- Replace the Tailwind play CDN on pages that use `base.html`, compress the large logo and background images, and lazy-load or drop the 18.8 MB background video.
- Add analytics only after confirming no PHI can reach it: guide pages invite people to paste denial text.

## 6. What the critic flagged that is still open

**Claims that overreach:**
- SEO hub title/H1 'Insurance claims savings starts before the claim goes out' and homepage sub-line 'Insurance claims savings for clinic billing teams' still imply savings. The plan itself says to avoid savings promises and then puts the phrase in title, H1 and meta. Use 'Denied claim help' language in the title/H1 and keep 'claims savings' only in body copy and URL, or accept the risk knowingly.
- Homepage title 'Denied Claims Help for Rural Clinics' and /denied-claims-recovery-rural-clinics ('claims recovery'): 'recovery' implies recovered dollars and the product has no recovered-dollar tracking and no payment-outcome evidence. Replace 'Recovery' with 'Appeals' or 'Work Denied Claims' in slug, title and target_query framing. Also the answer-first line 'you lose less money on claims' is an outcome claim; reword to 'catch common mistakes and draft appeals faster'.
- 'Lose less money on denied claims at your clinic' (homepage H1) is a payment-outcome promise with no customer evidence. Reword to a description of the workflow.
- Meta 'Catch coding and bundling issues' implies broad coverage; bundling covers about 62 pairs. 'Check code pairs' meta for /ncci-bundling-check is fine only because it states 62 and 'not the full CMS file'. Keep that qualifier in every other mention.
- Cold email 1 cites 'Experian 2025: 41% of providers report denial rates of 10%+' and offers a 'free 30-day pilot' and sample drafting from a denial; stating a stat from a search snippet in outbound is a claim risk until verified at source. Also email 2 asks them to send denial text 'remove patient names' by email: this is a PHI/de-identification hazard (dates of service, member IDs, claim numbers, free-text clinical rationale remain identifiers). Needs a defined Safe Harbor checklist and a non-email upload path.
- Revenue model: the revenue-prompt pilot offer says 'upload or paste 10-25 past denial letters (de-identified, or under BAA)', while the plan's 'free sample review' CTA says no patient information. Two different intake rules; unify before launch.
- Pricing: $199-$499 per clinic per month and the scenarios (10 clinics/$30K, 25/$105K, 75/$405K) are labeled assumptions, but 'inside the low-thousands ACV' reasoning is circular (both anchors are unverified). The stretch scenario's '1.4% of 6,838' framing adds false precision and mixes RHC and CAH counts (5,461 RHCs vs 1,377 vs 1,386 CAHs, and CAHs are explicitly out of scope). Present as a planning hypothesis only and never on the public site.
- Channel scores (9.5, 9, 8.5 ...) and time-to-first-lead figures are subjective with no stated method; they read as measurements. Label as judgment.
- Objection response cites KFF 'fewer than 1% of marketplace denials appealed' and 'MA prior-auth denials appealed 80.7% overturned'. Those are not clinic claims-denial data and prior auth is a segment Althais says it does not serve; using them to a rural clinic is mismatched context and could be read as implying appeal success. Remove or clearly caveat.
- Segment inconsistency: primary ICP includes freestanding RHCs 'as generic rural clinic buyer' but the lead list method is built on the CMS RHC Enrollments file and the outbound hook uses RHC telehealth billing changes (G2025 Oct 1 2026). Using RHC-specific rule hooks in outreach implies RHC competence the product lacks, even with the disclaimer. The CY2026 RHC/G0511 items are explicitly unverified yet are scheduled as week 5-8 articles.
- 'Pilot-to-paid', 'hospital-employed clinics about 75% of rural physicians', 'rural independent physicians down 43%' are advocacy/snippet figures used in the ICP justification; fine as internal context but must not appear in public copy.
- The SEO plan says Google removed FAQ rich results on 2026-06-15 from research; this is stated but flagged for re-verify. Treat as unverified and do not make a decision to drop or add markup on that alone.

**Top five actions this week:**
- Take down every unbacked claim from the live site and set noindex or remove until fixed: marketing_data.py case studies, quotes and stats, old pilot and design-partner names, clearinghouse/EHR/'follow it to payment' claims (demo.html lines 51-52), 65% recovery calculator, SOC 2 Ready and HIPAA Compliant badge, unbuilt pricing-tier features. Then request recrawl. This is the legal and trust gate for everything else; no traffic or outbound until done.
- Fix lead capture and tracking in one pass: route /request-demo and /request-pilot to a monitored inbox or sheet, confirm RESEND_API_KEY works in production by submitting a test, add honeypot/validation/rate limit and qualification fields, add sitemap.xml, robots.txt, canonicals, 301s, and install Search Console. Keep analytics off any form that could receive denial text.
- Do the free 30-minute SERP and keyword reality check for 6 target queries (insurance claims savings, denied claims recovery rural clinics, denial appeal letter generator, CO-50 denial appeal, ncci bundling check, rural clinic claim denials) in a logged-out browser plus Search Console/Keyword Planner. Decide the head-term bet and the title/H1 wording (avoid 'savings' and 'recovery' in H1/title) from what you see before writing any of the 12 pages. Ship only the homepage rewrite and 2 or 3 deep pages (appeal generator, bundling check, one verified denial-code guide) first.
- Settle the PHI question with counsel and a written path: one-page pilot agreement with consent clause, BAA stance, a Safe Harbor de-identification checklist, and a non-email upload method for sample reviews. Until then change the outbound email 2 and the CTA to use a fictional or fully de-identified example only, and do not accept denial text by email.
- Start 10 administrator interviews and a 50-clinic hand-built outbound test in one expansion state (not 200 across 3), from the CMS RHC file plus independent-practice sources, sending from a separate warmed domain with a postal address and opt-out. Use interviews to learn who does billing, what they pay, and what they use today (price benchmark gap), and track replies in a sheet. Skip events, paid search, EHR marketplaces and the Oct 30 ND Flex deadline this week.

Outside the pages changed here, these still carry unbacked claims and should be reviewed next: `/platform/claims-insurance` ("Followed to payment. Denials come back ready."), `/demo` (step 3 "follow it to payment"), `/pricing` (features that are not built), `/roi-calculator` (65 percent recovery assumption), `/security` and `/hipaa-compliance` (SOC 2 and encryption wording), and the setup flows. Pending counsel review.
