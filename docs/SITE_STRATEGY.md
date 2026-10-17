# Althais site strategy (research synthesis)

Generated from a multi-agent research pass: ECC digests, a repo audit, customer research and 14 competitor profiles. Competitor and market facts are vendor-sourced and mostly unverified. Treat every number as unconfirmed until a primary source is added.

**Audience:** For rural clinic doctors and the office managers who handle billing with a small staff and no billing department.

**Core promise:** Althais helps rural clinics catch the billing mistakes that get claims denied, and gives staff a ready appeal letter to chase the money back on claims that were denied anyway. A person always reviews the claim. We never promise a claim will be paid.

**Plain-English value:** When a claim gets denied, the money usually sits there because nobody has time to fix it. Althais works from the visit. You dictate or type it, and Althais writes the note, suggests the diagnosis and procedure codes, and checks those codes for common bundling mistakes before the claim goes out. When a claim still comes back denied, you mark it, and Althais drafts the appeal letter from the denial text you paste in. Your staff reviews and sends it. Today the recovery steps are manual and tracked by your staff. Headline direction for the site: "Get paid for the care you already gave." The plain-words support line says Althais helps you catch claim mistakes before they cost you, and draft the appeal when a claim is denied. Keep the SOAP, ICD-10, CPT and NCCI wording in a second section, each term explained once in plain language.

## What we do differently (only what exists in code)

- **One flow from the visit to the appeal letter, in one tool.**
  - Proof: Verified in code: the note and code suggestions come from the visit (main.py), NCCI flags are merged into claim validation (main.py:1326-1343), and /api/appeal-letter drafts a letter from denial text on demand (main.py:1350-1383). The Appeals page has Generate Letter and Mark Appealed (revenue_appeals.html:220, 263-275).
  - Contrast: Availity, Suki and Abridge have no denial-recovery or coding-check story on the pages read. Waystar, Experian Health and AKASA sell denial work but are built for health systems, not a 2-provider clinic. Each competitor fact is from vendor pages and is not independently confirmed.
- **Catches bundled-code mistakes before the claim leaves the building (prevention, which is a different thing from recovery).**
  - Proof: Verified in code: ncci_checker.py reads an NCCI pair table and flags pairs with modifier indicator 0 or 1. Caveat: the table holds 62 hand-picked pairs, not the full CMS file, and it ignores modifiers already on the claim. Say 'checks for common bundling mistakes', not 'checks against all CMS edits'.
  - Contrast: CollaborateMD, AdvancedMD and Tebra advertise claim scrubbing, but all of it is pre-submission and none of it is rural-specific. Whether their scrubbers include NCCI is not confirmed.
- **Plain-word, rural-first message from a smaller, narrower tool, with a human reviewing every claim.**
  - Proof: Design intent, not a code fact. The site is where this gets proven, and today it is not: 'rural' appears on no public marketing page (audit). It would be earned by the rewrite plus real rural customer proof. Human review is real in code, because production claims are always held and never auto-sent (billing_activation.py:657-663, 1276-1312).
  - Contrast: Most competitors lead with breadth ('Simplify healthcare payments', 'one EHR+ platform', 'Enterprise-Grade AI') and hide price behind a demo. Azalea and TruBridge do target rural, but as full EHR and billing bundles or hospital RCM. Azalea's headline could not be read, and TruBridge's 70% recovery claim is unverified. XpertDox is a rural AI-coding competitor seen only in a snippet. The direct small-clinic AI competitors were never researched.

## Claims we must not make yet

