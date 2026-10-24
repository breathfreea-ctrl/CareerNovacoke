ROLES = [


#This is our resource library, containing information on 10 careers. Each career is a comprehensive profile that includes the career title, required skills, related interests, salary, typical countries with promising career prospects, industry outlook, and relevant SDG information.


    {
        "id": "ai",
        "title": "AI Engineer",
        "required_skills": ["Python", "Machine Learning", "MLOps", "LLM (RAG/Agent)"],
        "interests": [
            "Coding & Building Systems",
            "Data, Metrics & Analysis",
            "Researching New Tech",
        ],
        "salary_range": [80000, 200000],
        "top_countries": ["United States", "Mainland China", "United Kingdom"],
        "ai_match": {
            "level": "Perfectly Adapted",
            "color": "#16a34a",
            "bg": "#f0fdf4",
        },
        "overview": (
            "Process datasets, fine-tune models, build RAG/Agent systems, and deploy "
            "production-grade AI. High financial return and excellent flexibility."
        ),
        "outlook": (
            "BLS projects 22% growth. Foundation models drive massive demand across industries."
        ),
        "sdgs": [
            "SDG 9: Industry & Infrastructure",
            "SDG 8: Decent Work",
            "SDG 10: Reduced Inequalities",
        ],
        "certs": {
            "Default": ["AWS Certified Machine Learning"],

#If there are no options for the country selected by the user, it will automatically fall back to "Default", making it a "second-best" answer.


            "United States": ["AWS ML Specialty"],
            "Mainland China": ["Huawei AI Certification"],
        },
        "learning_resources": {
            "courses": [
                "Coursera 'Machine Learning' (Stanford)",
                "MLOps Zoomcamp (DataTalksClub)",
                "Hugging Face Learn Docs",
            ],
            "practical": [
                "Build 2 end-to-end AI projects and push to GitHub",
                "Participate in Kaggle competitions",
                "Contribute to open-source AI repositories",
            ],
        },
        "mentor": {
            "name": "Marnix Jansma",
            "org": "Cadmatic (Netherlands)",
            "years": "5 years",
            "path": (
                "Junior Software Developer (2020) → Master's in AI (part-time, 2022) "
                "→ Senior Software Engineer, AI (2025)"
            ),
            "daily": (
                "Building tailored AI solutions across Cadmatic's global product portfolio "
                "— 3D modeling, geometric computation, legacy data models, and domain-specific logic."
            ),
        },
    },
    {
        "id": "mech",
        "title": "Mechanical Engineer",
        "required_skills": ["CAD/CAE", "Thermodynamics", "Manufacturing"],
        "interests": [
            "Building & Fixing Physical Things",
            "Data, Metrics & Analysis",
        ],
        "salary_range": [60000, 110000],
        "top_countries": ["United States", "Canada", "United Kingdom"],
        "ai_match": {
            "level": "Highly Adapted",
            "color": "#2563eb",
            "bg": "#eff6ff",
        },
        "overview": (
            "Design, develop, and test mechanical equipment. "
            "High social value with stable compensation."
        ),
        "outlook": (
            "Steady 11% growth in the US. Clean energy and automation driving new opportunities."
        ),
        "sdgs": [
            "SDG 9: Industry & Infrastructure",
            "SDG 8: Decent Work",
        ],
        "certs": {
            "Default": ["Professional Engineer (PE)"],
            "United States": ["PE License"],
            "United Kingdom": ["CEng (Chartered Engineer)"],
            "Malaysia": ["BEM Registered Engineer"],
        },
        "learning_resources": {
            "courses": [
                "EdX 'Mechanical Engineering' (MIT)",
                "SolidWorks/CAD official tutorials",
            ],
            "practical": [
                "Complete a capstone engineering project (e.g., heat exchanger)",
                "Seek industrial internships or placement years",
            ],
        },
        "mentor": {
            "name": "Megan",
            "org": "STERIS (Life Sciences)",
            "years": "5 years",
            "path": (
                "4 co-op rotations across 3 departments → Full-time Mechanical Engineer "
                "→ Senior Mechanical Engineer"
            ),
            "daily": (
                "Managing several parts of a project simultaneously, involved in concept, "
                "design, testing, and research phases within the New Product Development team."
            ),
        },
    },
    {
        "id": "ict",
        "title": "ICT-Access Project Officer",
        "required_skills": [
            "Project Management",
            "ICT Infrastructure",
            "M&E (Monitoring & Evaluation)",
        ],
        "interests": [
            "Community Engagement",
            "Policy & Governance",
            "Humanitarian Aid",
        ],
        "salary_range": [50000, 90000],
        "top_countries": ["United States", "Finland", "Singapore"],
        "ai_match": {
            "level": "Highly Adapted",
            "color": "#2563eb",
            "bg": "#eff6ff",
        },
        "overview": (
            "Manage inclusive connectivity projects. "
            "Meaningful social impact with solid NGO compensation."
        ),
        "outlook": (
            "UN connectivity goals drive demand. Budget fluctuations affect job supply."
        ),
        "sdgs": [
            "SDG 9: Industry & Infrastructure",
            "SDG 10: Reduced Inequalities",
            "SDG 4: Quality Education",
        ],
        "certs": {
            "Default": ["PMP (Project Management Professional)"],
            "United States": ["PMP"],
            "Singapore": ["ITU Certifications"],
        },
        "learning_resources": {
            "courses": [
                "ITU Academy 'Capacity Building'",
                "World Bank Project-Cycle Learning",
                "UNDP Learning Portal",
            ],
            "practical": [
                "Volunteer for ICT4D projects",
                "Draft mock project proposals and M&E frameworks",
            ],
        },
        "mentor": {
            "name": "Aseel Daoud Shakboua",
            "org": "UNICEF Iraq (GBV Programme Specialist)",
            "years": "13+ years",
            "path": (
                "Social Worker → Protection Officer (UN Women) → Protection Specialist (DRC) "
                "→ GBV Coordinator (Relief International) → GBV Programme Specialist "
                "(UNICEF, 2022-present)"
            ),
            "daily": (
                "Technical supervision of GBV and protection teams, capacity building, "
                "launching GBV case management initiatives, and supporting GBV sub-cluster coordination."
            ),
        },
    },
    {
        "id": "physician",
        "title": "Physician",
        "required_skills": ["Clinical Diagnosis", "Patient Care", "Medical Ethics"],
        "interests": [
            "Caring & Healing Others",
            "Understanding Human Behavior",
        ],
        "salary_range": [150000, 300000],
        "top_countries": ["United States", "Germany", "Australia"],
        "ai_match": {
            "level": "Highly Adapted",
            "color": "#2563eb",
            "bg": "#eff6ff",
        },
        "overview": (
            "Diagnose, treat, and prevent diseases. "
            "Extremely high social prestige and top-tier compensation."
        ),
        "outlook": (
            "Aging populations ensure stability. Structural shortages in rural areas."
        ),
        "sdgs": [
            "SDG 10: Reduced Inequalities",
            "SDG 5: Gender Equality",
            "SDG 8: Decent Work",
        ],
        "certs": {
            "Default": ["National Medical License"],
            "United States": ["USMLE Steps 1-3"],
            "United Kingdom": ["PLAB"],
            "Australia": ["AMC Exam"],
        },
        "learning_resources": {
            "courses": [
                "WFME-accredited medical curriculum",
                "OpenStax Anatomy & Physiology",
            ],
            "practical": [
                "Clinical Clerkship (hospital rotations)",
                "Hands-on Patient Care simulation labs",
            ],
        },
        "mentor": {
            "name": "Dr. Christopher Garofalo",
            "org": "Private Practice, Massachusetts (Family Medicine + OB)",
            "years": "24 years",
            "path": (
                "Northeastern co-op program → UMass Medical School → "
                "UMass Family Medicine Residency → Joined Sturdy Memorial Hospital "
                "(first job) → Private practice"
            ),
            "daily": (
                "Outpatient family medicine, obstetrics, teaching, and serving as "
                "a delegate to the AMA House of Delegates."
            ),
        },
    },
    {
        "id": "psych",
        "title": "Psychologist",
        "required_skills": [
            "Psychological Assessment",
            "Counselling",
            "Empathy",
        ],
        "interests": [
            "Listening & Counselling",
            "Understanding Human Behavior",
        ],
        "salary_range": [70000, 120000],
        "top_countries": ["United States", "United Kingdom", "Canada"],
        "ai_match": {
            "level": "Less Adapted",
            "color": "#d97706",
            "bg": "#fffbeb",
        },
        "overview": (
            "Assess and treat emotional/behavioral disorders. High job satisfaction."
        ),
        "outlook": (
            "11.2% growth for clinical roles. Rising mental health awareness."
        ),
        "sdgs": [
            "SDG 10: Reduced Inequalities",
            "SDG 5: Gender Equality",
            "SDG 4: Quality Education",
        ],
        "certs": {
            "Default": ["Licensed Psychologist"],
            "United States": ["State Licensure"],
            "United Kingdom": ["HCPC Registration"],
            "Hong Kong, China": ["HKPS Registration"],
        },
        "learning_resources": {
            "courses": [
                "OpenStax Psychology (Free)",
                "APA (American Psychological Association) guides",
            ],
            "practical": [
                "Supervised clinical practicum hours",
                "Role-play counselling sessions with feedback",
            ],
        },
        "mentor": {
            "name": "Dr. Claire Pitt",
            "org": (
                "NHS + Private Practice (UK), Clinical Psychologist "
                "& EMDR Europe Accredited Practitioner"
            ),
            "years": "12 years to qualification",
            "path": (
                "Undergraduate (2006) → Master's → Support Worker → "
                "Assistant Psychologist x2 → Doctorate → "
                "Qualified Clinical Psychologist (2018)."
            ),
            "daily": (
                "Clinical psychology in NHS and private practice; EMDR therapy; "
                "supervising and shortlisting aspiring psychologists."
            ),
        },
    },
    {
        "id": "lawyer",
        "title": "Lawyer",
        "required_skills": ["Legal Research", "Drafting", "Court Advocacy"],
        "interests": [
            "Public Speaking & Advocacy",
            "Social Justice & Human Rights",
            "Writing & Content Creation",
        ],
        "salary_range": [100000, 250000],
        "top_countries": ["United States", "United Kingdom", "Canada"],
        "ai_match": {
            "level": "Highly Adapted",
            "color": "#2563eb",
            "bg": "#eff2ff",
        },
        "overview": (
            "Provide legal counsel, draft documents, and represent clients. "
            "High earning potential in commercial law."
        ),
        "outlook": (
            "Steady demand. AI automates review but not court advocacy."
        ),
        "sdgs": [
            "SDG 5: Gender Equality",
            "SDG 10: Reduced Inequalities",
            "SDG 8: Decent Work",
        ],
        "certs": {
            "Default": ["Bar Admission"],
            "United States": ["State Bar Exam"],
            "United Kingdom": ["SQE (Solicitors Qualifying Exam)"],
            "Canada": ["Provincial Bar Exam"],
        },
        "learning_resources": {
            "courses": [
                "Coursera 'Introduction to Law' (Michigan)",
                "Harvard Online Legal Training",
            ],
            "practical": [
                "Law firm internship / Pupillage",
                "Moot court simulations and case-study analysis",
            ],
        },
        "mentor": {
            "name": "Zhang Zhenbin",
            "org": "Guoyao Qindao Law Firm, Senior Partner",
            "years": "8 years",
            "path": (
                "Intern (2017) → Practising Lawyer (2018) → Joined Partner Track "
                "(2022, year 4) → Preparatory Partner → General Partner → Senior Partner."
            ),
            "daily": (
                "Deep focus on construction engineering and real estate law; has handled "
                "multiple complex cases exceeding 100 million RMB; firm management "
                "and youth lawyer mentoring."
            ),
        },
    },
    {
        "id": "gbv",
        "title": "GBV Programme Officer",
        "required_skills": [
            "Survivor-centered Practice",
            "Policy Advocacy",
            "MEAL",
        ],
        "interests": [
            "Social Justice & Human Rights",
            "Community Engagement",
        ],
        "salary_range": [40000, 80000],
        "top_countries": ["United States", "Canada", "United Kingdom"],
        "ai_match": {
            "level": "Less Adapted",
            "color": "#d97706",
            "bg": "#fffbeb",
        },
        "overview": (
            "Support survivors and advocate for policy change. Deeply meaningful NGO work."
        ),
        "outlook": (
            "Funding competition is fierce, but demand remains high in humanitarian settings."
        ),
        "sdgs": [
            "SDG 5: Gender Equality",
            "SDG 10: Reduced Inequalities",
            "SDG 4: Quality Education",
        ],
        "certs": {
            "Default": ["GBV in Emergencies Training"],
            "United States": ["OVW Grants Training"],
        },
        "learning_resources": {
            "courses": [
                "UN Women Training Centre 'Essential Services Package'",
                "GBV AoR 'Advanced Training in Humanitarian Action'",
            ],
            "practical": [
                "Field internships with local NGOs",
                "Draft a mock grant proposal and M&E report",
            ],
        },
        "mentor": {
            "name": "Allen Samanya Zabibu",
            "org": "GBV Officer, humanitarian settings",
            "years": "10+ years",
            "path": (
                "Child Protection Assistant (Plan International, 2012-2015) "
                "→ Women Support Officer (Health Link South Sudan) "
                "→ GBV Officer (2024-present)."
            ),
            "daily": (
                "Implementing GBV prevention and response interventions, ensuring "
                "survivor-centred, ethical, and culturally appropriate service delivery "
                "across multiple sites."
            ),
        },
    },
    {
        "id": "teacher",
        "title": "Teacher",
        "required_skills": [
            "Curriculum Planning",
            "Classroom Management",
            "Assessment",
        ],
        "interests": [
            "Teaching & Mentoring",
            "Caring & Healing Others",
        ],
        "salary_range": [40000, 90000],
        "top_countries": ["United States", "Canada", "Australia"],
        "ai_match": {
            "level": "Highly Adapted",
            "color": "#2563eb",
            "bg": "#eff6ff",
        },
        "overview": (
            "Educate students and shape the future. Stable public sector employment."
        ),
        "outlook": (
            "Global demand remains huge (44M more teachers needed by 2030)."
        ),
        "sdgs": [
            "SDG 4: Quality Education",
            "SDG 5: Gender Equality",
            "SDG 10: Reduced Inequalities",
        ],
        "certs": {
            "Default": ["Teaching License"],
            "United States": ["State Teacher Certification"],
            "United Kingdom": ["QTS (Qualified Teacher Status)"],
        },
        "learning_resources": {
            "courses": [
                "Coursera 'Learning Design for 21st Century'",
                "ADDIE / Backward Design models",
            ],
            "practical": [
                "Student teaching practicum",
                "Prepare a portfolio of lesson plans and assessments",
            ],
        },
        "mentor": {
            "name": "Sun Jianshun",
            "org": "Primary School, China (Special-grade Teacher)",
            "years": "~30 years",
            "path": (
                "Rural all-subject teacher (1994) → Deputy Director of Teaching Affairs "
                "(2003) → Municipal Teaching Expert → Provincial Discipline Leader "
                "→ Special-grade Teacher."
            ),
            "daily": (
                "Teaching, lesson polishing, leading research projects, writing papers "
                "(100+ published/awarded), and mentoring young teachers."
            ),
        },
    },
    {
        "id": "esd",
        "title": "ESD Curriculum Developer",
        "required_skills": [
            "ESD Framework",
            "Curriculum Design",
            "LMS Tools",
        ],
        "interests": [
            "Protecting the Environment",
            "Teaching & Mentoring",
            "Design & Visuals",
        ],
        "salary_range": [40000, 80000],
        "top_countries": ["Finland", "Japan", "Germany"],
        "ai_match": {
            "level": "Highly Adapted",
            "color": "#2563eb",
            "bg": "#eff6ff",
        },
        "overview": (
            "Design educational materials aligned with UN SDGs. Highly meaningful work."
        ),
        "outlook": "SDG 4.7 mandates driving growth in public education.",
        "sdgs": [
            "SDG 4: Quality Education",
            "SDG 5: Gender Equality",
            "SDG 10: Reduced Inequalities",
        ],
        "certs": {
            "Default": ["UNESCO ESD Training"],
            "United Kingdom": ["ATD Instructional Design"],
        },
        "learning_resources": {
            "courses": [
                "UNESCO ESD for 2030 Capacity Building",
                "Coursera 'Sustainable Development for All'",
            ],
            "practical": [
                "Draft sample curricula and teacher guides",
                "Participate in educational pilot programs",
            ],
        },
        "mentor": {
            "name": "Endeara C.",
            "org": "EdTech (Senior Curriculum Manager)",
            "years": "8+ years since leaving classroom",
            "path": (
                "Classroom Teacher → Full-time Curriculum Developer (2018) "
                "→ Senior Curriculum Manager in EdTech."
            ),
            "daily": (
                "Designing learning sequences, building content, aligning courses to "
                "programme objectives, running feedback loops, and iterating curriculum."
            ),
        },
    },
    {
        "id": "acc",
        "title": "Accountant",
        "required_skills": [
            "Financial Accounting",
            "Audit Assurance",
            "Tax",
        ],
        "interests": [
            "Finance & Numbers",
            "Compliance & Risk Control",
        ],
        "salary_range": [60000, 120000],
        "top_countries": ["United States", "United Kingdom", "Canada"],
        "ai_match": {
            "level": "Highly Adapted",
            "color": "#2563eb",
            "bg": "#eff6ff",
        },
        "overview": (
            "Prepare financial reports and ensure compliance. "
            "High stability and clear progression."
        ),
        "outlook": (
            "5% growth. AI automates bookkeeping, pushing professionals toward advisory."
        ),
        "sdgs": [
            "SDG 8: Decent Work",
            "SDG 10: Reduced Inequalities",
            "SDG 5: Gender Equality",
        ],
        "certs": {
            "Default": ["CPA (Certified Public Accountant)"],
            "United States": ["US CPA"],
            "United Kingdom": ["ACCA"],
            "Australia": ["CPA Australia"],
        },
        "learning_resources": {
            "courses": [
                "Coursera 'Accounting for Decision Making' (Illinois)",
                "IFRS Foundation official resources",
            ],
            "practical": [
                "Audit working-paper simulations",
                "Seek a Big 4 or corporate finance internship",
            ],
        },
        "mentor": {
            "name": "Xu Bin",
            "org": "Anhui Kechuang Zhongguang Technology, CFO",
            "years": "7 years",
            "path": (
                "Audit Associate, Rongcheng CPA Firm (2017) → Finance Deputy Director, "
                "Nanjing Mulei Laser (2022) → CFO, Anhui Kechuang Zhongguang Technology (2024)."
            ),
            "daily": (
                "Financial strategy, digital transformation (RPA, OCR), shifting the finance "
                "team from traditional accounting to business-finance integration."
            ),
        },
    },
]


