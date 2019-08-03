def monthly_rate(annual_growth):
  """Calculates the monthly rate from the given annual growth rate."""
  return annual_growth ** (1/12.0)

def monthly(initial_deposit, monthly_deposit, annual_growth, years):
  """
  Calculates the total value of an investment based on regular monthly deposits,
  a steady growth rate, and a fixed holding period.
  
  NOTE: We use the monthly growth rate to calculate return.
  
  :param initial_deposit: The initial amount of money kept for investment.
  :param monthly_deposit: The amount of money added every month for investment.
  :param growth_rate: The percentage rate at which the investments grow.
  :param years: The number of years that the investment is held.
  """
  deposits = initial_deposit
  value = initial_deposit
  month_growth = monthly_rate(annual_growth)
  for _ in range(12):
    for _ in range(years):
      value *= month_growth
      value += monthly_deposit

  # Round to the nearest cent.
  return round(value, 2)