- Any dollar amount, recovery rate or '65% recovered'. The recovery rate and $165 average claim assumption have no data in the repo, and dashboard Recovered Revenue is hard-coded to $0.
- Case-study and ROI numbers on the live site ($4.2M recovered, 66% fewer denials, 52 to 19 days in A/R, and similar). They have no source, and several contradict their own tables. Pull them or label them clearly as examples.
- Testimonials, 'Trusted by' logos and 'From our pilots' (Tarin, Cox, Gupta, Ward Memorial, Excel ER). No consent or contract is in the repo, and the public chatbot's own rules forbid inventing these. Show them only after written permission.
- 'Checked against real CMS NCCI edits' or full NCCI coverage. The table has 62 hand-written pairs. The public demo can return a false 'no conflict' for a real bundled pair.
- 'Every claim followed from submission to payment', 'we track denials for you', or any automatic denial detection. No 835, 277CA or CARC parsing exists, and denial status is typed in by staff and stored in the browser only.
- 'We send your claims to the payer' or 'connected to your clearinghouse'. No clearinghouse is connected, and production claims are held and never transmitted.
- 'Appeal letter ready when a denial arrives'. Letters are written on demand by an AI model from text the user pastes in, and nothing is pre-drafted.
- Appeal success rates, 'get your money back', 'guaranteed' or 'more claims get paid'. NCCI checks coding correctness, not medical necessity or payer coverage. The 51.7% or 52% overturn figures are not Althais results.
- 'Works with Epic, athenahealth, eClinicalWorks, NextGen' or any EHR integration. No integration code was found.
- 'Live in 30 to 60 days' (no basis in the repo), 'immutable audit trail', 'TLS 1.2+ and encrypted at rest', SOC 2 controls 'in place', and any HIPAA badge. SOC 2 is shown as 'Not yet', and a BAA is Enterprise-only.
- 'Rural' proof: no rural customer, rural denial rate or rural case study exists. The '18% rural vs 10% urban' and '$330K' figures are vendor-cited with no primary study. Do not use them.
- 'The only' or 'first' claims. The competitor check is thin: direct small-clinic AI tools were not researched, and competitor facts are mostly from vendor pages.
- Medicare appeal deadlines or payer-specific appeal rules on the site without a primary CMS check. The 120-day Medicare redetermination window was read on the CMS page for Part B only.

## Product gaps to close or soften

- No payer data flows in. There is no 835 or 277 parsing and no clearinghouse, so Althais cannot see a denial itself. Soften: 'you tell Althais which claims were denied.' Close: build 835/CARC ingestion.
- Denied-claim data lives in browser localStorage (althais.claims.v1), not on the server. Clearing the browser loses it. This is a real risk for a billing record. Move it to server storage.
- Recovered dollars are never computed. Add a real 'recovered' field from payment posting, then use only real figures.
- Mark Appealed only changes a label. There is no resubmission workflow and no follow-up reminders or deadline tracking. Build deadline alerts if 'follow-up' is going to be promised.
- Appeal letters need a CARC-to-next-action step. Static text covers only CO-97, CO-50 and CO-29. A rural office manager needs 'what do I do with this denial code'. Expand and verify against a primary source.
- NCCI table has 62 pairs, ignores modifiers already present and has no date logic. Load the full CMS PTP file, fix the pipe-versus-whitespace parser mismatch, and handle modifier indicators. Until then, soften to 'common bundling mistakes'.
- Rural, Medicaid and RHC/FQHC billing is absent. RHCs bill under an all-inclusive rate with their own rules, CMS-1500 versus UB-04 matters, and Medicaid has its own NCCI files. The product has no RHC-specific logic. Either add it or do not imply it.
- Two code validators disagree on ICD-10 and CPT shape (code_validation.py versus billing_activation.py), and code_validation is format-only. Reconcile before claiming code accuracy.
- Demo data conflicts: the same chest-pain visit has R06.00 and R06.02, 94% and 95% confidence, age 54 versus 58, and CHC-2026-00412 shown as Submitted but flagged at risk. A rural admin spots this fast. Fix to one consistent example.
- The public chat misses 'denied' (the regex matches 'denial') and has no answer for 'money back'. Add keyword answers for denied, recover, appeal. The Althea label 'Clinical AI' also conflicts with the product's own guardrails.
- Site structure: the live H1 ('From encounter, to reimbursement.') cycles words and never mentions denials or rural. Orphan templates (about, pricing, resources, contact) are not routed, so editing them changes nothing. The live copy is in more_pages.py, practice_pages.py and marketing_data.py. Hero content also depends on JS with no fallback.
- Two competing CTAs (Join the Pilot versus Book A Demo). Pick one path: a sample-claim review with the clinic's own denied claim. Contact emails also route to a personal address while the site says hello@althais.com.
- Pricing tiers list no appeals or denial line item, though that is the main promise. Two ROI calculators use different models ($165 versus $185, 50% versus 65% recovery). Merge them and drop the unsourced 65%.
- Accessibility and weight: faint grey text is about 2.6:1 contrast (fails AA), a looping background video has no pause control and loads 18.8 MB, about 60 MB of unused video sits in the repo, the success message is not announced, and nested interactive testimonial cards are poor for screen readers. Two visual systems (dark navy and light) clash. Not browser-tested.
- Security hygiene to fix before real PHI: rate limit trusts a client-supplied X-Forwarded-For header; the encryption and TLS claims have no visible backing in code. HIPAA review by counsel and a signed BAA process are required before any trust section.

