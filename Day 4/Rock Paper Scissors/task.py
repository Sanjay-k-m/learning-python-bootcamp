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
hand_symbols = [rock,paper,scissors]

generate_random_symbol_index = random.randint(0,len(hand_symbols)-1)


player_choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))



print(f"Your choice : \n {hand_symbols[player_choice]}")

print(f"Computer choice :\n {hand_symbols[generate_random_symbol_index]}")

if player_choice == 0 and generate_random_symbol_index == 2:
    print("You Win ...")
elif player_choice == 2 and generate_random_symbol_index == 0:
    print("Computer Win ...")
elif player_choice == 1 and generate_random_symbol_index == 0:
    print("You Win ...")
elif player_choice == 0 and generate_random_symbol_index == 1:
    print("Computer Win ...")
elif player_choice == 2 and generate_random_symbol_index == 1:
    print("You Win ...")
elif player_choice == 1 and generate_random_symbol_index == 2:
    print("Computer Win ...")
else :
    print("Tie ...")

