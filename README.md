# Adventure Game
This is a simple text-based adventure game where you explore different rooms and make choices to progress through the game. The game incorporates randomness to introduce variation in each playthrough.
Functions
start_game()
This function initiates the game and presents the player with the first room. The player is prompted to choose a door and proceed to the corresponding room.

room_1()
This function represents the first room in the game. The player can choose to either take the key or leave it. The choice determines the outcome and leads to the next room.

room_2()
This function represents the second room in the game. The player encounters a treasure chest and has the option to open it or ignore it. The choice affects the outcome and the player's score.

increase_score(points)
This function increases the total score by the given number of points. It is called when the player successfully finds and obtains a treasure.

decrease_score(points)
This function decreases the total score by the given number of points. It is called when the player chooses to ignore the treasure chest, with a chance of a score decrease.

play_again()
This function asks the player if they want to play again. If the player chooses to play again, the score is reset, and the game starts from the beginning. If the player chooses not to play again, the game ends with a farewell message.

reset_score()
This function resets the total score to zero. It is called when the player chooses to play the game again.

Randomness
The game incorporates randomness in the room_2() function. When the player chooses to ignore the treasure chest, there is a 50% chance that the game will either deduct 5 points from the score or nothing will happen.

Have fun playing the Adventure Game!