## Objections and answers

- **Will this actually get my denied claims paid?** We cannot promise payment, and nobody honest can. What Althais does is catch common coding mistakes before you send, and draft the appeal letter when a claim is denied, so your staff spends minutes instead of hours. Outcomes depend on the payer and the claim. Offer a sample review on one of their own denied claims and show real numbers only once we have them.
- **Do you connect to my payers and see my denials automatically?** Not yet. Today you tell Althais which claims were denied, and it helps with the letter and tracking. Say so plainly rather than imply automatic detection. This is the largest gap between the money-back promise and the code.
- **We are an RHC or critical access clinic and bill differently. Does it handle that?** Not proven. There is no RHC or CAH-specific logic in the code, and RHC all-inclusive-rate rules differ from standard physician billing. Do not claim rural billing expertise on the site until it is built and tested with a real rural clinic.
- **Does it work with my EHR?** We cannot claim any named EHR integration, because none was found in the code. Say what is true: you can dictate or type the visit into Althais and review the claim there. Add EHR names only after an integration exists and is tested.
- **Is it safe for patient information (HIPAA)?** Visit and claim data is protected health information. Say only what is true and documented today, and have counsel review the wording. A BAA is currently offered on Enterprise only and SOC 2 is 'not yet', so a small clinic on a lower tier may not get a BAA. Fix this before targeting small clinics, since an AI note step on PHI without a BAA is a deal-breaker.
- **What does it cost, and is it worth it for 2 providers?** Pricing is hidden behind demos at most competitors, and prices for the closest tools run from about $49 a month for basic denial tools to $299 or more per provider for billing platforms (vendor-reported, unverified). Publish a plain starting price or pilot offer once decided. Do not show the ROI calculator's 65% recovery default until it has data.
- **We already have a biller, or use an outsourced billing company at 4 to 10% of collections.** Althais does not need to replace them. It can help the biller by cleaning the note and codes before the claim goes out and drafting appeal letters. Outsourced fees are vendor-quoted ranges and not verified. Do not claim to be cheaper until pricing is set.
- **Is this just another AI scribe?** Scribes such as Abridge, Suki and Dragon Copilot stop at the note, and are priced and sold for health systems. Althais goes on to the codes, the bundling check and the claim, and drafts the appeal for denials. Limit the claim to what the competitor pages say, since the review rests on vendor pages.

## Words to use

- denied claims
- get paid for care you already gave
- money left on the table
- fix it before you send it
- appeal letter you can edit and send
- your staff reviews every claim
- small clinic, small staff
- office manager
- bundled codes (two codes the payer will not pay for together)
- draft, suggest, flag, check
- sample claim review with your own denied claim
- a visit note, written from what you dictate

## Words to avoid

- autonomous, agentic, AI-powered platform, intelligence layer
- revenue cycle, RCM, mid-cycle, touchless claim rate
- guaranteed, recover up to X%, maximize reimbursement
- SOAP, ICD-10, CPT, NCCI, CMS-1500, PTP, MUE, CARC in headlines or first screen (explain once in a glossary)
- enterprise-grade, transform, unlock, seamless, end-to-end
- checked against all CMS edits, real-time payer data
- trusted by, thousands of clinics, proven results (until real)
- clinical AI, clinical assistant
- 'not X, just Y', 'no fluff', bait questions, 'excited to share'

## Concept scores (4 judge lenses, 1 to 10)

