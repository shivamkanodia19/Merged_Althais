"""Static content for the Solutions page: one entry per customer segment.

Kept out of main.py because it's page copy, not routing logic.
"""

SOLUTION_SEGMENTS = [
    {
        "id": "hospital-systems",
        "label": "Hospital Systems",
        "headline": "Standardize coding and claims across every facility, department, and EHR.",
        "problems": [
            "Denials compound across dozens of departments and quietly cost millions a year.",
            "Coding backlogs delay billing while certified coders are stretched across specialties.",
            "Disparate EHRs across facilities produce inconsistent documentation quality.",
        ],
        "workflow": [
            "Coders manually review each encounter, specialty by specialty, facility by facility.",
            "Claims queue for days waiting on coding capacity before they ever reach a payer.",
            "Reconciliation across systems happens by hand, department by department.",
        ],
        "solution": [
            "Specialty-tuned AI coding deploys system-wide, not department by department.",
            "One claims pipeline standardizes assembly and submission across every facility.",
            "Payer intelligence is shared system-wide. A denial pattern learned in one facility protects every other.",
        ],
        "roi": [
            {"value": 4.2, "decimals": 1, "prefix": "$", "suffix": "M+", "label": "Denial revenue recovered / yr"},
            {"value": 63, "suffix": "%", "label": "Faster days in A/R"},
            {"value": 31, "suffix": "%", "label": "Reduction in coding FTE hours"},
        ],
        "case_study": {
            "org": "A 6-hospital regional health system",
            "quote": "We stopped finding out about denial patterns in a monthly report and started catching them before the claim left the building.",
            "role": "VP of Revenue Cycle",
        },
        "before_after": [
            ("Days in A/R", "52 days", "19 days"),
            ("Denial rate", "11.4%", "3.8%"),
            ("Coding turnaround", "3.2 days", "4 hours"),
            ("Clean claim rate", "81%", "97%"),
        ],
    },
    {
        "id": "multi-specialty-groups",
        "label": "Large Multi-Specialty Groups",
        "headline": "Give every specialty its own coding logic, without fifteen different workflows.",
        "problems": [
            "Each specialty codes differently, and cross-specialty claims get denied for medical necessity mismatches.",
            "A central billing office tries to apply one process to fifteen very different specialties.",
            "The billing team is stretched thin trying to stay current on every specialty's rules.",
        ],
        "workflow": [
            "Notes route to specialty-specific coders who each apply their own mental checklist.",
            "Specialty rule-checking is manual, inconsistent, and easy to miss under volume.",
            "Denials trigger frequent, slow resubmission cycles.",
        ],
        "solution": [
            "Specialty-aware AI models are trained per department, not applied generically.",
            "One unified claims builder replaces fifteen inconsistent manual processes.",
            "A cross-specialty payer rule engine catches conflicts before submission.",
        ],
        "roi": [
            {"value": 1.8, "decimals": 1, "prefix": "$", "suffix": "M", "label": "Annual denial recovery"},
            {"value": 41, "suffix": "%", "label": "Fewer resubmissions"},
            {"value": 22, "suffix": " hrs/wk", "label": "Coder time returned"},
        ],
        "case_study": {
            "org": "A 40-provider multi-specialty group",
            "quote": "Our cardiology and ortho claims used to get denied for completely different reasons. Now both teams work off the same intelligence.",
            "role": "Director of Billing Operations",
        },
        "before_after": [
            ("Denial rate", "9.8%", "3.1%"),
            ("Clean claim rate", "84%", "96%"),
            ("Avg. coder caseload", "38/day", "61/day"),
            ("Cross-specialty rework", "High", "Rare"),
        ],
    },
    {
        "id": "private-practices",
        "label": "Private Practices",
        "headline": "Get a full coding and billing team's output without hiring one.",
        "problems": [
            "There's no dedicated coding staff. The provider or office manager handles it after hours.",
            "Denials often get written off entirely because there's no bandwidth to appeal.",
            "Billing knowledge lives in one person's head, which is a single point of failure.",
        ],
        "workflow": [
            "The provider or office manager manually codes notes at the end of a long day.",
            "Claims go out in batches whenever there's time to submit them.",
            "Denials pile up in a folder that rarely gets revisited.",
        ],
        "solution": [
            "AI does first-pass coding the moment the note is finished, with no after-hours catch-up.",
            "Appeal letters draft themselves from the denial reason and clinical note.",
            "A simple review queue fits into five minutes between patients, not an evening.",
        ],
        "roi": [
            {"value": 11, "suffix": " hrs/wk", "label": "Saved on billing admin"},
            {"value": 27, "suffix": "%", "label": "More denials successfully appealed"},
            {"value": 86, "prefix": "$", "suffix": "K", "label": "Avg. annual revenue recovered"},
        ],
        "case_study": {
            "org": "A 3-provider cardiology practice",
            "quote": "I used to do billing on Sunday nights. Now review takes ten minutes between patients and I actually appeal denials instead of eating them.",
            "role": "Practice Owner",
        },
        "before_after": [
            ("Time to code a note", "14 min", "90 sec"),
            ("Denials appealed", "12%", "68%"),
            ("Revenue per claim", "Baseline", "+9.4%"),
            ("After-hours billing work", "3-4 hrs/wk", "Under 1 hr/wk"),
        ],
    },
    {
        "id": "urgent-care",
        "label": "Urgent Care",
        "headline": "Code at the speed patients move through the door.",
        "problems": [
            "High patient volume leaves no time for careful E/M level selection.",
            "Seasonal volume spikes overwhelm billing staff without warning.",
            "Under- and over-coding both happen when speed is prioritized over precision.",
        ],
        "workflow": [
            "Coders batch-process notes at the end of the day, long after the visit.",
            "E/M leveling is done manually against a guideline sheet, encounter by encounter.",
            "High staff turnover means consistency resets every few months.",
        ],
        "solution": [
            "E/M levels are suggested in real time with documentation-based justification.",
            "The system scales instantly with volume. A flu-season spike doesn't slow it down.",
            "Coding logic stays consistent regardless of who's staffing the front desk.",
        ],
        "roi": [
            {"value": 19, "suffix": "%", "label": "Increase in correctly leveled E/M codes"},
            {"value": 3, "suffix": "x", "label": "Volume handled at same-day submission speed"},
            {"value": 310, "prefix": "$", "suffix": "K", "label": "Avg. recovered under-coding revenue / yr"},
        ],
        "case_study": {
            "org": "A 14-location urgent care network",
            "quote": "Flu season used to mean a two-week claims backlog. Now Tuesday's visits are submitted by Tuesday night.",
            "role": "Regional Billing Manager",
        },
        "before_after": [
            ("Same-day submission rate", "54%", "98%"),
            ("E/M under-coding", "21%", "4%"),
            ("Denial rate", "8.9%", "3.4%"),
            ("Seasonal backlog", "2+ weeks", "None"),
        ],
    },
    {
        "id": "fqhc",
        "label": "FQHCs",
        "headline": "Bill the way FQHCs actually get paid: PPS, wraparound, and all.",
        "problems": [
            "Sliding-fee and wraparound billing rules are complex and payer-specific.",
            "A small billing team serves a very high patient volume with thin margins.",
            "Strict compliance requirements turn every audit into a multi-week scramble.",
        ],
        "workflow": [
            "A small team manually tracks FQHC-specific billing rules payer by payer.",
            "Compliance audit prep means pulling documentation by hand across months of claims.",
            "Every denial is disproportionately costly given already-thin reimbursement.",
        ],
        "solution": [
            "FQHC PPS and wraparound billing logic is built in, not bolted on.",
            "Every AI decision is logged, timestamped, and audit-ready by default.",
            "Denial prevention is tuned specifically to Medicaid managed care plan behavior.",
        ],
        "roi": [
            {"value": 540, "prefix": "$", "suffix": "K", "label": "Additional annual reimbursement captured"},
            {"value": 89, "suffix": "%", "label": "Less compliance audit prep time"},
            {"value": 44, "suffix": "%", "label": "Fewer Medicaid managed care denials"},
        ],
        "case_study": {
            "org": "An FQHC serving 22,000 patients a year",
            "quote": "Audit prep went from three weeks of pulling files to two days of exporting a report that was already correct.",
            "role": "Compliance & Billing Director",
        },
        "before_after": [
            ("Medicaid denial rate", "14.2%", "6.1%"),
            ("Audit prep time", "3 weeks", "2 days"),
            ("Reimbursement captured", "Baseline", "+12%"),
            ("Wraparound billing errors", "Frequent", "Rare"),
        ],
    },
    {
        "id": "specialty-clinics",
        "label": "Specialty Clinics",
        "headline": "Get coding logic built for your specialty's edge cases, not general medicine.",
        "problems": [
            "Highly specific coding requirements don't fit generic billing software.",
            "Modifier errors are common and directly cause denials.",
            "Payer medical necessity policy varies procedure by procedure.",
        ],
        "workflow": [
            "Coders lean on specialty cheat sheets that go stale as payer policy changes.",
            "Modifier application is manual and inconsistent across coders.",
            "Medical necessity documentation gaps are only caught after a denial arrives.",
        ],
        "solution": [
            "Specialty-trained models understand procedure-specific modifier logic natively.",
            "Medical necessity is cross-checked against current LCD policy automatically.",
            "Prior auth documentation drafts itself from the clinical note.",
        ],
        "roi": [
            {"value": 37, "suffix": "%", "label": "Reduction in modifier-related denials"},
            {"value": 620, "prefix": "$", "suffix": "K", "label": "Recovered annual revenue"},
            {"value": 3.8, "decimals": 1, "suffix": "x", "label": "Faster prior auth documentation"},
        ],
        "case_study": {
            "org": "A 9-provider orthopedic and sports medicine group",
            "quote": "Our modifier denial rate was the thing we could never fix. It's now the metric we stopped worrying about.",
            "role": "Billing Operations Lead",
        },
        "before_after": [
            ("Modifier denial rate", "16%", "5%"),
            ("Prior auth prep time", "45 min", "12 min"),
            ("Clean claim rate", "79%", "95%"),
            ("LCD policy misses", "Common", "Rare"),
        ],
    },
    {
        "id": "revenue-cycle-teams",
        "label": "Revenue Cycle Teams",
        "headline": "Replace six disconnected tools with one system spanning coding to payment.",
        "problems": [
            "Manual coding review is the bottleneck that throttles everything downstream.",
            "Denial root causes are usually discovered a month late, in a report.",
            "Coding, billing, and analytics live in separate, disconnected tools.",
        ],
        "workflow": [
            "Coders and billers work in separate systems that don't talk to each other.",
            "Denial trends surface only when someone builds a monthly report.",
            "Leadership makes decisions without real-time visibility into KPIs.",
        ],
        "solution": [
            "One system spans coding, claims, submission, tracking, and payment.",
            "Denial root causes surface live, not thirty days later.",
            "Team-wide productivity and quality dashboards update in real time.",
        ],
        "roi": [
            {"value": 2.4, "decimals": 1, "suffix": "x", "label": "Coder throughput"},
            {"value": 58, "suffix": "%", "label": "Faster denial root-cause identification"},
            {"value": 100, "suffix": "%", "label": "Real-time KPI visibility across the team"},
        ],
        "case_study": {
            "org": "A centralized RCM team supporting 180 providers",
            "quote": "We used to find out what went wrong a month later. Now we see it the day it happens.",
            "role": "Director of Revenue Cycle Operations",
        },
        "before_after": [
            ("Reporting cadence", "Monthly", "Real-time"),
            ("Coder throughput", "45/day", "108/day"),
            ("Denial root cause ID", "9 days", "36 hours"),
            ("Tools in daily use", "6", "1"),
        ],
    },
    {
        "id": "medical-billers",
        "label": "Medical Billers",
        "headline": "Stop re-typing what the coder already decided.",
        "problems": [
            "Repetitive manual entry between coding systems and claim software wastes hours.",
            "Chasing denial documentation across payer portals eats the rest of the day.",
            "Appeal letters get written from scratch, every single time.",
        ],
        "workflow": [
            "Approved codes get re-keyed by hand into the claim software.",
            "Appeal letters are drafted manually, often reusing an old one as a template.",
            "Claim status is tracked by logging into six different payer portals.",
        ],
        "solution": [
            "Approved codes flow directly into claims, with zero re-entry and zero transcription errors.",
            "AI drafts a complete, payer-ready appeal letter in seconds.",
            "One dashboard tracks status across every payer, not six separate logins.",
        ],
        "roi": [
            {"value": 6.5, "decimals": 1, "suffix": " hrs/wk", "label": "Saved per biller"},
            {"value": 3, "suffix": "x", "label": "Faster appeal letter drafting"},
            {"value": 1, "suffix": " dashboard", "label": "Instead of 6 payer portals"},
        ],
        "case_study": {
            "org": "An independent billing service managing 40 client practices",
            "quote": "Appeal letters used to be the task everyone put off. Now it's a two-minute review, not a twenty-five minute write.",
            "role": "Billing Team Lead",
        },
        "before_after": [
            ("Appeal letter drafting", "25 min", "4 min"),
            ("Claims processed / day / biller", "32", "74"),
            ("Payer portals checked daily", "6", "1"),
            ("Re-keying errors", "Occasional", "Eliminated"),
        ],
    },
]


# ─────────────────────────────────────────────────────────────────────────
#  Resources page content
# ─────────────────────────────────────────────────────────────────────────
# The customer stories, before/after figures and ROI numbers that used to sit on each segment had no source and no customer
# consent, so they are removed from every page. Add them back here only with real, consented results.
for _seg in SOLUTION_SEGMENTS:
    for _key in ("case_study", "before_after", "roi"):
        _seg.pop(_key, None)

RESOURCE_CATEGORIES = [
    ("all", "All"),
    ("coding-updates", "Coding & CMS Updates"),
    ("ai-healthcare", "AI in Healthcare"),
    ("rcm-guides", "Revenue Cycle Guides"),
    ("case-studies", "Case Studies"),
    ("white-papers", "White Papers"),
    ("product-updates", "Product & Webinars"),
    ("docs", "Documentation & API"),
]

# The earlier article cards pointed at articles that were never written and quoted unsourced figures. Real guides live in seo_pages.py.
RESOURCE_ARTICLES = []
