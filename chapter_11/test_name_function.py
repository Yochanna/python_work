import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        self.assertEqual(get_formatted_name("janis", "joplin"), "Janis Joplin")

    def test_first_middle_last(self):
        self.assertEqual(
            get_formatted_name("wolfgang", "mozart", "amadeus"),
            "Wolfgang Amadeus Mozart"
        )

if __name__ == "__main__":
    unittest.main()
