# ///Project Name

> A one-sentence description of what your project does and who it is for.

---

## Team Information

| Field                  | Details                                        |
| ---------------------- | ---------------------------------------------- |
| **Team Name**          | 疯狂星期四                                      |
| **Team Domain**        | Domain 1                                       |
| **SDG Track (1–17)**   | SDG 4 — Quality Education,                     |
|                        | SDG 8 - Decnet Work And Economic Growth,       |
|                        | SDG 9 - Industry, Innovatio And Infrastructure,|
|                        | SDG 10 - Reduced Inequalities                  |
| **Team Leader**        | LIN JIA XI                                     |
| **University**         | Xiamen University Malaysia                     |
| **Number of Members**  | 4                                              |

## /Links

| Resource          | Link                                           |
| ----------------- | ---------------------------------------------- |
| GitHub Repository | https://github.com/your-username/your-project  |
| Replit Project    | https://replit.com/@your-username/your-project |
| Live Demo         | https://your-project.replit.app                |
| Slide Deck        | https://example.com/slides                     |
| Demo Video        | https://example.com/demo-video                 |

---

## Overview

### /Problem

Describe the real-world problem you are solving in 2–4 sentences. Who is affected, and why does it matter?

答案Rapid technological advancement and AI-driven changes are widening the gap between workers’ skills and industry requirements. Fresh graduates struggle to find suitable career paths, career changers face uncertainty, and workers in declining occupations risk unemployment. As AI increasingly automates specific human skills and tasks, people need better guidance to adapt and remain competitive in the evolving job market.

### /Solution

Explain how your project uses AI to solve the problem and what makes it valuable.

答案Our AI-powered career platform analyzes users’ profiles to recommend suitable careers, explain skill gaps, and generate personalized learning and training plans to improve employability. By continuously updating career information and industry trends, the platform helps users anticipate changes, develop relevant skills, and make informed career decisions. Its value lies in turning career uncertainty into actionable learning pathways, helping people adapt to changing industry demands and prepare for future opportunities.

### /Key Features

- **Feature 1** — Short description.
- **Feature 2** — Short description.
- **Feature 3** — Short description.

### Tech Stack

| Layer                            | Technology                   |
| ---------------------------------| ---------------------------- |
| Frontend                         | HTML,CSS,Javascript,React    |
| Backend                          | Python, Flask / FastAPI      |
| Data assistant & Documentation   | VScode, Replit               |
| Hosting / Dev                    | Replit                       |

---

## Project Structure

```
.
├── docs/                    # Screenshots, diagrams
├── src/
│   ├── main.py              # Application entry point
│   └── utils.py             # Helper functions
├── submission/              # Required submission documents
│   ├── SDC2026_TeamName_Preliminary.pdf      # Preliminary submission
│   ├── SDC2026_TeamName_TechDeclaration.pdf  # Technology declaration
│   ├── SDC2026_TeamName_Replit_POU.pdf       # Replit proof of use
│   └── SDC2026_TeamName_Runpod_POU.pdf       # RunPod proof of use
├── .env.example             # Example environment variables
├── .gitignore
├── .replit                  # Replit run configuration
├── LICENSE
├── requirements.txt         # Python dependencies
└── README.md
```

### Architecture

```
User ──► Replit (App / API) ──► RunPod Endpoint (GPU model)
                │
                └──► Response returned to user
```

---

## /How to Run

### Option 1 — Run on Replit (Recommended)

1. Open the [Replit Project](https://replit.com/@your-username/your-project), or import this repository via **Create Repl → Import from GitHub**.
2. Open the **Secrets** tab (🔒) and add the variables listed in `.env.example`:
   - `RUNPOD_API_KEY`
   - `RUNPOD_ENDPOINT_ID`
3. Click **Run**. Replit uses the `.replit` file to start `python src/main.py`.

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

## /How We Use Replit *(Required)*

Describe how your team used Replit. For example:

- **Development:** Collaborative coding in a shared Repl using Multiplayer.
- **Hosting:** The app is deployed with Replit Deployments at the Live Demo link above.
- **Secrets:** API keys are stored in Replit Secrets, never in the code.

📄 Proof of use: [`submission/SDC2026_TeamName_Replit_POU.pdf`](submission/SDC2026_TeamName_Replit_POU.pdf)

---

## /Challenges & Learnings

- What challenges did you face, and how did you overcome them?
- What did your team learn?

## /Future Improvements

- [ ] Improvement 1
- [ ] Improvement 2

## Team

| Name                  | Role                          | GitHub                                                  |
| --------------------- | ----------------------------- | ------------------------------------------------------- |
| LIN JIA XI            | Team Lead /Hosting/Dev        | [@breathfreea-ctrl](https://github.com/breathfreea-ctrl)|
| LIU XIAN YAO          | Backend                       | [@Iris0112-web](https://github.com/Iris0112-web)        |
| WANG JING YANG        | Fronted                       | [@wangjingyan-ithub](https://github.com/wangjingyan-ithub))                |
| JANICE WONG JYUN LYNN | Data assistant & Documentation| [@janicewongjl-del](https://github.com/janicewongjl-del)|

---

## /Submission Checklist

- [ ] Team name, domain (Domain 1 / Domain 2) and SDG track filled in
- [ ] Slide deck link added
- [ ] Demo video link added
- [ ] Replit used, with proof of use in `submission/`
- [ ] RunPod used, with proof of use in `submission/`
- [ ] Preliminary submission completed (`SDC2026_TeamName_Preliminary.pdf`)
- [ ] Technology declaration completed (`SDC2026_TeamName_TechDeclaration.pdf`)
- [ ] Submission files renamed with your team name (replace `TeamName`)
- [ ] "How to Run" steps verified
- [ ] No API keys or secrets committed to the repository

## License

This project is licensed under the [Apache License 2.0](LICENSE).