"""Transparent overlap matching against the repository's career catalog."""

from models import ROLES


def match_user(user_skills, experience_years, user_interests):
    """Rank by 70% skill coverage and 30% interest coverage.

    Experience is accepted for the survey interface but does not affect ranking:
    the imported catalog supplies no experience requirements.
    """
    skills = set(user_skills)
    interests = set(user_interests)
    matches = []
    for role in ROLES:
        required = role["required_skills"]
        role_interests = role["interests"]
        matched_skills = [skill for skill in required if skill in skills]
        matched_interests = [item for item in role_interests if item in interests]
        score = (
            70 * len(matched_skills) / len(required) if required else 0
        ) + (
            30 * len(matched_interests) / len(role_interests)
            if role_interests else 0
        )
        matches.append({
            **role,
            "match_score": round(score, 1),
            "matched_skills": matched_skills,
            "matched_interests": matched_interests,
            "missing_skills": [skill for skill in required if skill not in skills],
        })
    return sorted(matches, key=lambda role: -role["match_score"])
