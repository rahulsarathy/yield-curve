# 2019 Federal Tax Bracket Rates
FEDERAL_RATES = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]

# 2019 Federal Tax Brackets
SINGLE = [9700, 39475, 84200, 160275, 204100, 510300]
MARRIED = [19400, 78950, 168400, 321450, 408200, 612350]
MARRIED_SEPARATELY = [9700, 39475, 160275, 204100, 306175]
HEAD_OF_HOUSE = [13850, 52850, 84200, 160700, 204100, 510300]


def marginal_tax(rates, brackets, income):
  """
  Calculates the amount of marginal tax owed on a given income.
  
  :param: rates - A list of the tax rates for each bracket.
  :param: brackets - A list of the smallest value within each bracket.
  :param: income - Annual pre-tax income earned.
  """
  # Find the tax bracket that the given income falls in.
  tax_bracket = 0
  for b in range(len(brackets)):
    tax_bracket = b
    if income <= brackets[b]:
      break

  # Insert the income among the tax brackets.
  rates_copy = rates.copy()
  brackets_copy = brackets.copy()

  # If the income is in the highest tax bracket, we should add it to the end
  # of the brackets list.
  if income > brackets[len(brackets) - 1]:
    tax_bracket += 1
    brackets_copy.insert(tax_bracket, income)
  else:
    rates_copy.insert(tax_bracket, rates[tax_bracket])
    brackets_copy.insert(tax_bracket, income)
  brackets_copy.insert(0, 0)

  taxes = 0
  tax_bracket += 1
  for b in range(tax_bracket):
    taxes += rates_copy[b] * (brackets_copy[b + 1] - brackets_copy[b])
  return taxes

def federal(income):
  """
  Calculates the amount of federal taxes owed to the IRS given an annual
  income.
  """
  return marginal_tax(FEDERAL_RATES, SINGLE, income)
