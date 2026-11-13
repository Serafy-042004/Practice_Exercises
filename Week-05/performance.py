name = str(input('Whats your name: '))
number_1 = eval(input('Enter your employee score: '))

print()
print(f"Employee Name: {name}")
print(f"Performance Score: {number_1}")

if(number_1 >= 90) : 
    print("Outstanding")
elif(number_1 >= 80): 
    print('Exceeds Expectations')
elif(number_1 >= 70):
    print('Meets Expectations')
elif(number_1 >= 60):
    print('Below Expectations')
else :
    print('Unsatisfcatory')