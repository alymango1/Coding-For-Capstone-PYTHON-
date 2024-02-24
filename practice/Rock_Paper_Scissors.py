import random
import time

def lost():
    print("You lost!")

def won():
    print("You won!")


def tie():
    print("You tied!")


RockPaperScissors = True
print("Welcome to Rock, Paper, Scissors ")
round = 1
ai_score = 0
user_score = 0

while RockPaperScissors:

    print(f'Round {round}')
    time.sleep(0.5)
    print(f'Your score: {user_score}')
    time.sleep(0.5)
    print(f"AI score: {ai_score}")
    time.sleep(0.5)
    user_choice = input("Pick your choice: ").lower()
    list_of_choices = ["rock", "paper", "scissors"]
    ai = random.choice(list_of_choices)

    if round < 5:
        if user_choice not in list_of_choices:
            print("Only rock, paper, and scissors!")
        elif user_choice == "rock" and ai == "paper":
            time.sleep(0.5)
            print(f'The ai chose {ai}!')
            time.sleep(0.5)
            lost()
            ai_score += 1
            round += 1

        elif user_choice == "paper" and ai == "scissors":
            time.sleep(0.5)
            print(f'The ai chose {ai}!')
            time.sleep(0.5)
            lost()
            ai_score += 1
            round += 1
        elif user_choice == "scissors" and ai == "rock":
            time.sleep(0.5)
            print(f'The ai chose {ai}!')
            time.sleep(0.5)
            lost()
            ai_score += 1
            round += 1
        elif user_choice == "rock" and ai == "scissors":
            time.sleep(0.5)
            print(f'The ai chose {ai}!')
            time.sleep(0.5)
            won()
            user_score += 1
            round += 1
        elif user_choice == "paper" and ai == "rock":
            time.sleep(0.5)
            print(f'The ai chose {ai}!')
            time.sleep(0.5)
            won()
            user_score += 1
            round += 1
        elif user_choice == "scissors" and ai == "paper":
            time.sleep(0.5)
            print(f'The ai chose {ai}!')
            time.sleep(0.5)
            won()
            user_score += 1
            round += 1
        else:
            time.sleep(0.5)
            print(f'The ai chose {ai}!')
            time.sleep(0.5)
            tie()
            user_score += 0.5
            ai_score += 0.5
            round += 1
    elif round == 5:
        if ai_score > user_score:
            print("You lost to a bot")
            print(f'Your score: {user_score}')
            time.sleep(0.5)
            print(f"AI score: {ai_score}")
            time.sleep(0.5)
            break
        elif user_score > ai_score:
            print("You won!!! Congrats!")
            print(f'Your score: {user_score}')
            time.sleep(0.5)
            print(f"AI score: {ai_score}")
            time.sleep(0.5)
            break
        else:
            print("You tied!")
            print(f'Your score: {user_score}')
            time.sleep(0.5)
            print(f"AI score: {ai_score}")
            time.sleep(0.5)
            break



