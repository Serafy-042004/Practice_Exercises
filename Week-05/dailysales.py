
# Task 1: Create variables
day = 1

monday = 1200
tuesday = 1500
wednesday = 1100
thursday = 1800
friday = 1400

total_sales = 0

# Task 2: Create a while loop
while day <= 5:

    if day == 1:
        total_sales += monday

    elif day == 2:
        total_sales += tuesday

    elif day == 3:
        total_sales += wednesday

    elif day == 4:
        total_sales += thursday

    elif day == 5:
        total_sales += friday

    # Move to the next day
    day += 1

# Task 3: Calculate sales
average_sales = total_sales / 5

# Display results
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Daily Sales: ${average_sales:,.2f}")


# Define daily sales
daily_sales = [1200, 1500, 1100, 1800, 1400]

# Initialize total sales
total_sales = 0

# Calculate total sales using a for loop
for sales in daily_sales:
    total_sales += sales

# Calculate average daily sales
average_sales = total_sales / len(daily_sales)

# Display results
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Daily Sales: ${average_sales:,.2f}")