- Money Back Page: 8; Catch It Before It Goes Out, Chase It After: 7; The Stretched Front Office: 7; Simple Path: 6 (best: Money Back Page (8/10). It gives the clearest 10-second value: the headline promises getting paid, the subhead names the denied-claim pile and the appeal draft, and the visual shows a denied claim becoming a letter. To make it lighter, borrow the Stretched Front Office audience line and the Catch-It two-part framing, and move the stats and long sections lower on the page.)
- Catch It Before It Goes Out, Chase It After: 8; Simple Path: 7; Money Back Page: 6; The Stretched Front Office: 5 (best: Catch It Before It Goes Out, Chase It After (8/10). Its prevention-first story is the most concrete and honest value for a physician, it matches what the code actually does, and it states limits without sounding evasive. Fix the 'chase it' wording so it does not imply follow-up tracking, and cut the slogan line.)
- Money Back Page: 6; Simple Path: 7; The Stretched Front Office: 6; Catch It Before It Goes Out, Chase It After: 6 (best: Simple Path (7/10). It makes the fewest risky claims: no invented numbers, a clear limits section, deadlines and pricing left as placeholders, and no modifier or coding advice. Before any of the four ships, change the shared headline 'Get paid for the care you already gave' to wording that does not imply a payout, and do not collect denial text (PHI) until a BAA and a safe intake path are in place.)
- Money Back Page: 4; Simple Path: 7; The Stretched Front Office: 6; Catch It Before It Goes Out, Chase It After: 8 (best: Catch It Before It Goes Out, Chase It After (8). It is the only concept built on the real product shape (prevention plus appeal drafting in one small tool, with a person reviewing every claim), and it separates Althais from scribes, scrubbers and enterprise denial platforms. Keep its hedges: 'common mistakes' not 'every CMS edit', and 'you tell Althais which claims were denied'.)

## Concepts

### Money Back Page
**Get paid for the care you already gave.**  
Denied claims sit in a pile because nobody has time to fix them. Althais helps you catch claim mistakes before they cost you, and drafts the appeal letter when a claim is denied. Your staff reviews every claim.  
CTA: Send us one denied claim / See how it works (scroll link, not a second button path)
Hero visual: A plain, still image of one denied claim turning into a ready-to-edit appeal letter, shown as two cards side by side with an arrow. Left card: a claim marked "Denied" with a sample reason line. Right card: the draft letter with an "Edit and send" button. A small tag says "Sample, not a real patient." No looping video, no dashboard with dollar totals, no invented numbers. Light background, large type, high contrast. A mockup of a real Althais screen (the Appeals page with Generate Letter) can replace the illustration once the demo data is made consistent.

- **1. Hero: Get paid for the care you already gave**: Say the outcome in one breath, name who it is for, and offer one next step. No jargon, no numbers.
- **2. The money sitting in the pile**: Make the problem concrete for a small clinic using only verified, sourced facts. Stat cards, each with its source named. Frame honestly: these are industry figures, not Althais results.
- **3. How it works: from the visit to the appeal letter**: Show one simple flow in 4 steps so a non-technical reader sees the path. This is the core product story. Every step maps to something that exists in the product today.
- **4. Two places money gets lost, and what Althais does at each**: Separate prevention from recovery in plain words. This is a core difference and sets honest expectations about what is automatic and what is manual.
- **5. What Althais does not do (yet)**: Build trust with a rural office manager who has been burned by software promises. State the limits plainly. This section turns gaps into honesty and protects the company from forbidden claims.
- **6. How Althais is different**: Plain comparison in words a clinic uses, with no competitor names on the page and no 'only' or 'first' claims. Based on vendor pages, so keep the language soft.
- **7. Try it on your own denied claim**: The single conversion section. Explain exactly what the sample review is, what we need, what they get, and how privacy is handled. Replaces both 'Join the Pilot' and 'Book a Demo'.
- **8. Questions you are probably asking**: Answer the real objections from the research in plain words, short answers, same honest tone. Use an accessible accordion or just open text.
- **9. Words we use, in plain English**: Move the billing jargon out of the headline and first screen. Explain each term once, in plain language, for readers who see these words on their claims every day.

