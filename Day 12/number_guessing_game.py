#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)

number = random.randint(0, 100)
mode = int(input("""
Choose difficulty levels (type 1 or 2) 
1: 10 guesses in easy mode
2: 5 guesses in hard mode.
                       """))

if mode == 1:
    difficulty = 10
else:
    difficulty = 5

guesses = 0

while(guesses < difficulty):
    guess = int(input("submit a guess for a number between 1 and 100: "))

    if guess == number:
        print("Wow you got it!")
        exit()
    
    elif guess < number:
        print("Your guess is lower")
        guesses += 1

    else:
        print("Your guess is higher")
        guesses += 1        