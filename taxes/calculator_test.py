from taxes.calculator import federal, marginal_tax
import unittest


class CalculatorTest(unittest.TestCase):
  def test_calculator_single(self):
    """
    Checks that federal() correctly calculates the amount of taxes an individual
    filing under single status should pay.
    """
    # Lowest tax bracket
    self.assertEqual(federal(5000), 500)

    # On the 1st / 2nd tax bracket border
    self.assertEqual(federal(9700), 970)

    # 2nd tax bracket
    self.assertEqual(federal(10000), 1006)

    # 4th tax bracket
    self.assertEqual(federal(100000), 18174.5)
    
    # On the 6th / 7th tax bracket border
    self.assertEqual(federal(510300), 153834.5)

    # Top tax bracket
    self.assertEqual(federal(1000000), 335023.5)

  def test_calculator_single_california(self):
    """
    Checks that marginal_tax() appropriately calculates the owed tax for
    an individual earning income in the State of California, by supplying the
    2019 brackets and rates to the function.
    """    
    rates = [0.01, 0.02, 0.03, 0.04, 0.08, 0.093, 0.103, 0.113, 0.123]
    minimums = [0, 8223, 19495, 30769, 42711, 53980, 275738, 330884, 551473, 1000000]
    self.assertAlmostEqual(marginal_tax(rates, minimums, 10000), 117.77)
    self.assertAlmostEqual(marginal_tax(rates, minimums, 100000), 6304.95)

  def test_calculator_single_alaska(self):
    """
    Checks that marginal_tax() returns 0 when a state does not charge income
    taxes.
    """
    self.assertEqual(marginal_tax([0], [0], 123456), 0)

if __name__ == '__main__':
  unittest.main()