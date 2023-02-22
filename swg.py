import random

#Score Shower result
def score(user,computer):
    print("Your Score is ",user," Computer Score is ",computer)
# Result checking function 
def result(computer_choice,user_choice):
    winner=-1
    if computer_choice=="w" and user_choice=="g":
        winner=0
    elif computer_choice=="w" and user_choice=="s":
        winner=1
    elif computer_choice=="s" and user_choice=="w":
        winner=0
    elif computer_choice=="s" and user_choice =="g":
        winner=1
    elif computer_choice=="g" and user_choice=="s":
        winner=0
    elif computer_choice=="g" and user_choice=="w":
        winner=1
    else:
        winner=-1
    return winner
# Game variable fhgdfgjffdhdfdhg
game_input=['s','w','g']
# Game loop
print("WELCOME TO THhk WATER GUN GAME  ---- Created by Puneet Dwivedi\n")
game=input("To start game press any button")
while game != 'exit':
    total_turn=10
    computer_socre=0
    user_score=0
    while total_turn > 0:   
        user=input("Enter 'S' for Snake 'W' for Water and 'G' for Gun ")
        computer=random.choice(game_input)
        turn_result=result(computer,user)
        if turn_result==0:
            computer_socre=computer_socre+1
            score(user_score,computer_socre)
            print("Computer Score!!!!")
        elif turn_result==1:
            user_score=user_score+1
            score(user_score,computer_socre)
            print("You Scored!!!!")
        else:
            score(user_score,computer_socre)
            print("No Result!!!!")
        total_turn=total_turn-1
    #Game winner
    if(computer_socre>user_score):
        score(user_score,computer_socre)
        print("SORRY! COMPUTER WINS")
    elif(user_score>computer_socre):
        score(user_score,computer_socre)
        print("CONGRATULATION! YOU WINS")
    else:
        score(user_score,computer_socre)
        print("GAME IS DRAW NO RESULT")
    game=input("Press any button to play again")







