import unittest
from charting.compound import monthly_rate, monthly


class CompoundTest(unittest.TestCase):
  def test_monthly_rate(self):
    """
    Checks that monthly_rate() produces the correct monthly growth rate when
    given a valid annual growth rate.
    """
    # 1.00797414**12 = 1.1
    self.assertAlmostEqual(monthly_rate(1.1), 1.00797414)

  def test_compound_monthly_one_year_no_deposits(self):
    """
    Checks that monthly() produces the correct total value of an investment
    after a single year, but with no regular monthly deposits.
    """
    # 1000 * 1.1 = 1100
    self.assertAlmostEqual(monthly(1000, 0, 1.1, 1), 1100)

  def test_compound_monthly_one_year_with_deposits(self):
    """
    Checks that monthly() produces the correct total value of an investment
    after a single year with regular monthly deposits.
    """
    self.assertAlmostEqual(monthly(1000, 100, 1.1, 1), 2354.05)

if __name__ == '__main__':
  unittest.main()
