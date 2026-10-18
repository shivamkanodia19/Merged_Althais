"""
more_pages.py: the Solutions, Resources and Company pages from the site footer, in the landing page's style.
Rendered by platform_pages.render with templates/platform_page.html (same template as Platform and For Your Practice).

Copy comes from what the site already says: the Solutions segments and their stories (marketing_data.SOLUTION_SEGMENTS),
the resource library (marketing_data.RESOURCE_ARTICLES), and the About page (two co-founders). Book A Demo (/demo) and
Join The Pilot (/pilot) keep their own pages because they carry the sign-up forms.
"""

from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

import platform_pages
import seo_pages
from auth import current_user
from marketing_data import RESOURCE_ARTICLES, RESOURCE_CATEGORIES, SOLUTION_SEGMENTS

router = APIRouter()
SEG = {s["id"]: s for s in SOLUTION_SEGMENTS}
OWN_PAGE = ("private-practices", "hospital-systems", "revenue-cycle-teams")

SECTIONS = {
    "Solutions": [("Private Practices", "/solutions/private-practices"), ("Hospital Systems", "/solutions/hospital-systems"),
                  ("Revenue Cycle Teams", "/solutions/revenue-cycle-teams"), ("All Solutions", "/solutions")],
    "Resources": [("Resources", "/resources"), ("Case Studies", "/case-studies"), ("Walkthrough", "/walkthrough"),
                  ("ROI Calculator", "/roi-calculator"), ("FAQs", "/faq")],
    "Company": [("Our Story", "/about"), ("Careers", "/careers"), ("Contact Us", "/contact"), ("Book A Demo", "/demo"), ("Join The Pilot", "/pilot")],
}


def _seg_href(seg_id):
    return f"/solutions/{seg_id}" if seg_id in OWN_PAGE else f"/solutions#{seg_id}"


FIT = {  # which tier and tools each kind of organization usually starts with (tiers as on /pricing)
    "private-practices": ("Starter", "Code suggestions, a claims builder, and a Scribe that drafts notes from the visit.", ["AI Scribe", "Medical Coding", "Claims & Insurance"]),
    "hospital-systems": ("Enterprise", "Staff roles, training modules, credential tracking and onboarding for a larger team.", ["Medical Coding", "Claims & Insurance", "Team & Onboarding"]),
    "multi-specialty-groups": ("Professional", "Code suggestions and staff roles for a group with several providers.", ["Medical Coding", "Claims & Insurance"]),
    "urgent-care": ("Professional", "A Scribe note and code suggestions for each visit. A person approves every claim.", ["AI Scribe", "Medical Coding", "Claims & Insurance"]),
    "fqhc": ("Professional", "Code suggestions and a bundling check, with a person approving every claim.", ["Medical Coding", "Claims & Insurance"]),
    "specialty-clinics": ("Professional", "Code suggestions and a bundling check against about 62 common code pairs. The check does not read modifiers already on the claim.", ["Medical Coding", "Claims & Insurance"]),
    "revenue-cycle-teams": ("Professional", "A claims queue where a person approves each claim, a bundling check, and appeal letters drafted from denial text you paste in.", ["Claims & Insurance", "Medical Coding", "Team & Onboarding"]),
    "medical-billers": ("Starter", "One claims queue, plus appeal letters drafted from denial text you paste in.", ["Claims & Insurance", "Althea Assistant"]),
}
TOOL_HREF = {"AI Scribe": "/platform/ai-scribe#demo", "Medical Coding": "/platform/medical-coding#demo", "Claims & Insurance": "/platform/claims-insurance#demo",
             "Team & Onboarding": "/platform/team-onboarding#demo", "Althea Assistant": "/platform/althea#demo"}


def _stat(r):
    v = r["value"]
    num = f"{v:.{r['decimals']}f}" if r.get("decimals") else f"{v:,.0f}"
    return (f"{r.get('prefix', '')}{num}{r.get('suffix', '')}", r["label"])


