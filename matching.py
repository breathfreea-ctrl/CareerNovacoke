"""问卷答案与职业匹配评分，以及个性化学习计划生成。"""


def get_salary_range(salary_answer):
    """将问卷中的薪资选项转换为最低值和最高值。"""
    salary_ranges = {
        "Under $30,000": (0, 30000),
        "$30,000 – $60,000": (30000, 60000),
        "$60,000 – $100,000": (60000, 100000),
        "$100,000 – $150,000": (100000, 150000),
        "$150,000 – $250,000": (150000, 250000),
        "Above $250,000": (250000, 9999999),
    }
    return salary_ranges.get(salary_answer, (0, 9999999))


def match_user(answers, roles=None):
    """
    按技能、兴趣、薪资和地区计算职业匹配分。

    返回按分数从高到低排列的职业字典列表。
    """
    if roles is None:
        # 延迟导入，避免模块互相导入时出现循环依赖。
        from models import ROLES

        roles = ROLES

    user_skills = answers.get("skills_detail", {})
    user_interests = answers.get("interest", [])
    user_salary_min, user_salary_max = get_salary_range(answers.get("salary"))
    user_country = answers.get("country")

    results = []

    for role in roles:
        total_points = 0
        breakdown = []

        # 已选择的必需技能加 10 分；有证书再加 20 分。
        for skill in role.get("required_skills", []):
            skill_detail = user_skills.get(skill)
            if skill_detail:
                total_points += 10
                breakdown.append(
                    {
                        "label": f"{skill} (Skill)",
                        "points": 10,
                        "type": "skill",
                    }
                )

                if skill_detail.get("cert") == "Yes":
                    total_points += 20
                    breakdown.append(
                        {
                            "label": f"{skill} (Certification)",
                            "points": 20,
                            "type": "cert",
                        }
                    )

        # 多个兴趣匹配时，沿用原逻辑，只按第一个匹配项加分。
        matched_interests = [
            interest
            for interest in role.get("interests", [])
            if interest in user_interests
        ]
        if matched_interests:
            total_points += 20
            breakdown.append(
                {
                    "label": f"Interest Match ({matched_interests[0]})",
                    "points": 20,
                    "type": "interest",
                }
            )

        role_salary_min, role_salary_max = role.get("salary_range", (0, 9999999))
        salary_is_disjoint = (
            user_salary_max < role_salary_min
            or user_salary_min > role_salary_max
        )

        if salary_is_disjoint:
            total_points -= 20
            breakdown.append(
                {
                    "label": "Salary Expectation Mismatch",
                    "points": -20,
                    "type": "salary_minus",
                }
            )
        else:
            total_points += 20
            breakdown.append(
                {
                    "label": "Salary Expectation Match",
                    "points": 20,
                    "type": "salary_plus",
                }
            )

        if user_country in role.get("top_countries", []):
            total_points += 25
            breakdown.append(
                {
                    "label": f"Top Country Match ({user_country})",
                    "points": 25,
                    "type": "country",
                }
            )

        results.append(
            {
                **role,
                "totalPoints": total_points,
                "breakdown": breakdown,
            }
        )

    return sorted(results, key=lambda result: result["totalPoints"], reverse=True)


def get_tier(points):
    """根据总分返回结果页展示的匹配等级。"""
    if points >= 115:
        return {
            "title": "You are born for this!",
            "desc": (
                "Your skills, interests, and expectations are perfectly aligned."
            ),
            "color": "#16a34a",
            "bg": "#f0fdf4",
            "border": "#bbf7d0",
            "emoji": "🌟",
        }

    if points >= 75:
        return {
            "title": "You are highly suitable for this job",
            "desc": (
                "You have a strong foundation. A little polish and you are good to go."
            ),
            "color": "#2563eb",
            "bg": "#eff6ff",
            "border": "#bfdbfe",
            "emoji": "💙",
        }

    if points >= 35:
        return {
            "title": "Suitable, but needs improvement",
            "desc": (
                "You have some basics, but there are clear skill gaps to fill."
            ),
            "color": "#d97706",
            "bg": "#fffbeb",
            "border": "#fde68a",
            "emoji": "💛",
        }

    return {
        "title": "Not quite suitable",
        "desc": "This role does not match your current profile well.",
        "color": "#dc2626",
        "bg": "#fef2f2",
        "border": "#fecaca",
        "emoji": "❤️",
    }


