# CareerNovacoke

>CareerNovacoke is an AI-powered career guidance platform that helps job seekers, fresh graduates, and career changers identify suitable career paths, understand future job market trends, discover skill gaps, and create personalised reskilling plans for the AI era.
---

## Team Information

| Field                  | Details                                        |
| ---------------------- | ---------------------------------------------- |
| **Team Name**          | 疯狂星期四                                       |
| **Team Domain**        | Domain 1                                       |
| **SDG Track (1–17)**   | SDG 4 — Quality Education,                     |
|                        | SDG 8 - Decnet Work And Economic Growth,       |
|                        | SDG 9 - Industry, Innovatio And Infrastructure,|
|                        | SDG 10 - Reduced Inequalities                  |
| **Team Leader**        | LIN JIA XI                                     |
| **University**         | Xiamen University Malaysia                     |
| **Number of Members**  | 4                                              |

## Links

| Resource          | Link                                               |
| ----------------- | -------------------------------------------------- |
| GitHub Repository | https://github.com/breathfreea-ctrl/CareerNovacoke |
| Live Demo         | https://careernova-coke.replit.app                 |
| Slide Deck        | https://drive.google.com/file/d/1kjFNzraZ--nkRZWUzv4FBf7diD-kte7q/view?usp=sharing|
| Demo Video        | https://youtu.be/Ehhi850yV5c                       |

---

## Overview

### Problem

As AI and technology change the job market, many workers face a growing gap between their skills and job requirements. Fresh graduates and career changers struggle to find the right career direction, while some workers risk losing their jobs. This affects workers, students, HR teams, and education centers, making career guidance and skill training more important than ever.

### Solution

Our AI-powered website matches users with suitable careers, identifies their skill gaps, and creates personal learning plans. It also updates career trends to help users build the right skills, find direction, and prepare for future jobs.

### Key Features

- **Feature 1** — Personalised Career Matching: Analyses users’ skills, interests, salary expectations, and preferred countries through a structured questionnaire to recommend suitable careers ranked by matching scores.
- **Feature 2** — Customised Learning Plans: Generates step-by-step learning plans based on users’ selected career goals, skill gaps, target timeline, and predefined learning resources.
- **Feature 3** — Career Insights and Learning Resources: Provides career information, salary ranges, target countries, relevant certifications, learning resources, and mentor profiles to help users explore career pathways and plan their next steps.

### Tech Stack

| Layer                            | Technology                              |
|----------------------------------|-----------------------------------------|
| Frontend                         | HTML, CSS, JavaScript, Jinja2 Templates |
| Backend                          | Python, Flask, models.py                |
| Data & Documentation             | Product documentation,README.md         |
| Hosting / Development            | Replit Core, GitHub, matching.py         |

---

## Project Structure

```
.
├── .agents/                 # Agent-related configuration
├── src/
│   └── repl_nix_workspace/  # Python workspace package
├── static/                  # Frontend static assets (CSS, JavaScript, images)
├── templates/               # HTML templates for the web pages
├── submission/              # Required submission documents
│   ├── SDC2026_疯狂星期四_Preliminary.pdf      # Preliminary submission
│   ├── SDC2026_疯狂星期四_TechDeclaration.pdf  # Technology declaration
│   ├── SDC2026_疯狂星期四_Replit_POU.pdf       # Replit proof of use
|   ├── demo_slide.pdf
|   ├── SDC2026_疯狂星期四_slide_deck.pdf
├── tests/                   # Application tests
├── .gitignore               # Git ignore rules
├── .replit                  # Replit run and deployment configuration
├── .replitignore            # Files excluded from Replit
├── LICENSE                  # Apache License 2.0
├── README.md                # Project documentation
├── main.py                  # Flask application entry point
├── matching.py              # Career matching and learning-plan logic
├── models.py                # Career data and questionnaire schema
├── pyproject.toml           # Python project metadata and dependencies
├── replit.md                # Replit project instructions
└── uv.lock                  # Locked Python dependency versions
```

