import random

from art import logo, vs
from game_data import data

print(logo)

def get_data():
    fl_1 = data[random.randint(0, len(data)-1)]
    fl_2 = data[random.randint(0, len(data)-1)]

    while fl_1 == fl_2:
        fl_2 = data[random.randint(0, len(data)-1)]

    return fl_1, fl_2

def print_menu(fl_1, fl_2):
    print(f"Compare A: {fl_1['name']}, a {fl_1['description']}, from {fl_1['country']}")
    print(vs)
    print(f"Compare B: {fl_2['name']}, a {fl_2['description']}, from {fl_2['country']}")

    guess = input("Who has more followers? (A or B): ")
    return guess

def get_higher(fl_1, fl_2):
    follow_A = fl_1['follower_count']
    follow_B = fl_2['follower_count']
    higher = ''

    if(follow_A > follow_B):
        higher = 'A'

    else:
        higher = 'B'
    
    return higher


def game():
    score = 0

    print("Welcome to the guessing game. Keep guessing who has the most followers until you lose!")

    fl_1, fl_2 = get_data()
    higher = get_higher(fl_1, fl_2)

    guess = print_menu(fl_1, fl_2)

    while(guess == higher):
        score += 1
        print(f"You are right! Current score: {score}")

        fl_1, fl_2 = get_data()
        higher = get_higher(fl_1, fl_2)

        guess = print_menu(fl_1, fl_2)    

    print(f"Wrong! Your game ends with a score of {score}")    


game()