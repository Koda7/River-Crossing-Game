# River-Crossing-Game
Game developed using python library `pygame`.

## Summary 
Two player game in which both players compete for the highest score by crossing the river from opposite ends.

## Features
1. Fixed and Moving Obstacles
2. Level is mentioned and scores are constantly updated
3. User friendly interface

## My Game

 - I've implemented a grid system for the player to traverse using the `'w', 'a', 's', 'd'` keys.
 - Each player is depicted with a different color box.
 - The game includes levels which increases after both players play their turn.
 - The fixed obstacles have fixed positions but the moving obstacles increase speed after each level.
 - There's an increment in score after crossing any set of obstacles and a bonus increment for reaching the end.
 - The score decreases as the player takes more time to traverse to the other end or when the player dies.
 - The player scores are shown on the top left and bottom left corners and are instantaneously updated.
 - The level is displayed on the top right corner of the window.
 - There's a power-up which slows down the game when the 'f' key is pressed(each player has two of these power-ups).
 - There's an end game screen which signifies the winning player and it automatically closes.

## To play
Run `python3 test.py`
