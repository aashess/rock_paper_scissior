import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissior = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''


#take input
choice = input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.")

user_choice = int(choice)
computer_choice = random.randint(0,2)

print("\n\n")

#condition for displaying input of user
if user_choice == 0:
    print(f"----rock----\n{rock}")

elif user_choice == 1:
    print(f"----paper----\n{paper}")
else:
    print(f"----scissior----\n{scissior}")
print("\n\n")

#condition for displaying input of computer
if computer_choice == 0:
    print(f"---rock--\n{rock}")

elif computer_choice == 1:
    print(f"----paper----\n{paper}")
else:
    print(f"----scissior----\n{scissior}")


print("\n\n")

if user_choice != computer_choice:
    if user_choice == 0 and computer_choice == 1:
        print("You lost")
    elif user_choice == 0 and computer_choice == 2:
        print("You won")
    elif user_choice == 1 and computer_choice == 0:
        print("You won")
    elif user_choice == 1 and computer_choice == 2:
        print("You lost")
    elif user_choice == 2 and computer_choice == 0:
        print("You lost")
    else:
        print("You won")
else:
    print("Try again Both of You selected same value.")

