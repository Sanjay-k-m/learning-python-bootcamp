game_over = False
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
import random


def print_output():
    print(f"player_card : {player_cards} and your score is : {sum(player_cards)}")
    print(f"computer_card : {computer_cards} and your score is : {sum(computer_cards)}")

def first_card_generate():
    for i in range (2):
        player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    print_output()
def generate_computer_card():
    for i in range(random.randint(0,5)):
        computer_cards.append(random.choice(cards))
    print_output()
while not game_over:
    hit = True
    print(art.logo)
    continue_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    first_card_generate()

    while hit:
        hit_or_pass = input("Type 'y' to get another card, type 'n' to pass:")
        if hit_or_pass == "n":
            generate_computer_card()
            if sum(player_cards) == sum(computer_cards):
                print("Draw ..... 🥲")
                print_output()
            elif sum(player_cards) < sum(computer_cards):
                print("computer win...")
            else:
                print("Player Winn .....")
            hit = False
        else:
            player_cards.append(random.choice(cards))
            if sum(player_cards) > 21 :
                print("You Lost 🥲")
                hit = False
            print_output()
    if continue_or_not == "n":
        game_over = True