### Simple Path
**Get paid for the care you already gave.**  
Althais helps your small clinic catch claim mistakes before they cost you, and writes the appeal letter when a claim is denied anyway. Your staff reviews every claim and every letter.  
CTA: See it on your own denied claim / Read the four steps below (a link that scrolls down the page, not a second sign-up path)
Hero visual: A plain four-step strip across the top of the page, not a stock photo and not a dashboard screenshot. Four large numbered cards in a row (stacks vertically on a phone): 1 Visit, 2 Check, 3 Denied?, 4 Appeal letter. Each card has one line of text and one simple icon (microphone, checkmark, flagged envelope, letter). Beside the strip sits one consistent sample claim (a single sample patient visit, labeled 'Sample, not a real patient') showing a before and after: 'Two codes the payer will not pay for together' flagged, then fixed. The sample must use one set of facts everywhere on the site. Large type (18px or more), high contrast, no looping video, no animated headline. The headline is plain text that works with JavaScript off.

- **1. Hero: Get paid for the care you already gave**: Say the one promise and the one next step in under ten seconds. Name the reader (small clinic, small staff). Make the honesty line visible on the first screen.
- **2. The problem in plain words: why denied money just sits there**: Name the pain in the reader's own words without invented numbers. Make the reader nod: nobody has time to fix denials. Use only sourced, labeled facts.
- **3. What happens to a claim: four steps in plain words**: This is the heart of the page and the angle. Walk through one claim, step by step, with no jargon. Each step says what Althais does, what your staff does, and what Althais does NOT do. Be honest about the manual parts.
- **4. Why this is different: one place, from the visit to the letter**: State what we do differently in plain words, using only verified product facts and soft competitor contrast. No 'only' or 'first'. Make the reader understand why a small tool beats a big platform for a 2-provider clinic.
- **5. What Althais does not do (yet)**: Build trust by stating the limits plainly. This is the section competitors will not write. It also protects us from every forbidden claim. A rural office manager has been burned by overpromising software.
- **6. Real proof (placeholders until we earn it)**: Hold space for proof without faking it. Show the reader how we will earn trust. Keep every number and name honest.
- **7. Words you may hear, explained once**: Move the billing jargon out of the headlines and into one calm glossary. Each term is explained one time in plain language. Helps the office manager talk to payers and helps the doctor trust the output.
- **8. Questions you are probably asking**: Answer the real objections in plain, honest words. Cover payment, payers, EHR, safety, cost and existing billers, without overpromising.
- **9. One last step: send us one denied claim**: Close with the single call to action. Make it low-risk and concrete. One path only. Do not offer a demo, a pilot signup and a calculator together.

### The Stretched Front Office
**Get paid for the care you already gave.**  
Althais helps a small clinic catch claim mistakes before they cost you, and writes the appeal letter when a claim is denied. Your staff reviews and sends it. No billing department needed.  
CTA: Send us one denied claim for a free sample review / See how it works (scrolls to the three-step section; a text link, not a second button path)
Hero visual: A simple three-step strip, drawn from one plain example visit and used consistently on the page. Step 1: "Visit" shows a short dictated note. Step 2: "Check" shows a yellow flag reading "These two codes are often not paid together. Fix before sending." Step 3: "Appeal" shows a draft letter with an Edit button and a "Reviewed by you" tag. A small label under it reads "Example screen, sample data, not a real patient." No dollar figures, no logos, no stock photo of a hospital. Static image, no autoplay video, so it loads fast on rural connections.

- **1. Hero**: Say in five seconds what Althais is, who it is for, and the one thing to do next.
- **2. The problem in your words**: Show we know the stretched front office. Name the pain: denied claims sit because nobody has time. Use only verified facts, framed as industry-wide, not as rural proof.
- **3. How it works in three steps**: Make the whole product understandable in one scroll. One flow from visit to appeal letter, in plain words. Uses the hero example so it stays consistent.
- **4. What changes for your office**: Land the angle: less rework, fewer hours, no extra hire. State benefits as what staff do, not as dollars. Keep every sentence something the product does today.
- **5. How Althais is different**: State what we do differently without 'only' or 'first' claims and without naming competitors in a way we cannot back up. A short, honest comparison by type of tool.
- **6. What Althais does not do yet**: Build trust by stating limits plainly. Closes the biggest gap between the promise and the product, and answers the top objections (payment, payer connection, EHR, rural billing rules).
- **7. Words you may hear, explained once**: Move the billing jargon out of the first screen but keep it available for the doctor or biller who wants the exact terms. Each term gets one plain sentence.
- **8. Your questions**: Answer the top objections in the doctor's own voice, in short answers, so the CTA feels safe. Covers price, HIPAA, existing biller, and 'is this just a scribe'.
- **9. Final call to action and honest proof slot**: One clear next step, with a human face. Leaves a visible, honest slot for real rural proof later. Closes the page.

