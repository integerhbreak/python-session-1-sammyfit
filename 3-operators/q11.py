# Task:
# Use > and < operators to compare numbers and print the results.

# Your code goes here

iNum1 = int(input("Enter first number: "))
iNum2 = int(input("Enter second number: "))

if(iNum1 > iNum2):
    print(f"Number {iNum1} is greater {iNum2}")
elif(iNum1 < iNum2):
    print(f"Number {iNum1} is less than {iNum2}")
else:
    print(f"Numbers {iNum1} and {iNum2} are same")