import random
from enum import nonmember

import art
import game_data



def display_question(option_a,option_b):
    print(art.logo)
    print(f"{game_data.data[option_a]["name"]} {game_data.data[option_a]["description"]} {game_data.data[option_a]["country"]} ")
    print(art.vs)
    print(f"{game_data.data[option_b]["name"]} {game_data.data[option_b]["description"]} {game_data.data[option_b]["country"]} ")



def generate_random_person(option_a,option_b):
    option_a = option_b
    if option_a == 0:
        option_a =  random.randint(0,len(game_data.data)-1)
    option_b=random.randint(0 ,len(game_data.data)-1)
    # while not option_b == option_a:
    #     option_b=random.randint(0 ,len(game_data.data)-1)
    return [option_a,option_b]

def compare_these_person(option_a,option_b):
    # print(option_a,option_b)
    if game_data.data[option_a]["follower_count"] > game_data.data[option_b]["follower_count"]:
        # print("option_a higher")
        return "a"
    elif  game_data.data[option_a]["follower_count"] < game_data.data[option_b]["follower_count"]:
        return "b"
    else:
        print("Tie...")
        return "Tie"
def game_continue():
    option_a=0
    option_b=0
    score =0
    game = False
    while not game:


        result = generate_random_person(option_a, option_b)
        print("result",result)
        option_a = result[0]
        option_b = result[1]
        display_question(option_a,option_b)
        result = compare_these_person(option_a,option_b)
        # print(option_a,option_b)
        user_input = input("Please Select A or B :").lower()
        if result == user_input:
            score += 1
            print(score,"IS YOUR SCORE ....")
        else:
            print("You Lose ....")
            print(f"Your Score {score}")
            user_input = input("Do You want to Continue : ( y /N )").lower()
            if user_input == "y":
                score = 0
                option_b =0
                option_a = 0
            else:
                print("Great Game ........... ")
                game = True
game_continue()