### Catch It Before It Goes Out, Chase It After
**Get paid for the care you already gave.**  
Althais helps your clinic catch claim mistakes before they cost you, and drafts the appeal letter when a claim is denied anyway. Your staff reviews every claim. We never promise a claim will be paid.  
CTA: See it on your own denied claim / Watch the 2-minute walkthrough (use only once a real, consistent walkthrough exists; otherwise show the 3-step strip and a text link to 'How it works')
Hero visual: A simple three-step strip, drawn as one claim moving left to right. Step 1 'The visit': a doctor's spoken note turns into a written visit note. Step 2 'Before it goes out': the claim shows a yellow flag, 'These two codes are bundled. The payer may not pay for both together,' with a Fix button. Step 3 'If it comes back denied': a pasted denial notice turns into a draft appeal letter with Edit and Send buttons for the office manager. Below the strip, one line: 'A person reviews every claim.' Use ONE consistent example claim across the whole page (same patient age, same codes, same status) and label it 'Example, not a real patient.' Light, warm, high-contrast design with large type (4.5:1 contrast or better). No looping background video. Hero text must show without JavaScript. No rotating words.

- **1. Hero: Get paid for the care you already gave**: Say the value in one breath for a doctor or office manager: fewer mistakes going out, a ready draft when a claim is denied. Set honest expectations immediately (a person reviews; no payment promise). Single call to action.
- **2. The problem in your own words**: Name the pain in the customer's language: denied claims sit because nobody has time. Show we understand a 2-provider office. Use only sourced, plainly stated facts; no rural statistics.
- **3. How it works: three steps, one tool**: Make the whole flow obvious in under a minute, from the visit to the appeal. This is the main differentiator: prevention and recovery in one flow. Be exact about what is manual today.
- **4. Catch it before it goes out**: Lead with prevention, the angle's first half. Show one concrete bundling mistake in plain words, with the right modesty about coverage (common mistakes, not every payer rule).
- **5. If it still comes back denied: the appeal letter**: Deliver the second half of the angle: getting back what was already denied, with realistic framing of time saved, no payment promise, and honest handling of deadlines.
- **6. Why a small, narrow tool**: Differentiate from large vendors and EHR bundles without 'only' or 'first' claims or unverified rural claims. Contrast on scope and audience, kept factual.
- **7. Questions you are probably asking**: Answer the real objections plainly and honestly, including the ones we cannot yet satisfy. Doing this builds trust with skeptical office managers and keeps us inside the forbidden-claims list.
- **8. Plain-words glossary**: Keep the first screens free of coding jargon while giving billing-literate readers the exact terms. Each term explained once, at the grade 8 level.
- **9. Start with one of your own denied claims**: One call to action, low risk, low effort, and the only proof path we can honestly offer. Doubles as the way to collect real outcomes and consented stories later.


## Critic: missing before launch

