import numpy as np

sales_data = np.array([
    #1
    [
        [1200, 1500, 1800], 
        [2000, 2200, 2500]  
    ],

    #2
    [
        [1400, 1600, 1900],  
        [2100, 2300, 2600]   
    ]
])

print(sales_data)

for value in np.nditer(sales_data):
    print(value)
print(" ")
for layer in range(sales_data.shape[0]):
    for row in range(sales_data.shape[1]):
        for coloum in range(sales_data.shape[2]):
            value = sales_data[layer, row, coloum]
            print(value)

total_sales = 0
number_of_sales = 0
highest_sale = 0
for layer in range(sales_data.shape[0]):
    for row in range(sales_data.shape[1]):
        for coloum in range(sales_data.shape[2]):
            value = sales_data[layer, row, coloum]
            total_sales += sales_data[layer, row, coloum]
            number_of_sales += 1
            if(value > highest_sale):
                highest_sale = value

print(total_sales)
print(f'{total_sales/number_of_sales}')
print(highest_sale)
