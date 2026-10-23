"""Imported career reference data; market figures are not verified or displayed."""

CAREERS = [
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
]