### Architecture

```

User
  │
  ▼
Replit (Web Application)
  │
  ▼
Flask Backend (main.py)
  │
  ▼
Career Matching Logic (matching.py)
  │
  ▼
Predefined Career Data (models.py)
  │
  ▼
Ranked Career Recommendations
  │
  ▼
Results displayed to User
```

---

## How to Run

### Option 1 — Run on Replit (Recommended)

1. Open the [CareerNovacoke GitHub Repository](https://github.com/breathfreea-ctrl/CareerNovacoke), then import the repository into Replit using **Create Repl → Import from GitHub**.

2. Allow Replit to set up the project environment and install the dependencies specified in `pyproject.toml`.

3. Click **Run**. The `.replit` configuration starts the application using `python main.py`.

4. Once the application starts successfully, open the Replit web preview to access CareerNova.

**Note:** CareerNovacoke uses predefined career data and rule-based matching. No RunPod API keys or endpoint configuration are required.

### Option 2 — Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-project.git
cd your-project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env            # then fill in your values

# 5. Run the app
python src/main.py
```

### /Run Tests

```bash
python -m unittest discover tests
```

---

## How We Use Replit *(Required)

- **Development:** Used Replit’s online development environment to write, modify, and debug CareerNova’s code.
- **Testing:** Tested the questionnaire and fixed issues to ensure the website worked correctly.
- **Hosting:** Used Replit Deployments to publish CareerNova as a publicly accessible website.
- **Version Control:** Connected the project to GitHub to manage source code and track changes.

📄 Proof of use: [`submission/SDC2026_TeamName_Replit_POU.pdf`](submission/SDC2026_TeamName_Replit_POU.pdf)

---

## Challenges & Learnings

- Challenges & Solutions
Our main challenge was that the career questionnaire kept returning to the first question instead of progressing to the next step. We used debugging logs to trace the issue and discovered that although the answers and next question were correctly processed, the Flask session was not preserved because the browser was not sending the session cookie. We adjusted the session cookie configuration and tested the application again using the Replit preview and a separate browser tab.

- Key Learnings
We learned the importance of systematic debugging, understanding Flask sessions and browser cookies, configuring secure cookies correctly, and testing the application across different environments. We also learned to verify the actual cause of a problem through logs rather than relying on assumptions.
What did your team learn?

## Future Improvements

- Improvement 1:Expand and regularly update career data, salary ranges, country-specific requirements, and learning resources to improve accuracy.
- Improvement 2:Enhance recommendation accuracy, improve mobile responsiveness, and conduct more user testing to ensure a smoother experience.


## Team

| Name                  | Role                          | GitHub                                                    |
| --------------------- | ----------------------------- | --------------------------------------------------------- |
| LIN JIA XI            | Team Lead /Hosting/Dev        | [@breathfreea-ctrl](https://github.com/breathfreea-ctrl)  |
| LIU XIAN YAO          | Backend                       | [@Iris0112-web](https://github.com/Iris0112-web)          |
| WANG JING YANG        | Fronted                       | [@wangjingyan-ithub](https://github.com/wangjingyan-ithub)|
| JANICE WONG JYUN LYNN | Data assistant & Documentation| [@janicewongjl-del](https://github.com/janicewongjl-del)  |

---

## Submission Checklist

- [x] Team name, domain (Domain 1 / Domain 2) and SDG track filled in
- [x] Slide deck link added
- [x] Demo video link added
- [x] Replit used, with proof of use in `submission/`
- [ ] (GPU not used) RunPod used, with proof of use in `submission/`
- [x] Preliminary submission completed (`SDC2026_TeamName_Preliminary.pdf`)
- [x] Technology declaration completed (`SDC2026_TeamName_TechDeclaration.pdf`)
- [x] Submission files renamed with your team name (replace `TeamName`)
- [x] "How to Run" steps verified
- [ ] （API not used）No API keys or secrets committed to the repository

## License

This project is licensed under the [Apache License 2.0](LICENSE).