SKILL_GROUPS = [


#Information is organized by major categories containing subcategories.

    {
        "id": "tech",
        "label": "Technology & Engineering",
#The major category.

        "children": [

#The subcategories.

            {"id": "python", "label": "Python"},
            {"id": "ml", "label": "Machine Learning"},
            {"id": "mlops", "label": "MLOps"},
            {"id": "llm", "label": "LLM (RAG/Agent)"},
            {"id": "cad", "label": "CAD/CAE"},
            {"id": "thermo", "label": "Thermodynamics"},
            {"id": "manufacturing", "label": "Manufacturing"},
            {"id": "pm", "label": "Project Management"},
            {"id": "ict_infra", "label": "ICT Infrastructure"},
            {"id": "me", "label": "M&E (Monitoring & Evaluation)"},

#The id is for machine recognition, and the label is for customer recognition.

        ],
    },
    {
        "id": "health",
        "label": "Health & Wellbeing",
        "children": [
            {"id": "clinical", "label": "Clinical Diagnosis"},
            {"id": "patient", "label": "Patient Care"},
            {"id": "med_ethics", "label": "Medical Ethics"},
            {"id": "psych_assess", "label": "Psychological Assessment"},
            {"id": "counselling", "label": "Counselling"},
            {"id": "empathy", "label": "Empathy"},
        ],
    },
    {
        "id": "law",
        "label": "Law & Social Impact",
        "children": [
            {"id": "legal_research", "label": "Legal Research"},
            {"id": "drafting", "label": "Drafting"},
            {"id": "advocacy", "label": "Court Advocacy"},
            {"id": "survivor", "label": "Survivor-centered Practice"},
            {"id": "policy_adv", "label": "Policy Advocacy"},
            {"id": "meal", "label": "MEAL"},
        ],
    },
    {
        "id": "edu",
        "label": "Education & Sustainability",
        "children": [
            {"id": "curriculum_plan", "label": "Curriculum Planning"},
            {"id": "classroom", "label": "Classroom Management"},
            {"id": "assessment", "label": "Assessment"},
            {"id": "esd_framework", "label": "ESD Framework"},
            {"id": "curriculum_design", "label": "Curriculum Design"},
            {"id": "lms", "label": "LMS Tools"},
        ],
    },
    {
        "id": "biz",
        "label": "Business & Finance",
        "children": [
            {"id": "fin_acc", "label": "Financial Accounting"},
            {"id": "audit", "label": "Audit Assurance"},
            {"id": "tax", "label": "Tax"},
        ],
    },
]


