import random

user_action = input("Enter rock, paper or scissors: ")

possible_actions = ["rock", "paper", "scissors"]

while True:
    user_action = input("Enter rock, paper or scissors: ")

    computer_action = random.choice(possible_actions)

    if user_action == 'rock':
        if computer_action == 'rock':
            print("Its a tie")
        elif computer_action == 'paper':
            print("you lost")
        
        elif computer_action == 'scissors':
            print("you won!!!")
            again = input("Do you want to play again(y/n)?: ")
            if again == 'y':
                continue
            else:
                break



    if user_action == 'paper':
        if computer_action == 'paper':
            print("Its a tie")
        elif computer_action == 'scissors':
            print("you lost")
        
        elif computer_action == 'rock':
            print("you won!!!")
            again = input("Do you want to play again(y/n)?: ")
            if again == 'y':
                continue
            else:
                break


    if user_action == 'scissors':
        if computer_action == 'scissors':
            print("Its a tie")
        elif computer_action == 'rock':
            print("you lost")
        
        elif computer_action == 'paper':
            print("you won!!!")
            again = input("Do you want to play again(y/n)?: ")
            if again == 'y':
                continue
            else:
                break





        
