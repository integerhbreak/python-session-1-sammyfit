# Task:
# Use type casting to safely perform division and print the result.

# Your code goes here

firstNum = int(input("Enter number: "))

numToDiv = int(input("Number to be divide by ?"))

if(numToDiv == 0):
    print("Zero not a valid number to divide")
else:
    result = firstNum/numToDiv
    print(f"Number: {firstNum} divided by {numToDiv} results in: ", result)