import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

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

#    testing from file

    def test_AdditionFromFile(self):
        test_data = CsvReader('./src/Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)


    def test_subtractionFromFile(self):
        test_dataS = CsvReader('./src/Subtraction.csv').data
        for row in test_dataS:
            result = float(row['Result'])
            print("hello")
            print(result)
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), result)


    def test_MultiplicationFromFile(self):
        test_dataM = CsvReader('./src/Multiplication.csv').data
        for row in test_dataM:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)

    def test_DividisionFromFile(self):
        test_dataD = CsvReader('./src/Division.csv').data
        for row in test_dataD:
            result = float(row['Result'])
            self.assertEqual(round(self.calculator.divide(row['Value 2'], row['Value 1']),9),result)

    def test_sqrFromFile(self):
        test_dataQ = CsvReader('./src/Square.csv').data
        for row in test_dataQ:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqr(row['Value 1']), result)

    def test_sqrRootFromFile(self):
        test_dataR = CsvReader('./src/Square Root.csv').data
        for row in test_dataR:
            result = float(row['Result'])
            self.assertEqual(round(self.calculator.sqrRoot(row['Value 1']),7), round(result,7))

if __name__ == '__main__':
    unittest.main()
