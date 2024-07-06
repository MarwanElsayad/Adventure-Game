import time
import random

def start_game():
    print("Welcome to the Adventure Game!")
    print("You are in a dark room. There are two doors in front of you.")
    print("Which door do you choose? (1 or 2)")

    choice = input("> ")

    if choice == "1":
        room_1()
    elif choice == "2":
        room_2()
    else:
        print("Invalid input. Please try again.")
        start_game()

def room_1():
    print("You entered room 1.")
    time.sleep(1)
    print("There is a key on the table.")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)
    print("1. Take the key.")
    print("2. Leave it.")

    choice = input("> ")

    if choice == "1":
        print("You took the key. You can proceed to the next room.")
        time.sleep(1)
        room_2()
    elif choice == "2":
        print("You left the key behind, but you can still proceed to the next room.")
        time.sleep(1)
        room_2()
    else:
        print("Invalid input. Please try again.")
        room_1()

def room_2():
    print("You entered room 2.")
    time.sleep(1)
    print("There is a treasure chest in the corner.")
    time.sleep(1)
    print("What do you do?")
    time.sleep(1)
    print("1. Open the chest.")
    print("2. Ignore it.")

    choice = input("> ")

    if choice == "1":
        print("Congratulations! You found a treasure!")
        time.sleep(1)
        increase_score(10)
        play_again()
    elif choice == "2":
        print("You chose to ignore the chest. The game is over.")
        time.sleep(1)
        decrease_score(5)
        play_again()
    else:
        print("Invalid input. Please try again.")
        room_2()

def increase_score(points):
    global total_score
    total_score += points
    print(f"Score increased by {points}. Your total score is now: {total_score}.")

def decrease_score(points):
    global total_score
    total_score -= points
    print(f"Score decreased by {points}. Your total score is now: {total_score}.")

def play_again():
    print("Do you want to play again? (yes or no)")

    choice = input("> ")

    if choice.lower() == "yes":
        reset_score()
        start_game()
    elif choice.lower() == "no":
        print("Thank you for playing!")
    else:
        print("Invalid input. Please try again.")
        play_again()

def reset_score():
    global total_score
    total_score = 0

total_score = 0
start_game()
