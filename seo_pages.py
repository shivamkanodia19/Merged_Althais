"""
seo_pages.py: plain-language guides for clinic billing teams, built on templates/platform_page.html (page.article).

Each guide targets one search a clinic administrator would really make about denied claims, and answers it in the first
paragraph. What each page says about Althais matches what the product does today: about 62 hand-picked NCCI code pairs, appeal
letters drafted from pasted denial text, a person approving every claim, no payer connection, denials entered by hand.
No savings percentages, customer names or outcome promises belong on these pages.
"""

from fastapi import APIRouter, Depends, Request

import platform_pages
from auth import current_user

router = APIRouter()

NAV = [("Claims savings", "/insurance-claims-savings-for-clinics"), ("Appeal letters", "/denial-appeal-letter-help"),
       ("Bundling check", "/ncci-bundling-check"), ("CO-97 denials", "/co-97-denial-bundled-service"),
       ("CO-50 denials", "/co-50-medical-necessity-denial")]

CTAS = [("Join the Pilot", "/pilot"), ("See how it works", "/how-it-works")]
PHI = ("Denial letters and notes often contain patient details. Take out names, dates of birth and other identifiers before you "
       "paste anything into any tool, or ask us about a business associate agreement first.")
REVIEWED = "Last reviewed October 2026. This is general guidance for clinic staff, not legal or coding advice."


def _more(here):
    cards = {
        "/insurance-claims-savings-for-clinics": ("Overview", "Insurance claims savings for clinics", "Where clinics lose money on claims, and what helps."),
        "/denial-appeal-letter-help": ("Appeals", "Denial appeal letters", "What a good appeal letter includes."),
        "/ncci-bundling-check": ("Before filing", "NCCI bundling check", "Why bundled codes get denied, and what our check covers."),
        "/co-97-denial-bundled-service": ("Denial code", "CO-97: bundled service", "How to work a bundling denial."),
        "/co-50-medical-necessity-denial": ("Denial code", "CO-50: medical necessity", "How to appeal a medical necessity denial."),
    }
    return [{"eyebrow": e, "title": t, "text": x, "href": h} for h, (e, t, x) in cards.items() if h != here]


