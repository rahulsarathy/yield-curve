from taxes.calculator import federal
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


if __name__ == '__main__':
  unittest.main()