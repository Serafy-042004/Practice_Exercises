import statistics
days = [
'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
]
sales = [1250, 1480, 1100, 1650, 1850,
1420, 1700, 1300, 2100, 1950]

for i in range(len(days)):
    print(f"{days[i]}: {sales[i]:.2f}")

mean = statistics.mean(sales)
median = statistics.median(sales)
mode = statistics.mode(sales)
stdev = statistics.stdev(sales)
sum = sum(sales)
min = min(sales)
max = max(sales)
print(" ")
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Mode: {mode:.2f}")
print(f"Standard Deviation: {stdev:.2f}")
print(f"Total Sales: {sum:.2f}")
print(f"Minimum Sales: {min:.2f}")
print(f"Maximum Sales: {max:.2f}")
print(" ")
countofExc = 0
countofgood = 0
countofAVG = 0
countofImp = 0
for i in range(len(days)):
    print(f"{days[i]}: {sales[i]:.2f}", end = " ")
    if sales[i] >= 1800:
        print("- Excellent")
        countofExc += 1
    elif sales[i] >= 1500:
        print("- Good")
        countofgood += 1  
    elif sales[i] >= 1200:
        print("- Average")
        countofAVG += 1
    else:
        print("- Needs Improvement")
        countofImp += 1

print(" ")
print(f"The count of Excellent sales days are {countofExc}")
print(f"The count of good sales days are {countofgood}")
print(f"The count of average sales days are {countofAVG}")
print(f"The count of sales days that need improvement are {countofImp}")
print(" ")

target = 1500
count_target = 0

for i in range(len(days)):
    if sales[i] >= target:
        print(f"{days[i]}: ${sales[i]:,.2f}")
        count_target += 1

print(f"Total days that met the target: {count_target}")
print(" ")

if mean >= 1700:
    print("Sales performance is excellent.")
elif mean >= 1500:
    print("Sales performance is good.")
else:
    print("Sales performance needs improvement.")