INTEREST_GROUPS = [
    {
        "id": "int-tech",
        "label": "Technology & Engineering",
        "children": [
            {"id": "coding", "label": "Coding & Building Systems"},
            {"id": "making", "label": "Building & Fixing Physical Things"},
            {"id": "data", "label": "Data, Metrics & Analysis"},
            {"id": "newtech", "label": "Researching New Tech"},
        ],
    },
    {
        "id": "int-people",
        "label": "People & Wellbeing",
        "children": [
            {"id": "caring", "label": "Caring & Healing Others"},
            {"id": "listening", "label": "Listening & Counselling"},
            {"id": "teaching", "label": "Teaching & Mentoring"},
            {"id": "behavior", "label": "Understanding Human Behavior"},
        ],
    },
    {
        "id": "int-creative",
        "label": "Creativity & Communication",
        "children": [
            {"id": "writing", "label": "Writing & Content Creation"},
            {"id": "design", "label": "Design & Visuals"},
            {"id": "speaking", "label": "Public Speaking & Advocacy"},
            {"id": "community", "label": "Community Engagement"},
        ],
    },
    {
        "id": "int-biz",
        "label": "Business & Organization",
        "children": [
            {"id": "finance", "label": "Finance & Numbers"},
            {"id": "managing", "label": "Organizing & Managing"},
            {"id": "compliance", "label": "Compliance & Risk Control"},
            {"id": "entrepreneur", "label": "Entrepreneurship"},
        ],
    },
    {
        "id": "int-society",
        "label": "Nature & Society",
        "children": [
            {"id": "environment", "label": "Protecting the Environment"},
            {"id": "justice", "label": "Social Justice & Human Rights"},
            {"id": "policy", "label": "Policy & Governance"},
            {"id": "humanitarian", "label": "Humanitarian Aid"},
        ],
    },
]


