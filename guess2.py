print("Welcome to the Number Guessing Game!")
print("Player 1: Please think of a number between 1 and 100.")

# Player 1 enters the target number
while True:
    try:
        target_number = int(input("Enter the target number (1-100): "))
        if 1 <= target_number <= 100:
            break
        else:
            print("Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Clear the screen (optional) to hide the target number from Player 2
print("\n" * 50)  # Prints 50 blank lines to "clear" the screen

print("Player 2: Now it's your turn to guess the number!")
attempts = 0

# Player 2 guesses the number
while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")