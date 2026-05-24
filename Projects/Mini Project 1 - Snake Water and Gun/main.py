import random
import os

def game_code():
    random_num = random.randint(1, 3)

    # Computer's turn: Snake(s), Water(w), Gun(g)
    if random_num == 1:
        computer = "s"
    elif random_num == 2:
        computer = "w"
    else:
        computer = "g"

    print("Computer already selected.")

    print("Now your turn: Type 's' for Snake, 'w' for Water, 'g' for Gun")
    user = input("Your turn: ").lower()

    def game_winner(user, computer):
        if user == computer:
            return None

        # Snake vs Gun
        if user == "s" and computer == "g":
            return False
        elif user == "g" and computer == "s":
            return True
        # Gun vs Water
        if user == "g" and computer == "w":
            return False
        elif user == "w" and computer == "g":
            return True
        # Water vs Snake
        if user == "w" and computer == "s":
            return False
        elif user == "s" and computer == "w":
            return True
        else:
            os.system("cls")
            print("Enter a valid argument!")
            print("Restarting the game...\n")
            game_code()
            re_play()
            return

    names = {
        "s": "Snake",
        "w": "Water",
        "g": "Gun"
    }

    result = game_winner(user, computer)  # Returns True if user won, False if user lost, None if its a draw

    print(f"\nYou chose - {names[user]} \n")
    print(f"Computer chose - {names[computer]} \n")

    if result is None:
        print("It's a tie!")
    elif result is True:
        print("You won!")
    elif result is False:
        print("You lost!")

    print("\nDo you want to play again?")
    

def re_play():
    replay = input("Type 'y' for Yes and 'n' for No: ").lower()

    if replay == "y":
        os.system("cls")
        game_code()
        re_play()
        return
    elif replay == "n":
        exit()
    else:
        os.system("cls")
        print("Enter a valid argument!")
        print("Do you want to play again?")
        re_play()
    

game_code()

re_play()

