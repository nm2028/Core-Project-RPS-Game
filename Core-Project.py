import time
import random
#Instructions
print("Welcome to Nikhil Mishra Gaming:")
print("----- ROCK, PAPER & SCISSOR -----")
time.sleep(1)
print("Dont use any other format than this:")
time.sleep(1.5)
print("A- For ROCK use 'rock' or 'r' or 'R' ")
time.sleep(1.5)
print("B- For PAPER use 'paper' or 'p' or 'P' ")
time.sleep(1.5)
print("C- For SCISSOR use 'scissor' or 's' or'S'")
time.sleep(1.5)


def statement():
    #Taking User Input
    print("Enter your choice Rock, Paper or Scissor : ")
    choice = input()
    choose = ["R", "P", "S"]
    #Making the Computer Choose
    comp = random.choice(choose)
    return choice, comp


def game():
    i = 1
    comw = 0
    youw = 0
    while i <= 100:
        print()
        print(" Round:")
        user, com = statement()
        #Determine a Winner, Loser or a Tie
        if (user == "rock" or user == "r") or user == "R":
            if com == "R":
                print("--TIED--")
                print()
                break
            elif com == "P":
                print("--YOU-LOSE--")
                comw = comw + 1
                print()
                break
            elif com == "S":
                print("--YOU-WIN--")
                youw = youw + 1
                print()
                break
            else:
                print("Sorry you used illegal format!!")
                print()
                break
        if (user == "paper" or user == "p") or user == "P":
            if com == "P":
                print("--TIED--")
                print()
                break
            elif com == "S":
                print("--YOU-LOSE--")
                print()
                comw = comw + 1
                break
            elif com == "R":
                print("--YOU-WIN--")
                youw = youw + 1
                print()
                break
            else:
                print("Sorry you used illegal format!!")
                print()
                break
        if (user == "scissor" or user == "s") or user == "S":
            if com == "S":
                print("--TIED--")
                print()
                break
            elif com == "R":
                print("--YOU-LOSE--")
                comw = comw + 1
                print()
                break
            elif com == "P":
                print("--YOU-WIN--")
                youw = youw + 1
                print()
                break
            else:
                print("Sorry you used illegal format!!")
                print()
                break
    #Play Again
    print("Do you want to play again!!")
    time.sleep(0.6)
    stop = input("y=yes  and n=no  :")
    if stop == "y":
        game()
    else:
        exit()
game()


