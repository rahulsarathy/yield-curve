# 2019 Federal Tax Bracket Rates
FEDERAL_RATES = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]

# 2019 Federal Tax Brackets
SINGLE = [9700, 39475, 84200, 160275, 204100, 510300]
MARRIED = [19400, 78950, 168400, 321450, 408200, 612350]
MARRIED_SEPARATELY = [9700, 39475, 160275, 204100, 306175]
HEAD_OF_HOUSE = [13850, 52850, 84200, 160700, 204100, 510300]


def federal(income):
  """
  Calculates the amount of federal taxes owed to the IRS given an annual
  income.
  """
  
  # Find the tax bracket that the given income falls in.
  tax_bracket = 0
  for bracket in range(len(SINGLE)):
    tax_bracket = bracket
    if income <= SINGLE[bracket]:
      break

  # Insert the income among the tax brackets.
  federal_rates = FEDERAL_RATES.copy()
  single = SINGLE.copy()

  # If the income is in the highest tax bracket, we should add it to the end
  # of the brackets list.
  if income > SINGLE[len(SINGLE) - 1]:
    tax_bracket += 1
    single.insert(tax_bracket, income)
  else:
    federal_rates.insert(tax_bracket, FEDERAL_RATES[tax_bracket])
    single.insert(tax_bracket, income)
  single.insert(0, 0)


  taxes = 0
  tax_bracket += 1
  for b in range(tax_bracket):
    taxes += federal_rates[b] * (single[b + 1] - single[b])
  return taxes
