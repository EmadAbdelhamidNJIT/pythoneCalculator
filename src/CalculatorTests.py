import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
      #  self.csv_reader = CsvReader('Subtraction.csv')

    def test_instantiate_claculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculatorr(self):
        self.assertEqual(self.calculator.add(2, 2), 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)

    def test_sqr_method_calculator(self):
        self.assertEqual(self.calculator.sqr(2), 4)

    def test_sqrRoot_method_calculator(self):
        self.assertEqual(self.calculator.sqrRoot(4), 2)

    # testing from file

    def test_AdditionFromFile(self):
        test_data = CsvReader('./src/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)


if __name__ == '__main__':
    unittest.main()
