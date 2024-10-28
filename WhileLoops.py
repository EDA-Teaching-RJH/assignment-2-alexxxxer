### Part Two -- your code goes here. 
import random

secret_number = random.randint(1, 100)
attempts = 0

print("I am thinking of a number between 1 and 100!")
print("Guess the correct number!")

while True:
    try:
        guess = int(input("Enter your number: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Number is too low. Try again.")
        else:
            print("Number is too high. Try again.")

    except ValueError:
        print("Please enter a valid number.")