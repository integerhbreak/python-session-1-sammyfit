# Task:
# Swap two variables without using a temporary variable.

# Your code goes here
previous_location = 'UK'
current_location = 'India'
print(f'I was in {previous_location} and moved back to {current_location} 2 years ago.')

# Swap previus and curren location without using temporary variable 
# Hind - multiple variable assignment

previous_location, current_location = current_location, previous_location

print(f'I was in {previous_location} and moved back to {current_location} 2 years ago.')