def _segment_page(seg_id, title, em):
    s = SEG[seg_id]
    tier, why, tools = FIT.get(seg_id, ("Professional", "", []))
    page = {
        "ctas": [("See what changes", "#rows"), ("Try the " + tools[0] + " demo", TOOL_HREF[tools[0]])] if tools else [("See what changes", "#rows")],
        "card": s["headline"],
        "recommend": {"tier": tier + " tier", "text": why, "tools": [(t, TOOL_HREF[t]) for t in tools]},
        "nav": s["label"], "eyebrow": s["label"], "title": title, "em": em, "lede": s["headline"],
        "meta": f"Althais for {s['label']}: {s['headline']}",
        "hero": [{"type": "list", "eyebrow": "Common pressures", "list": s["problems"][:3]}],
        "rows": [
            {"eyebrow": "The problem", "title": "What gets", "em": "in the way.", "text": "Common pressures for " + s["label"].lower() + ".",
             "cards": [{"type": "list", "eyebrow": "The problem", "list": s["problems"]}]},
            {"eyebrow": "Today", "title": "How it's", "em": "usually done.", "text": "The workarounds teams fall back on when coding and claims are done by hand.",
             "cards": [{"type": "list", "eyebrow": "How it's done today", "list": s["workflow"]}]},
            {"eyebrow": "With Althais", "title": "What", "em": "changes.", "text": "Althais drafts and checks. Your team makes the decisions.",
             "cards": [{"type": "list", "eyebrow": "With Althais", "good": True, "list": s["solution"]}]},
        ],
        "links_head": ("Also built for", "Every kind of", "care setting."),
        "links_grid": [{"eyebrow": o["label"], "title": o["label"], "text": o["headline"], "href": _seg_href(o["id"])}
                       for o in SOLUTION_SEGMENTS if o["id"] != seg_id][:3],
        "faq": [("How do we start?", "Try the demo tools on this site. They use simulated sample data. Then contact us and tell us about your clinic."),
                ("Who approves the codes?", "Your team. Every claim is held for a person to approve."),
                ("Can we start with a pilot?", "You can ask to join the pilot from the Join the Pilot page. Althais is early, and we cannot promise a start date.")],
    }
    return page


