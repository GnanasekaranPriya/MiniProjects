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

#Write your code below this line 👇
import random
computer_pick = random.randint(0,2)
if computer_pick == 0: 
    print(rock)
elif computer_pick == 1: 
    print(paper)
else: 
    print(scissors)

    

user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))

if user_pick == 0: 
    print(rock)
elif user_pick == 1: 
    print(paper)
else: 
    print(scissors)

if (user_pick == 0 and computer_pick == 1) or (user_pick == 1 and computer_pick == 0): 
    if user_pick == 1:
        print("User Wins")
    else: 
        print("Computer Wins")

elif (user_pick == 1 and computer_pick == 2) or (user_pick == 2 and computer_pick == 1): 
    if user_pick == 2:
        print("User Wins")
    else: 
        print("Computer Wins")
    
elif (user_pick == 0 and computer_pick == 2) or (user_pick == 2 and computer_pick == 0): 
    if user_pick == 0:
        print("User Wins")
    else: 
        print("Computer Wins")

else: 
    print("You tied!")



