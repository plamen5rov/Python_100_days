import os
from art import logo, vs 
from game_data import data
from random import randint

should_continue = True
COUNT = 0
random_range = len(data) - 1


while should_continue:
    compare_a = data[randint(0, random_range)]
    compare_b = data[randint(0, random_range)]
    right_answer = 'a'
    print(logo)
    if COUNT > 0:
        print(f"You're right! Score is {COUNT}")
        
    print(f"Compare A: {compare_a['name']}, {compare_a['description']} from {compare_a['country']}.\n")
    print(vs)
    print(f"Against B: {compare_b['name']}, {compare_b['description']} from {compare_b['country']}.\n")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if compare_b['follower_count'] > compare_a['follower_count']:
        right_answer = 'b'
    if guess == right_answer:
        COUNT += 1
    else:
        should_continue = False
    
os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
print(f"Sorry, that's wrong. Final score: {COUNT}")
    