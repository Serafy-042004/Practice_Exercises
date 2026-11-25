import pandas as pd
import numpy as np

price_list = [4.75, 4.25, 5.25]
prices = pd.Series(price_list)
print(prices)
prices = pd.Series(price_list, index=['Latte', 'Cold Brew', 'Mocha'])
print(prices)
menu_dict = {'Chai': 4.50, 'Espresso': 3.00}
more_prices = pd.Series(menu_dict)
print(more_prices)
print(prices['Mocha'])

stock_data = {
    'drink': ['Latte', 'Cold Brew', 'Mocha'],
    'cups_left': [120, 54, 98]
}
stock = pd.DataFrame(stock_data)
print(stock)
print(stock.to_string())
arr = np.array([[120, 54, 98]])
print(pd.DataFrame(arr))

stock.insert(1, 'size', ['M', 'L', 'M'])
print(stock)
sample = pd.DataFrame(np.arange(6).reshape((3, 2)),
                        index=['Back Bay', 'Kendall', 'Seaport'],
                        columns=['Mon', 'Tue'])
print(sample)

cups = pd.DataFrame({'Mon': [120, 98, 143], 'Tue': [135, 110, 128]},
                   index =['Back Bay', 'Kendal', 'Seaport'])
print(cups)
print(cups['Kendal':])
print(cups.loc['Seaport'])
print(cups.loc[['Back Bay', 'Seaport']])
print(cups.iloc[0])
#print(cups.loc(0))
#<pandas.core.indexing._LocIndexer object at 0x000001E520FC12B0>
cups.loc['Fenway'] = [88, 91]
print(cups)

orders = pd.read_csv('bb_orders.csv')
print(orders)
print(pd.options.display.max_rows)

print(orders.head(3))
print(orders.tail(2))
print(orders.describe())
orders.info()
print(orders['store'].value_counts())

print(orders['order_date'].dtype)
#print(orders['order_data'].dt.month)
orders['order_date'] = pd.to_datetime(orders['order_date'])
print(orders['order_date'].dtype)
march = orders[orders['order_date'] >= '2026-03-01']
print(len(march))

orders = orders.drop('notes', axis=1)
print(orders.shape)
print(orders.duplicated().sum())
result = orders.drop_duplicates(inplace=True)
print(result)
print(orders.shape)
print(len(orders.dropna()))

big = orders[orders['qty'] >= 4]
print(big)
back_bay = orders[orders['store'] == 'Back Bay']
print(len(back_bay))
bb_big = orders[(orders['store'] == 'Back Bay') & (orders['qty'] >= 2)]
print(bb_big[['order_id', 'qty']])

print(orders['store'].value_counts())
orders.replace({'store': {'Kendal Sq': 'Kendall Square'}}, inplace = True)
print(orders['store'].value_counts())
orders['price'] = orders.price.fillna(5.25)
print(orders.loc[8])

orders.loc[12, 'qty'] = 5
for x in orders.index:
    if orders.loc[x, 'qty'] <=0:
        orders.drop(x, inplace =True)
print(orders[['order_id', 'qty']].tail(4))
print(orders.shape)

print(orders['qty'].sum())
print(orders.qty.max())
orders['revenue'] = orders['qty'] * orders['price']
print(orders[['drink', 'qty', 'price', 'revenue']].head())

rev = orders['revenue']
print(rev.sum())
print(rev.count())
print(round(rev.mean(), 2))
print(rev.median())
print(rev.min(), rev.max())
print(orders.aggregate({'qty': ['sum', 'mean'],
                        'revenue':['sum', 'mean']}))

store_rev = orders.groupby('store')['revenue'].sum()
print(store_rev)
drink_qty = orders.groupby(['drink'])[['qty']].sum()
print(drink_qty)
print(orders.groupby('store')['qty'].mean().round(2))

print(store_rev.sort_values(ascending=False))
top = orders.sort_values('revenue', ascending=False)
print(top[['order_id', 'store', 'revenue']].head(3))
print(drink_qty.sort_index(ascending=False))

print(store_rev.rank(ascending=False))
drink_qty['rank'] = drink_qty['qty'].rank(ascending=False)
print(drink_qty)

menu = pd.DataFrame({
'drink': ['Chai', 'Cold Brew', 'Espresso', 'Latte', 'Mocha'],
'cost': [1.40, 1.10, 0.90, 1.60, 1.90]})
drink_cost = pd.merge(menu, drink_qty[['qty']], on=['drink'])
drink_cost['total_cost'] = drink_cost['qty'] * drink_cost['cost']
print(drink_cost)
detail = pd.merge(orders, menu, on=['drink'])
print(detail.shape)

orders['month'] = orders['order_date'].dt.month
orders['weekday'] = orders['order_date'].dt.day_name()
print(orders[['order_date', 'month', 'weekday']].head(3))
orders['order_month'] = orders['order_date'].dt.to_period('M')
monthly_sales = orders.groupby('order_month')['revenue'].sum()
print(monthly_sales)
#1. In Task 1.4, why did cups.loc[0] fail when cups.iloc[0] worked? After Task 2.4 dropped row 7,
#which one would you use to get “the 8th row”, and why?
#loc uses rows and that starts at 0, so to get 8 we had to drop by 1
#2. In Task 2.1, result printed None. Explain what inplace=True does, and what would go wrong if
#you wrote orders = orders.drop_duplicates(inplace=True).
#inplace true makes changes to the dataframe, it returns none becuase the change already happened
#3. In Task 2.4 we fixed one quantity and dropped another. When is it right to fix a bad value, and
#when is it better to drop the record?
#It is better to fix a value if we have the info, if we cant confirm a number we should drop it to keep infomation accurate
#4. Rule 4 says clean before you count. Using the numbers from Tasks 1.5 and 3.2, describe how
#Seaport’s revenue would have been wrong if you had skipped Part 2.
#sea port would have a quantity of 50 instead of 5. Seaport would seems to have higher sales than it did
#5. Why is to_period('M') a better way to group by month than .dt.month when the data covers
#more than one year?
#.dt.month would return all months rather than a specific month