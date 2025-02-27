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
#Refer to Angela's lesson for more sophisticated way of creating this code.

import random

my_choice = int(input("Pick an integer. 0 for rock, 1 for paper, or 2 for scissors.\n"))

if my_choice == 0:
    print(rock)
elif my_choice == 1:
    print(paper)
elif my_choice == 2:
    print(scissors)

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

print(my_choice)
print(computer_choice)

if my_choice == 0 and computer_choice == 2:
    print("You win.")
elif my_choice == 0 and computer_choice == 1:
    print("You lose.")
elif my_choice == 1 and computer_choice == 0:
    print("You win.")
elif my_choice == 1 and computer_choice == 2:
    print("You lose.")
elif my_choice == 2 and computer_choice == 1:
    print("You win.")
elif my_choice == 2 and computer_choice == 0:
    print("You lose.")
elif my_choice == computer_choice:
    print("It's a tie. Go again.")
else:
    print("You lose.")
