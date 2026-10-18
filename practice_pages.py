"""
practice_pages.py: the "For Your Practice" pages (How It Works, HIPAA Compliance, Security, Pricing, Compare Althais),
in the landing page's style. Rendered by platform_pages.render with templates/platform_page.html.

Copy matches what the site already says: the How It Works steps and screenshots, the Pricing tiers, and the security
wording (BAAs available on Enterprise plans, SOC 2 readiness rather than certification).
"""

from fastapi import APIRouter, Depends, Request

import platform_pages
from auth import current_user

router = APIRouter()

NAV = [("How It Works", "/how-it-works"), ("Compare Althais", "/compare"), ("Security", "/security"),
       ("Pricing", "/pricing"), ("HIPAA Compliance", "/hipaa-compliance")]


def _shot(name, alt, eyebrow):
    return {"type": "shot", "eyebrow": eyebrow, "src": f"/static/screenshots/{name}.png", "alt": alt}


PAGES = {
    "/how-it-works": {
        "ctas": [("Walk through the eight steps", "#rows"), ("Try the product demos", "/platform/ai-scribe#demo")],
        "card": "One visit from the note to a claim your team approves, in eight steps.",
        "timeline_head": ("Getting started", "Start small,", "then add your team."),
        "timeline": [("Step 1", "Set up", "Enter your practice, provider and payer details. Billing setup checklists show what is still missing."),
                     ("Step 2", "Invite", "Roles are set, and your team is invited and works through the training modules."),
                     ("Step 3", "Try it", "A few providers try the scribe and coding tools while you check the results yourself."),
                     ("Step 4", "Add more people", "Bring in the rest of your staff when you are ready.")],
        "specs_label": "Who does what", "specs_title": "Everyone keeps their job. The busywork goes.",
        "specs": [("Providers", "Record the visit, review the drafted note, sign it, and approve or change the codes"),
                  ("Coders", "Review suggested codes with their confidence and reasons, and run the code check"),
                  ("Billers", "Work the claims queue, fix held claims, and work on appeal letters"),
                  ("Front desk", "Schedule and register patients so visits start with the right details"),
                  ("Managers", "Invite staff, set role access, and see the whole practice's claims"),
                  ("Althais", "Drafts notes, suggests codes, runs the checks, and assembles claims for a person to approve")],
        "nav": "How It Works", "eyebrow": "How It Works",
        "title": "From the visit", "em": "to the claim.",
        "lede": "Follow one visit through Althais: the note, the codes, your review, the claim, the checks, and the approval step.",
        "meta": "Follow a single visit through Althais: the provider note, AI coding, provider review, claim assembly, a bundling check, staff approval, status tracking and appeals.",
        "hero": [
            {"type": "rows", "eyebrow": "One encounter · example", "rows": [("Note", "Signed", "g"), ("Codes", "99285 · R07.9 · R06.00", ""), ("Review", "Approved by provider", "g"),
                                                                           ("Claim", "CMS-1500 assembled", ""), ("Status", "Held for approval", "a")]},
            {"type": "chips", "eyebrow": "Eight steps", "soft": True, "tags": [("Note", ""), ("Codes", ""), ("Review", ""), ("Claim", ""), ("Checks", ""), ("Approve", ""), ("Track", ""), ("Appeal", "")]},
        ],
        "rows_head": ("Eight steps", "One encounter,", "start to finish."),
        "rows": [
            {"eyebrow": "Provider note", "title": "It starts with", "em": "the note.",
             "text": "Dictate the visit, paste a transcript, or type it. Althais drafts a SOAP note for the provider to review.",
             "cards": [_shot("provider-note", "The SOAP note entry screen in Althais, with chief complaint, HPI, vitals and assessment and plan", "Write a note")]},
            {"eyebrow": "AI coding", "title": "Codes come from", "em": "the documentation.",
             "text": "Althais suggests ICD-10 and CPT codes from the note, with a confidence score on each.",
             "cards": [_shot("ai-coding", "AI-suggested ICD-10 and CPT codes generated from the clinical note, with confidence scores", "Suggested codes")]},
            {"eyebrow": "Provider review", "title": "A person decides", "em": "on every code.",
             "text": "The rendering provider accepts, edits or rejects each suggested code. Nothing moves forward without that decision.",
             "cards": [_shot("provider-review", "A provider accepting AI-suggested codes in Althais", "Review codes")]},
            {"eyebrow": "Claim assembly", "title": "The claim", "em": "builds itself.",
             "text": "Approved codes and visit details are assembled into a CMS-1500 claim for a person to read and approve.",
             "cards": [_shot("claim-assembly", "A CMS-1500 claim form assembled from the approved codes", "Claim form")]},
            {"eyebrow": "Bundling check", "title": "Checked before", "em": "a person approves it.",
             "text": "Each claim is checked against a list of about 62 common NCCI code pairs that should not be billed together. It is not the full CMS table and it does not look at modifiers already on the claim.",
             "cards": [{"type": "rows", "eyebrow": "Bundling check · example", "rows": [("Code pairs checked", "About 62 common pairs", ""), ("Result", "Flagged for review if found", "a")]}]},
            {"eyebrow": "Approval", "title": "Held until", "em": "a person approves.",
             "text": "Every production claim is held for a person to approve. Althais does not send claims to a payer or clearinghouse today.",
             "cards": [{"type": "rows", "eyebrow": "Claim status · example", "rows": [("Claim", "Held for approval", "a"), ("Approved by", "A staff member", "")]}]},
            {"eyebrow": "Tracking", "title": "Your team sets", "em": "each status.",
             "text": "Staff mark a claim as accepted, pending or denied by hand, and these marks are saved in your browser. Paste in the denial text and Althais can draft an appeal letter.",
             "cards": [_shot("claim-tracking", "Claims overview with statuses set by staff", "Claims overview")]},
            {"eyebrow": "Appeals", "title": "Denials get", "em": "a draft letter.",
             "text": "When a claim is denied, paste in the denial text. An AI model drafts an appeal letter, and your team reviews and edits it.",
             "cards": [{"type": "checklist", "eyebrow": "Appeal · example", "items": [("Denial text pasted in", True), ("Appeal letter drafted", True), ("Staff review and edit", False)]}]},
        ],
        "faq": [("How long does setup take?", "It depends on your practice. You can invite staff, set roles and work through the training modules as soon as you sign in. Billing setup checklists show what is still missing."),
                ("Who approves the codes?", "The rendering provider approves every code before it reaches a claim."),
                ("Does Althais send claims for us?", "Not today. Althais does not connect to a payer or clearinghouse. Claims are held for a person to approve.")],
    },
    "/hipaa-compliance": {
        "ctas": [("Who handles what", "#compare-tiers"), ("Read the security details", "/security")],
        "card": "The safeguards behind Althais and what your clinic controls.",
        "matrix_head": ("Shared responsibility", "What Althais handles,", "and what stays with you."),
        "matrix": {"cols": ["Althais", "Your clinic"], "groups": [
            ("Protecting data", [("Logging key staff and billing actions", ["Handles", ""]), ("Hashing passwords", ["Handles", ""])]),
            ("Access", [("Role-based permissions", ["Provides", "Sets them"]), ("Inviting and removing staff", ["Provides", "Decides"]), ("Pausing a person's access", ["Provides", "Decides"])]),
            ("People and paperwork", [("Business Associate Agreement", ["Ask us", "Signs"]), ("HIPAA training module", ["Provides", "Assigns"]), ("Patient consent to record", ["Provides a tick box", "Obtains"])]),
        ]},
        "nav": "HIPAA Compliance", "eyebrow": "HIPAA Compliance",
        "title": "Built for protected", "em": "health information.",
        "lede": "Althais gives your clinic role-based access, a record of key staff and billing actions, and a HIPAA training module. HIPAA has no certification, and Althais does not claim one.",
        "meta": "What Althais does today for patient health information: role-based access, an action log and a HIPAA training module for staff.",
        "hero": [
            {"type": "checklist", "eyebrow": "HIPAA safeguards", "items": [("Access limited by role", True), ("Key staff and billing actions logged", True), ("HIPAA training module managers can assign", True)]},
            {"type": "rows", "eyebrow": "Business Associate Agreement", "soft": True, "rows": [("Availability", "Ask us before you sign up", ""), ("Status", "Terms not final", "")]},
        ],
        "rows": [
            {"eyebrow": "Access", "title": "Each person sees", "em": "only what they need.",
             "text": "Providers, billers, front desk and managers each get the access their job calls for. Managers can change a role, pause a person, or remove them at any time.",
             "cards": [{"type": "rows", "eyebrow": "Roles · example", "rows": [("Provider", "Their patients and notes", ""), ("Biller", "Claims", ""), ("Front Desk", "Schedule and intake", ""), ("Manager", "Everything + team", "g")]}]},
            {"eyebrow": "Accountability", "title": "Who did what,", "em": "and when.",
             "text": "Key staff and billing actions are recorded, such as invitations, role changes and claim approvals. Any time the Althais team opens a time-limited view of an account to help you, that is logged too.",
             "cards": [{"type": "rows", "eyebrow": "Activity log · made-up example", "rows": [("09:12", "Role changed to Biller", ""), ("09:40", "Invitation sent to new staff member", ""), ("10:05", "Claim approved by biller", ""), ("11:20", "Support view, logged", "a")]}]},
            {"eyebrow": "People", "title": "Compliance is part", "em": "of onboarding.",
             "text": "Staff onboarding can include HIPAA training and policy acknowledgments. Your manager assigns them and can see who has finished.",
             "cards": [{"type": "checklist", "eyebrow": "New staff · example", "items": [("HIPAA training", True), ("Policy acknowledgment", True), ("Role-based access granted", True)]}]},
        ],
        "grid": [("Business Associate Agreement", "Ask us about this before you sign up."), ("Passwords", "Stored as one-way hashes, not plain text."), ("Least privilege", "Access matched to each role."),
                 ("Action log", "Key staff and billing actions are logged."), ("Privacy Policy", "Read how Althais handles your information."), ("Training module", "A HIPAA training module managers can assign.")],
        "grid_label": "The safeguards",
        "links": [("Security", "/security"), ("Privacy Policy", "/legal/privacy"), ("Contact Us", "/contact")],
        "faq": [("Will Althais sign a BAA?", "Contact us before you sign up. Business Associate Agreement terms are not final yet, so we cannot promise one on any plan today."),
                ("Who can see our patients' information?", "Only people in your clinic with a role that allows it. Althais support can open a time-limited view of an account to help you, and each view is logged."),
                ("Where can I read more?", "See the Security page and our Privacy Policy, or contact us with your compliance team's questions.")],
    },
    "/security": {
        "ctas": [("See the details", "#specs"), ("HIPAA compliance", "/hipaa-compliance")],
        "card": "Role-based access, sign-in safeguards and an action log. No SOC 2 yet.",
        "specs_title": "How Althais is secured.",
        "specs": [("Passwords", "Stored as one-way hashes, never as plain text"),
                  ("Access", "Role-based; managers grant and remove access"), ("Sign-in", "Sessions expire after 12 hours; temporary passwords must be changed on first use"),
                  ("Paused accounts", "Can't sign in until a manager restores them"), ("Support access", "Althais staff viewing an account is time-limited and logged"),
                  ("Action log", "Staff changes, invitations, role changes and billing actions are recorded"), ("SOC 2", "Not certified and not audited yet")],
        "nav": "Security", "eyebrow": "Security",
        "title": "Security built into", "em": "every layer.",
        "lede": "Patient information deserves care at every step. Here's how Althais protects it.",
        "meta": "Althais security today: role-based access, password hashing, session expiry and an action log. No SOC 2 report yet.",
        "hero": [
            {"type": "rows", "eyebrow": "Security posture", "rows": [("Passwords", "Hashed", "g"), ("Access", "Role-based", ""), ("Action log", "Staff and billing actions", "g"), ("SOC 2", "Not yet", "a")]},
        ],
        "rows": [
            {"eyebrow": "Data", "title": "Passwords are", "em": "never kept as plain text.",
             "text": "Passwords are stored as one-way hashes. This page does not make other claims about how data is encrypted or stored. Ask us if your compliance team needs those details.",
             "cards": [{"type": "rows", "eyebrow": "Data protection", "rows": [("Passwords", "Hashed", "g"), ("Other data protections", "Ask us", "")]}]},
            {"eyebrow": "Sign-in", "title": "Sessions that expire,", "em": "passwords that change.",
             "text": "Sign-ins time out, temporary passwords must be replaced on first use, and paused accounts can't sign in at all.",
             "cards": [{"type": "checklist", "eyebrow": "Account safeguards", "items": [("Sessions time out", True), ("Temporary passwords replaced on first sign-in", True), ("Paused accounts blocked", True)]}]},
            {"eyebrow": "Controls", "title": "No SOC 2", "em": "report yet.",
             "text": "Althais does not have a SOC 2 report today, and no audit has been completed. What exists now is described on this page.",
             "cards": [{"type": "rows", "eyebrow": "SOC 2 status", "rows": [("Role-based access", "Yes", "g"), ("Action log", "Yes", "g"), ("SOC 2 report", "Not yet", "a")]}]},
        ],
        "grid": [("HIPAA", "HIPAA has no certification, and Althais does not claim one. Ask us about a Business Associate Agreement."), ("SOC 2", "Not certified and not audited yet."), ("Passwords", "Stored as one-way hashes."),
                 ("Role-based access", "Set and adjusted by your managers."), ("Audit logs", "Including any Althais support view."), ("Session safety", "Timeouts and forced password changes.")],
        "grid_label": "How we protect your data",
        "links": [("HIPAA Compliance", "/hipaa-compliance"), ("Privacy Policy", "/legal/privacy"), ("Terms", "/legal/terms")],
        "faq": [("Does the Althais team see our patients' data?", "Althais support can open a time-limited view of an account to help you, and each view is logged."),
                ("Can we control who sees what?", "Yes. Managers set each role's access and can pause or remove a person at any time."),
                ("Is Althais SOC 2 certified?", "No. Althais has no SOC 2 certification or audit yet.")],
    },
    "/pricing": {
        "ctas": [("Compare the tiers", "#compare-tiers"), ("Estimate your ROI", "/roi-calculator")],
        "card": "Three tiers priced around claim volume, not seats.",
        "matrix_head": ("Compare tiers", "Everything in each tier,", "side by side."),
        "matrix": {"cols": ["Starter", "Professional", "Enterprise"], "groups": [
            ("Coding and claims", [("AI medical coding (ICD-10 + CPT)", [True, True, True]), ("Claim drafting, held for your approval", [True, True, True]), ("Bundling check on common code pairs", [True, True, True])]),
            ("Denials", [("Appeal letters drafted by AI from denial text you paste in", [True, True, True])]),
            ("Your team", [("Staff invitations and roles", [False, True, True])]),
            ("Training", [("Staff training modules", [True, True, True])]),
        ]},
        "nav": "Pricing", "eyebrow": "Pricing",
        "title": "Priced around", "em": "your claim volume.",
        "lede": "Pricing follows claim volume and provider count, not a flat per-seat fee. Every tier includes staff training modules.",
        "meta": "Althais pricing: Starter, Professional and Enterprise tiers, priced around claim volume.",
        "hero": [
            {"type": "rows", "eyebrow": "Every tier includes", "rows": [("Training modules", "Included", "g")]},
            {"type": "chips", "eyebrow": "Priced by", "soft": True, "chips": ["Claim volume", "Provider count"]},
        ],
        "tiers": [
            {"for": "Small Practices", "name": "Starter", "text": "For small practices that want help with notes, codes and claim drafts.",
             "button": "Contact Sales", "href": "/demo", "features": ["AI medical coding (ICD-10 + CPT)", "Claim drafting, held for your approval", "Bundling check on common code pairs", "Appeal letters drafted on request"]},
            {"for": "Growing Organizations", "name": "Professional", "featured": True, "text": "For groups with several providers who need staff roles and invitations.",
             "button": "Book A Demo", "href": "/demo", "plus": "Everything in Starter, plus:",
             "features": ["Staff invitations and roles", "Credential tracking and onboarding"]},
            {"for": "Health Systems", "name": "Enterprise", "text": "For larger groups. Talk to us about what you need and we will give you a quote.",
             "button": "Get A Quote", "href": "/demo", "plus": "Everything in Professional, plus:",
             "features": ["Pricing set with you based on claim volume and provider count"]},
        ],
        "tiers_note": 'Not sure where you fit? <a href="/roi-calculator" style="text-decoration:underline">Estimate what denials cost you</a>, then talk to us for a quote.',
        "faq": [("How is pricing structured?", "Pricing is based on claim volume and provider count, not a flat per-seat fee. Every tier includes staff training modules. Contact us for a quote."),
                ("How long does setup take?", "We do not promise a set timeline yet. You can try the demo with sample data today. Tell us about your office and we will explain what setup would involve."),
                ("Can we try it first?", "You can try the demo, which uses simulated sample data, not real patients. Contact us if you would like to talk about trying Althais in your office."),
                ("Does Althais work with our EHR and clearinghouse?", "Not yet. Althais has its own workspace for patients, schedules and charts. It does not connect to other EHRs, and it does not send claims to payers or clearinghouses. Claims are drafted and held for a person to approve.")],
    },
    "/compare": {
        "ctas": [("See the reasons", "#rows"), ("Side by side", "#compare")],
        "card": "How Althais differs from a typical EMR setup.",
        "nav": "Compare Althais", "eyebrow": "Compare Althais",
        "title": "Built for the claim,", "em": "not just the chart.",
        "lede": "Most EMRs were built to store records. Althais was built to turn a visit into a claim your team can approve, with the note, the codes and a check in one flow.",
        "meta": "How Althais compares with traditional EMRs: one flow from note to claim, codes with confidence scores, a check before approval, drafted appeals, and an assistant that scribes the visit.",
        "hero": [
            {"type": "rows", "eyebrow": "A traditional EMR, typically", "rows": [("Note", "Typed, or a separate scribe add-on", ""), ("Codes", "Picked by hand or a coding vendor", ""), ("Checks", "Often at the clearinghouse", "a"), ("Denials", "Worked in payer portals", "a")]},
            {"type": "rows", "eyebrow": "Althais", "soft": True, "rows": [("Note → codes → claim", "One flow", "g"), ("Checks", "Before a person approves", "g")]},
        ],
        "rows_head": ("The differences", "Ten ways Althais", "is different."),
        "rows": [
            {"eyebrow": "One flow", "title": "Note, codes and claim", "em": "in one place.",
             "text": "In many EMRs the scribe, the coding and the claim scrubber are separate modules or separate vendors. In Althais a signed note becomes suggested codes and then a claim, without retyping anything.",
             "cards": [{"type": "checklist", "eyebrow": "One visit in Althais", "items": [("Visit recorded, note drafted", True), ("Codes suggested from the note", True), ("Claim assembled and checked", True), ("Held for a person to approve", True)]}]},
            {"eyebrow": "Explainable coding", "title": "Every code shows", "em": "its reasons.",
             "text": "Each suggested code comes with a confidence score and a short reason, so your team can check it. Nothing moves forward until a person approves it.",
             "cards": [{"type": "codes", "eyebrow": "Suggested · example", "codes": [("CPT", "99214", "Moderate MDM", "92%"), ("ICD-10", "J18.1", "Lobar pneumonia", "94%"), ("ICD-10", "E11.65", "T2DM, hyperglycemia", "93%")]}]},
            {"eyebrow": "Checked first", "title": "Problems caught", "em": "before the payer sees them.",
             "text": "Every claim is held for a person to approve. Before that, Althais checks codes against about 62 common NCCI bundling pairs (not the full CMS table) and flags items that are missing.",
             "cards": [{"type": "rows", "eyebrow": "Before approval · example", "rows": [("NCCI bundling", "0 conflicts", "g"), ("Missing items", "flagged for review", "a"), ("Claim", "Held for approval", "a")]}]},
            {"eyebrow": "Althea", "title": "An assistant that", "em": "scribes the visit.",
             "text": "Say “scribe my visit” and Althea listens to the encounter, writes the note into the chart and gets the codes. She also reads back allergies, medications and claim status on request.",
             "cards": [{"type": "chat", "eyebrow": "Althea", "chat": [("u", "Althea, scribe my visit with Maria Alvarez."), ("a", "Scribing the visit. I'll stay quiet and listen. Say <mark>end visit</mark> when it's over.")]}]},
        ],
        "grid_label": "And six more",
        "grid": [("One workspace", "Patients, schedule, charts, notes, codes and claims live in one place. Althais does not connect to other EHRs today."),
                 ("Appeal letters on demand", "Paste in the denial text and an AI model drafts an appeal letter for your team to review."),
                 ("Time-based codes, exactly", "Critical care thresholds, office time ranges and prolonged services are computed, not guessed."),
                 ("Staff onboarding built in", "Invitations, credentials, Althais Training and role-based access, instead of separate HR tools."),
                 ("Billing setup tracking", "Checklists, NPI checks against the public NPPES registry and prepared enrollment packets help you get ready to bill payers."),
                 ("Training built in", "Training modules for your staff are part of the product. See the Pricing page for plans.")],
        "table_head": ("Side by side", "Althais and", "a traditional EMR."),
        "table": {"cols": ["Althais", "Traditional EMR, typically"], "rows": [
            ("Writing the note", "AI Scribe or Althea drafts the SOAP note for you to sign", "Typed by the provider, or a scribe add-on bought separately"),
            ("Choosing codes", "Suggested from the note, with confidence and the supporting text", "Picked by hand, or sent to a coding team or vendor"),
            ("Time-based codes", "Computed from documented minutes (critical care, office time, prolonged services)", "Looked up and applied by hand"),
            ("Bundling checks", "Checked against about 62 common NCCI pairs before a person approves", "Often caught by the clearinghouse or after a denial"),
            ("Not ready to bill a payer", "Every claim is held for a person to approve; readiness checklists show what is missing", "Rejected or denied later"),
            ("Denials and appeals", "Paste in the denial text and an appeal letter is drafted for review", "Worked by hand in payer portals"),
            ("Help in the moment", "Althea answers about the visit on screen, by voice or text", "Help articles and support tickets"),
            ("Staff onboarding", "Invites, credentials, training and roles built in", "Separate HR and credentialing tools"),
            ("Switching", "A separate workspace; it does not connect to other EHRs today", "Full EMR changes are often long, all-at-once projects"),
        ]},
        "timeline_head": ("Switching", "Moving over", "one step at a time."),
        "timeline": [("Step 1", "Start small", "Try Althais on a few visits while your current system keeps running."),
                     ("Step 2", "Set up", "Enter your practice, provider and payer details."),
                     ("Step 3", "Compare", "Compare the notes and codes with your usual way before you move more over."),
                     ("Step 4", "Add your team", "Invite staff, set roles and train them with Althais Training.")],
        "faq": [("Do we have to replace our EMR?", "Althais has its own EMR-style workspace for patients, schedule, charts, notes, codes and claims. It does not connect to other EHRs today, so you can try it alongside your current system or move over."),
                ("Does Althais work with Epic, athenahealth, eClinicalWorks or NextGen?", "Not today. Althais has no connections to Epic, athenahealth, eClinicalWorks, NextGen or any other EHR."),
                ("Who is responsible for the codes?", "Your team. Althais suggests codes with reasons; a person approves every one before it reaches a claim."),
                ("Can we try it first?", "Yes. Demo mode uses sample data so you can look around first.")],
    },
}

def _view(href):
    async def view(request: Request, user=Depends(current_user)):
        return platform_pages.render(request, user, PAGES[href], href, "For Your Practice", NAV)
    view.__name__ = "practice_" + href.strip("/").replace("-", "_")
    return view


for _href in PAGES:
    router.add_api_route(_href, _view(_href), methods=["GET"], include_in_schema=False)

platform_pages.register("For Your Practice", PAGES, NAV)