GUIDES = {
    "/insurance-claims-savings-for-clinics": {
        "nav": "Insurance Claims Savings for Clinics",
        "title_tag": "Insurance Claims Savings for Clinics | Althais",
        "eyebrow": "Guide",
        "title": "Insurance claims savings", "em": "for clinics, not patients.",
        "lede": "For a clinic, saving money on insurance claims means not losing it to claim mistakes and to denials nobody has time to work.",
        "meta": "Insurance claims savings for clinic billing teams: catch claim mistakes before filing and draft appeals for denials. Staff approve every claim.",
        "card": "Where clinics lose money on claims, and what helps.",
        "hero": [
            {"type": "rows", "eyebrow": "Where clinics lose money", "rows": [("Before filing", "Code and bundling mistakes", ""), ("After a denial", "Appeals never written", ""), ("Over time", "Deadlines missed", "")]},
            {"type": "rows", "eyebrow": "Where Althais helps", "soft": True, "rows": [("Before filing", "Flags common bundling mistakes", "g"), ("After a denial", "Drafts the appeal letter", "g"), ("Always", "A person approves", "g")]},
        ],
        "answer": ("For a clinic, insurance claims savings means losing less money to claim mistakes and unworked denials. Althais helps in two places. "
                   "Before a claim is filed, it flags common bundling mistakes. After a denial, it drafts an appeal letter from the denial text you paste in. "
                   "Your staff approve every claim and every letter. Althais cannot promise that a payer will pay."),
        "article": [
            {"h": "Where a clinic loses money on claims", "p": ["Most of the loss comes from a few places that repeat."],
             "list": ["Coding mistakes: a wrong or missing code, or two codes a payer will not pay for together.",
                      "Missing detail: a note that does not support the code that was billed.",
                      "Denials that sit: someone has to find the reason and fix it, and in a small clinic that person is also busy with everything else.",
                      "Appeals never written: a good appeal letter takes time, so many are skipped.",
                      "Missed deadlines: payers set time limits for corrections and appeals, and they are easy to run past."]},
            {"h": "What helps, and when", "p": ["There are two moments where a little work saves the most."],
             "list": ["Before the claim goes out: a second check on the codes catches mistakes while the note is still open. Althais flags common bundling mistakes and shows a confidence score on each code it suggests.",
                      "After a denial: read the reason, decide whether to correct the claim or appeal, and write the letter. Althais drafts the letter from the denial text you paste in. A person edits and sends it."]},
            {"h": "What Althais does today, and what it does not",
             "p": ["Today it writes the visit note from what you say or type, suggests diagnosis and procedure codes, runs a starter bundling check on about 62 selected code pairs, and drafts appeal letters from pasted denial text. A person approves every claim.",
                    "It does not yet connect to your payers, see your denials on its own, send claims for you, plug into a specific EHR, or track the dollars you recover. You tell Althais which claims were denied."]},
            {"h": "How to tell whether it is worth it for your clinic",
             "p": ["The numbers that matter are your own. We do not publish savings percentages, because we do not have clinic results to show yet."],
             "steps": ["Count the claims that were denied last quarter.", "Count how many of those were appealed.", "Time how long one appeal takes your staff, start to finish.", "After a trial, count again and compare."]},
            {"h": "A note on patient information", "p": [PHI]},
        ],
        "updated": REVIEWED,
        "faq": [("Does Althais recover money for me?", "No. Althais helps your staff find mistakes and write appeals. Whether a payer pays is up to the payer."),
                ("Is this for patients disputing their own insurance bills?", "No. Althais is for clinic billing teams."),
                ("Does Althais connect to my insurance payers?", "Not yet. You tell Althais which claims were denied and paste in the denial text."),
                ("How do I try it?", "Join the pilot and tell us about your clinic. Please leave patient details out of the form.")],
        "links_head": ("More guides", "Keep", "reading."),
    },
    "/denial-appeal-letter-help": {
        "nav": "Denial Appeal Letters",
        "title_tag": "Denial Appeal Letters for Small Clinics | Althais",
        "eyebrow": "Guide",
        "title": "Denial appeal letters", "em": "for small clinics.",
        "lede": "A denied claim is not always the end. A clear appeal letter gives the payer a reason to take a second look.",
        "meta": "What a clinic's appeal letter for a denied claim needs, and how Althais drafts one from pasted denial text for staff to edit and sign.",
        "card": "What a good appeal letter includes.",
        "hero": [{"type": "rows", "eyebrow": "An appeal letter says", "rows": [("Which claim", "Claim number, date, codes", ""), ("Why denied", "The payer's own reason", ""), ("Why you disagree", "In plain words", ""), ("What backs it up", "Records you attach", "")]}],
        "answer": ("An appeal letter should say which claim was denied, why the payer denied it, why you disagree, and which records support you. "
                   "Althais drafts that letter from the denial text you paste in. Your staff edit it, check every fact and sign it. We cannot tell you an appeal will succeed."),
        "article": [
            {"h": "What a good appeal letter includes", "p": ["Keep it short and specific. A reviewer reads many of these."],
             "list": ["Claim details: the claim number, date of service, codes billed and amount billed.",
                      "The denial: the payer's stated reason and any reason code on the remittance advice.",
                      "Your case: why the service was correct and covered, in plain words.",
                      "Supporting records: the visit note, test results or policy language that back you up.",
                      "The ask: what you want, such as reprocessing and payment.",
                      "A contact and a signature: who at the clinic the payer should reach."]},
            {"h": "Read the deadline first", "p": ["Every payer sets a time limit for appeals. It is usually printed on the denial or on the remittance advice. Read it before anything else. The limit differs by payer and by plan, so do not rely on a number from a web page, including this one."]},
            {"h": "Appeal, or correct the claim?", "p": ["Some denials are fixed with a corrected claim, such as a wrong code or a missing field. Others need an appeal because you believe the payer decided wrongly. The denial reason usually tells you which."]},
            {"h": "How Althais drafts the letter", "steps": ["Paste the denial text into Althais.", "Althais drafts a letter that restates the denial, answers it and lists records to attach.", "Your staff edit the letter, check every fact and add the records.", "A person signs the letter and sends it."],
             "p": ["The letter is a starting draft. Althais does not know your records, so your staff must check every statement before it goes out."]},
            {"h": "What Althais does not do yet", "p": ["Althais does not see your denials by itself, send the letter to the payer, or track the outcome. You mark a claim as denied and send the letter yourself."]},
            {"h": "A note on patient information", "p": [PHI]},
        ],
        "updated": REVIEWED,
        "faq": [("Can Althais draft a letter for any payer?", "The letter starts from the text you paste, so it can start from any denial. Payer-specific forms and rules are not built in."),
                ("Does an Althais letter guarantee approval?", "No. Outcomes depend on the payer and the claim."),
                ("Who writes the letter?", "Althais drafts it with AI. Your staff review, edit and sign it.")],
        "links_head": ("More guides", "Keep", "reading."),
    },
    "/ncci-bundling-check": {
        "nav": "NCCI Bundling Check",
        "title_tag": "NCCI Bundling Check for Clinic Claims | Althais",
        "eyebrow": "Guide",
        "title": "NCCI bundling check", "em": "for clinic claims.",
        "lede": "NCCI edits stop some codes from being billed together. When a claim breaks one, the payer usually denies the second line.",
        "meta": "What NCCI edits are, why bundled codes get denied, and what the Althais starter bundling check covers today: about 62 selected code pairs.",
        "card": "Why bundled codes get denied, and what our check covers.",
        "hero": [{"type": "rows", "eyebrow": "Example pair", "rows": [("Code 1", "99291 critical care", ""), ("Code 2", "36415 blood draw", ""), ("Modifier indicator", "0: no modifier allowed", "g"), ("Result", "Second line likely denied", "")]}],
        "answer": ("NCCI edits are Medicare rules that list pairs of codes that normally should not be billed together. For some pairs a modifier can show the services were separate. For others nothing can. "
                   "Althais runs a starter check on about 62 selected pairs and flags a match. It is not the full CMS table, so a clear result does not mean a claim is free of NCCI problems."),
        "article": [
            {"h": "What an NCCI edit is", "p": ["NCCI stands for National Correct Coding Initiative. CMS publishes procedure-to-procedure edits: pairs of codes where one is treated as part of the other. If both are billed for the same patient on the same day, the payer generally pays one and denies the other. Medicare uses these edits, and many other payers apply similar ones."]},
            {"h": "The modifier indicator", "p": ["Each pair carries an indicator that says whether a modifier can override the edit."],
             "list": ["0: no modifier can override the edit. The two codes cannot be billed together.",
                      "1: a modifier may override the edit if the two services were truly separate and the note supports it."]},
            {"h": "An example", "p": ["Critical care (99291) and a blood draw (36415) are listed in our check with an indicator of 0. If both are billed on one claim for the same patient and day, the blood draw line will normally be denied. This is an example only. Check the current CMS table before you rely on any single pair."]},
            {"h": "What the Althais check covers today",
             "list": ["A starter list of about 62 selected code pairs, chosen by hand.", "It flags pairs with an indicator of 0 or 1.", "It does not read the modifiers already on your claim.", "It is not the full CMS table and is not updated on a fixed schedule yet."]},
            {"h": "What to do when a pair is flagged",
             "steps": ["Read the note. Were the two services really separate?", "If not, remove one of the codes.", "If they were separate and the indicator is 1, check whether a modifier is allowed and whether the note supports it.", "Never add a modifier only to get a claim paid. A person makes the call."]},
            {"h": "Use the full table too", "p": ["For the complete list, use the current procedure-to-procedure edit tables on the CMS NCCI page at cms.gov. The Althais check is a quick extra look, not a replacement."]},
        ],
        "updated": REVIEWED,
        "faq": [("Does Althais check modifiers?", "Not yet. The check flags the pair but does not read the modifiers already on your claim."),
                ("Is this only for Medicare?", "The table comes from Medicare. Many other payers apply similar edits, and your payer's own rules may differ."),
                ("Does a clear result mean my claim is clean?", "No. The check covers about 62 pairs, not every NCCI edit.")],
        "links_head": ("More guides", "Keep", "reading."),
    },
    "/co-97-denial-bundled-service": {
        "nav": "CO-97 Denial",
        "title_tag": "CO-97 Denial: Bundled Service Fix Guide | Althais",
        "eyebrow": "Guide",
        "title": "CO-97 denial:", "em": "what it means and what to do.",
        "lede": "CO-97 is a common reason for a denied line. It says the payer treats one service as part of another service it already paid.",
        "meta": "CO-97 means the payer treats a service as included in payment for another. How clinics check the code pair and decide whether to correct or appeal.",
        "card": "How to work a bundling denial.",
        "hero": [{"type": "rows", "eyebrow": "On the remittance advice", "rows": [("Group code", "CO", ""), ("Reason code", "97", ""), ("In plain words", "Included in another service", "g")]}],
        "answer": ("CO-97 is a claim adjustment reason code. In plain words, payment for this service is included in the payment for another service on the claim or already processed. "
                   "First find the other service. Then check whether the two codes are an NCCI pair and whether a modifier could legitimately apply. "
                   "If the services were separate and your note shows it, send a corrected claim or appeal. If not, accept the denial."),
        "article": [
            {"h": "What the code says", "p": ["On a remittance advice, the group code CO means contractual obligation. That usually means the clinic, not the patient, bears the loss. Reason code 97 says the benefit for this service is included in the payment or allowance for another service."]},
            {"h": "How to work a CO-97 denial",
             "steps": ["Find the denied line and the other service it is bundled with on the remittance advice.", "Check whether the two codes are an NCCI pair and note the modifier indicator.", "Read the visit note. Were the services separate, for example a different site, a different session or a different problem?", "If they were, and a modifier is allowed, send a corrected claim with the right modifier, or appeal with the note.", "If they were not, write off the line.", "Record the reason so the same mistake is not repeated."]},
            {"h": "What not to do", "list": ["Do not add a modifier only to get the line paid.", "Do not rebill the same codes unchanged.", "Check your payer contract before billing a patient for any denied amount."]},
            {"h": "Where Althais fits", "p": ["The Althais starter bundling check flags some pairs before filing. It covers about 62 selected pairs, described on the bundling check page. When a CO-97 denial still comes, you can paste the denial text into Althais to draft an appeal. Althais does not read remittance files or work the denial for you."]},
            {"h": "Check the exact wording", "p": ["Reason codes are published in a standard list, and payers sometimes add their own remark codes. Check the current code list and your payer's remittance advice for the exact wording."]},
        ],
        "updated": REVIEWED,
        "faq": [("Can I bill the patient for a CO-97 denial?", "Usually not. The CO group code generally means the clinic bears the loss. Check your payer contract."),
                ("Is a CO-97 denial always correct?", "No. If the services were truly separate and your note shows it, you may be able to correct the claim or appeal.")],
        "links_head": ("More guides", "Keep", "reading."),
    },
    "/co-50-medical-necessity-denial": {
        "nav": "CO-50 Denial",
        "title_tag": "CO-50 Denial: Medical Necessity Appeal Steps | Althais",
        "eyebrow": "Guide",
        "title": "CO-50 denial:", "em": "medical necessity appeals.",
        "lede": "CO-50 means the payer decided a service was not medically necessary under its coverage rules.",
        "meta": "CO-50 means the payer decided a service was not medically necessary. Steps a clinic can take: check the policy, the diagnosis link and the note, then appeal.",
        "card": "How to appeal a medical necessity denial.",
        "hero": [{"type": "rows", "eyebrow": "On the remittance advice", "rows": [("Group code", "CO", ""), ("Reason code", "50", ""), ("In plain words", "Not medically necessary", "g")]}],
        "answer": ("CO-50 means the payer decided the service was not medically necessary under its coverage rules. "
                   "Check the payer's coverage policy for the service, check that the diagnosis codes on the claim support it, and read your note for the clinical reason. "
                   "If the record supports the service, appeal with the note and the policy language. If the note is thin, a corrected claim will not help."),
        "article": [
            {"h": "What the code says", "p": ["Reason code 50 says the service is not covered because the payer did not consider it medically necessary. The decision rests on the payer's coverage policy and on what your record shows."]},
            {"h": "How to work a CO-50 denial",
             "steps": ["Find the coverage policy for the service. For Medicare this is a local or national coverage determination. Other payers publish their own policies.", "Check the diagnosis codes linked to the denied line. Is the diagnosis that supports the service on the claim and linked to it?", "Read the note. Does it record the symptoms, findings and clinical reason for the service?", "Check whether the service needed prior authorization.", "If the record supports the service, appeal with the note and the policy language.", "If it does not, do not change the record. A later addendum must be dated and truthful."]},
            {"h": "What a strong appeal shows", "list": ["The patient's condition and why the service was needed, from the note.", "The payer's own policy language and how the patient meets it.", "Test results or prior treatment that support the decision.", "A clear request for reprocessing."]},
            {"h": "Where Althais fits", "p": ["Althais can suggest diagnosis and procedure codes with a confidence score and can draft an appeal letter from pasted denial text. It does not check coverage policies or judge medical necessity. Your staff and clinicians make that call."]},
            {"h": "A note on patient information", "p": [PHI]},
        ],
        "updated": REVIEWED,
        "faq": [("Can Althais tell me if a service is medically necessary?", "No. It does not check coverage policies. A clinician and your billing staff decide."),
                ("Should I add a diagnosis code to get the claim paid?", "Only if the record supports it. Never add a code that the note does not support.")],
        "links_head": ("More guides", "Keep", "reading."),
    },
}

for _href, _p in GUIDES.items():
    _p["ctas"] = CTAS
    _p["links_grid"] = _more(_href)


def _view(href):
    async def view(request: Request, user=Depends(current_user)):
        return platform_pages.render(request, user, GUIDES[href], href, "Guides", NAV)
    view.__name__ = "guide_" + href.strip("/").replace("-", "_")
    return view


for _href in GUIDES:
    router.add_api_route(_href, _view(_href), methods=["GET"], include_in_schema=False)

platform_pages.register("Guides", GUIDES, NAV)
