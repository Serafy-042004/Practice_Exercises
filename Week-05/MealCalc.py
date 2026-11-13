cost_of_meal = float(input('How muuch was the meal: $'))
tip = cost_of_meal * .20
tax = cost_of_meal * .0825
total = cost_of_meal + tax + tip
print("----- Meal Cost Breakdown -----")
print(f"{'Meal Cost:':<15} ${cost_of_meal:>6.2f}")
print(f"{'Tip (20%):':<15} ${tip:>6.2f}")
print(f"{'Tax (8.25%):':<15} ${tax:>6.2f}")
print('-------------------------------')