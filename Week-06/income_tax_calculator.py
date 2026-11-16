# TODO 1: Add a header comment
# Name: Henry
# Date: 11/16/2026
# Description: Prompts the user for their income to find information relating to their taxabled income and amount owed in taxes
# TODO 2: Define the constants
# TODO 3: Display the program title and a divider line
# TODO 4: Prompt for gross annual income and convert it to a float
# TODO 5: Prompt for the number of dependents and convert it to an int
# TODO 6: Calculate the dependent deductions and the total deductions
# TODO 7: Calculate the taxable income
# TODO 8: Calculate the estimated income tax
# TODO 9: Display the income tax summary
# Show: gross income, standard deduction, dependent deductions,
# total deductions, taxable income, tax rate, and estimated income tax.
# Use f-strings and format monetary values with .2f
TAX_RATE = .20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 2000
print("Income Tax Calculator")
print("______________________________")
print("What is your income")
income = float(input())
print("Any Dependables")
dependables = int(input())
dependent_deductions = DEPENDENT_DEDUCTION * dependables
user_deduction = dependent_deductions + STANDARD_DEDUCTION
taxable_income = income - user_deduction
estimated_tax = taxable_income * TAX_RATE

print("\n----- Income Tax Summary -----")
print(f"Gross Income:          ${income:,.2f}")
print(f"Standard Deduction:    ${STANDARD_DEDUCTION:,.2f}")
print(f"Dependent Deductions:  ${dependent_deductions:,.2f}")
print(f"Total Deductions:      ${user_deduction:,.2f}")
print(f"Taxable Income:        ${taxable_income:,.2f}")
print(f"Tax Rate:              {TAX_RATE:.0%}")
print(f"Estimated Income Tax:  ${estimated_tax:,.2f}")