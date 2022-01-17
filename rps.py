rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("Welcome to rock, paper, scissors game!!")
option = int(input("For rock press 0, for paper press 1 for scissors press 2, "))
rps = [rock, paper, scissors]
compchoice = random.randint(0, 2)

if option == 0 :
    print(rock)
if option == 1:
    print(paper)
if option == 2:
    print(scissors)
if option >= 3 or option < 0:
        print("you typed an invalid number")
else:
        print("computer chose:")

        if compchoice == 0:
            print(rock)
        if compchoice == 1:
            print(paper)
        if compchoice == 2:
            print(scissors)

        if option ==2 and compchoice==0:
            print(" You lose.")
        elif compchoice==2 and option==0:
            print("You win!!")
        elif compchoice > option:
            print("You lose")
        elif option > compchoice:
            print("you win!!")
        elif compchoice == option:
            print("its a draw")

