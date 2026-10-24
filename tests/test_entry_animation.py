"""Checks for the current Morandi homepage and progressive entry animation."""
import shutil
import threading
import unittest

from playwright.sync_api import expect, sync_playwright
from werkzeug.serving import make_server

from main import app


class EntryAnimationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server("127.0.0.1", 0, app, threaded=True)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}/"
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(
            executable_path=shutil.which("chromium"), headless=True
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.server.shutdown()
        cls.thread.join()
        cls.server.server_close()

    def check_page(self, **options):
        context = self.browser.new_context(**options)
        self.addCleanup(context.close)
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        self.addCleanup(lambda: self.assertEqual(errors, []))
        page.goto(self.url)
        return page

    def test_keyboard_skip_and_survey_navigation(self):
        for key in ("Enter", "Escape"):
            page = self.check_page()
            button = page.locator("#entry-continue")
            expect(button).to_be_focused()
            page.keyboard.press("Tab")
            expect(button).to_be_focused()
            page.keyboard.press("Shift+Tab")
            expect(button).to_be_focused()
            self.assertTrue(page.locator(".welcome-card").evaluate("(el) => el.inert"))
            page.keyboard.press(key)
            expect(page.locator("#entry-screen")).to_be_hidden()
            expect(page.locator(".welcome-card .button")).to_be_focused()
            page.locator(".welcome-card .button").click()
            expect(page.locator(".question")).to_be_visible()
            self.assertIn("/survey", page.url)

    def test_automatic_dismissal(self):
        page = self.check_page()
        expect(page.locator("#entry-screen")).to_be_visible()
        expect(page.locator("#entry-screen")).to_be_hidden(timeout=4000)
        self.assertFalse(page.locator(".welcome-card").evaluate("(el) => el.inert"))

    def test_mobile_click_skip_and_no_clipping(self):
        for width, height in ((320, 568), (390, 844), (667, 375)):
            page = self.check_page(viewport={"width": width, "height": height})
            self.assertLessEqual(
                page.evaluate("document.documentElement.scrollWidth"), width
            )
            button = page.locator("#entry-continue")
            button.scroll_into_view_if_needed()
            bounds = button.bounding_box()
            self.assertGreaterEqual(bounds["x"], 0)
            self.assertLessEqual(bounds["x"] + bounds["width"], width)
            button.click()
            expect(page.locator("#entry-screen")).to_be_hidden()
            self.assertLessEqual(
                page.evaluate("document.documentElement.scrollWidth"), width
            )

    def test_reduced_motion_and_no_javascript_bypass_overlay(self):
        for options in (
            {"reduced_motion": "reduce"},
            {"java_script_enabled": False},
        ):
            page = self.check_page(**options)
            expect(page.locator("#entry-screen")).to_be_hidden()
            page.locator(".welcome-card .button").click()
            expect(page.locator(".question")).to_be_visible()


if __name__ == "__main__":
    unittest.main()
