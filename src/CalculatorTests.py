import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_instance_claculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)


if __name__ == '__main__':
    unittest.main()
