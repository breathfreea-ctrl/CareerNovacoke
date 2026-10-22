import unittest

from main import app
from matching import match_user
from models import ROLES


class CareerAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_pages(self):
        for path in ["/", "/survey"] + [
            f'/role/{role["id"]}' for role in ROLES
        ]:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertIn(b"<html", response.data.lower())
        self.assertEqual(self.client.get("/role/999").status_code, 404)
        self.assertEqual(self.client.get("/results").status_code, 405)

    def test_results(self):
        role = ROLES[0]
        response = self.client.post("/results", data={
            "skills": role["required_skills"],
            "interests": role["interests"],
            "experience_years": "2",
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(role["name"].encode(), response.data)
        self.assertIn(b"100", response.data)

    def test_invalid_and_empty_input(self):
        for experience in ["", "-1", "abc", "NaN", "Infinity", "1e999"]:
            with self.subTest(experience=experience):
                response = self.client.post(
                    "/results", data={"experience_years": experience}
                )
                self.assertEqual(response.status_code, 200)

    def test_matching_is_deterministic_and_does_not_mutate_catalog(self):
        role = ROLES[0]
        result = match_user(role["required_skills"], 0, role["interests"])
        self.assertEqual(result[0]["id"], role["id"])
        self.assertEqual(result[0]["match_score"], 100)
        self.assertNotIn("match_score", role)
        self.assertEqual(result, match_user(
            role["required_skills"] * 2, 10, role["interests"] * 2
        ))
        self.assertTrue(all(
            item["match_score"] == 0 for item in match_user([], 0, [])
        ))
        self.assertTrue(all(
            item["match_score"] == 0
            for item in match_user(["unknown"], 0, ["unknown"])
        ))


if __name__ == "__main__":
    unittest.main()
