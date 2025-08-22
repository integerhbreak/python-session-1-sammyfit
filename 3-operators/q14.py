# Task:
# Combine conditions using 'or' operator and print the result.

# Your code goes here

iNum1 = int(input("Enter first number: "))
iNum2 = int(input("Enter second number: "))

if(iNum1 > 10 or iNum2 < 5):
    print(f"True as either - Number {iNum1} is greater than 10 or {iNum2} is less than 5")
elif(iNum1 < 10 or iNum2 > 5):
    print(f"True as either - Number {iNum1} is less than 10 or {iNum2} is greater than 5")