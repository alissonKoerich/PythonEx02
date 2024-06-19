import unittest
from datetime import date
from main.Sex import Sex
from main.Person import Person
from main.ShareHolder import ShareHolder
from main.Employee import Employee


class TestEmployee(unittest.TestCase):

    def testIncomeCalculation(self):
        employee = Employee(
            "Biankati",
            "1111111111",
            "11111111",
            date(2002, 2, 21),
            Sex.MALE,
            5000,
            "11111111",
            "11111111")

        self.assertEqual(3914.36, employee.calculateIncome())

    def testTotalSalary(self):
        totalSalary = Employee(
            "Alisson",
            "111111111",
            "111111111",
            date(2002, 3, 21),
            Sex.MALE,
            3000,
            "111111111",
            "111111111111")

        self.assertEqual(3000, totalSalary.salary)

    def testIrCalculation(self):
        totalIr = Employee(
            "Guilherme Sartori",
            "2222222",
            "22222222",
            date(2003, 7, 26),
            Sex.MALE,
            5000,
            "22222222",
            "22222222")

        self.assertEqual(535.64, totalIr.getIr())

    def testInssValue(self):
        totalInss = Employee(
            "Guilherme Sartori",
            "2222222",
            "22222222",
            date(2003, 7, 26),
            Sex.MALE,
            2850,
            "22222222",
            "22222222")

        self.assertEqual(313.5, totalInss.getInss())

if __name__ == '__main__':
    unittest.main()