import art
from game_data import data
import random

print(art.logo)

def format_data(acoount):
    acoount_name = acoount["name"]
    acount_descr = acoount["description"]
    acount_country = acoount["country"]
    acount_follower = acoount["follower_count"]
    return f"{acoount_name},a {acount_descr}, from {acount_country}"

def check_answer(guess, follower_A, follower_b): 
        if follower_A > follower_B:
            return guess == "y"
        else:
            return guess == "n"

score = 0
game_continue = True
acoount_b = random.choice(data)

while game_continue:

    acoount_a = acoount_b
    acoount_b = random.choice(data)
    while acoount_a == acoount_b:
      random.choice(data)

    print(f"compare A : {format_data(acoount_a)}")
    print(art.vs)
    print(f"against B : {format_data(acoount_b)}")

    follower_A = acoount_a["follower_count"]
    follower_B = acoount_b["follower_count"]

    guess = input("Is option A have more follower than option B, type 'y' for yes, or type 'n' for no\n").lower()
    is_correct = check_answer(guess, follower_A, follower_B)

    if is_correct:
        score += 1
        print(f"You'r right! your score is {score}.")
        acoount_a = acoount_b
    else:
        print(f"You'r Wrong!, your final score is {score}")
        game_continue = False