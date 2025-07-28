from art import logo,vs
import random
from game_data import data

count = 0
game_continue = True

print(logo)

def format_data(celebrity_data):
    name = celebrity_data["name"]
    description = celebrity_data["description"]
    country = celebrity_data["country"]

    return f"{name}, a {description}, from {country}"

def check_followers(a_followers, b_followers, user_answer):
    if a_followers > b_followers:
        if user_answer == "a":
            return True
    elif b_followers > a_followers:
        if user_answer == "b":
            return True
    else:
        return False

celebrity_b = random.choice(data)

while game_continue:
    celebrity_a = celebrity_b
    celebrity_b = random.choice(data)

    if celebrity_a == celebrity_b:
        celebrity_b = random.choice(data)

    formatted_a = format_data(celebrity_a)
    formatted_b = format_data(celebrity_b)

    celebrity_a_followers = celebrity_a["follower_count"]
    celebrity_b_followers = celebrity_b["follower_count"]

    print(celebrity_a_followers)
    print(celebrity_b_followers)

    print(f"A = {formatted_a}")
    print(vs)
    print(f"B = {formatted_b}")
    print()

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 50)
    print(logo)

    result = check_followers(celebrity_a_followers, celebrity_b_followers, answer)

    if result:
        count += 1
        print(f"Right! Score = {count}")
    else:
        game_continue = False
        print(f"Wrong! Score = {count}")