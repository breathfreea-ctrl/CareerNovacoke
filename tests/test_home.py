"""Homepage regressions. Run: python -m unittest discover -s tests -v."""

import shutil
import threading
import unittest

from playwright.sync_api import expect, sync_playwright
from werkzeug.serving import make_server

from main import app


class HomepageResponseTests(unittest.TestCase):
    def test_homepage_returns_html(self):
        with app.test_client() as client:
            response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "text/html")
        self.assertIn('lang="zh-CN"', response.get_data(as_text=True))
        self.assertIn('id="welcome"', response.get_data(as_text=True))
        self.assertIn("探索适合你的", response.get_data(as_text=True))


class HomepageBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # An isolated ephemeral port avoids conflicts with the preview workflow.
        cls.server = make_server("127.0.0.1", 0, app, threaded=True)
        cls.addClassCleanup(cls.server.server_close)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.addClassCleanup(cls.thread.join)
        cls.addClassCleanup(cls.server.shutdown)
        cls.url = f"http://127.0.0.1:{cls.server.server_port}/"
        cls.playwright = sync_playwright().start()
        cls.addClassCleanup(cls.playwright.stop)
        # Replit provides Chromium; elsewhere use Playwright's installed browser.
        chromium = shutil.which("chromium") or shutil.which("chromium-browser")
        cls.browser = cls.playwright.chromium.launch(
            executable_path=chromium, headless=True,
        )
        cls.addClassCleanup(cls.browser.close)

    def setUp(self):
        self.context = self.browser.new_context(
            viewport={"width": 1280, "height": 900},
            reduced_motion="no-preference",
            has_touch=True,
        )
        self.addCleanup(self.context.close)
        # Test offline fallback fonts, without depending on Google's availability.
        self.context.route("https://fonts.googleapis.com/**", lambda route: route.abort())
        self.page = self.context.new_page()
        self.errors = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))
        self.addCleanup(lambda: self.assertEqual(self.errors, []))

    def open_home(self):
        response = self.page.goto(self.url, wait_until="load")
        self.assertEqual(response.status, 200)
        expect(self.page.locator("#enter-home")).to_be_focused()
        expect(self.page.get_by_role("dialog")).to_be_visible()

    def assert_background_inert(self, expected):
        states = self.page.locator("main > :not(#welcome)").evaluate_all(
            "elements => elements.map(element => element.inert)"
        )
        self.assertTrue(states)
        self.assertEqual(states, [expected] * len(states))

    def assert_home_ready(self):
        expect(self.page.locator("#welcome")).to_have_count(0, timeout=10000)
        self.assert_background_inert(False)
        expect(self.page.locator("h1")).to_be_focused()
        # The heading is not an extra stop in the normal Tab sequence.
        expect(self.page.locator("h1")).to_have_attribute("tabindex", "-1")
        self.page.keyboard.press("Tab")
        expect(self.page.locator(".career-cta")).to_be_focused()
        # Use the real in-page link, not /survey (outside this task's scope).
        self.page.locator(".scroll-cue").click()
        expect(self.page).to_have_url(self.url + "#explore")
        expect(self.page.locator("#explore")).to_be_in_viewport()

    def test_click_closes_welcome_and_restores_focus(self):
        self.open_home()
        self.assert_background_inert(True)
        self.page.locator("#enter-home").click()
        self.assert_home_ready()

    def test_escape_closes_welcome_and_restores_focus(self):
        self.open_home()
        self.page.keyboard.press("Escape")
        self.assert_home_ready()

    def test_tab_and_shift_tab_stay_in_welcome(self):
        self.open_home()
        for key in ("Tab", "Shift+Tab", "Tab"):
            self.page.keyboard.press(key)
            expect(self.page.locator("#enter-home")).to_be_focused()
            self.assert_background_inert(True)
        self.page.keyboard.press("Enter")
        self.assert_home_ready()

    def test_automatic_close_leaves_page_operable(self):
        self.open_home()
        self.assert_background_inert(True)
        # Real timers intentionally exercise both the delay and exit transition.
        self.assert_home_ready()

    def test_reduced_motion_close_paths(self):
        self.page.emulate_media(reduced_motion="reduce")
        for action in ("click", "escape", "automatic"):
            with self.subTest(action=action):
                self.open_home()
                if action == "click":
                    self.page.locator("#enter-home").click()
                elif action == "escape":
                    self.page.keyboard.press("Escape")
                self.assert_home_ready()

    def assert_mobile_content_fits(self, welcome_visible):
        dimensions = self.page.evaluate("""() => ({
            viewport: document.documentElement.clientWidth,
            document: document.documentElement.scrollWidth,
            body: document.body.scrollWidth
        })""")
        self.assertLessEqual(dimensions["document"], dimensions["viewport"])
        self.assertLessEqual(dimensions["body"], dimensions["viewport"])
        # overflow:hidden must not disguise clipped text or controls.
        selector = (
            "#welcome .welcome-content, #welcome h2, #welcome p, #enter-home"
            if welcome_visible else
            ".career-brand, .header-note, h1, .hero-intro, .career-cta, "
            ".hero-reassurance, .scroll-cue, .section-heading, "
            ".pathway-copy, .pathway-link, .career-footer > *"
        )
        failures = self.page.locator(selector).evaluate_all("""elements =>
            elements.flatMap(element => {
                const r = element.getBoundingClientRect();
                const width = document.documentElement.clientWidth;
                const issues = [];
                if (r.left < -1 || r.right > width + 1)
                    issues.push(element.className + ': outside viewport');
                if (element.scrollWidth > element.clientWidth + 1)
                    issues.push(element.className + ': clipped content');
                return issues;
            })
        """)
        self.assertEqual(failures, [])

    def test_mobile_layout_before_and_after_welcome(self):
        for width in (320, 375, 390, 414):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width": width, "height": 740})
                self.open_home()
                # Wait for arrival animation without disabling production CSS.
                self.page.locator(".welcome-content").evaluate(
                    "async el => { await Promise.all(el.getAnimations()"
                    ".filter(a => a.effect.getTiming().iterations !== Infinity)"
                    ".map(a => a.finished)); }"
                )
                self.assert_mobile_content_fits(welcome_visible=True)
                expect(self.page.locator("#enter-home")).to_be_in_viewport(ratio=1)
                self.page.locator("#enter-home").tap()
                self.assert_home_ready()
                self.assert_mobile_content_fits(welcome_visible=False)


if __name__ == "__main__":
    unittest.main()
