"""
platform_pages.py: the five Platform pages (AI Scribe, Medical Coding, Claims & Insurance, Althea, Team & Onboarding),
built in the landing page's style (templates/platform_page.html, static/althais-landing.css).

Each page: a hero with a product card, three alternating feature rows each with its own mock card, a capability grid,
FAQs, and the dark call to action. Mock cards use example data only (labeled "Example" where it could read as real).
Card types (rendered by the `mock` macro): note, rows, codes, chips, claims, chat, people, checklist.
"""

from fastapi import APIRouter, Depends, Request

from auth import current_user

router = APIRouter()
_templates = None   # set by main.py

NAV = [("AI Scribe", "/platform/ai-scribe"), ("Medical Coding", "/platform/medical-coding"), ("Claims & Insurance", "/platform/claims-insurance"),
       ("Althea", "/platform/althea"), ("Team & Onboarding", "/platform/team-onboarding")]


REGISTRY = {}   # href -> {"section", "name", "text", "demo"}: every page built on this template, for "Keep exploring"
CROSS = {"Platform": "/how-it-works", "For Your Practice": "/platform/ai-scribe", "Solutions": "/platform/medical-coding",
         "Resources": "/platform/ai-scribe", "Company": "/how-it-works"}


def register(section: str, pages: dict, nav: list):
    names = {h: n for n, h in nav}
    for href, p in pages.items():
        REGISTRY[href] = {"section": section, "name": names.get(href, p["nav"]), "text": p.get("card") or p["lede"], "demo": bool(p.get("demo")), "href": href, "noindex": bool(p.get("noindex"))}


def related(here: str, section: str, nav: list) -> list:
    """Three neighbours from the same section, then one page from elsewhere on the site."""
    own = [REGISTRY[h] for _, h in nav if h != here and h in REGISTRY]
    i = [h for _, h in nav].index(here) if here in [h for _, h in nav] else 0
    own = own[i:] + own[:i]
    cross = REGISTRY.get(CROSS.get(section, ""))
    out = own[:3] + ([cross] if cross and cross["href"] != here else own[3:4])
    return out


def render(request: Request, user, page: dict, here: str, section: str, nav: list, ctas=None):
    """Shared by every page built on templates/platform_page.html (Platform, For Your Practice, Solutions, Resources, Company)."""
    return _templates.TemplateResponse(request, "platform_page.html", {
        "user": user, "page": page, "here": here, "section": section, "nav_items": nav,
        "ctas": page.get("ctas", ctas) or [], "related": related(here, section, nav)})

