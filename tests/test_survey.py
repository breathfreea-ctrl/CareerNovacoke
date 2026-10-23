import re
import unittest
from pathlib import Path
from unittest.mock import patch

from main import app
from survey_questions import QUESTIONS


class SurveyFlowTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def get(self, path, client=None):
        return (client or self.client).get(path, base_url="https://example.test")

    def post(self, path, data, client=None):
        return (client or self.client).post(
            path, data=data, base_url="https://example.test"
        )

    def token(self, client=None, path="/survey"):
        html = self.get(path, client).get_data(as_text=True)
        match = re.search(r'name="csrf_token"\s+value="([^"]+)"', html)
        self.assertIsNotNone(match, "Page must include a CSRF token")
        return match.group(1)

    def answer(self, question_id, values, action="next", client=None):
        token = self.token(client)
        return self.post(
            "/survey",
            {
                "csrf_token": token,
                "question_id": question_id,
                "action": action,
                question_id: values,
            },
            client,
        )

    def complete(self):
        for question in QUESTIONS:
            response = self.answer(question["id"], question["options"][0]["value"])
            self.assertEqual(response.status_code, 303)
        self.assertTrue(response.location.endswith("/results"))

    def test_home_and_start_navigation(self):
        home = self.get("/")
        self.assertEqual(home.status_code, 200)
        self.assertIn('href="/survey/welcome"', home.text)
        welcome = self.get("/survey/welcome")
        self.assertEqual(welcome.status_code, 200)
        self.assertIn('action="/survey"', welcome.text)
        self.assertIn('method="get"', welcome.text)
        page = self.get("/survey")
        self.assertIn("Question 1 of 3", page.text)
        self.assertIn(QUESTIONS[0]["title"], page.text)
        self.assertIn("no-store", page.headers["Cache-Control"])

    def test_cookie_supports_secure_embedded_preview(self):
        headers = self.get("/survey").headers.getlist("Set-Cookie")
        cookie = next(header for header in headers if header.startswith("session="))
        for flag in ("Secure", "HttpOnly", "SameSite=None", "Partitioned"):
            self.assertIn(flag, cookie)

    def test_brush_font_is_only_used_on_the_homepage(self):
        self.assertIn("Ma Shan Zheng", self.get("/").text)
        for route in ("/survey/welcome", "/survey"):
            page = self.get(route)
            self.assertIn("Noto+Sans+SC", page.text)
            self.assertNotIn("Ma+Shan+Zheng", page.text)
        css = Path(app.static_folder, "survey.css").read_text()
        question_css = Path(app.static_folder, "survey-questions.css").read_text()
        for stylesheet in (css, question_css):
            self.assertNotIn("Ma Shan Zheng", stylesheet)
            self.assertNotIn("KaiTi", stylesheet)
            self.assertIn("font-family: var(--survey-font)", stylesheet)

    def test_empty_required_checkbox_question_stays_on_step(self):
        page = self.get("/survey")
        # Requiring every checkbox would force users to select every option.
        self.assertNotRegex(page.text, r'<input[^>]*type="checkbox"[^>]*\brequired\b')
        response = self.answer("skills", [])
        self.assertEqual(response.status_code, 422)
        self.assertIn("请至少选择一项", response.text)
        self.assertIn("Question 1 of 3", response.text)

    def test_one_checkbox_is_sufficient_and_refresh_preserves_step(self):
        response = self.answer("skills", "programming")
        self.assertEqual(response.status_code, 303)
        page = self.get("/survey")
        self.assertIn("Question 2 of 3", page.text)
        self.assertIn("Question 2 of 3", self.get("/survey").text)

    def test_back_without_answer_and_checked_state(self):
        self.answer("skills", ["programming", "writing"])
        response = self.answer("experience", [], action="back")
        self.assertEqual(response.status_code, 303)
        page = self.get("/survey")
        self.assertIn("Question 1 of 3", page.text)
        for selected in ("programming", "writing"):
            self.assertRegex(
                page.text,
                rf'<input[^>]*value="{selected}"[^>]*\bchecked\b',
            )

    def test_multiple_answers_and_human_readable_summary(self):
        self.answer("skills", ["programming", "writing", "writing"])
        self.answer("experience", "1_2")
        response = self.answer("interests", ["technology", "creative"])
        self.assertTrue(response.location.endswith("/results"))
        summary = self.get("/results")
        self.assertEqual(summary.status_code, 200)
        for text in ("编程与技术应用", "写作与内容表达", "1–2 年", "科技与数字产品"):
            self.assertIn(text, summary.text)
        self.assertIn("no-store", summary.headers["Cache-Control"])
        self.assertIn("不是职业匹配结果，也没有评分", summary.text)

    def test_each_rendered_input_matches_the_post_contract(self):
        for question in QUESTIONS:
            page = self.get("/survey")
            inputs = re.findall(r'<input\b[^>]*>', page.text)
            options = [
                element for element in inputs
                if re.search(r'type="(?:radio|checkbox)"', element)
            ]
            self.assertEqual(len(options), len(question["options"]))
            for element in options:
                self.assertIn(f'name="{question["id"]}"', element)
            actions = re.findall(
                r'<button[^>]*name="action"[^>]*value="([^"]+)"', page.text
            )
            self.assertIn("next", actions)
            self.assertTrue(set(actions).issubset({"next", "back"}))
            self.answer(question["id"], question["options"][0]["value"])

    def test_empty_question_configuration_has_explicit_empty_state(self):
        with patch("main.QUESTIONS", []):
            page = self.get("/survey")
        self.assertEqual(page.status_code, 200)
        self.assertIn("No questions are available.", page.text)

    def test_invalid_options_and_multiple_radio_answers_rejected(self):
        response = self.answer("skills", "<script>bad</script>")
        self.assertEqual(response.status_code, 422)
        self.assertNotIn("<script>bad</script>", response.text)
        self.answer("skills", "research")
        self.assertEqual(self.answer("experience", ["1_2", "3_5"]).status_code, 422)
        self.assertIn("Question 2 of 3", self.get("/survey").text)

    def test_incomplete_results_redirect_to_survey(self):
        self.assertEqual(self.get("/results").status_code, 302)
        self.answer("skills", "design")
        self.assertTrue(self.get("/results").location.endswith("/survey"))

    def test_missing_invalid_and_unicode_csrf_rejected(self):
        self.get("/survey")
        for token in ("", "invalid", "无效"):
            response = self.post(
                "/survey", {"csrf_token": token, "question_id": "skills", "action": "next"}
            )
            self.assertEqual(response.status_code, 400)
        self.assertEqual(self.post("/survey/restart", {}).status_code, 400)
        self.assertEqual(self.post("/survey/edit", {}).status_code, 400)

    def test_stale_step_submission_does_not_advance(self):
        token = self.token()
        self.answer("skills", "communication")
        response = self.post(
            "/survey",
            {"csrf_token": token, "question_id": "skills", "skills": "design", "action": "next"},
        )
        self.assertEqual(response.status_code, 303)
        self.assertIn("Question 2 of 3", self.get("/survey").text)

    def test_invalid_action_rejected(self):
        response = self.answer("skills", "writing", action="delete")
        self.assertEqual(response.status_code, 400)

    def test_edit_keeps_answers_and_restart_clears_them(self):
        self.complete()
        token = self.token(path="/results")
        response = self.post("/survey/edit", {"csrf_token": token})
        self.assertEqual(response.status_code, 303)
        self.assertRegex(
            self.get("/survey").text,
            r'<input[^>]*value="communication"[^>]*\bchecked\b',
        )
        response = self.post("/survey/restart", {"csrf_token": token})
        self.assertEqual(response.status_code, 303)
        page = self.get("/survey")
        self.assertIn("Question 1 of 3", page.text)
        self.assertNotRegex(page.text, r'<input[^>]*\bchecked\b')
        self.assertEqual(self.get("/results").status_code, 302)

    def test_completion_redirect_and_sessions_are_independent(self):
        self.complete()
        self.assertTrue(self.get("/survey").location.endswith("/results"))
        other = app.test_client()
        self.assertIn("Question 1 of 3", self.get("/survey", other).text)
        self.assertEqual(self.get("/results", other).status_code, 302)


if __name__ == "__main__":
    unittest.main()
