### Part Four -- your code goes here. 
import random

numbers = [random.randint(1,100) for _ in range(10)]
print(f"The original list is: {numbers}")

odd_numbers = []

# This is a for loop that iterates over each number in the numbers list.
for num in numbers:
    if num % 2 != 0:
        # This checks to see if the current number is odd. The % returns the remainder of the divison of the current number by 2. If the remainder is not 0, the number is odd.
        odd_numbers.append(num)
        # This adds the odd number to the odd_numbers list.

print(f"List with only odd numbers: {odd_numbers}")

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
    else:
        i += 1

print(f"Original list after removing even numbers: {numbers}")
# This program creates a seperate list of odd numbers as well as a prints the original list without the even numbers. 