PAGES = {
    "ai-scribe": {
        "demo": "ai-scribe", "card": 'Record or paste a visit; get a SOAP note to review and sign.',
        "specs": [('Capture', 'Live recording in the browser, or a pasted transcript'), ('Consent', 'A patient-consent check must be ticked before recording starts'), ('Note sections', 'Chief complaint, HPI, review of systems, vitals, exam, assessment and plan'), ('More history', 'Current medications, allergies, past medical, surgical and family history'), ('Visit types', 'Office visit, follow-up, new patient, telehealth, urgent care, emergency and procedures'), ('Review', 'Every field stays editable; the draft is labeled until you sign it'), ('Sign', 'You review the draft, edit anything, then mark the note signed'), ('After signing', 'Copy, download, add to the chart, or send straight to Coding')],
        "nav": "AI Scribe", "eyebrow": "AI Scribe",
        "title": "Say the visit.", "em": "Get the note.",
        "lede": "Record the encounter or paste a transcript. Althais drafts a structured SOAP note in the way you'd write it, ready for you to review and sign.",
        "meta": "Althais AI Scribe turns a recorded visit or transcript into a structured SOAP note you review, edit and sign.",
        "hero": [
            {"type": "note", "eyebrow": "Example · you say", "text": "58-year-old with chest pain and shortness of breath for two hours. BP 148/92, HR 88. EKG normal sinus rhythm, troponin pending. Rule out ACS, serial troponins, cardiology consult."},
            {"type": "rows", "eyebrow": "Example SOAP note · draft", "soft": True, "rows": [("Subjective", "Chest pain, SOB × 2 hr", ""), ("Objective", "BP 148/92 · HR 88 · NSR", ""),
                                                                                  ("Assessment", "Rule out ACS", ""), ("Plan", "Serial troponins, cardiology", ""), ("Status", "Ready to sign", "g")]},
        ],
        "rows": [
            {"eyebrow": "Capture", "title": "However you already work.", "em": "Spoken or typed.",
             "text": "Record the visit live, or paste a transcript from another tool. Say it the way you'd tell a colleague. There's nothing to memorize.",
             "cards": [{"type": "chips", "eyebrow": "Bring in the visit", "chips": ["Record live", "Paste transcript", "Type it"]},
                       {"type": "rows", "eyebrow": "Example visit", "soft": True, "rows": [("Visit type", "Office visit · established", ""), ("Length", "18 min", ""), ("Captured", "Transcript", "g")]}]},
            {"eyebrow": "Structure", "title": "A real SOAP note,", "em": "not a text box to fix.",
             "text": "Althais organizes what was said into Subjective, Objective, Assessment and Plan, so you can read it, fix it and sign it.",
             "cards": [{"type": "rows", "eyebrow": "Example note", "rows": [("Chief complaint", "Chest pain, SOB", ""), ("History", "2 hr onset, at rest", ""), ("Exam", "Lungs clear, no edema", ""),
                                                                             ("Assessment", "Rule out ACS", ""), ("Plan", "Troponins, cardiology", ""), ("Status", "Draft to review", "")]}]},
            {"eyebrow": "Sign", "title": "Nothing is final", "em": "until you sign it.",
             "text": "Every note starts as a draft. Change anything, then sign when it says what you meant. Signed notes go to the chart, to your clipboard or to a download, and straight into coding.",
             "cards": [{"type": "checklist", "eyebrow": "Before it's signed", "items": [("Review the draft", True), ("Edit anything that needs your judgment", True), ("Sign the note", True), ("Send to Medical Coding", False)]},
                       {"type": "chips", "eyebrow": "After signing", "soft": True, "chips": ["Copy", "Download", "Add to chart", "Code this note"]}]},
        ],
        "grid": [("Record or paste", "Live recording, or a transcript from another tool."), ("Structured SOAP", "Organized into Subjective, Objective, Assessment and Plan."),
                 ("Drafts you control", "Edit freely. Nothing is final until you sign."), ("Into the chart", "Copy, download or chart the signed note."),
                 ("Straight to coding", "A signed note flows into Medical Coding."), ("You stay in charge", "A person reviews and signs every note.")],
        "faq": [("Does the scribe replace my judgment?", "No. It writes a draft. Nothing becomes part of the record until you review and sign it."),
                ("Can I use transcripts from another tool?", "Yes. Paste a transcript and Althais builds the note from it."),
                ("What happens after I sign?", "The note is ready for Medical Coding, which suggests CPT and ICD-10 codes with the reasons behind each one.")],
        "next": "medical-coding",
    },
    "medical-coding": {
        "demo": "medical-coding", "card": 'CPT and ICD-10 codes with confidence and reasons, checked before billing.',
        "specs": [('Code sets', 'CPT and HCPCS procedures, ICD-10-CM diagnoses'), ('Inputs', 'A note from Scribe or the EMR, or any pasted note, plus encounter type and visit minutes'), ('Encounter types', 'Office / outpatient, urgent care and emergency department'), ('Time-based rules', 'Office E/M by total time, critical care 99291 and 99292 thresholds, prolonged services'), ('Emergency visits', 'ED levels 99281 to 99285 follow medical decision making, not time'), ('Bundling', 'Codes are checked against a built-in list of about 62 common NCCI code pairs. It is not the full CMS table'), ('Format checks', 'Malformed CPT, HCPCS and ICD-10 codes are flagged before they reach a claim'), ('Confidence floor', "Suggestions under your clinic's confidence setting are set aside until you ask for them"), ('Export', 'Copy the codes or export them to CSV')],
        "nav": "Medical Coding", "eyebrow": "Medical Coding",
        "title": "Codes you can defend,", "em": "with the reasons attached.",
        "lede": "Althais reads the note and suggests ICD-10 and CPT codes, each with a confidence score and the documentation behind it. You decide on every one.",
        "meta": "Althais Medical Coding suggests CPT and ICD-10 codes from the clinical note with confidence and reasons, and checks them for common bundling conflicts before you build a claim.",
        "hero": [
            {"type": "codes", "eyebrow": "Example · suggested codes", "codes": [("CPT", "99285", "ED visit, high complexity", "95%"), ("ICD-10", "R07.9", "Chest pain, unspecified", "90%"), ("ICD-10", "R06.02", "Shortness of breath", "85%")]},
            {"type": "chips", "eyebrow": "Your call on every one", "soft": True, "tags": [("Keep", ""), ("Remove", "n"), ("Add your own", "n")]},
        ],
        "rows": [
            {"eyebrow": "Confidence", "title": "See what's solid,", "em": "and what needs a look.",
             "text": "Every suggestion carries a confidence score, so you know at a glance where to spend your attention. Codes with a lower score are the ones to look at more closely.",
             "cards": [{"type": "codes", "eyebrow": "Example · office visit", "codes": [("CPT", "99214", "Established patient, moderate", "93%"), ("ICD-10", "E11.9", "Type 2 diabetes", "96%"), ("ICD-10", "I10", "Essential hypertension", "94%"), ("CPT", "83036", "Hemoglobin A1c", "71%")]}]},
            {"eyebrow": "Reasons", "title": "Every code points", "em": "back to the note.",
             "text": "Each suggestion comes with a short reason explaining why it was chosen, so you can check it against the note yourself.",
             "cards": [{"type": "rows", "eyebrow": "Example · Why 99214", "rows": [("Problems addressed", "2 chronic, 1 worsening", ""), ("Data reviewed", "A1c, BMP ordered", ""), ("Risk", "Prescription drug management", ""), ("MDM level", "Moderate", "g")]},
                       {"type": "rows", "eyebrow": "Example · from a note", "soft": True, "rows": [("“A1c up to 8.4…”", "E11.9", ""), ("“BP 148/92 on lisinopril…”", "I10", "")]}]},
            {"eyebrow": "Check", "title": "Checked before", "em": "it ever leaves.",
             "text": "Codes are compared against a built-in list of about 62 common bundling pairs, so some conflicts are caught early. It is not the full CMS table and it does not read modifiers already on the claim, so your biller should still review.",
             "cards": [{"type": "rows", "eyebrow": "Example · the check", "rows": [("Bundling conflicts", "0 found in the built-in list", "g"), ("Code format", "checked", "")]}]},
        ],
        "grid": [("Code A Note", "CPT and ICD-10 suggestions from a finished note."), ("Confidence scores", "Know where to look closer."), ("Reasons attached", "Each code comes with a short reason."),
                 ("Check Codes", "Paste codes you chose and check them against the note."), ("Bundling checks", "A built-in list of common code pairs is checked."), ("Human approval", "Nothing bills without your decision.")],
        "faq": [("Who is responsible for the final codes?", "Your team. Althais suggests and explains; a person approves every code before it reaches a claim."),
                ("Can it check codes I picked myself?", "Yes. Check Codes compares your codes with the note and flags anything the documentation doesn't support."),
                ("Which code sets does it use?", "CPT and HCPCS for procedures and ICD-10-CM for diagnoses. Bundling is checked against a built-in list of about 62 common NCCI pairs, not the full CMS table.")],
        "next": "claims-insurance",
    },
    "claims-insurance": {
        "demo": "claims-insurance", "card": 'Build and check claims, track denials and draft appeal letters.',
        "specs": [('Claims queue', 'Every claim in one list with status, payer, amount, risk and AI confidence'), ('Statuses', 'Pending, submitted, held, denied, appealed and paid, set by your staff'), ('Import', 'Bring in existing claims from a CSV file'), ('Bundling check', 'Codes are checked against a short list of common code pairs that should not be billed together. It is not the full CMS list.'), ('Held claims', 'Every claim is held for a person to approve'), ('Submission', 'Not available yet. Althais does not send claims to payers or clearinghouses today.'), ('Denials', 'Your staff enter the denial and paste in the denial text. Althais drafts an appeal letter for a person to review.'), ('Billing activation', 'A guided setup of practice, provider and payer details before the first claim')],
        "nav": "Claims & Insurance", "eyebrow": "Claims & Insurance",
        "title": "From approved codes", "em": "to a clean claim.",
        "lede": "Althais assembles the claim from approved codes, checks it for common bundling problems and holds it for a person to approve. When a claim is denied, it drafts an appeal letter for you to review.",
        "meta": "Althais Claims & Insurance builds and checks claims, holds them for your approval, and drafts appeal letters for denials you enter.",
        "hero": [
            {"type": "claims", "eyebrow": "Claims overview · example", "claims": [("CHC-2026-00412", "Smith, John · 99291", "Submitted", ""), ("CHC-2026-00411", "Patel, R. · 99285", "Paid", ""),
                                                                                 ("CHC-2026-00409", "Torres, M. · 99283", "Denied", "w"), ("CHC-2026-00408", "Kim, S. · 99284", "Paid", "")]},
            {"type": "rows", "eyebrow": "Denied claims", "soft": True, "rows": [("Appeal letter for CHC-2026-00409", "ready", "g")]},
        ],
        "rows": [
            {"eyebrow": "Assemble", "title": "Everything in one claim,", "em": "ready to review.",
             "text": "Patient, payer, codes, diagnosis pointers and provider come together on a CMS-1500 claim. You read it once before it goes.",
             "cards": [{"type": "rows", "eyebrow": "CMS-1500 · example", "rows": [("Patient", "Demo Patient, 54", ""), ("Payer", "Entered by your team", ""), ("Lines", "99285 · R07.9, R06.00", ""), ("Rendering provider", "NPI on file", ""), ("Status", "Ready for review", "g")]}]},
            {"eyebrow": "Gate", "title": "Held, not bounced,", "em": "when something's missing.",
             "text": "Every claim is held until a person approves it. Althais also checks the codes against a short list of common bundling pairs, so your team can fix a problem before approving. This check does not cover every rule and does not read modifiers already on the claim.",
             "cards": [{"type": "rows", "eyebrow": "Checks · example", "rows": [("Bundling check", "no conflicts found", "g"), ("Person approval", "waiting", "a")]},
                       {"type": "rows", "eyebrow": "Held claim · example", "soft": True, "rows": [("Reason", "Missing referring NPI", "a"), ("Next step", "Add it, then approve", "")]}]},
            {"eyebrow": "Track", "title": "Denials tracked by your team.", "em": "Appeal letters drafted.",
             "text": "Your staff mark a claim as denied and paste in the denial text. Althais then drafts an appeal letter on request, and a person reviews it. Denials are not received from payers automatically, and they are saved in your browser.",
             "cards": [{"type": "checklist", "eyebrow": "CHC-2026-00409 · example", "items": [("Marked denied by staff", True), ("Denial text pasted in", True), ("Appeal letter drafted", True), ("Letter reviewed by a person", False)]}]},
        ],
        "grid": [("Claims builder", "CMS-1500 claims assembled from approved codes."), ("Bundling check", "Common code-pair problems flagged."),
                 ("Held for approval", "A person approves every claim."), ("Denials and appeals", "Paste the denial, get a draft letter."),
                 ("Claims queue", "Every claim in one list."), ("Billing activation", "Guided setup before the first claim.")],
        "faq": [("Does Althais send claims to payers?", "Not today. Althais does not connect to a clearinghouse or send claims to any payer. You still submit claims the way you do now."),
                ("What happens when a claim is denied?", "Your staff mark it denied and paste in the denial text. Althais can then draft an appeal letter for a person to review."),
                ("Does a person approve claims?", "Yes. Every claim is held until a person approves it.")],
        "next": "althea",
    },
    "althea": {
        "demo": "althea", "card": 'An assistant that answers questions and helps with steps in Althais.',
        "specs": [('Where', 'One click away on every Althais page'), ('Questions', 'Answers questions about Althais in plain language'), ('Product help', 'How to do anything in Althais, in plain language'), ('Clinic control', 'Althea is switched on for each clinic by Althais. Managers can turn off pages and features, including Althea, for a person'), ('Plans', 'Included with the full suite, or switched on for a clinic by Althais'), ('Themes', 'Follows light and dark mode')],
        "nav": "Althea Assistant", "eyebrow": "Althea Assistant",
        "title": "Ask Althea.", "em": "Get back to patients.",
        "lede": "Althea is the AI inside Althais. Ask how to do something, what a screen means, or what's at risk today, and get a plain answer in seconds.",
        "meta": "Althea is the AI assistant inside Althais: plain-language answers and help with steps inside Althais.",
        "hero": [
            {"type": "chat", "eyebrow": "Althea · example", "chat": [("u", "Why was 99285 suggested for this visit?"),
                                                          ("a", "The note documents a high-complexity ED visit: chest pain with possible ACS, an EKG, labs and a cardiology consult. That meets the level for <mark>99285</mark>.")]},
        ],
        "rows": [
            {"eyebrow": "Ask anything", "title": "Ask the way you'd ask", "em": "a colleague.",
             "text": "No manuals to search and no tickets to file. Type your question in your own words and Althea answers in plain language, with where to go next.",
             "cards": [{"type": "chat", "eyebrow": "Althea · example", "chat": [("u", "How do I send a claim that was held?"), ("a", "Open <mark>Claims</mark>, read the reason the claim is held and fix it. A person has to approve the claim. Althais does not send claims to a payer for you.")]}]},
            {"eyebrow": "In context", "title": "Help with the steps,", "em": "not just answers.",
             "text": "Althea can help you start a note, get code suggestions and prepare a claim for review. A person still reviews and approves each step.",
             "cards": [{"type": "rows", "eyebrow": "Example visit", "rows": [("Note", "Chest pain visit, signed", ""), ("Codes", "99285 · R07.9 · R06.00", ""), ("Claim", "Ready for review", "g")]},
                       {"type": "chat", "eyebrow": "Althea · example", "soft": True, "chat": [("u", "Anything missing before I file?"), ("a", "Check the codes and the bundling results, then review the claim. A person approves it before it is final.")]}]},
            {"eyebrow": "Your clinic decides", "title": "On where you want her,", "em": "off where you don't.",
             "text": "Althea is switched on for each clinic by Althais. Managers can turn off parts of Althais for a person, including Althea.",
             "cards": [{"type": "rows", "eyebrow": "Clinic settings · example", "rows": [("Althea", "On", "g"), ("In the EMR", "Shown", ""), ("In Revenue", "Shown", ""), ("In Staff Portal", "Hidden", "a")]}]},
        ],
        "grid": [("Plain answers", "No jargon, no manuals."), ("Knows Althais", "Every step, from note to claim."), ("Helps with steps", "Can help start a note, suggest codes and prepare a claim for review."),
                 ("Always one click away", "Open her from any page."), ("Helps new staff", "Learn by asking."), ("Clinic controls", "On, off, or hidden by area.")],
        "faq": [("Is Althea available on every plan?", "Not automatically. Althea comes with the full suite, and Althais can also switch her on for a single clinic."),
                ("Can we turn her off?", "Althea is switched on or off for each clinic, and managers can hide parts of Althais from a person."),
                ("Can I try her now?", "Yes. Open Althea from the bottom corner of the Althais home page.")],
        "next": "team-onboarding",
    },
    "team-onboarding": {
        "demo": "team-onboarding", "card": 'Invite staff, collect documents, train them and set access by role.',
        "specs": [('Invitations', 'Each invite creates a sign-in and a guided Staff Portal setup'), ('Documents', 'Licenses, certifications and IDs, with expiration dates tracked'), ('Forms', 'Policies and onboarding forms signed inside the portal'), ('Training', 'Althais Training: guided lessons, interactive practice and a quiz, by role'), ('Billing readiness', 'A manager can keep a biller in their portal until billing training and forms are done'), ('Roles', 'Provider, biller, front desk and manager, each with adjustable access'), ('Portal lock', "Send someone back to their portal to finish training; access returns when they're done"), ('Audit', 'Onboarding steps and access changes are recorded')],
        "nav": "Team & Onboarding", "eyebrow": "Team & Onboarding",
        "title": "Your team,", "em": "set up right from day one.",
        "lede": "Invite staff, collect their documents, assign training, and give each person exactly the access their role needs, all in one place.",
        "meta": "Althais Team & Onboarding handles staff invitations, documents, credentials, training and role-based access for your clinic.",
        "hero": [
            {"type": "people", "eyebrow": "Team · example", "people": [("PR", "Priya Raman", "Provider", "Active", ""), ("BL", "Bea Lee", "Biller", "Training", "w"), ("FO", "Fay Ortiz", "Front Desk", "Onboarding", "w")]},
            {"type": "rows", "eyebrow": "Bea Lee · onboarding", "soft": True, "rows": [("Documents", "3 of 3", "g"), ("Billing training", "in progress", "a"), ("Access", "Staff Portal only", "")]},
        ],
        "rows": [
            {"eyebrow": "Invite", "title": "One invitation,", "em": "and they take it from there.",
             "text": "Add a person and choose their role. They get a sign-in and finish onboarding in their own Staff Portal: forms, documents and training, at their own pace.",
             "cards": [{"type": "checklist", "eyebrow": "Fay Ortiz · Staff Portal", "items": [("Accept the invitation", True), ("Upload ID and certifications", True), ("Sign policies", True), ("Complete Althais Training", False)]}]},
            {"eyebrow": "Train", "title": "Training that teaches", "em": "the real thing.",
             "text": "Althais Training walks each role through the product with guided lessons, interactive practice and a short quiz. A manager can keep a biller in their portal until billing training is done.",
             "cards": [{"type": "rows", "eyebrow": "Althais Training · example", "rows": [("Tour the EMR", "done", "g"), ("Write and sign a note", "done", "g"), ("Practice a claim", "in progress", "a"), ("Final quiz", "not started", "")]}]},
            {"eyebrow": "Access", "title": "Exactly the access", "em": "each role needs.",
             "text": "Providers, billers, front desk and managers each get the permissions their job calls for. Managers can adjust roles, and can send someone back to their portal to finish training. Access returns automatically when they're done.",
             "cards": [{"type": "rows", "eyebrow": "Roles · example", "rows": [("Provider", "EMR, Scribe, Coding", ""), ("Biller", "Claims", ""), ("Front Desk", "Schedule, Patients", ""), ("Manager", "Everything + Team", "g")]}]},
        ],
        "grid": [("Invitations", "A sign-in and a guided setup for each person."), ("Documents", "Licenses and certifications, with expirations tracked."),
                 ("Althais Training", "Lessons, practice and a quiz by role."), ("Roles & permissions", "Access matched to each job."),
                 ("Billing readiness", "Managers can require billing training first."), ("Pause access", "Send someone back to finish training.")],
        "faq": [("Do staff need an Althais account first?", "No. The invitation creates their sign-in and walks them through setup."),
                ("Can access be limited by role?", "Yes. Each role has its own permissions, and managers can adjust them."),
                ("What if someone hasn't finished training?", "A manager can lock them to their Staff Portal until it's done; access returns automatically when they finish.")],
        "next": "ai-scribe",
    },
}


def _view(slug):
    async def view(request: Request, user=Depends(current_user)):
        return render(request, user, PAGES[slug], f"/platform/{slug}", "Platform", NAV,
                      ctas=[("Try the demo", "#demo"), ("See the details", "#specs")])
    view.__name__ = "platform_" + slug.replace("-", "_")
    return view


for _slug in PAGES:
    router.add_api_route(f"/platform/{_slug}", _view(_slug), methods=["GET"], include_in_schema=False)

register("Platform", {f"/platform/{k}": v for k, v in PAGES.items()}, NAV)
