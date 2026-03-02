import random
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

Choices = [rock, paper, scissors]

playerChoice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
print("You chose: ")
print(Choices[int(playerChoice)])

if playerChoice == '0':
    computerChoice = random.choice(Choices)
    (print("Computer chose: "))
    print(computerChoice)
    if computerChoice == rock:
        print("Draw")
    elif computerChoice == paper:
        print("You lose")
    else:
        print("You win")

elif playerChoice == '1':
    computerChoice = random.choice(Choices)
    (print("Computer chose: "))
    print(computerChoice)
    if computerChoice == rock:
        print("You win")
    elif computerChoice == paper:
        print("Draw")
    else:
        print("You lose")

elif playerChoice == '2':
    computerChoice = random.choice(Choices)
    (print("Computer chose: "))
    print(computerChoice)
    if computerChoice == rock:
        print("You lose")
    elif computerChoice == paper:
        print("You win")
    else:
        print("Draw")
