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


selection_array = [rock, paper, scissors]
computer_chose = random.randint(1, 3)
selection = input("Please choose Rock, Paper, or Scissors\n").lower()

if selection == "rock":
  print("You chose Rock!")
  print(selection_array[0])
  if computer_chose == 2:
    print(selection_array[1])
    print("Computer chose Paper :( you lost my friend")
  elif computer_chose == 3:
    print(selection_array[2])
    print("Computer chose scissors! You smashed him")
  else:
    print(selection_array[0])
    print("Its a draw!")
elif selection == "paper":
  print("You chose paper!")
  print(selection_array[1])
  if computer_chose == 3:
    print(selection_array[2])
    print("Computer chose Scissors :( you lost my friend")
  elif computer_chose == 1:
    print(selection_array[0])
    print("Computer chose rock! You covered him!")
  else:
    print(selection_array[1])
    print("Its a draw!")
elif selection == "scissors":
  print("You chose scissors!")
  print(selection_array[2])
  if computer_chose == 1:
    print(selection_array[0])
    print("Computer chose Rock :( you lost my friend")
  elif computer_chose == 2:
    print(selection_array[1])
    print("Computer chose paper! You cut him!")
  else:
    print(selection_array[2])
    print("Its a draw!")

