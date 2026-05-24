import random
import os

print("Welcome to number guessing game...")

def guess_num():

    print("\nComputer selected a number")
    print("You have to guess it...")

    org_num = random.randint(1, 100)
    try:
        user_num = int(input("\nGuess the number: "))
    except ValueError:
        os.system("cls")
        print("\nEnter a valid number!\nRestarting the game...")
        guess_num()
        return
    attempts = 1

    try:
        while org_num != user_num:
            if org_num > user_num:
                user_num = int(input(f"Guess higher than {user_num}: "))
            elif org_num < user_num:
                user_num = int(input(f"Guess lower than {user_num}: "))
            attempts += 1
    except ValueError:
        os.system("cls")
        print("\nEnter a valid number!\nRestarting the game...")
        guess_num()
        return
    
    print(f"\nCorrect! The number was {org_num}")
    print(f"Your attempts - {attempts}\n")
    print("Do you want to play again?")

guess_num()

def re_play():
    replay = input("Type y for 'Yes' and n for 'No' : ").lower()

    if replay == "y":
        os.system("cls")
        guess_num()
        re_play()
    elif replay == "n":
        print("\nThanks for playing")
        exit()
    else:
        print("\nEnter a valid argument!")
        print("Do you want to play again?")
        re_play()

re_play()

