# Task:
# Combine conditions using 'and' operator and print the result.

# Your code goes here

iNum1 = int(input("Enter first number: "))
iNum2 = int(input("Enter second number: "))

if((iNum1 > iNum2) and iNum1 > 100):
    print(f"Number {iNum1} is greater than {iNum2} and has a value more than 100")
elif((iNum1 > iNum2) and iNum1 < 100):
    print(f"Number {iNum1} is greater than {iNum2} and has a value less than 100")