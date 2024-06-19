import unittest
from datetime import date
from main.Sex import Sex
from main.Person import Person
from main.ShareHolder import ShareHolder
from main.Employee import Employee


class TestShareHolder(unittest.TestCase):

    def testWith20participation(self):
        shareholder = ShareHolder(
            "Gabriel",
            "1111111",
            "095.428.233.23",
            date(2002, 2, 21),
            Sex.MALE,
            20,
            800)

        self.assertEqual(160, shareholder.calculateIncome())

    def testWith70participation(self):
        shareholder70 = ShareHolder(
            "Gabriel",
            "1111111",
            "095.428.233.23",
            date(2002, 2, 21),
            Sex.MALE,
            70,
            2000)

        self.assertEqual(14000, shareholder70.calculateIncome())


    def testWith30participation(self):
        shareholder30 = ShareHolder(
        "Gabriel",
        "1111111",
        "095.428.233.23",
        date(2002, 2, 21),
        Sex.MALE,
        30,
        5000)

        self.assertEqual(7500, shareholder30.calculateIncome())


    def testGetCapital(self):
        getCapital = ShareHolder("Gabriel",
            "1111111",
            "095.428.233.23",
            date(2002, 2, 21),
            Sex.MALE,
            20,
            800)

        self.assertEqual(16000, getCapital.get_capital())

if __name__ == '__main__':
    unittest.main()