TIME_OPTIONS = [
    "Less than 1 year",
    "1–2 years",
    "2–3 years",
    "More than 3 years",
]

SALARY_OPTIONS = [
    "Under $30,000",
    "$30,000 – $60,000",
    "$60,000 – $100,000",
    "$100,000 – $150,000",
    "$150,000 – $250,000",
    "Above $250,000",
]

COUNTRY_OPTIONS = [
    "United States",
    "United Kingdom",
    "Canada",
    "Australia",
    "Singapore",
    "Malaysia",
    "Hong Kong, China",
    "Mainland China",
    "Germany",
    "Finland",
    "Japan",
]


SCHEMA = [


#Start to define which questions the questionnaire contains, what each question looks like, and when it appears.

    {
        "id": "path",
        "type": "single",
        "required": True,
        "title": (
            "Do you want to work in a field you already have experience in, "
            "or start a completely new career path?"
        ),
        "options": [
            {"v": "A", "t": "A. Work in a field I already have experience in"},
            {"v": "B", "t": "B. Start a completely new career path"},
        ],
    },
    {
        "id": "skills",
        "type": "groupedMulti",
        "required": True,
        "when": lambda answers: answers.get("path") in {"A", "B"},
        "title": "Your areas of expertise",
        "hint": (


#Displayed below the question as an operation guide for the user.

            "Select a category, then select specific skills you have "
            "or are currently learning."
        ),
        "groups": SKILL_GROUPS,
        "hasFollowUp":True,


#Indicates whether there is a follow-up.

    },
    {
        "id": "interest",
        "type": "groupedMulti",
        "required": True,
        "when": lambda answers: answers.get("path") in {"A", "B"},
        "title": "What kind of tasks do you enjoy doing?",
        "hint": (
            "Select a category, then select the activities you find engaging."
        ),
        "groups": INTEREST_GROUPS,
        "hasFollowUp": False,
    },
    {
        "id": "time",
        "type": "single",
        "required": True,
        "when": lambda answers: answers.get("path") in {"A", "B"},
        "title": "When do you plan to start working in this field?",
        "options": [
            {"v": value, "t": value}
            for value in ["This year", "In 1 year", "In 2-3 years", "Longer than 3 years"]
        ],
    },
    {
        "id": "salary",
        "type": "single",
        "required": True,
        "when": lambda answers：    
answers.get("path") in {"A", "B"},


#Determine whether the subsequent questions should be displayed.

        "title": "What is your expected annual salary? (in USD)",
        "options": [{"v": value, "t": value} 

#What the user sees is t (text), while the hidden data sent from the frontend to the backend is v (value).

            for value in SALARY_OPTIONS],
    },
    {
        "id": "country",
        "type": "single",
        "required": True,
        "when": lambda answers: answers.get("path") in {"A", "B"},
        "title": "Which country or region do you plan to work in?",
        "options": [{"v": value, "t": value} for value in COUNTRY_OPTIONS],
    },
    {
        "id": "ready",
        "type": "single",
        "required": True,
        "when": lambda answers: answers.get("path") == "B",
        "title": "Do you have enough time and determination to prepare?",
        "options": [
            {"v": "YES", "t": "YES, I am ready"},
            {"v": "NO", "t": "NO, not yet"},
        ],
    },
]
