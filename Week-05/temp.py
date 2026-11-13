sale = 25.75 + 45.67 + 45.75 + 55.67 + 45.60
print(f'Sub-Total {sale: .2f}')
tax = sale * .07
print(f'Tax {tax: .2f}')
sale += tax
print(f'Total Cost {sale: .2f}')