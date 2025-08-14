import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("grace", "hopper", 100000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.salary, 105000)

    def test_give_custom_raise(self):
        self.emp.give_raise(12000)
        self.assertEqual(self.emp.salary, 112000)

if __name__ == "__main__":
    unittest.main()
