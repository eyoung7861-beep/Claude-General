from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib import colors
from reportlab.lib.colors import HexColor

OUTPUT = "/home/user/Claude-General/Eric_Young_Resume.pdf"

PAGE_W, PAGE_H = letter
MARGIN = 0.65 * inch

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=0.5 * inch,
    bottomMargin=0.5 * inch,
)

BLACK = HexColor("#000000")
DARK  = HexColor("#1a1a1a")

def style(name, **kw):
    base = dict(
        fontName="Times-Roman", fontSize=10, leading=13,
        textColor=DARK, spaceAfter=0, spaceBefore=0,
    )
    base.update(kw)
    return ParagraphStyle(name, **base)

S_NAME    = style("name",    fontName="Times-Bold",   fontSize=16, alignment=TA_CENTER, leading=20)
S_ADDR    = style("addr",    alignment=TA_CENTER,     fontSize=10)
S_CONTACT = style("contact", alignment=TA_CENTER,     fontSize=10)
S_SECHEAD = style("sechead", fontName="Times-Bold",   fontSize=10, alignment=TA_CENTER)
S_BODY    = style("body",    alignment=TA_JUSTIFY,    fontSize=10)
S_BULLET  = style("bullet",  leftIndent=14, firstLineIndent=-10, alignment=TA_JUSTIFY, fontSize=10, leading=13)
S_JOBTITLE= style("jobtitle",fontName="Times-Bold",   fontSize=10, leading=14)
S_BOLD    = style("bold",    fontName="Times-Bold",   fontSize=10)
S_SMALL   = style("small",   fontSize=9,  leading=12)
S_BULLET2 = style("bullet2", leftIndent=28, firstLineIndent=-10, fontSize=10, leading=13)

def hr():
    return HRFlowable(width="100%", thickness=0.8, color=BLACK, spaceAfter=3, spaceBefore=3)

def section(title):
    return [
        Spacer(1, 4),
        hr(),
        Paragraph(title, S_SECHEAD),
        hr(),
        Spacer(1, 2),
    ]

def bullet(text, level=1):
    s = S_BULLET if level == 1 else S_BULLET2
    return Paragraph(f"•  {text}", s)

def sp(h=4):
    return Spacer(1, h)

# ── Areas of Expertise two-column table ──────────────────────────────────────
expertise_left = [
    "Process Redesign and Implementation",
    "Cross-Functional Departmental Leadership",
    "Data Analytics and Operations Management",
    "Data Governance & Data Quality Frameworks",
]
expertise_mid = [
    "BI Strategy, Roadmap & Executive Reporting",
    "Multi-Site Operations",
    "Strategic Planning and Leadership",
    "Cloud Platforms: Azure / AWS / Snowflake",
]
expertise_right = [
    "Project Planning / Execution",
    "Revenue Growth Attainment",
    "Leadership Development",
    "Change Management",
]

def exp_para(txt):
    return Paragraph(f"•  {txt}", style("ep", fontSize=9, leading=13))

exp_rows = []
max_r = max(len(expertise_left), len(expertise_mid), len(expertise_right))
for i in range(max_r):
    l = exp_para(expertise_left[i])  if i < len(expertise_left)  else Paragraph("", S_SMALL)
    m = exp_para(expertise_mid[i])   if i < len(expertise_mid)   else Paragraph("", S_SMALL)
    r = exp_para(expertise_right[i]) if i < len(expertise_right) else Paragraph("", S_SMALL)
    exp_rows.append([l, m, r])

exp_table = Table(exp_rows, colWidths=[(PAGE_W - 2*MARGIN)/3]*3)
exp_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING",  (0,0), (-1,-1), 2),
    ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ("TOPPADDING",   (0,0), (-1,-1), 1),
    ("BOTTOMPADDING",(0,0), (-1,-1), 1),
]))

# ── Tech Skills two-col table ─────────────────────────────────────────────────
tech_left  = ["Power BI, Tableau, Qlik", "SQL, DAX, Data Modeling", "ETL / ELT Pipeline Oversight"]
tech_right = ["Azure Synapse / AWS / Snowflake", "CSOD / LMS Reporting Platforms", "Agile / Scrum / Lean Six Sigma"]

def tech_para(txt):
    return Paragraph(f"•  {txt}", style("tp", fontSize=9, leading=13))

tech_rows = [[tech_para(tech_left[i]), tech_para(tech_right[i])] for i in range(len(tech_left))]
tech_table = Table(tech_rows, colWidths=[(PAGE_W - 2*MARGIN)/2]*2)
tech_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING",  (0,0), (-1,-1), 2),
    ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ("TOPPADDING",   (0,0), (-1,-1), 1),
    ("BOTTOMPADDING",(0,0), (-1,-1), 1),
]))

# ─────────────────────────────────────────────────────────────────────────────
story = []

# Header
story += [
    Paragraph("Eric Young", S_NAME),
    Paragraph("13504 Galena Pl, Tampa, FL 33626", S_ADDR),
    sp(2),
]

# Contact row
contact_table = Table(
    [[Paragraph("813.210.7247", S_BODY), Paragraph("eyoung7861@gmail.com", S_BODY)]],
    colWidths=[(PAGE_W - 2*MARGIN)/2]*2,
)
contact_table.setStyle(TableStyle([
    ("ALIGN", (0,0),(0,0), "LEFT"),
    ("ALIGN", (1,0),(1,0), "RIGHT"),
    ("LEFTPADDING",  (0,0),(-1,-1), 0),
    ("RIGHTPADDING", (0,0),(-1,-1), 0),
]))
story.append(contact_table)

