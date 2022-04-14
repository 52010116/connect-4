# Description of Unit-Tests #

The tests were designed to test the general function of the game and only cover game logic. AI is not tested.

## Field test ##

* “test_field_init” tests if the playing field is displayed as it is supposed to be.

## Input test ##

* “test_exit_input” tests if the game exits when the player enters “q” or “Q” or what happens when the input is different from the expected.
* “test_legal_move_check” tests what happens when the input is out of range from the expected or when it is a string. 

## Game test ##

* “test_set_move” tests if the moves are executed in the entered column.
* “test_legal_move_check2” tests if the selected column still has empty spaces or if its already filled.
* “test_check_if_win” tests if there are any four of a kind in a row.

## Coverage ##

The tests do not cover 100% of the game logic, but we tried to cover the basic functionality so that the game runs without errors. We tried to write tests for each method (except “ai_move”) with occasions which could occur in a real game.