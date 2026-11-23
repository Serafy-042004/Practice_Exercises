
import os

filename = "interactions.txt"


if not os.path.exists(filename):

    try:
        with open(filename, "w") as file:
            file.write("Customer Interaction Log | Total Visits: 0\n")
            print("New customer log created.")

    except FileNotFoundError:
        print("Error: Could not create the customer log.")


customer_name = input("\nEnter customer name: ")
interaction = input("Enter customer interaction: ")

new_records = [
    f"Customer: {customer_name} | Interaction: {interaction}\n"
]


try:
    with open(filename, "a") as file:
        file.writelines(new_records)
        print("\nCustomer record added successfully.")

except FileNotFoundError:
    print("Error: Customer log file not found.")


try:
    with open(filename, "r") as file:
        content = file.read()

        print("\n--- Complete Customer Log ---")
        print(content)

except FileNotFoundError:
    print("Error: Customer log file not found.")


try:
    with open(filename, "r") as file:
        header = file.readline()

        print("--- Log Header ---")
        print(header)

except FileNotFoundError:
    print("Error: Customer log file not found.")


try:
    with open(filename, "r") as file:
        lines = file.readlines()

        total_entries = len(lines) - 1

        print("Total customer interactions:", total_entries)

        search_name = input("\nEnter customer name to search: ")

        print("\n--- Search Results ---")

        found = False

        for line in lines[1:]:
            if search_name.lower() in line.lower():
                print(line.strip())
                found = True

        if not found:
            print("No matching customer found.")

except FileNotFoundError:
    print("Error: Customer log file not found.")


try:
    with open(filename, "r+") as file:

        content = file.read()

        records = content.splitlines(keepends=True)

        updated_header = (
            f"Customer Interaction Log | Total Visits: {total_entries}\n"
        )

        file.seek(0)

        file.write(updated_header)
        file.writelines(records[1:])

        file.truncate()

        print("\nCustomer log header updated successfully.")

except FileNotFoundError:
    print("Error: Customer log file not found.")