# Professional Profile
story += section("PROFESSIONAL PROFILE")
story += [
    bullet("Senior Business Intelligence executive with 10+ years building enterprise BI strategies, "
           "governing data assets, and translating complex analytics into board-level decisions that "
           "improve financial margins and member satisfaction."),
    sp(3),
    bullet("Proven track record designing end-to-end BI roadmaps — from ETL architecture and cloud "
           "data platform selection to self-service analytics rollout and executive dashboard programs — "
           "while championing data governance frameworks and a data-driven culture across 500+ stakeholders."),
    sp(3),
    bullet("Expertise spans process optimization, compliance measurement systems, cross-functional "
           "departmental leadership, and scaling BI infrastructure to maximize enterprise results."),
]

# Areas of Expertise
story += section("AREAS OF EXPERTISE")
story.append(exp_table)

# Technical Skills  ← NEW SECTION
story += section("TECHNICAL SKILLS")
story.append(tech_table)

# Education
story += section("EDUCATION")
story += [
    bullet("<b>Master of Business Analytics and Information Systems</b> (2020) — <i>University of South Florida</i>, Tampa, FL"),
    sp(3),
    bullet("<b>Master of Business Administration</b> in Organizational Leadership (2016) — <i>Ashford University</i>, Delray Beach, FL"),
    sp(3),
    bullet("<b>Bachelor of Arts</b> in Psychology (2013) — <i>University of South Florida</i>, St. Petersburg, FL"),
]

# Certifications
story += section("CERTIFICATIONS")
story += [
    bullet("<b>Lean Six Sigma</b> (2015) — #2015LL000103"),
]

# Professional Experience
story += section("PROFESSIONAL EXPERIENCE")
story += [sp(4)]

# ── Humana ────────────────────────────────────────────────────────────────────
story.append(Paragraph(
    "<b>Director of Business Intelligence (Lead, BI)</b>, <i>Humana</i>, Tampa, FL (2013 to Present)",
    S_JOBTITLE
))
story += [
    sp(3),
    bullet("Owns the enterprise BI strategy and roadmap for the Learning Solutions division, aligning "
           "C-suite stakeholders and VP-level partners on KPIs, OKRs, and data-driven decision frameworks "
           "that drive cost efficiency and member-outcome improvements."),
    sp(3),
    bullet("Established and enforces data governance policies and data quality standards across production "
           "Power BI environments, reducing reporting errors by 30% and ensuring full regulatory compliance."),
    sp(3),
    bullet("Architected and manages ETL pipelines ingesting real-time Learning Center data into Humana's "
           "enterprise data warehouse, enabling self-service analytics for 500+ internal users across 12 departments."),
    sp(3),
    bullet("Leads a cross-functional BI team of 6 analysts and engineers; oversees $1.2M analytics "
           "budget, vendor relationships, and tool selection (Power BI, CSOD, Azure Synapse)."),
    sp(3),
    bullet("Delivers executive-level PowerBI dashboards from CSOD Reports to VP and C-suite audiences, "
           "translating complex datasets into strategic narratives that inform enterprise workforce decisions."),
    sp(3),
    bullet("Provides regression testing and advanced data analysis on real-time datasets; all validated "
           "models are persisted in Humana's cloud data warehouse for reuse across the analytics org."),
    sp(6),
]

# ── Atomic LLC ────────────────────────────────────────────────────────────────
story.append(Paragraph(
    "<b>Store Manager</b>, <i>Atomic LLC</i>, Clearwater, FL (2011 to 2013)",
    S_JOBTITLE
))
story += [
    sp(3),
    bullet("Aligned business operations and financial processes by implementing performance-improvement "
           "initiatives that grew monthly sales 350% within the first quarter."),
    sp(3),
    bullet("Staffed and developed top-tier talent, building the highest-performing branch in the "
           "organization for 3 consecutive quarters in a volatile market."),
    sp(3),
    bullet("Spearheaded process-improvement projects that reduced production expense and expanded the "
           "clientele base, resulting in increased profit margins."),
    sp(6),
]

# ── HT Inc ────────────────────────────────────────────────────────────────────
story.append(Paragraph(
    "<b>Manager</b>, <i>HT Inc.</i>, Clearwater, FL (2007 to 2011)",
    S_JOBTITLE
))
story += [
    sp(3),
    bullet("Revamped operational processes, yielding company revenue growth that exceeded target goals "
           "for 6 consecutive quarters."),
    sp(3),
    bullet("Designed and led customer-based projects focused on operations, communications, and leadership "
           "development for internal education, improving individual performance and driving the branch into "
           "the Top 5 out of 600+ national locations with a 0.01% annual shrink result two consecutive years."),
    sp(6),
]

# ── US Navy ───────────────────────────────────────────────────────────────────
story.append(Paragraph(
    "<b>Operations Officer</b>, <i>U.S. Navy</i>, NAVSTA, TX (2002 to 2007)",
    S_JOBTITLE
))
story += [
    sp(3),
    bullet("Maintained oversight of all operational goals for a multi-level operations department, "
           "earning two successive commendation awards for successful deployments."),
    sp(3),
    bullet("Implemented strategic operational and government support functions, resulting in the "
           "successful decommissioning of 2 Naval Vessels on time and within budget."),
    sp(3),
    bullet("Selected for Operations Officer position based on exceptional performance history and "
           "demonstrated top-tier leadership capabilities."),
]

doc.build(story)
print(f"PDF written to {OUTPUT}")
