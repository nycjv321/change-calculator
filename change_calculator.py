from decimal import *

getcontext().prec = 2


class ChangeCalculator(object):
    quarter = Decimal(".25")
    dime = Decimal(".1")
    nickel = Decimal(".05")
    penny = Decimal(".01")

    def __init__(self):
        self.change = ChangeCalculator.Change()

    def calculate(self, amount):
        amount = Decimal(str(amount))

        if amount <= 0:
            return self.change
        elif amount > Decimal(".99"):
            one = Decimal("1")
            remainder = amount % one
            self.change.dollars += amount / one - remainder
            self.calculate(remainder)
        elif amount >= ChangeCalculator.quarter:
            self.calculate_change(amount, ChangeCalculator.quarter, (lambda: self.change.add_quarter()))
        elif amount >= ChangeCalculator.dime:
            self.calculate_change(amount, ChangeCalculator.dime, (lambda: self.change.add_dime()))
        elif amount >= ChangeCalculator.nickel:
            self.calculate_change(amount, ChangeCalculator.nickel, (lambda: self.change.add_nickel()))
        elif amount >= ChangeCalculator.penny:
            self.calculate_change(amount, ChangeCalculator.penny, (lambda: self.change.add_penny()))

        return self.change

    def calculate_change(self, amount, divisor, function):
        remainder = amount % divisor

        if remainder > 0:
            self.calculate(remainder)

        new_amount = amount - divisor
        if new_amount > 0 or amount == divisor:
            function()
            self.calculate(new_amount - remainder)

    class Change(object):
        def __init__(self):
            self.dollars = 0
            self.quarters = 0
            self.dimes = 0
            self.nickels = 0
            self.pennies = 0

        def add_quarter(self):
            self.quarters += 1

        def add_dime(self):
            self.dimes += 1

        def add_nickel(self):
            self.nickels += 1

        def add_penny(self):
            self.pennies += 1

        def is_empty(self):
            return self.quarters == 0 and self.dimes == 0 and self.nickels == 0 and self.pennies == 0
