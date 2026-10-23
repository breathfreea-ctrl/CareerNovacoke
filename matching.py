"""Transparent exploratory rules, not a validated aptitude or employment model."""

from models import CAREERS
from survey_questions import QUESTIONS

MATCH_THRESHOLD = 20
LABELS = {
    question["id"]: {option["value"]: option["label"] for option in question["options"]}
    for question in QUESTIONS
}

# Broad categories describe relevance, not proof of professional competence.
PROFILES = {
    1: {
        "title": "人工智能工程师",
        "skills": ("programming", "data", "research"),
        "interests": ("technology",),
        "overview": "把编程、机器学习和数据工程结合起来，将模型转化为可使用的软件系统。",
        "practice": "用公开且允许使用的数据做一个小型模型项目，记录数据处理、评估和部署过程。",
    },
    2: {
        "title": "会计与财务专业人员",
        "skills": ("data", "research", "management"),
        "interests": ("business",),
        "overview": "整理财务信息，参与报表、审计、税务和合规工作，帮助组织作出有依据的决策。",
        "practice": "用虚构账目练习记录交易、编制简单报表和检查差错，了解目标地区的会计准则。",
    },
    3: {
        "title": "可持续发展教育课程开发者",
        "skills": ("teaching", "writing", "design", "research", "management"),
        "interests": ("education", "environment"),
        "overview": "围绕可持续发展主题设计课程、教材和学习活动，关注学习效果与包容性。",
        "practice": "选择一个可持续发展主题，设计一节微课，写出目标、活动和反馈方式并请人试学。",
    },
    4: {
        "title": "心理学专业人员",
        "skills": ("communication", "research", "service"),
        "interests": ("health", "education"),
        "overview": "运用心理学研究和专业方法理解行为、支持心理健康；临床工作通常有严格的资质要求。",
        "practice": "学习心理学研究方法和伦理，阅读一篇入门研究并写摘要，不自行开展诊断或治疗。",
    },
    5: {
        "title": "数字接入项目专员",
        "skills": ("management", "communication", "programming", "service"),
        "interests": ("technology", "community"),
        "overview": "协调信息通信技术普及项目，改善社区数字接入，连接技术、项目管理和社会服务。",
        "practice": "为一个社区数字服务设计需求调研和简要项目方案，列出参与方、资源及评估指标。",
    },
    6: {
        "title": "医生",
        "skills": ("research", "communication", "service"),
        "interests": ("health",),
        "overview": "在规定的专业训练和执业许可范围内参与疾病诊断、治疗及健康照护。",
        "practice": "了解目标地区认可的医学教育和执业路径，学习基础医学知识与医疗伦理，不进行医疗操作。",
    },
    7: {
        "title": "律师",
        "skills": ("research", "writing", "communication"),
        "interests": ("justice", "business"),
        "overview": "在获准执业的地区提供法律分析、文书、协商或诉讼服务，具体资格要求因地区而异。",
        "practice": "阅读公开案例，练习整理事实、争议与论证，并核查目标地区的法律教育和执业要求。",
    },
}


def score_role(career, answers):
    """Build a report from source facts and explicit survey mappings."""
    profile = PROFILES[career["id"]]
    selected_skills = set(answers.get("skills", []))
    selected_interests = set(answers.get("interests", []))
    skill_values = [value for value in profile["skills"] if value in selected_skills]
    interest_values = [value for value in profile["interests"] if value in selected_interests]
    skill_points = round(60 * len(skill_values) / len(profile["skills"]))
    interest_points = round(40 * len(interest_values) / len(profile["interests"]))
    score = skill_points + interest_points
    gaps = [
        LABELS["skills"][value] for value in profile["skills"]
        if value not in selected_skills
    ]
    experience_value = next(iter(answers.get("experience", [])), "starting")
    experience = LABELS["experience"].get(experience_value, "尚未提供")
    learning_focus = (
        "先盘点可迁移的项目经验，并用一个职业相关的小项目检验它们。年限不等于该职业的专业经验。"
        if experience_value in {"3_5", "6_plus"} else
        "先从基础概念和一个低风险练习入手，再决定是否深入学习。"
    )
    if score >= 70:
        tier = {
            "key": "strong", "title": "较多探索线索",
            "desc": "你的自报技能与兴趣和这条方向有较多交集，仍需了解专业门槛与实际工作。",
        }
    elif score >= 40:
        tier = {
            "key": "explore", "title": "值得进一步了解",
            "desc": "这条方向与你的一部分回答相符，可以用小项目和真实职业信息继续核实。",
        }
    else:
        tier = {
            "key": "start", "title": "初步探索线索",
            "desc": "目前只有少量交集；先了解工作内容，不必据此急于作出选择。",
        }
    return {
        "id": career["id"], "title": profile["title"], "totalPoints": score,
        "tier": tier,
        "breakdown": [
            {"label": f"相关技能：{len(skill_values)} / {len(profile['skills'])} 项（满分 60）",
             "points": skill_points},
            {"label": f"相关兴趣：{len(interest_values)} / {len(profile['interests'])} 项（满分 40）",
             "points": interest_points},
        ],
        "overview": profile["overview"],
        "outlook": "当前职业库不提供经核验的实时招聘、增长率或薪资数据，请结合当地官方信息了解行业。",
        "ai_match": {"level": "未作适应性评级；建议学习相关工具，并重视隐私、伦理和人工核验。"},
        "required_skills": list(career["required_skills"]),
        "sdgs": list(career["sdgs"]),
        "mentor": None,
        "matched_skills": [LABELS["skills"][value] for value in skill_values],
        "matched_interests": [LABELS["interests"][value] for value in interest_values],
        "skill_gaps": gaps,
        "learning_plan": {
            "experience": experience, "time": None, "country": None,
            "phases": [
                {"title": "梳理起点", "description": learning_focus},
                {"title": "补充相关能力", "description": (
                    "优先了解你尚未勾选的相关类别：" + "、".join(gaps) +
                    "。未勾选只代表未自报，并不证明你缺乏这些能力。"
                    if gaps else
                    "你已勾选所有相关基础类别；下一步应核实职业专门知识与实际熟练度。"
                )},
                {"title": "做一次小规模验证", "description": profile["practice"]},
            ],
            "tip": "问卷未询问目标国家或就业时间，不能据此预测入职周期。医生、律师、心理学及部分会计岗位需核查当地学历、训练与执业要求。",
        },
    }


def match_careers(answers):
    """Return at most three eligible careers; tied scores use stable source IDs."""
    ranked = [score_role(career, answers) for career in CAREERS]
    ranked.sort(key=lambda role: (-role["totalPoints"], role["id"]))
    return [role for role in ranked if role["totalPoints"] >= MATCH_THRESHOLD][:3]
