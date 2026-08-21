from art import logo
print(logo)
import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
ASKING_DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
random_number = random.randint(1,100)
nick = True
def easy(attempts):
    global random_number,nick
    while nick:
        guess = int(input("Make a guess: "))
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            nick = False
        elif random_number == guess:
            print("You won")
            nick = False
        elif random_number > guess:
            print(f"Too low\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
        elif random_number < guess:
            print(f"Too high\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
if ASKING_DIFFICULTY == "easy":
    easy(10)
else:
    easy(5)


