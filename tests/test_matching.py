import unittest

from matching import LABELS, MATCH_THRESHOLD, PROFILES, match_careers, score_role
from models import CAREERS
from main import app
from test_survey import SurveyHelpers


class MatchingRuleTests(unittest.TestCase):
    def test_catalog_and_profiles_are_complete_and_valid(self):
        self.assertEqual(len(CAREERS), 7)
        self.assertEqual({role["id"] for role in CAREERS}, set(PROFILES))
        for profile in PROFILES.values():
            self.assertTrue(set(profile["skills"]) <= set(LABELS["skills"]))
            self.assertTrue(set(profile["interests"]) <= set(LABELS["interests"]))
            self.assertNotIn("beginner", profile["skills"])

    def test_score_formula_and_explanation_add_up(self):
        role = score_role(CAREERS[0], {
            "skills": ["programming", "data"], "interests": ["technology"],
            "experience": ["1_2"],
        })
        self.assertEqual(role["totalPoints"], 80)
        self.assertEqual(sum(item["points"] for item in role["breakdown"]), 80)
        self.assertEqual(role["matched_skills"], ["编程与技术应用", "数据整理与分析"])
        self.assertEqual(role["skill_gaps"], ["研究与信息检索"])
        self.assertIsNone(role["mentor"])
        self.assertIsNone(role["learning_plan"]["time"])
        self.assertIsNone(role["learning_plan"]["country"])

    def test_experience_only_changes_learning_plan(self):
        base = {"skills": ["research"], "interests": ["health"]}
        beginner = score_role(CAREERS[5], {**base, "experience": ["starting"]})
        advanced = score_role(CAREERS[5], {**base, "experience": ["6_plus"]})
        self.assertEqual(beginner["totalPoints"], advanced["totalPoints"])
        self.assertNotEqual(beginner["learning_plan"]["phases"][0],
                            advanced["learning_plan"]["phases"][0])

    def test_empty_matches_are_not_fabricated(self):
        self.assertEqual(match_careers({}), [])
        self.assertEqual(match_careers({
            "skills": ["beginner"], "interests": ["creative"],
        }), [])

    def test_interest_only_can_be_a_starting_point(self):
        matches = match_careers({"skills": ["beginner"], "interests": ["technology"]})
        self.assertTrue(matches)
        self.assertTrue(all(not role["matched_skills"] for role in matches))
        self.assertTrue(all(role["totalPoints"] >= MATCH_THRESHOLD for role in matches))

    def test_full_selection_scores_are_bounded_and_ties_stable(self):
        matches = match_careers({
            "skills": list(LABELS["skills"]),
            "interests": list(LABELS["interests"]),
        })
        self.assertEqual(len(matches), 3)
        self.assertEqual([role["id"] for role in matches], [1, 2, 3])
        self.assertTrue(all(role["totalPoints"] == 100 for role in matches))

    def test_duplicate_or_unknown_values_do_not_inflate_scores(self):
        answers = {"skills": ["programming", "programming", "unknown"],
                   "interests": ["technology", "technology", "unknown"]}
        self.assertEqual(score_role(CAREERS[0], answers)["totalPoints"], 60)


class ReportIntegrationTests(SurveyHelpers, unittest.TestCase):
    """Reuse existing browser-session helpers for the newly connected report."""

    def test_all_role_pages_and_download_require_completion(self):
        for path in ["/roles/1", "/survey/answers.json"]:
            self.assertEqual(self.get(path).status_code, 302)
        self.assertEqual(self.get("/roles/9999").status_code, 404)

    def test_every_detail_page_renders_and_never_exposes_unverified_salaries(self):
        self.complete()
        for career in CAREERS:
            page = self.get(f"/roles/{career['id']}")
            self.assertEqual(page.status_code, 200)
            self.assertIn(PROFILES[career["id"]]["title"], page.text)
            self.assertIn("no-store", page.headers["Cache-Control"])
            self.assertIn("问卷没有收集目标", page.text)
            self.assertIn('href="/results"', page.text)
            self.assertNotIn("salary_ranges", page.text)
            self.assertNotIn("BLS projects", page.text)

    def test_download_is_an_attachment_and_only_contains_current_answers(self):
        self.complete()
        page = self.get("/survey/answers.json")
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.mimetype, "application/json")
        self.assertIn("attachment", page.headers["Content-Disposition"])
        self.assertIn("no-store", page.headers["Cache-Control"])
        self.assertEqual(set(page.json), {"skills", "experience", "interests"})
        self.assertNotIn("csrf_token", page.json)
        self.assertEqual(self.get("/survey/answers.json", app.test_client()).status_code, 302)

    def test_report_links_download_and_csrf_post_actions_are_wired(self):
        self.complete()
        page = self.get("/results")
        self.assertIn('href="/survey/answers.json"', page.text)
        self.assertIn('href="/roles/', page.text)
        self.assertNotIn("reset=1", page.text)
        self.assertIn('action="/survey/restart"', page.text)
        self.assertIn('action="/survey/edit"', page.text)
        self.assertIn('name="csrf_token"', page.text)
        self.assertIn("7 个职业方向", page.text)
        self.assertIn("60 分", page.text)
        self.assertIn("40 分", page.text)

    def test_empty_report_retains_download_edit_and_restart(self):
        self.answer("skills", ["beginner"])
        self.answer("experience", "starting")
        self.answer("interests", ["creative"])
        page = self.get("/results")
        self.assertEqual(page.status_code, 200)
        self.assertNotIn('class="role-card', page.text)
        self.assertIn("7 个职业方向", page.text)
        self.assertIn('href="/survey/answers.json"', page.text)
        self.assertIn('action="/survey/edit"', page.text)
        self.assertIn('action="/survey/restart"', page.text)
