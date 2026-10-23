
ROLES = [
    {
        "id": 1,
        "name": "AI Engineer",
        "description": "Combines software engineering, machine learning, and data engineering to transform AI models into stable production-grade systems.",
        "required_skills": [
            "Python Programming", "Machine Learning", "Deep Learning",
            "PyTorch/TensorFlow", "Data Pre-processing", "LLM Application (RAG/Agent)",
            "MLOps & Model Deployment", "Docker/K8s", "Cloud AI Platforms (AWS/GCP)",
            "AI Safety & Compliance"
        ],
        "interests": ["Technology", "AI Models", "System Architecture", "Open Source"],
        "learning_steps": [
            "Learn Python and Math fundamentals",
            "Master deep learning frameworks and data processing",
            "Complete end-to-end AI projects and deploy them",
            "Participate in real-world AI projects and track frontier tech"
        ],
        "sdgs": ["SDG 8: Decent Work and Economic Growth", "SDG 9: Industry, Innovation and Infrastructure", "SDG 10: Reduced Inequalities"],
        "trend_status": "BLS projects 22% growth (2024-2034). High demand for hybrid engineers combining software dev, ML, and MLOps.",
        "certifications": [
            {"name": "AWS Certified Machine Learning - Specialty", "issuer": "AWS", "region": "Global", "url": "https://aws.amazon.com/certification/"},
            {"name": "Azure AI Engineer Associate", "issuer": "Microsoft", "region": "Global", "url": "https://learn.microsoft.com/"},
            {"name": "Google Professional Machine Learning Engineer", "issuer": "Google Cloud", "region": "Global", "url": "https://cloud.google.com/certification/"}
        ],
        "salary_ranges": {
            "MYR": {"Junior": "65k-90k", "Mid": "90k-140k", "Senior": "140k-200k", "Tech Lead": "200k-280k"},
            "SGD": {"Junior": "60k-80k", "Mid": "80k-120k", "Senior": "120k-180k", "Tech Lead": "180k-250k"},
            "HKD": {"Junior": "360k-500k", "Mid": "500k-800k", "Senior": "800k-1,200k", "Tech Lead": "1,200k-1,800k"},
            "AUD": {"Junior": "85k-105k", "Mid": "105k-140k", "Senior": "140k-190k", "Tech Lead": "190k-260k"},
            "USD": {"Junior": "130k-180k", "Mid": "170k-240k", "Senior": "230k-320k", "Staff": "320k-450k"},
            "GBP": {"Junior": "40k-55k", "Mid": "55k-80k", "Senior": "80k-110k", "Tech Lead": "110k-150k"},
            "CAD": {"Junior": "75k-95k", "Mid": "95k-130k", "Senior": "130k-175k", "Tech Lead": "175k-230k"}
        },
        "top_countries": [
            {"country": "United States", "highlights": "World-leading AI ecosystem, top universities, and highest VC investment."},
            {"country": "China", "highlights": "Huge internet and manufacturing market, large-scale foundation models and compute clusters."},
            {"country": "United Kingdom", "highlights": "European AI talent hub, home to DeepMind, strong in finance and biotech AI."}
        ],
        "data_sources": ["Robert Half 2026 Salary Guide", "U.S. BLS 2025", "Michael Page 2026"],
        "data_date": "2026-10-21"
    },
    {
        "id": 2,
        "name": "Accountant (Chartered Professional)",
        "description": "Licensed professionals performing financial accounting, audit assurance, tax compliance, management accounting, and ESG reporting.",
        "required_skills": [
            "Financial Accounting", "Audit Assurance", "Tax Compliance",
            "Management Accounting", "Internal Control", "Accounting Ethics",
            "Financial Data Analytics", "ESG Reporting", "Commercial Law"
        ],
        "interests": ["Finance", "Compliance", "Corporate Governance", "Tax Planning"],
        "learning_steps": [
            "Learn fundamental financial accounting and commercial law",
            "Study IFRS, auditing standards, and tax systems",
            "Complete supervised practical experience in a firm or corporate finance",
            "Pass qualification exams and complete mandatory CPD"
        ],
        "sdgs": ["SDG 8: Decent Work and Economic Growth", "SDG 10: Reduced Inequalities", "SDG 12: Responsible Consumption and Production", "SDG 16: Peace, Justice and Strong Institutions"],
        "trend_status": "BLS projects 5% growth (2025-2035). Routine bookkeeping is shrinking, while hybrid skills in data analytics and ESG are in high demand.",
        "certifications": [
            {"name": "ACCA", "issuer": "ACCA", "region": "Global", "url": "https://www.accaglobal.com"},
            {"name": "CPA Australia", "issuer": "CPA Australia", "region": "Australia, HK, etc.", "url": "https://www.cpaaustralia.com.au"},
            {"name": "ICAEW ACA", "issuer": "ICAEW", "region": "UK, HK, etc.", "url": "https://www.icaew.com"},
            {"name": "CGMA", "issuer": "CIMA/AICPA", "region": "Global", "url": "https://www.cgma.org"},
            {"name": "ESG Reporting Certificate", "issuer": "IFAC", "region": "Global", "url": "https://education.ifac.org/"}
        ],
        "salary_ranges": {
            "MYR": {"Entry": "60k-75k", "Mid": "75k-100k", "Senior": "100k-130k", "Manager": "130k-180k"},
            "SGD": {"Entry": "45k-55k", "Mid": "55k-80k", "Senior": "80k-110k", "Manager": "110k-160k"},
            "HKD": {"Entry": "240k-300k", "Mid": "360k-500k", "Senior": "500k-700k", "Manager": "700k-1000k"},
            "AUD": {"Entry": "65k-80k", "Mid": "80k-105k", "Senior": "105k-130k", "Manager": "130k-170k"},
            "USD": {"Entry": "65k-85k", "Senior": "90k-120k", "Manager": "130k-175k", "Senior Manager": "170k-230k"},
            "GBP": {"Entry": "30k-35k", "Mid": "45k-60k", "Senior": "60k-80k", "Manager": "80k-110k"},
            "CAD": {"Entry": "60k-75k", "Mid": "75k-95k", "Senior": "95k-130k", "Manager": "130k-170k"}
        },
        "top_countries": [
            {"country": "United States", "highlights": "World's largest accountancy market with mature AICPA-CPA framework."},
            {"country": "United Kingdom", "highlights": "Birthplace of modern accountancy, home to ICAEW and ACCA."},
            {"country": "Canada", "highlights": "Unified CPA Canada framework with provincial regulation and North American recognition."}
        ],
        "data_sources": ["IFAC 2025 Annual Report", "U.S. BLS 2025", "Robert Half 2026", "Michael Page 2026"],
        "data_date": "2026-10-21"
    },
    {
        "id": 3,
        "name": "Sustainable Development Education Curriculum Developer",
        "description": "Designs curricula, materials, and learning activities aligned with UN SDGs and UNESCO ESD-for-2030 standards.",
        "required_skills": [
            "ESD & SDG Framework", "Curriculum Design", "Instructional Design (ADDIE)",
            "Inclusive Curriculum", "Curriculum Evaluation", "Stakeholder Communication",
            "Content Research", "LMS Platforms", "Project Management"
        ],
        "interests": ["Education Innovation", "Sustainability", "Curriculum Design", "NGO Work"],
        "learning_steps": [
            "Learn SDG frameworks and foundational pedagogy",
            "Master backward design/ADDIE and UNESCO-IBE guidance",
            "Produce sample curricula and pilot evaluations",
            "Participate in real ESD projects and continuous CPD"
        ],
        "sdgs": ["SDG 4: Quality Education", "SDG 13: Climate Action", "SDG 15: Life on Land", "SDG 16: Peace, Justice and Strong Institutions"],
        "trend_status": "BLS projects 1% growth (2024-2034, slower than average). Demand expands in public education, NGOs, and ESG corporations.",
        "certifications": [
            {"name": "WSQ DDDLP 2.0 Diploma", "issuer": "IAL Singapore", "region": "Singapore", "url": "https://www.ial.edu.sg/"},
            {"name": "UNESCO ESD for 2030 Course", "issuer": "UNESCO", "region": "Global", "url": "https://en.unesco.org/esd-for-2030/capacity-building"},
            {"name": "WISDP CSDP", "issuer": "WISDP", "region": "Hong Kong, etc.", "url": "https://wisdp.org/"},
            {"name": "ATD Instructional Design Certificate", "issuer": "ATD", "region": "Global", "url": "https://www.atd.edu/"}
        ],
        "salary_ranges": {
            "MYR": {"Junior": "45k-60k", "Mid": "60k-85k", "Senior": "85k-115k", "Manager": "115k-150k"},
            "SGD": {"Junior": "38k-50k", "Mid": "50k-70k", "Senior": "70k-95k", "Manager": "95k-125k"},
            "HKD": {"Junior": "240k-340k", "Mid": "340k-480k", "Senior": "480k-650k", "Manager": "650k-850k"},
            "AUD": {"Junior": "62k-78k", "Mid": "78k-100k", "Senior": "100k-115k", "Manager": "115k-140k"},
            "USD": {"Junior": "48k-62k", "Mid": "62k-80k", "Senior": "80k-105k", "Manager": "105k-135k"},
            "GBP": {"Junior": "28k-36k", "Mid": "36k-48k", "Senior": "48k-62k", "Manager": "62k-80k"},
            "CAD": {"Junior": "48k-62k", "Mid": "62k-78k", "Senior": "78k-98k", "Manager": "98k-125k"}
        },
        "top_countries": [
            {"country": "Finland", "highlights": "Deep integration of phenomenon-based learning and sustainability, legally embedded in national curricula."},
            {"country": "Japan", "highlights": "Systematic ESD since the 1990s, clear national curriculum requirements, and mature school-NGO networks."},
            {"country": "Germany", "highlights": "Mandatory interdisciplinary ESD in state laws, supported by federal grants and corporate foundations."}
        ],
        "data_sources": ["U.S. BLS 2025", "UNESCO A/80/236", "Michael Page 2026"],
        "data_date": "2026-10-21"
    },
    {
        "id": 4,
        "name": "Psychologist",
        "description": "Applies psychological theories and assessment tools for mental health intervention, research, and organizational consulting. Clinical psychologists cannot prescribe medication.",
        "required_skills": [
            "Active Listening", "Empathy", "Ethical Decision-Making",
            "Psychological Assessment", "Intervention Planning", "Critical Thinking",
            "Psychological Statistics", "Clinical Documentation", "Cross-cultural Competence",
            "Interviewing Skills"
        ],
        "interests": ["Mental Health", "Helping Others", "Behavioral Research", "Organizational Consulting"],
        "learning_steps": [
            "Learn foundational psychology courses",
            "Study CBT, psychometrics, and major therapy orientations",
            "Complete research or clinical training with supervision",
            "Obtain advanced degrees/licensure and maintain continuing education"
        ],
        "sdgs": ["SDG 3: Good Health and Well-being", "SDG 4: Quality Education", "SDG 10: Reduced Inequalities", "SDG 16: Peace, Justice and Strong Institutions"],
        "trend_status": "BLS projects 6% overall growth (2024-2034), with 11.2% growth for clinical and counseling psychologists. Driven by rising global mental health demand.",
        "certifications": [
            {"name": "ASPPB CPQ", "issuer": "ASPPB", "region": "North America/Global", "url": "https://www.asppb.net/"},
            {"name": "EuroPsy", "issuer": "EFPA", "region": "Europe/Global", "url": "https://www.efpa.eu/"},
            {"name": "EMDR Therapist", "issuer": "EMDRIA", "region": "Global", "url": "https://www.emdria.org/"},
            {"name": "CBT Certification", "issuer": "CACBT", "region": "Global", "url": "https://worldcbt.org/"},
            {"name": "WHO PFA Certificate", "issuer": "WHO / PAHO", "region": "Global", "url": "https://campus.paho.org/"}
        ],
        "salary_ranges": {
            "MYR": {"Assistant": "42k-55k", "Registered": "55k-75k", "Mid": "75k-100k", "Senior": "100k-130k", "Private": "160k-300k+"},
            "SGD": {"Assistant": "40k-50k", "Registered": "55k-70k", "Mid": "70k-95k", "Senior": "95k-120k", "Private": "150k-250k+"},
            "HKD": {"Assistant": "220k-300k", "Registered": "300k-420k", "Mid": "420k-600k", "Senior": "600k-800k", "Private": "1,000k-2,000k+"},
            "AUD": {"Assistant": "60k-75k", "Registered": "75k-90k", "Mid": "90k-115k", "Senior": "115k-140k", "Private": "170k-260k+"},
            "USD": {"Assistant": "52k-68k", "Registered": "68k-85k", "Mid": "85k-110k", "Senior": "110k-140k", "Private/I-O": "160k-240k+"},
            "GBP": {"Assistant": "28k-36k", "Trainee": "38k-48k", "Mid": "48k-60k", "Senior": "60k-72k", "Principal": "72k-90k"},
            "CAD": {"Assistant": "48k-60k", "Registered": "60k-78k", "Mid": "78k-95k", "Senior": "95k-115k", "Private": "120k-160k+"}
        },
        "top_countries": [
            {"country": "United States", "highlights": "World's most mature system for psychology education, licensure, and employment. APA sets global standards."},
            {"country": "United Kingdom", "highlights": "Statutory registration by HCPC, accreditation by BPS, and well-established NHS psychological services."},
            {"country": "Canada", "highlights": "Provincial colleges govern registration, unified ethics and supervision requirements, balanced research and clinical focus."}
        ],
        "data_sources": ["U.S. BLS 2025", "TherapyRoute 2025", "APA Psychologist Salary Survey 2025"],
        "data_date": "2026-10-21"
    },
    {
        "id": 5,
        "name": "ICT-Access Project Officer",
        "description": "Manages full-cycle inclusive connectivity projects in the ICT4D sector, expanding broadband/mobile access for remote and underserved populations.",
        "required_skills": [
            "ICT4D Policy Literacy", "Logical Framework Design", "Budget & Compliance",
            "Multi-stakeholder Coordination", "Monitoring & Evaluation (M&E)",
            "ICT Infrastructure Literacy", "Procurement Oversight", "Report Writing",
            "Cross-cultural Communication", "Data Analysis"
        ],
        "interests": ["Digital Inclusion", "International Development", "Project Management", "Social Impact"],
        "learning_steps": [
            "Learn digital divide concepts and UN UMC objectives",
            "Master LFA, M&E methodologies, and PPP models",
            "Complete ICT4D internships and build a project portfolio",
            "Participate in full-cycle real-world projects and track policy updates"
        ],
        "sdgs": ["SDG 9: Industry, Innovation and Infrastructure", "SDG 10: Reduced Inequalities", "SDG 11: Sustainable Cities and Communities", "SDG 17: Partnerships for the Goals"],
        "trend_status": "BLS projects 7% growth for project management specialists (2025-2035). Developing nations continuously release inclusive broadband jobs.",
        "certifications": [
            {"name": "PMP", "issuer": "PMI", "region": "Global", "url": "https://www.pmi.org/"},
            {"name": "PMD-PRO", "issuer": "PM4DEV", "region": "Global", "url": "https://www.pm4dev.com/"},
            {"name": "ITU Academy Certificate", "issuer": "ITU", "region": "Global", "url": "https://academy.itu.int/"},
            {"name": "UNDP M&E Certificate", "issuer": "UNDP", "region": "Global", "url": "https://learning.undp.org/"},
            {"name": "CCNA", "issuer": "Cisco", "region": "Global", "url": "https://www.cisco.com/"}
        ],
        "salary_ranges": {
            "MYR": {"Junior": "50k-70k", "Mid": "70k-100k", "Senior": "100k-140k", "PM": "140k-190k"},
            "SGD": {"Junior": "42k-55k", "Mid": "55k-75k", "Senior": "75k-100k", "PM": "100k-140k"},
            "HKD": {"Junior": "300k-420k", "Mid": "420k-650k", "Senior": "650k-900k", "PM": "900k-1,300k"},
            "AUD": {"Junior": "70k-88k", "Mid": "88k-115k", "Senior": "115k-145k", "PM": "145k-190k"},
            "USD": {"Junior": "55k-72k", "Mid": "72k-95k", "Senior": "95k-120k", "PM": "120k-160k"},
            "GBP": {"Junior": "32k-42k", "Mid": "42k-58k", "Senior": "58k-78k", "PM": "78k-105k"},
            "CAD": {"Junior": "55k-72k", "Mid": "72k-95k", "Senior": "95k-120k", "PM": "120k-160k"}
        },
        "top_countries": [
            {"country": "United States", "highlights": "Dense multilateral institutions, federal/state rural broadband programs, and complete ICT4D research clusters."},
            {"country": "Finland", "highlights": "High domestic universal broadband coverage, exports digital inclusion expertise, and mature universal service funds."},
            {"country": "Singapore", "highlights": "Highly advanced domestic infrastructure, Asia-Pacific hub for multilateral bodies, and strong hybrid talent pool."}
        ],
        "data_sources": ["U.S. BLS 2025", "ITU ICT Development Index 2026", "Michael Page 2026"],
        "data_date": "2026-10-21"
    },
    {
        "id": 6,
        "name": "Physician (Medical Doctor)",
        "description": "Licensed healthcare professionals responsible for disease diagnosis, treatment, preventive care, and patient management.",
        "required_skills": [
            "Clinical Consultation", "Diagnosis & Differential Diagnosis", "Lab/Imaging Interpretation",
            "Treatment Plan Formulation", "Emergency Care", "Doctor-patient Communication",
            "Medical Ethics", "Medical Documentation", "Evidence-based Medicine",
            "Public Health Mindset"
        ],
        "interests": ["Healthcare", "Patient Care", "Medical Research", "Public Health"],
        "learning_steps": [
            "Study basic medical sciences",
            "Complete clinical theory and clerkship",
            "Finish supervised internship and residency training",
            "Pass licensing exams and maintain CME (Continuing Medical Education)"
        ],
        "sdgs": ["SDG 3: Good Health and Well-being", "SDG 4: Quality Education", "SDG 10: Reduced Inequalities", "SDG 17: Partnerships for the Goals"],
        "trend_status": "BLS projects 3% growth (2024-2034, on par with average). Aging populations drive demand, though long training cycles limit short-term expansion.",
        "certifications": [
            {"name": "AMC (Australian Medical Council)", "issuer": "AMC", "region": "Australia", "url": "https://www.amc.org.au/"},
            {"name": "PLAB / GMC Registration", "issuer": "GMC", "region": "UK", "url": "https://www.gmc-uk.org/"},
            {"name": "USMLE", "issuer": "ECFMG/NBME", "region": "US", "url": "https://www.ecfmg.org/"},
            {"name": "WFME Accreditation", "issuer": "WFME", "region": "Global", "url": "https://wfme.org/"}
        ],
        "salary_ranges": {
            "MYR": {"Intern": "54k-66k", "MO": "72k-96k", "Registrar": "108k-168k", "Consultant": "180k-240k", "Private": "300k-700k+"},
            "SGD": {"Intern": "60k-72k", "MO": "78k-108k", "Registrar": "108k-168k", "Assoc Consultant": "180k-220k", "Private": "400k-800k+"},
            "HKD": {"Resident": "900k-1,200k", "Assoc Consultant": "1,400k-1,800k", "Consultant": "2,000k-3,000k", "Private": "3,500k-8,000k+"},
            "AUD": {"Intern": "80k-98k", "Resident": "90k-110k", "Registrar": "110k-160k", "Staff Consultant": "205k-345k", "Private": "300k-680k+"},
            "USD": {"Resident": "65k-85k", "Fellow": "80k-100k", "Primary Care": "220k-320k", "Specialist": "350k-600k+"},
            "GBP": {"FY1": "32k-38k", "FY2": "38k-45k", "Registrar": "48k-70k", "Consultant": "90k-130k"},
            "CAD": {"Resident": "60k-85k", "Family Physician": "180k-260k", "Specialist": "240k-420k"}
        },
        "top_countries": [
            {"country": "United States", "highlights": "Large physician workforce, rigorous MD/USMLE pathway, mature residency and fellowship training."},
            {"country": "Germany", "highlights": "Mature European medical system, standardised residency, universal statutory health insurance, and GP gatekeeping."},
            {"country": "Australia", "highlights": "Strict WFME standards, AMC regulation, universal Medicare, and strong rural/remote incentives."}
        ],
        "data_sources": ["U.S. BLS 2025", "WHO Global Health Workforce Report 2026", "OECD Health Statistics 2025", "Michael Page 2026"],
        "data_date": "2026-10-21"
    },
    {
        "id": 7,
        "name": "Lawyer (Attorney-at-Law)",
        "description": "Licensed professionals providing legal advice, drafting legal documents, negotiation, and courtroom representation.",
        "required_skills": [
            "Legal Research", "Legal Document Drafting", "Case Strategy Analysis",
            "Court Advocacy & Negotiation", "Legal Ethics", "Client Communication",
            "Evidence Organization", "Time Management", "Legal Tech Tools",
            "Cross-jurisdictional Perspective"
        ],
        "interests": ["Law & Justice", "Debate & Negotiation", "Compliance", "Pro Bono Work"],
        "learning_steps": [
            "Study foundational law subjects",
            "Practice legal writing, case analysis, and moot court",
            "Complete qualifying law degree and supervised training (pupillage/articling)",
            "Pass bar exams, apply for practising certificate, and maintain CLE (Continuing Legal Education)"
        ],
        "sdgs": ["SDG 5: Gender Equality", "SDG 10: Reduced Inequalities", "SDG 16: Peace, Justice and Strong Institutions", "SDG 17: Partnerships for the Goals"],
        "trend_status": "BLS projects 4% growth (2024-2034, on par with average). Corporate compliance, cross-border trade, and ESG legal work drive demand; AI automates routine drafting but not courtroom advocacy.",
        "certifications": [
            {"name": "Singapore QLPT", "issuer": "Ministry of Law Singapore", "region": "Singapore", "url": "https://www.mlaw.gov.sg/"},
            {"name": "Malaysian Bar Practising Certificate", "issuer": "Malaysian Bar", "region": "Malaysia", "url": "https://www.malaysianbar.org.my/"},
            {"name": "Legal Profession Board (State)", "issuer": "Australia", "region": "Australia", "url": "https://www.legalprofession.gov.au/"},
            {"name": "CIArb Membership", "issuer": "Chartered Institute of Arbitrators", "region": "Global", "url": "https://www.ciarb.org/"},
            {"name": "HK Solicitors/Barristers", "issuer": "Law Society of Hong Kong", "region": "Hong Kong", "url": "https://www.hklawsoc.org.hk/"}
        ],
        "salary_ranges": {
            "MYR": {"Chambering": "42k-60k", "NQ": "60k-90k", "Mid": "90k-130k", "Senior": "130k-180k", "Partner": "240k-500k+"},
            "SGD": {"Pupillage": "40k-55k", "NQ": "100k-140k", "Mid": "140k-190k", "Senior": "190k-260k", "Partner": "350k-800k+"},
            "HKD": {"Trainee": "240k-300k", "NQ": "360k-480k", "Mid": "480k-700k", "Senior": "700k-1,100k", "Partner": "1,600k-4,000k+"},
            "AUD": {"Articling": "60k-75k", "NQ": "75k-95k", "Mid": "95k-130k", "Senior": "130k-180k", "Partner": "260k-450k+"},
            "USD": {"First-Year Big Law": "225k-250k", "Mid": "270k-350k", "Senior": "350k-450k", "Counsel": "420k-600k"},
            "GBP": {"Trainee": "38k-50k", "NQ": "70k-110k", "Mid": "110k-150k", "Senior": "150k-200k", "Partner": "280k-700k+"},
            "CAD": {"Articling": "60k-80k", "First-Year": "115k-130k", "Mid": "130k-170k", "Senior": "170k-220k", "Partner": "280k-500k+"}
        },
        "top_countries": [
            {"country": "United States", "highlights": "World's largest lawyer workforce, state-based bar licensing, and highly developed corporate/capital market legal sectors."},
            {"country": "United Kingdom", "highlights": "Dual-track solicitor and barrister system, global hub for cross-border commercial law in London."},
            {"country": "Canada", "highlights": "Provincial law societies, coexistence of common law and Quebec civil law, balanced commercial and public legal aid practice."}
        ],
        "data_sources": ["U.S. BLS 2025", "ABA 2025", "Robert Half 2026", "Michael Page 2026"],
        "data_date": "2026-10-21"
    }
<<<<<<< HEAD
]
>>>>>>> origin/LIU

"""职业数据、问卷选项和问卷题目配置。"""

ROLES = [
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
    {
        "id": "tech",
        "label": "Technology & Engineering",
        "children": [
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


# 首页负责欢迎说明；这里从第一道实际问卷题开始。
SCHEMA = [
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
            "Select a category, then select specific skills you have "
            "or are currently learning."
        ),
        "groups": SKILL_GROUPS,
        "hasFollowUp": True,
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
        "when": lambda answers: answers.get("path") in {"A", "B"},
        "title": "What is your expected annual salary? (in USD)",
        "options": [{"v": value, "t": value} for value in SALARY_OPTIONS],
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