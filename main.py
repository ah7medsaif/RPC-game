import random

choices = ["rock","paper","scissors"]

def play ():
    game_number = 0
    game_to_play = 0
    
    while game_to_play <= 0:
        try:
            game_to_play = int(input("how many games do you want to play? "))
        except:
            print("you must enter a number ")

    while game_number < game_to_play:
        game_number += 1
        
        print("*" * 30)
        print(f"Game{game_number} of {game_to_play}")
        print("*" * 30)
        
        user = input("please enter a choice 'rock ,paper ,scissors': ")
        while user not in choices:
            input("please enter a choice 'rock ,paper ,scissors': ")
    
        computer = random.choice(choices)       
        result = {"you" :user, "computer":computer }
        print(f" \n {result} \n ")
        
        check_win(user,computer)
        print()
    print("thanks for playing :) \n ")
    
def check_win(user,computer,gameover = False ):
    if not gameover:
        if user == "rock" and computer == "rock":
            print("it's a tie")
        elif user == "paper" and computer == "paper":
            print("it's a tie")
        elif user == "scissors" and computer == "scissors":
                print("it's a tie")
        elif user == "rock" and computer == "scissors":
            print("YOU WIN!!!")
        elif user == "paper" and computer == "rock":
            print("YOU WIN!!!")
        elif user == "scissors" and computer == "paper":
            print("YOU WIN!!!")
        else:
            print(" oooh YOU LOSE :( ")
            
play()





#made_by_AHMEDSAIF