PAGES = {
    # ── Solutions ─────────────────────────────────────────────────────────────
    "/solutions/private-practices": _segment_page("private-practices", "A full billing team,", "without hiring one."),
    "/solutions/hospital-systems": _segment_page("hospital-systems", "One standard,", "across every facility."),
    "/solutions/revenue-cycle-teams": _segment_page("revenue-cycle-teams", "Your team,", "at full throughput."),
    "/solutions": {
        "nav": "All Solutions", "eyebrow": "All Solutions",
        "title": "Built for every", "em": "care setting.",
        "lede": "Althais is early software for clinics and billing teams. Here is where each kind of team could start.",
        "meta": "Althais solutions for hospital systems, multi-specialty groups, private practices, urgent care, FQHCs, specialty clinics, revenue cycle teams and medical billers.",
        "hero": [{"type": "chips", "eyebrow": "Who it's for", "chips": [s["label"] for s in SOLUTION_SEGMENTS]}],
        "links_head": ("Solutions", "Find your", "starting point."),
        "links_grid": [{"eyebrow": s["label"], "title": s["label"], "text": s["headline"], "href": _seg_href(s["id"]),
                        "go": "See how" if s["id"] in OWN_PAGE else "Learn more"} for s in SOLUTION_SEGMENTS],
        "ctas": [("Find your setup", "#compare-tiers"), ("Compare tiers", "/pricing#compare-tiers")],
        "card": "Kinds of teams Althais could help.",
        "matrix_head": ("Which setup fits", "Where each kind of team", "could start."),
        "matrix": {"cols": ["Suggested tier", "Tools to try first"], "groups": [("By organization", [
            (o["label"], [FIT[o["id"]][0], ", ".join(FIT[o["id"]][2])]) for o in SOLUTION_SEGMENTS if o["id"] in FIT])]},
        "faq": [("Does Althais work for small practices?", "Yes. Small clinics are who we build for first. The Starter tier covers notes, code suggestions and claim checking."),
                ("Can large systems standardize on it?", "We do not know yet. Althais is early and has not been tested across a large system. Tell us what you need and we will say honestly if it fits."),
                ("Which care settings does it support?", "Althais has no features built for one care setting. The same tools are meant for any clinic or billing team that does its own coding and claims. The groups on this page are examples, not a list of customers.")],
    },

    # ── Resources ─────────────────────────────────────────────────────────────
    "/resources": {
        "nav": "Resources", "eyebrow": "Resources",
        "title": "Guides, updates", "em": "and insights.",
        "lede": "Guides for the people who work the claims: denied claims, appeal letters, bundling and denial codes.",
        "meta": "Plain-language guides for clinic billing teams on denied claims, appeal letters, NCCI bundling and denial codes.",
        "hero": [{"type": "chips", "eyebrow": "Topics", "chips": ["Denied claims", "Appeal letters", "NCCI bundling", "Denial codes"]}],
        "links_head": ("Guides", "Plain-language help", "for billing teams."),
        "links_grid": seo_pages._more(""),
        "faq": [("How often are the guides updated?", "We review each guide when the rules it describes change, and the date is shown at the bottom of each one."),
                ("Can I suggest a topic?", "Please do. Tell us what your team is wrestling with.")],
    },
    "/case-studies": {
        "nav": "Case Studies", "eyebrow": "Case Studies",
        "title": "Case studies,", "em": "once they are real.",
        "lede": "We will publish a clinic's story only after that clinic has approved it in writing, and only with numbers the clinic measured itself. None are published yet.",
        "meta": "Althais will publish case studies only with a clinic's written approval and its own measured results. None are published yet.",
        "noindex": True,
        "ctas": [("Join the Pilot", "/pilot"), ("See how it works", "/how-it-works")],
        "faq": [("Why are there no case studies yet?", "Althais is early. We would rather show nothing than show numbers that clinics have not measured and approved."),
                ("How will the numbers be measured?", "By the clinic. Each pilot clinic records its own denials, appeals and staff time before and after, and we report what it recorded."),
                ("Can I be one of the first?", "Yes. Join the pilot and tell us about your clinic.")],
    },
    "/walkthrough": {
        "nav": "Walkthrough", "eyebrow": "Walkthrough",
        "title": "One visit,", "em": "start to finish.",
        "lede": "Follow one example visit through Althais, from the conversation in the exam room to a claim held for a person to approve.",
        "meta": "A walkthrough of Althais: one patient visit from the recorded conversation to the SOAP note, codes and a claim held for approval. Example only.",
        "hero": [{"type": "checklist", "eyebrow": "Six stops · example", "items": [("The visit", True), ("The note", True), ("The codes", True), ("The review", True), ("The claim", True), ("The follow-through", False)]}],
        "rows": [
            {"eyebrow": "The visit", "title": "No typing", "em": "during the visit.", "text": "The provider records the conversation or brings in a transcript, and stays with the patient.",
             "cards": [{"type": "note", "eyebrow": "You say", "text": "58-year-old with chest pain and shortness of breath for two hours. EKG normal sinus rhythm, troponin pending. Rule out ACS."}]},
            {"eyebrow": "The note", "title": "A SOAP draft,", "em": "ready to sign.", "text": "AI Scribe drafts the note. The provider edits anything and signs it.",
             "cards": [{"type": "shot", "eyebrow": "Write a note", "src": "/static/screenshots/provider-note.png", "alt": "The SOAP note screen in Althais"}]},
            {"eyebrow": "The codes", "title": "Codes with", "em": "their reasons.", "text": "Medical Coding suggests CPT and ICD-10 codes, each with a confidence score.",
             "cards": [{"type": "shot", "eyebrow": "Suggested codes", "src": "/static/screenshots/ai-coding.png", "alt": "AI-suggested codes with confidence scores"}]},
            {"eyebrow": "The review", "title": "A person", "em": "approves each one.", "text": "The provider or coder accepts, changes or removes each code. Nothing moves on without that approval.",
             "cards": [{"type": "shot", "eyebrow": "Review codes", "src": "/static/screenshots/provider-review.png", "alt": "A provider accepting suggested codes"}]},
            {"eyebrow": "The claim", "title": "Checked,", "em": "then held.", "text": "The claim is assembled and checked against about 62 common bundling pairs, then held for a person to approve. Althais does not send claims to a payer or clearinghouse.",
             "cards": [{"type": "shot", "eyebrow": "Claim form", "src": "/static/screenshots/claim-assembly.png", "alt": "Example claim screen built from approved codes"}]},
            {"eyebrow": "The follow-through", "title": "Denials", "em": "marked by hand.", "text": "Your staff mark a denial by hand. If you paste in the denial text, Althais drafts an appeal letter when you ask. Althais does not receive payer replies or track payments.",
             "cards": [{"type": "shot", "eyebrow": "Claims overview", "src": "/static/screenshots/claim-tracking.png", "alt": "Claims overview (example data)"}]},
        ],
        "faq": [("How long does the whole flow take?", "It depends on how fast your team reviews. Nothing is held up by Althais, and every claim waits for a person to approve it."),
                ("Who approves what?", "Providers sign notes and your team approves every claim. Althais does not send claims out."),
                ("Can I see it live?", "Yes. Try the demo tools on this site. They use simulated sample data, not your own payers.")],
    },
    "/roi-calculator": {
        "nav": "ROI Calculator", "eyebrow": "ROI Calculator",
        "title": "What are denials", "em": "costing you?",
        "lede": "Enter your own numbers to see what denied claims and billing hours may cost your practice. Then pick a cut of your own to see what that would be worth. The sliders start at placeholder values, so change every one to match your practice.",
        "meta": "Estimate what claim denials and billing admin time cost your practice with the Althais ROI calculator.",
        "calculator": True,
        "faq": [("Where do these numbers come from?", "The sliders start at placeholder values we picked so the page is not empty. They are not data and not typical results. Set each one to your own numbers."),
                ("Is this a quote?", "No. It's an estimate to size the problem. A demo looks at your real claims."),
                ("What counts as an unrecovered denial?", "A denied claim that's never appealed or resubmitted, so the revenue is written off.")],
    },
    "/faq": {
        "nav": "FAQs", "eyebrow": "FAQs",
        "title": "Questions,", "em": "answered.",
        "lede": "The things practices ask most before getting started with Althais.",
        "meta": "Frequently asked questions about Althais: what it does today, what it does not do yet, pricing, data handling and how claim approval works.",
        "faq_groups": [
            ("Getting started", [
                ("How long does implementation take?", "We do not promise a set timeline. You can try the demo with sample data today, and contact us to talk about what getting started would look like for your clinic."),
                ("Can we start with a pilot?", "Not as a formal program yet. You can try the demo with sample data. Contact us and we will talk about what a trial could look like for your clinic."),
                ("Do we need a new clearinghouse?", "Althais does not send claims to any clearinghouse or payer today. No clearinghouse is connected. Your staff still submit claims the way they do now.")]),
            ("Coding and claims", [
                ("Who's responsible if a suggested code is wrong?", "A person on your team approves every production claim before it moves forward. Althais shows a confidence score for each suggested code, but it only suggests. Your staff decide."),
                ("What happens to denied claims?", "Althais does not receive denials from payers. Your staff mark a claim as denied and paste in the denial text. Althais can then draft an appeal letter when you ask. A person must review and send it."),
                ("Can Althais check codes we chose ourselves?", "Yes, in part. Check Codes looks at the codes you enter for format problems and for about 62 common code pairs that should not be billed together. It does not cover the full federal list, and it does not read your note to find missing support.")]),
            ("Security and pricing", [
                ("Is my data secure?", "Althais uses staff roles so people only see what their job needs, and it keeps a log of some account actions. Althais does not have a SOC 2 report, and HIPAA has no official certificate. We have not finished the terms for a business associate agreement. Please ask us before putting real patient information into Althais."),
                ("How is pricing structured?", "Plans and prices are listed on the Pricing page. Contact us if you have questions about which plan fits your clinic."),
                ("Can we turn features on and off?", "Managers can invite staff and set a role for each person, which controls what that person can open.")]),
        ],
    },

    # ── Company ───────────────────────────────────────────────────────────────
    "/about": {
        "nav": "Our Story", "eyebrow": "Our Story",
        "title": "Built by two people", "em": "tired of denied claims.",
        "lede": "Althais is a small team building billing software for small clinics. It helps turn a visit into a written note and suggested codes, so there is less paperwork after the visit.",
        "meta": "The Althais story: a small team building billing software that turns patient visits into notes and suggested codes.",
        "story": ("Why we're building Althais",
                  "Clinicians didn't train for years to spend their evenings typing notes and fixing claims.",
                  "Althais helps with the paperwork after the visit. It drafts the note, suggests codes, and holds each claim for a person to approve."),
        "people_head": ("The founders", "Two co-founders,", "one problem."),
        "people": [("KQ", "Kevin Qu", "Co-founder & CEO", ""), ("KY", "Kanishk Yankarla", "Co-founder & CTO", "")],
        "faq": [("How big is the team?", "Two co-founders, and we read every message."),
                ("How do I reach you?", "Email hello@althais.com or use the Contact page."),
                ("Are you hiring?", "See our Careers page, or tell us what you'd like to work on.")],
    },
    "/careers": {
        "nav": "Careers", "eyebrow": "Careers",
        "title": "Help clinicians spend", "em": "more time with patients.",
        "lede": "We're a small team building software to cut down clinic paperwork. If that's work you want to do, we'd like to hear from you.",
        "meta": "Careers at Althais: help build billing and documentation software for small clinics.",
        "grid": [("Work that matters", "Help build tools that cut down paperwork in small clinics."), ("Real ownership", "On a small team, your work goes straight into the product."),
                 ("Built with clinicians", "We want to design with the providers and billers who will use it.")],
        "grid_label": "Why Althais",
        "links": [("Get In Touch", "/contact"), ("Our Story", "/about")],
        "faq": [("Do you have open roles?", "We don't have listings posted right now, but we'd still like to hear from you."),
                ("How do I apply?", "Email hello@althais.com with what you'd like to work on and a link to something you've built."),
                ("Is the team remote?", "Ask us. We'll tell you how we work today.")],
    },
    "/contact": {
        "nav": "Contact Us", "eyebrow": "Contact Us",
        "title": "Ready", "em": "to start?",
        "lede": "Tell us about your practice and we'll be in touch. A demo or a conversation does not commit you to anything. We're a small team.",
        "meta": "Contact Althais: book a demo, join the pilot, or email hello@althais.com.",
        "hero": [{"type": "rows", "eyebrow": "Reach us", "rows": [("Email", "hello@althais.com", "g"), ("Reply", "We reply as soon as we can", "")]}],
        "links_head": ("Ways to reach us", "Pick what", "fits you best."),
        "links_grid": [{"eyebrow": "Email", "title": "hello@althais.com", "text": "Questions, partnerships or anything else. We reply as soon as we can.", "href": "mailto:hello@althais.com", "go": "Email us"},
                       {"eyebrow": "Demo", "title": "Book A Demo", "text": "See Althais work on a sample visit, then ask us how it would fit your clinic.", "href": "/demo", "go": "Book a demo"},
                       {"eyebrow": "Pilot", "title": "Join The Pilot", "text": "Try Althais on your own documentation before rolling it out.", "href": "/pilot", "go": "Join the pilot"}],
        "faq": [("How fast will you reply?", "We reply as soon as we can. We are a small team, so we cannot promise an exact time."),
                ("Is there a commitment?", "No. A demo or a conversation commits you to nothing."),
                ("Who will I talk to?", "One of our two co-founders.")],
    },
}


def _view(href, section):
    nav = SECTIONS[section]

    async def view(request: Request, user=Depends(current_user)):
        return platform_pages.render(request, user, PAGES[href], href, section, nav)
    view.__name__ = "more_" + href.strip("/").replace("/", "_").replace("-", "_")
    return view


for _section, _nav in SECTIONS.items():
    for _name, _href in _nav:
        if _href in PAGES:
            router.add_api_route(_href, _view(_href, _section), methods=["GET"], include_in_schema=False)


for _section, _nav in SECTIONS.items():
    platform_pages.register(_section, {h: PAGES[h] for _, h in _nav if h in PAGES}, _nav)


@router.get("/our-story", include_in_schema=False)
async def our_story():
    return RedirectResponse(url="/about", status_code=302)
