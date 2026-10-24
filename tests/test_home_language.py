import re
import unittest

from test_survey import SurveyHelpers


class HomepageLanguageTests(SurveyHelpers, unittest.TestCase):
    def test_home_has_native_controls_in_header_and_welcome(self):
        page = self.get("/")
        self.assertEqual(page.status_code, 200)
        controls = re.findall(r"<button\b[^>]*\bdata-language-toggle[^>]*>", page.text)
        self.assertEqual(len(controls), 2)
        self.assertTrue(all('type="button"' in control for control in controls))
        self.assertIn('lang="zh-CN"', page.text)
        self.assertIn('href="/survey/welcome"', page.text)
        self.assertIn("探索适合你的", page.text)

    def test_translation_asset_is_served_and_linked(self):
        home = self.get("/")
        script = self.get("/static/home-language.js")
        self.assertEqual(script.status_code, 200)
        self.assertIn('src="/static/home-language.js"', home.text)
        self.assertIn("career-home-language", script.text)
        self.assertIn("localStorage", script.text)
        self.assertNotIn("innerHTML", script.text)
        script.close()

    def test_language_switch_is_scoped_to_homepage(self):
        for path in ("/survey/welcome", "/survey"):
            page = self.get(path)
            self.assertNotIn("data-language-toggle", page.text)
            self.assertNotIn("/static/home-language.js", page.text)
