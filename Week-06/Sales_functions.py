employees = ['John', 'Sarah', 'Michael', 'Jennifer', 'David']
sales = [5200, 6800, 4500, 7200, 5800]

def calculate_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]

    return sum
def calculate_average(list):
    return calculate_total(list)/len(list)

def evaluate_performance(sale):
    if sale >= 7000:
        return("Excellent")
    elif sale >= 6000:
        return("Good")
    elif sale >= 5000:
        return("Average")
    else:
        return("Needs Improvement")

def find_highest_sales(list):
    highest = 0
    for i in range(len(list)):
        if highest < list[i]:
            highest = list[i]
    return highest

def calculate_comission(sale_amount):
    if sale_amount > 7000:
        return sale_amount * .1
    return sale_amount * .05

def above_average(list, avg):
    count = 0
    for i in range(len(list)):
        if list[i] > avg:
            count += 1
    return count

def calculate_annual_sales(sale):
    return sale * 12

print(f"Total Monthly Sales: {calculate_total(sales)}")
print(" ")

print(f"Average Sales per Employee: {calculate_average(sales)}")
print(" ")

for i in range(len(employees)):
    print(f"{employees[i]}: ${sales[i]:,.2f} - {evaluate_performance(sales[i])}")
print(" ")
print(f"Highest Sales Amount: ${find_highest_sales(sales):,.2f}")
print(" ")
print(f"{employees[0]}'s Comission: ${calculate_comission(sales[0]):,.2f}")

print("EMPLOYEE SALES SUMMARY")
print("-" * 65)

print(f"{'Employee':<12}{'Sales':<15}{'Performance':<22}{'Commission':<12}")
print("-" * 65)

for i in range(len(employees)):
    performance = evaluate_performance(sales[i])
    commission = calculate_comission(sales[i])

    sales_formatted = f"${sales[i]:,.2f}"
    commission_formatted = f"${commission:,.2f}"

    print(f"{employees[i]:<12}{sales_formatted:<15}{performance:<22}{commission_formatted:<12}")
print(" ")
print(f"Employees Above Average: {above_average(sales, calculate_average(sales))}")
print(" ")
for i in range(len(employees)):
    annual_sales = calculate_annual_sales(sales[i])
    print(f"{employees[i]}: ${annual_sales:,.2f}")
#A userdefined functions is a fully customizable function that the user dictates what to do. It is useful in handling specific tasks
#A parameter is something being put into a function. An arugement is when we call, we have specific number for the parameters.
#return simply returns soemthing from a functions
# print does something on screen and resumes where it left off. Return only returns wto where it was called form.
#Breaking down a large propblem is key into haing movign parts. It makes debugging and testing easier.
#name calculate_commission, parameters are amount and rate, arguements are 5200, and .05