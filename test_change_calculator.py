import unittest

from change_calculator import ChangeCalculator


class TestChangeCalculator(unittest.TestCase):
    def setUp(self):
        self.change_calculator = ChangeCalculator()

    def testGetNegativeChange(self):
        change = self.change_calculator.calculate(-1)
        self.assertTrue(change.is_empty())

    def testGetZeroChange(self):
        change = self.change_calculator.calculate(0)
        self.assertTrue(change.is_empty())

    def testGetChangeGreaterThanDollar(self):
        change = self.change_calculator.calculate(2.99)
        self.assertEqual(change.dollars, 2)
        self.assertEqual(change.pennies, 4)
        self.assertEqual(change.nickels, 0)
        self.assertEqual(change.dimes, 2)
        self.assertEqual(change.quarters, 3)

    def testGetChangeForOnePenny(self):
        change = self.change_calculator.calculate(.01)
        self.assertEqual(change.pennies, 1)
        self.assertEqual(change.nickels, 0)
        self.assertEqual(change.dimes, 0)
        self.assertEqual(change.quarters, 0)

    def testGetChangeForThreePennies(self):
        change = self.change_calculator.calculate(.03)
        self.assertEqual(change.pennies, 3)
        self.assertEqual(change.nickels, 0)
        self.assertEqual(change.dimes, 0)
        self.assertEqual(change.quarters, 0)

    def testGetChangeForOneNickel(self):
        change = self.change_calculator.calculate(.05)
        self.assertEqual(change.pennies, 0)
        self.assertEqual(change.nickels, 1)
        self.assertEqual(change.dimes, 0)
        self.assertEqual(change.quarters, 0)

    def testGetChangeForOneDime(self):
        change = self.change_calculator.calculate(.1)
        self.assertEqual(change.pennies, 0)
        self.assertEqual(change.nickels, 0)
        self.assertEqual(change.dimes, 1)
        self.assertEqual(change.quarters, 0)

    def testGetChangeForOneQuarter(self):
        change = self.change_calculator.calculate(.25)
        self.assertEqual(change.pennies, 0)
        self.assertEqual(change.nickels, 0)
        self.assertEqual(change.dimes, 0)
        self.assertEqual(change.quarters, 1)

    def testGetChangeForNinetyNineCents(self):
        change = self.change_calculator.calculate(.99)
        self.assertEqual(change.pennies, 4)
        self.assertEqual(change.nickels, 0)
        self.assertEqual(change.dimes, 2)
        self.assertEqual(change.quarters, 3)


if __name__ == '__main__':
    unittest.main()
