# Task:
# Check if an element exists in a list using 'in' operator and print the result.

# Your code goes here

list = [5, 4, 3, 2, 6]
valueToFind = int(input("enter number to find ? "))

if valueToFind in list:
    print(f"{valueToFind} present in {list}")
else:
    print(f"{valueToFind} is not present in {list}")