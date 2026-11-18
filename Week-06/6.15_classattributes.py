
class Employee:
    company = "DataPulse Analytics"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display_info(self):
        print("\nCompany:", Employee.company)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

    def annual_bonus(self):
        bonus = self.salary * 0.10
        print("Annual Bonus:", bonus)


print("Enter information for Employee 1")
name1 = input("Name: ")
department1 = input("Department: ")
salary1 = float(input("Salary: "))

print("\nEnter information for Employee 2")
name2 = input("Name: ")
department2 = input("Department: ")
salary2 = float(input("Salary: "))

employee1 = Employee(name1, department1, salary1)
employee2 = Employee(name2, department2, salary2)

print("\n--- Employee 1 ---")
employee1.display_info()
employee1.annual_bonus()

print("\n--- Employee 2 ---")
employee2.display_info()
employee2.annual_bonus()
