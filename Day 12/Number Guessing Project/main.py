import art
import random


def game():
    life = 0
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1,2)
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Ty pe 'easy' or 'hard': ")
    if level == "easy":
        life = 10
    else:
        life = 5
    while life != 0:
        guss = int(input("Make a guess:"))
        if guss == number:
            print("You win ....")
            print(f"Remining Life {life}")
            user_dec = input("Do you want to continue 'yes' or 'no' : ")
            if user_dec == 'yes':
                game()
        elif guss > number:
            print("Guss is too High")
            life -= 1
            print(f"Remining Life {life}")

        else:
            print("Guss is too low")
            life -= 1
            print(f"Remining Life {life}")

    if life == 0 :
        print("You Lose....")
    user_dec = input("Do you want to continue 'yes' or 'no' : ")
    if user_dec == 'yes':
        game()
game()