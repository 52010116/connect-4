# Design #

## Implementation of what happens before the game ##

* We tried to keep the start screen as simple as possible, therefore we used the print function and implemented it to the main function.
* At first the start screen displays the question if the player wants to play vs Ai (1) or another player (2). The answer is stored in a variable p. If p is not 1 or 2 or an Integer, an error message will be displayed.
* As soon as the player made a choice, it is displayed what kind of game the player is playing and how to quit the game.

## Implementation of the game ##

* The playing field is displayed with the “_” symbol. Underneath the field the columns 0-6 are displayed. It is stored in a list.
* In order to give the player the option to exit the game at any time, the “exit_game” was created, which checks input for “q” or “Q”. 
* With the intention of letting the player only make valid inputs, “check_legal_move” was created to check if input is an Integer, if its between 0-6, and if the column is already filled.
* If the input is valid “set_move” puts the symbol in the chosen column. The symbols stack up on each other until the column is full.
* After every move “check_win” examines if one party has won. It checks vertically, horizontally and diagonally.
* The “ai_move” method is a very simple AI which generates a random number between 0-6 and sets the “A” symbol in the column of the number which was generated. It also uses “check_win” to determine if it has won.
* If the variable p equals 1, the player is asked which column the symbol should be placed. (All the validation, winner checks are executed after every move) After that “ai_move” is used to generate a move. This goes back and forth until one party has won.
* If the variable p equals 2, player X gets the first turn. (All the validation, winner checks are executed after every move) Player P gets the second turn. This goes back and forth until one party has won.

## Implementation of what happens after the game ##

* Once a player has won, it will be displayed in the console.
* If you want to play again, the code must be re-executed. 