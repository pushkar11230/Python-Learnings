'''

How It Works

The program:

1. Shows random numbers for a few seconds
2. Hides them
3. User types what they remember
4. Program checks accuracy
5. Difficulty increases every round
6. Give them score

'''


import random
import os
import time

def main_code():
    # Instructions
    print("You will see a random number for few seconds.")
    print("You have to remember that number and then enter what you remembered.")
    input("Press Enter when you are ready: \n")

    # difficulty levels
    difficulties = {
        "Level 1: Easy -> 3 digits number": [100, 999],
        "Level 2: Medium -> 4 digits number": [1000, 9999],
        "Level 3: Hard -> 5 digits number": [10000, 99999],
        "Level 4: Very Hard -> 6 digits number": [100000, 999999],
        "Level 5: Pro -> 7 digits number": [1000000, 9999999],
        "Level 6: Extreme -> 8 digits number": [10000000, 99999999]
    }

    # score counting
    score = 0
    
    for level in difficulties:
        # showing the round
        print(level)
        time.sleep(2)
        
        limit = difficulties[level]

        # choosing a random number
        rand_num = random.randint(limit[0], limit[1])

        # printing the random number only for few seconds
        print(rand_num)
        time.sleep(3)
        os.system("cls")
        
        # taking user input
        try:
            user_input = int(input("Enter the number: "))
        except ValueError:
            print("Error! You did not entered a number.")
            break

        # checking the number
        if rand_num == user_input:
            print("Correct")
            score += 10
            if level != "Level 6: Extreme -> 8 digits number":
                input("\nPress Enter to go in next round: \n")
                os.system("cls")
        else:
            print("Wrong!")
            print(f"The number was: {rand_num}")
            print(f"You entered: {user_input}")
            break

    print(f"\nYour score: {score}")

def replay_system():
    print("Do you want to play again?")
    play = input("Type 'y' for Yes and 'n' for No: ").lower()

    if play == "y":
        os.system("cls")
        game_code()
    elif play == "n":
        print("Thanks for playing...")
        input()

def game_code():
    main_code()
    replay_system()

game_code()