def generate_learning_plan(role, answers):
    """
    根据目标职业和问卷答案生成学习计划数据。

    返回字典，模板可以遍历其中的 phases、courses 和 practical。
    """
    target_time = answers.get("time", "")
    country = answers.get("country", "")
    user_skills = answers.get("skills_detail", {})

    skills_to_learn = []
    for skill in role.get("required_skills", []):
        skill_detail = user_skills.get(skill)

        if not skill_detail:
            skills_to_learn.append(skill)
            continue

        years = skill_detail.get("years")
        if years in {"Less than 1 year", "1–2 years"}:
            skills_to_learn.append(skill)

    certifications = role.get("certs", {})
    recommended_certifications = (
        certifications.get(country)
        or certifications.get("Default")
        or ["Industry Standard Certification"]
    )

    learning_resources = role.get("learning_resources", {})
    courses = learning_resources.get("courses", [])[:2]
    practical = learning_resources.get("practical", [])[:2]

    course_text = " and ".join(courses)
    practical_text = " and ".join(practical)
    skills_text = ", ".join(skills_to_learn) or "your existing strengths"
    certification = recommended_certifications[0]

    if target_time == "This year":
        phases = [
            {
                "title": "Months 1–3: Intensive Skill Acquisition",
                "description": (
                    f"Take specialized courses via {course_text} to cover "
                    f"the missing areas: {skills_text}."
                ),
            },
            {
                "title": "Months 4–6: Certification & Portfolio",
                "description": (
                    f"Prepare for {certification}. Build your portfolio by "
                    f"doing: {practical_text}."
                ),
            },
            {
                "title": "Immediate Action",
                "description": (
                    "Start applying for junior roles or internships after "
                    "your portfolio is ready. Don't wait for the certificate."
                ),
            },
        ]

    elif target_time == "In 1 year":
        phases = [
            {
                "title": "Months 1–6: Deep Skill Building",
                "description": (
                    f"Study through {course_text}. Focus on "
                    f"{skills_text}."
                ),
            },
            {
                "title": "Months 7–9: Certification & Practical Application",
                "description": (
                    f"Prepare for {certification} and apply your knowledge "
                    f"through: {practical_text}."
                ),
            },
            {
                "title": "Months 10–12: Internship & Job Hunting",
                "description": (
                    f"Seek an internship or volunteer role, polish your resume, "
                    f"and begin interviewing in {country}."
                ),
            },
        ]

    elif target_time == "In 2-3 years":
        phases = [
            {
                "title": "Year 1: Academic & Foundational Deep Dive",
                "description": (
                    f"Build a strong foundation using {course_text} and "
                    f"develop {skills_text}."
                ),
            },
            {
                "title": "Year 2: Certification & Long-term Practice",
                "description": (
                    f"Work towards {certification} and gain practical "
                    f"experience through: {practical_text}."
                ),
            },
            {
                "title": "Year 3: Networking & Transition",
                "description": (
                    f"Build your professional network in {country}, attend "
                    "industry events, and prepare to transition into the field."
                ),
            },
        ]

    else:
        phases = [
            {
                "title": "Years 1–2: Advanced Academic Route",
                "description": (
                    f"Pursue a suitable long-term qualification and develop "
                    f"{skills_text} using resources such as {course_text}."
                ),
            },
            {
                "title": "Years 3–4: Specialized Practice",
                "description": (
                    f"Work towards {certification} and build practical "
                    f"experience through: {practical_text}."
                ),
            },
            {
                "title": "Year 5+: Thought Leadership",
                "description": (
                    f"Publish research, lead projects, and build expertise "
                    f"in your chosen field in {country}."
                ),
            },
        ]

    return {
        "time": target_time,
        "country": country,
        "skills_to_learn": skills_to_learn,
        "certification": certification,
        "courses": courses,
        "practical": practical,
        "phases": phases,
        "tip": (
            "Don't drown yourself in certificates. Focus on practical projects "
            "and one core credential. Employers value real experience."
        ),
    }