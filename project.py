def start_game():
    print("Welcome to the Adventure Game!")
    print("You wake up in a dark room. What do you do?")
    print("1. Look for a light switch")
    print("2. Scream for help")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You find a light switch and turn it on.")
        room_1()
    elif choice == "2":
        print("No one hears your screams.")
        game_over()
    else:
        print("Invalid choice. Try again.")
        start_game()


def room_1():
    print("You are now in a well-lit room.")
    print("There are two doors in front of you.")
    print("1. Take the left door")
    print("2. Take the right door")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You enter the left door and find a treasure chest!")
        print("Congratulations! You win!")
    elif choice == "2":
        print("You enter the right door and are attacked by a monster.")
        game_over()
    else:
        print("Invalid choice. Try again.")
        room_1()


def game_over():
    print("Game over. Would you like to play again?")
    play_again = input("Enter 'yes' to play again, or 'no' to quit: ")

    if play_again.lower() == "yes":
        start_game()
    else:
        print("Thank you for playing!")


start_game()
