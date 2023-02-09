from random import randint

play = ["Rock", "Paper", "Scissors"]

computer = play[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
        else:
            print("You win", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose", computer, "cut", player)
        else:
            print("You win", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
        else:
            print("You win", player, "cut", computer)
    else:
        print("Incorrect spelling!")
    player = False
    computer = play[randint(0,2)]
