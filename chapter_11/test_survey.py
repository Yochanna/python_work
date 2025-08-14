import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        s = AnonymousSurvey("What language did you first learn?")
        s.store_response("Python")
        self.assertIn("Python", s.responses)

    def test_store_three_responses(self):
        s = AnonymousSurvey("What language did you first learn?")
        answers = ["Python", "C", "Ruby"]
        for a in answers:
            s.store_response(a)
        self.assertEqual(s.responses, answers)

if __name__ == "__main__":
    unittest.main()
