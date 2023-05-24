import random
l=["rock","paper","scissor"]
while True:
    Comcount=0  # Computer Count
    Usercount=0   # User Count
     # UserIput=>Ui
    ui=int(input('''   
    Game Start...
    1 Play Game
    2 No | Exit
    Enter Your choice:- '''))
    if ui==1:  # UserIput
        for a in range(1,6):
            userInput=int(input('''
            1 Rock
            2 Paper
            3 Scissor 
            Enter One Option:- '''))
            if userInput==1:
                uchoicce="rock"
            elif userInput==2:
                uchoicce="paper"
            elif userInput==3:
                uchoicce="scissor"
            computer=random.choice(l)
            if computer==uchoicce:  # User Choice=>uchoice
                print("Your Guess:-", uchoicce)
                print("Computer Guess:-", computer)
                print("Draw")
                # Usercount=Usercount+1
                # Comcount=Comcount+1
            elif (uchoicce=="rock" and computer=="scissor") or (uchoicce=="paper" and computer=="rock") or (uchoicce=="scissor" and computer=="paper"):
                print("Your Guess:-", uchoicce)
                print("Computer Guess:-", computer)
                print("You Win")
                Usercount=Usercount+1
            else:
                print("Your Guess:-", uchoicce)
                print("Computer Guess:-", computer)
                print("Computer win")
                Comcount=Comcount+1
        if  Usercount==Comcount:
                print("Computer Score:-",Comcount)
                print("Your Score:-",Usercount)
                print("The Final Result:- Game Draw🥲🤷‍♂️")
        elif Usercount>Comcount:
                print("Computer Score:-", Comcount)
                print("Your Score:-", Usercount)
                print("The Final Result:- You Win😍🤩")
        else:
                print("Computer Score:-", Comcount)
                print("Your Score:-", Usercount)
                print("The Final Result:- Computer Win😪")

    elif ui==2:
        break
    else:
        print("invalid Input")