# Task:
# Compare two variables using 'is' operator and print the result.

# Your code goes here

lsValues1 = [4, 6, 9]
lsValues2 = [4, 6, 9]

lsValues3 = lsValues2


if lsValues1 is lsValues2:
    print("Condition is True, lsValues1 is lsValues2")
elif lsValues3 is lsValues2:
    print("Condition is True, lsValues3 is lsValues2")
elif lsValues3 is lsValues1:
    print("Condition is True, lsValues3 is lsValues1")
