import numpy as np
cups = np.array([[120, 135, 150],
                 [98, 110, 104]])
for row in cups:
    print(row)
#2
for row in cups:
    for value in row:
        print(value)
#6

seaport = np.array([[143, 128, 161]])
all_stores = np.concatenate((cups, seaport))

for row in cups:
    print(row)
print("__________________________________")
thu_fri = np.array([[140,172], [101, 95], [150, 166]])
week = np.concatenate((all_stores, thu_fri), axis = 1)
print(week)
print("__________________________________")
mon = np.array([120, 98, 143])
tue = np.array([135, 110, 128])
print(np.hstack((mon, tue)))
print("__________________________________")
print(np.vstack((mon, tue)))
print("__________________________________")
print(np.stack((mon, tue), axis=1))
print("__________________________________")
seaport_week = np.array([143, 128, 161, np.nan, 166])
print(seaport_week)
print(seaport_week.dtype)
print(np.sum(seaport_week))
seaport_none = np.array([143, 128, 161, None, 166])
print(seaport_none.dtype)
print(seaport_week + 1)
print("__________________________________")
days = np.array([140, 152, 138, 160, 171, 199, 185])
halves = np.array_split(days, 2)
print(halves)
print(halves[1])
by_store = np.array_split(week, 3)
print(by_store[2])
print("__________________________________")
TARGET = 150
print(np.where(days < TARGET))
print(np.where(days < TARGET, 'below', 'met'))
print(np.where(days < TARGET, days + 15, days))
print("__________________________________")
print(np.sort(days))
print(days)
codes = np.array(['95', '100', '9', '120'])
print(np.sort(codes)) 
print(np.sort(week))
busy = days > 160
print("__________________________________")
print(busy)
print(days[busy])
codes = np.array(['95', '100', '9', '120' ])
print(np.sort(codes))
print(np.sort(week))
busy = days > 100
print(busy)
print(days[busy])
print("__________________________________")
np.random.seed(7)
test_orders = np.random.randint(1, 6, size=(2,5))
print(test_orders)
tips = np.random.rand(2, 3)
print(tips)
print("__________________________________")
np.random.seed(7)
sizes = ['small', 'medium', 'large']
orders = np.random.choice(sizes, p=[0.2, 0.5, 0.3], size=10)
print(orders)
print(orders[orders == 'large'])
print(np.random.choice(sizes))
print("__________________________________")
np.random.seed(7)
waits = np.random.normal(loc=4, scale=1, size=1000)
print(np.round(np.mean(waits), 2))
print(np.round(np.std(waits), 2))
within_1 = waits[np.absolute(waits - 4) < 1]
print(len(within_1))
within_2 = waits[np.absolute(waits - 4) < 2]
print(len(within_2))
print("__________________________________")
np.random.seed(7)
baristas = np.array(['Ana', 'Ben', 'Cho', 'Dev', 'Eli'])
print(np.random.permutation(baristas))
print(baristas)
np.random.shuffle(baristas)
print(baristas)
print("__________________________________")
mon_cups = np.array([120, 98, 143])
avg_price = np.array([4.50, 4.25, 4.75])
revenue = np.multiply(mon_cups, avg_price)
print(revenue)
cost = np.array([310, 260, 380])
print(np.subtract(revenue, cost))
print(np.divmod(mon_cups, 25))
print(np.absolute(np.array([-12, 5, -3])))
print("__________________________________")
changes = np.array([-2.7, -0.5, 0.5, 1.5, 2.5, 3.46])
print(np.trunc(changes))
print(np.floor(changes))
print(np.ceil(changes))
print(np.round(changes))
print(np.round(changes, 1))
print("__________________________________")
print(week)
print(np.sum(week))
print(np.sum(week, axis=1)) 
print(np.sum(week, axis=0)) 
print(np.cumsum(days))
print("__________________________________")
growth = np.array([1.10, 1.05, 1.20])
print(np.round(np.prod(growth), 3))
print(np.round(np.cumprod(growth), 3))
print(np.diff(days))
print(np.diff(days, n=2))

#In Task 3.4, np.sum(week, axis=0) returned 5 values and axis=1 returned 3. Explain why, using
#the words rows and columns.
#By adding up all the colums, there are 5 outputs, but if we add by the rows, ther are only 3 rows
#2. Why is np.nan a better way to record Seaport’s missing Thursday than None or 0? What would go
#wrong in a weekly total with each one?
#If 0, it means that there were 0 sales, it could be that we are simply missing data thus messing with the analysis
#3. In Task 1.6, '9' sorted after '120'. Why? How would you get a proper numeric order?
# 9 was stored aplhebetically, thus it was not sorted as a number
#4. Why is setting a seed useful when you build test data? Give one situation where NumPy’s pseudo-
#random numbers would not be good enough (1.B.1).
# Setting a seed means there is a way to reach an exact output
#5. Dana wants to know how many full sleeves of 25 cups to order for 143 cups. Which rounding or
#division tool from Part 3 would you use, and why not round()?
#np.divmod would be useful to find how many are still needed after the full sleeves.