- Competitor research is thin: direct small-clinic AI tools were never researched; XpertDox seen only in a snippet; Azalea headline unread; TruBridge 70% claim and all pricing figures are vendor-reported and unverified. No 'only/first' claim is safe.
- No rural primary evidence: no rural customer, no rural denial-rate or payment-delay source (18% vs 10%, $330K are uncited). Need a primary source (CMS, MGMA, NRHA or similar) or leave the numbers out.
- No RHC/CAH/FQHC billing research (all-inclusive rate, CMS-1500 vs UB-04, Medicaid NCCI) and no decision on whether the product supports it. Page must not imply it.
- Payer appeal deadlines and rules: only the Medicare Part B 120-day window was read. Medicaid and commercial deadlines are unchecked. Verify CARC meanings (CO-97, CO-50, CO-29) against a primary source or leave them out.
- No evidence of real customers: testimonials, 'Trusted by' logos and pilot names have no consent. No verified proof anywhere, so the page has no trust section except the sample-claim offer.
- Pricing or pilot terms are undecided, so the CTA offer (sample review of one denied claim) has no price, turnaround or intake process defined.
- No HIPAA/PHI plan for the sample-review intake: pasting denial text sends PHI, but a BAA is Enterprise-only and SOC 2 is 'Not yet'. Need a de-identified submission option or a BAA path, plus counsel review of any security wording.
- Rural-specific content is absent: no rural page copy, no office-manager workflow story, no staffing-shortage framing sourced to anything, no glossary (SOAP, ICD-10, CPT, NCCI, CARC) and no 'what Althais does not do yet' section written.
- Product gaps that would make copy dishonest if unsoftened: no payer data/835/277 ingestion (staff must mark denials), denied-claim data lives only in browser localStorage, recovered dollars never computed, NCCI table is 62 hand-picked pairs ignoring existing modifiers, Mark Appealed is only a label with no deadline tracking, no EHR integration, no clearinghouse (claims are held, never sent).
- Concept judges disagree on the headline: 'Get paid for the care you already gave' may imply a payout. Needs a final wording decision with the 'we cannot promise payment' line placed beside it. Also drop 'chase it' (implies follow-up tracking) and the 'cheapest denial is the one that never happens' slogan. The bundling example must not suggest adding a modifier to get past an edit.
- Accessibility and low-bandwidth plan not specified for the new build: no budget for page weight (existing 18.8 MB autoplay video, ~60 MB unused video, Tailwind Play CDN at runtime), no static-HTML-first/no-JS fallback (current hero is invisible without JS), no pause control for motion, no contrast target (existing faint grey is about 2.6:1), no keyboard/screen-reader pass (nested interactive cards, non-focusable timeline, hamburger, unannounced success message). Rural connections need a text-first page that works on slow links and old phones.
- SEO basics not defined: title and og:title are just 'Althais', meta description omits denials, no canonical, sitemap, robots, structured data, social card image, or target queries such as 'denied claims rural clinic' or 'appeal letter for denied claim'. The H1 must name denials in plain text, not a rotating word.
- Site structure undecided: four orphan templates (about, pricing, resources, contact) are not routed and live copy is in more_pages.py, practice_pages.py and marketing_data.py. Single CTA path not chosen (Join the Pilot vs Book A Demo). Contact email routes to a personal address while the site says hello@althais.com. No page-level plan for what happens to the unsourced case-study and segment pages.
- Public Althea chat is untested for the core question: 'denied' misses the keyword fallback and nothing answers 'money back'. Label 'Clinical AI' conflicts with product guardrails.
- Not browser-tested: mobile layout, real contrast, launcher overlap with CTAs, and the actual live site were never rendered. Haiku-subagent research and the ECC repo review were not done in the audits, so those learnings are not reflected.

## Critic: must fix before launch

- Remove or clearly label as examples every unsourced number and name: $4.2M, 66% fewer denials, 52 to 19 days, 65% recovery, '30 to 60 days', testimonials, 'Trusted by' logos, and EHR logos. Make the ROI cards, which contradict their own tables, consistent or delete them.
- Make the H1 and first screen say plainly: denied claims, appeal letter, rural clinics, a person reviews every claim, no payment promise. Static, no rotating word, works without JS.
- Soften all copy to match the code: 'common bundling mistakes', 'you tell Althais which claims were denied', 'appeal letter drafted on request from the denial text you paste in', and no claim of sending claims, payer tracking, or a connected clearinghouse.
- Resolve PHI intake for the sample review (de-identified option or BAA path) and have counsel check any security or HIPAA wording. Remove unbacked TLS, at-rest encryption, SOC 2 'in place' and 'immutable audit trail' claims.
- Pick one CTA (sample review of one denied claim), fix the contact email route, and write real page title, meta description and og tags.
- Fix demo data to one consistent sample claim labeled 'Sample, not a real patient' (code, confidence, age, claim ID, status).
- Fix accessibility and weight basics before launch: contrast of at least 4.5:1, no autoplay video (or add pause and a poster), noscript-safe content, keyboard-reachable controls, announced form success.
- Fix the public chat keywords for denied, recover, appeal and money back, and relabel 'Clinical AI'.
- Decide the product fix list for any later claims: move denied-claim data off localStorage to server storage, build real recovered-dollar tracking, and load the full CMS NCCI table before ever saying 'checked against CMS edits'.