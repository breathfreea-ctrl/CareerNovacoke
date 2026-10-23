"""Basic career-exploration questions, independent of unfinished career data."""

QUESTIONS = [
    {
        "id": "skills",
        "title": "你已经掌握或正在学习哪些技能？",
        "hint": "可多选，至少选一项。正在入门也没关系，选择最接近你现状的选项。",
        "required": True,
        "input_type": "checkbox",
        "options": [
            {"value": "communication", "label": "沟通与团队协作"},
            {"value": "writing", "label": "写作与内容表达"},
            {"value": "data", "label": "数据整理与分析"},
            {"value": "programming", "label": "编程与技术应用"},
            {"value": "design", "label": "设计与创意表达"},
            {"value": "management", "label": "项目组织与管理"},
            {"value": "research", "label": "研究与信息检索"},
            {"value": "teaching", "label": "讲解与教学"},
            {"value": "service", "label": "客户服务与问题解决"},
            {"value": "beginner", "label": "正在入门，愿意学习新技能"},
        ],
    },
    {
        "id": "experience",
        "title": "你目前有多少实践或工作经验？",
        "hint": "请选择一项。可以包括实习、兼职、志愿活动，以及持续参与的项目经验。",
        "required": True,
        "input_type": "radio",
        "options": [
            {"value": "starting", "label": "还没有经验 / 不满 1 年"},
            {"value": "1_2", "label": "1–2 年"},
            {"value": "3_5", "label": "3–5 年"},
            {"value": "6_plus", "label": "6 年及以上"},
        ],
    },
    {
        "id": "interests",
        "title": "哪些方向让你更有探索的兴趣？",
        "hint": "可多选，至少选一项。选择你真正愿意了解的方向，不必局限于已有技能。",
        "required": True,
        "input_type": "checkbox",
        "options": [
            {"value": "technology", "label": "科技与数字产品"},
            {"value": "creative", "label": "艺术、设计与内容创作"},
            {"value": "business", "label": "商业与组织管理"},
            {"value": "education", "label": "教育与个人成长"},
            {"value": "health", "label": "健康与照护"},
            {"value": "environment", "label": "环境与可持续发展"},
            {"value": "justice", "label": "法律与社会公平"},
            {"value": "community", "label": "社区服务与社会影响"},
        ],
    },
]


def validate_selection(question, values, *, required=True):
    """Return ordered, deduplicated allowed values and a user-facing error."""
    allowed = {option["value"] for option in question["options"]}
    if any(value not in allowed for value in values):
        return [], "有选项已失效，请重新选择。"
    selected = list(dict.fromkeys(values))
    if question["input_type"] == "radio" and len(selected) > 1:
        return [], "这道题只能选择一项。"
    if required and question["required"] and not selected:
        return [], "请至少选择一项，再继续下一步。"
    return selected, None
