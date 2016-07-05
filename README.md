# Change Calculator

Calculates exact change needed using US currency worth less than a 
dollar. Underlying algorithm is recursive in nature and is powered by 
`decimal.Decimal`

## About

I was shown this algorithm in a comp. scie class a few years back and 
wanted to try implementing it on my own.

## Example
    change_calculator = ChangeCalculator()
    change = self.change_calculator.calculate(.99)
    self.assertEqual(change.pennies, 4)
    self.assertEqual(change.nickels, 0)
    self.assertEqual(change.dimes, 2)
    self.assertEqual(change.quarters, 3)
    
(See unit tests)