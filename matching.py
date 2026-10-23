import re

from models import ROLES


def getSalaryRange(salary_str):
    """把原问卷的薪资选项转换为美元数值范围。"""
    ranges = {
        "Under $30,000": (0, 30000),
        "$30,000 – $60,000": (30000, 60000),
        "$60,000 – $100,000": (60000, 100000),
        "$100,000 – $150,000": (100000, 150000),
        "$150,000 – $250,000": (150000, 250000),
        "Above $250,000": (250000, 999999999),
    }
    return ranges.get(salary_str)


def _salary_numbers(value):
    """从职业资料的 USD 薪资文字中提取数值，并统一换算成美元。"""
    if not isinstance(value, str):
        return []

    numbers = []
    for number, suffix in re.findall(r"(\d[\d,]*(?:\.\d+)?)\s*(k)?", value.lower()):
        amount = float(number.replace(",", ""))
        if suffix == "k":
            amount *= 1000
        numbers.append(amount)

    return numbers


def _role_usd_range(role):
    """兼容 models.py 的数值区间和旧格式的 USD 薪资资料。"""
    salary_range = role.get("salary_range")
    if isinstance(salary_range, (list, tuple)) and len(salary_range) >= 2:
        try:
            low, high = float(salary_range[0]), float(salary_range[1])
            return min(low, high), max(low, high)
        except (TypeError, ValueError):
            pass

    salary_ranges = role.get("salary_ranges", {})
    if not isinstance(salary_ranges, dict):
        return None
    usd_levels = salary_ranges.get("USD", {})
    values = usd_levels.values() if isinstance(usd_levels, dict) else [usd_levels]

    amounts = []
    for value in values:
        amounts.extend(_salary_numbers(value))

    if not amounts:
        return None

    return min(amounts), max(amounts)


def _selected_skills(answers):
    """兼容问卷中以 skills_detail 或 skills 保存技能的格式。"""
    details = answers.get("skills_detail", {})
    selected = set(details.keys()) if isinstance(details, dict) else set()

    skills = answers.get("skills", [])
    if isinstance(skills, (list, tuple, set)):
        selected.update(skills)

    return selected, details if isinstance(details, dict) else {}


def _selection_set(value):
    """将单选或多选答案统一转换为集合。"""
    if isinstance(value, str):
        return {value} if value else set()
    if isinstance(value, (list, tuple, set)):
        return {item for item in value if isinstance(item, str) and item}
    return set()


def getTier(points):
    """返回与原结果页面相同的匹配等级。"""
    if points >= 115:
        return {
            "title": "You are born for this!",
            "desc": "Your skills, interests, and expectations are perfectly aligned.",
            "color": "#16a34a",
            "bg": "#f0fdf4",
            "border": "#bbf7d0",
            "emoji": "🌟",
        }
    if points >= 75:
        return {
            "title": "You are highly suitable for this job",
            "desc": "You have a strong foundation. A little polish and you are good to go.",
            "color": "#2563eb",
            "bg": "#eff6ff",
            "border": "#bfdbfe",
            "emoji": "💙",
        }
    if points >= 35:
        return {
            "title": "Suitable, but needs improvement",
            "desc": "You have some basics, but there are clear skill gaps to fill.",
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


def match_user(answers):
    """根据问卷答案为 models.py 中的职业资料评分并排序。"""
    selected_skills, skill_details = _selected_skills(answers)
    selected_interests = _selection_set(answers.get("interest"))
    user_salary_range = getSalaryRange(answers.get("salary"))
    user_country = answers.get("country")

    results = []

    for role in ROLES:
        total_points = 0
        breakdown = []

        required_skills = role.get("required_skills", [])
        for skill in required_skills:
            if skill not in selected_skills:
                continue

            total_points += 10
            breakdown.append({
                "label": f"{skill} (Skill)",
                "points": 10,
                "type": "skill",
            })

            detail = skill_details.get(skill, {})
            if isinstance(detail, dict) and detail.get("cert") == "Yes":
                total_points += 20
                breakdown.append({
                    "label": f"{skill} (Certification)",
                    "points": 20,
                    "type": "cert",
                })

        role_interests = set(role.get("interests", []))
        matched_interests = role_interests.intersection(selected_interests)
        if matched_interests:
            interest = sorted(matched_interests)[0]
            total_points += 20
            breakdown.append({
                "label": f"Interest Match ({interest})",
                "points": 20,
                "type": "interest",
            })

        role_salary_range = _role_usd_range(role)
        if user_salary_range and role_salary_range:
            user_salary_min, user_salary_max = user_salary_range
            role_salary_min, role_salary_max = role_salary_range
            if user_salary_max < role_salary_min or user_salary_min > role_salary_max:
                total_points -= 20
                breakdown.append({
                    "label": "Salary Expectation Mismatch",
                    "points": -20,
                    "type": "salary_minus",
                })
            else:
                total_points += 20
                breakdown.append({
                    "label": "Salary Expectation Match",
                    "points": 20,
                    "type": "salary_plus",
                })

        country_names = {
            item if isinstance(item, str) else item.get("country")
            for item in role.get("top_countries", [])
            if isinstance(item, (str, dict))
        }
        if user_country and user_country in country_names:
            total_points += 25
            breakdown.append({
                "label": f"Top Country Match ({user_country})",
                "points": 25,
                "type": "country",
            })

        result = dict(role)
        result["title"] = role.get("title") or role.get("name", "")
        result["totalPoints"] = total_points
        result["breakdown"] = breakdown
        result["tier"] = getTier(total_points)
        results.append(result)

    return sorted(results, key=lambda item: item["totalPoints"], reverse=True)


def generateLearningPlan(role, answers):
    """根据职业的 learning_steps 和问卷答案整理学习计划。"""
    steps = role.get("learning_steps", [])
    if not steps:
        resources = role.get("learning_resources", {})
        if isinstance(resources, dict):
            courses = resources.get("courses", [])
            practical = resources.get("practical", [])
            steps = [
                *(f"Study: {course}" for course in courses),
                *(f"Practice: {activity}" for activity in practical),
            ]
    country = answers.get("country", "")
    time = answers.get("time", "")

    return {
        "time": time,
        "country": country,
        "steps": [
            {
                "phase": f"Step {index}",
                "description": step,
            }
            for index, step in enumerate(steps, start=1)
        ],
    }