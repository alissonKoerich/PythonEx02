import unittest
from datetime import date
from main.Sex import Sex
from main.Person import Person
from main.ShareHolder import ShareHolder
from main.Employee import Employee


class TestEmployee(unittest.TestCase):

    def testIncomeCalculation(self):
        self.employee = Employee(
            "Biankati",
            "1111111111",
            "11111111",
            date(2002, 2, 21),
            Sex.MALE,
            5000,
            "11111111",
            "11111111")

        self.assertEqual(3914.36, self.employee.calculateIncome())
