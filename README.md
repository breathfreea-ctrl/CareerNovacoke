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

| Resource          | Link                                           |
| ----------------- | ---------------------------------------------- |
| GitHub Repository | https://github.com/breathfreea-ctrl/CareerNovacoke |
| Live Demo         | https://your-project.replit.app                |
| Slide Deck        | https://example.com/slides                     |
| Demo Video        | https://example.com/demo-video                 |

---

## Overview

### Problem

As AI and technology change the job market, many workers face a growing gap between their skills and job requirements. Fresh graduates and career changers struggle to find the right career direction, while some workers risk losing their jobs. This affects workers, students, HR teams, and education centers, making career guidance and skill training more important than ever.

### Solution

Our AI-powered website matches users with suitable careers, identifies their skill gaps, and creates personal learning plans. It also updates career trends to help users build the right skills, find direction, and prepare for future jobs.

### /Key Features我们的网站有什么特点。。（客制化的学习计划和技能培训？问卷分析匹配度？提供优质资源？AI互动？更新职业趋势？）

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

## Project Structure/待完善

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
├── .env.example             # Example environment variables
├── .gitignore
├── .replit                  # Replit run configuration
├── LICENSE
├── requirements.txt         # Python dependencies
└── README.md
```

### Architecture

```
User ──► Replit (App/Web) ──► RunPod Endpoint (GPU model)
                │
                └──► Response returned to user
```

---

## How to Run

### Option 1 — Run on Replit (Recommended)

1. Open the [Replit Project](https://replit.com/@your-username/your-project), or import this repository via **Create Repl → Import from GitHub**.
2. Open the **Secrets** tab (🔒) and add the variables listed in `.env.example`:
   - `RUNPOD_API_KEY`我们没用runpod，要换掉这里
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

## How We Use Replit *(Required)*我们怎么用replit（用replit干了什么

Describe how your team used Replit. For example:

- **Development:** Collaborative coding in a shared Repl using Multiplayer.
- **Hosting:** The app is deployed with Replit Deployments at the Live Demo link above.
- **Secrets:** API keys are stored in Replit Secrets, never in the code.

📄 Proof of use: [`submission/SDC2026_TeamName_Replit_POU.pdf`](submission/SDC2026_TeamName_Replit_POU.pdf)

---

## Challenges & Learnings（我们在开发过程遇到什么难题，怎么解决难题，从中学到什么

- What challenges did you face, and how did you overcome them?
- What did your team learn?

## /Future Improvements（网站哪些方面要提升，怎么提升

- [ ] Improvement 1
- [ ] Improvement 2

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
- [ ] Slide deck link added
- [ ] Demo video link added
- [ ] Replit used, with proof of use in `submission/`
- [ ] (GPU not used) RunPod used, with proof of use in `submission/`
- [ ] Preliminary submission completed (`SDC2026_TeamName_Preliminary.pdf`)
- [ ] Technology declaration completed (`SDC2026_TeamName_TechDeclaration.pdf`)
- [ ] Submission files renamed with your team name (replace `TeamName`)
- [ ] "How to Run" steps verified
- [ ] （API not used）No API keys or secrets committed to the repository

## License

This project is licensed under the [Apache License 2.0](LICENSE).
