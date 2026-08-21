from art import logo,vs
from game_data import data
import random
score = 0
DATA_number =  random.randint(0,50)
restart = 0
nigga_value = 0
nick = True
while nick:
    print(logo)
    if restart == 2:
        DATA_number = random.randint(0, 50)
        restart = 0
    value = data[DATA_number]
    a_value_name = (value['name'])
    a_value_followers = (value['follower_count'])
    a_value_description = (value['description'])
    a_value_country = (value['country'])
    print(f"Compare A: {a_value_name}, a {a_value_description}, from {a_value_country}")
    print(vs)
    NEW_DATA_number =  random.randint(0,50)
    NEW_value = data[NEW_DATA_number]
    b_value_name = (NEW_value['name'])
    b_value_followers = (NEW_value['follower_count'])
    b_value_description = (NEW_value['description'])
    b_value_country = (NEW_value['country'])
    print(f"Compare B: {b_value_name}, a {b_value_description}, from {b_value_country}")


    ask = input("Who has more followers? Type 'A' or 'B':").lower()

    if ask == "a":
        if a_value_followers> b_value_followers:
            score += 1
            restart += 1
            print(f"You're right! Current score:{score}.")
        else:
            nick = False

    elif ask == "b":
        if a_value_followers < b_value_followers:
            score += 1
            print(f"You're right! Current score:{score}.")
            DATA_number = NEW_DATA_number
        else:
            nick = False

print("\n" * 20)
print(logo)
print(f"Sorry! that's wrong. Final score: {score}")

