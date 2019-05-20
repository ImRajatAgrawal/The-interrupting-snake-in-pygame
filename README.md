# The-interrupting-snake-in-pygame
The Interrupting Snake is an AI-based snake game in python using pygame module. It lets the player to navigate the snake to eat as many apples as it can but while playing the user should be careful of the computer snake as it will try to catch the player's snake and kill it. Also there are walls, hitting the wall means game-over and when the player snake eats an apple the speed of both player and computer snake increases.

Run the code on any suitable python IDE. Also for playing the game you must have the pygame module dowloaded on your machine.

## Algorithm used for computer Snake 
The computer snake is programmend according to the algorithm of finding the closest point (x,y) from a set of points in a 2-D space.
The algorithm maintains the Player snake's coordinates in a list and finds the closest point in it to the coordinates of the computer snake's head.

## Converting the program to an executable
   Install cx_Freeze Package on your machine using the command -
   
   **pip install cx_Freeze**
   
   Locate the file setup.py from the repository, make changes in the file path and run the following command on the command prompt -
   
   **build setup.py**
   
   and then you are good to go.
   
This is just a simple game for entertainment. Further improvements will be done soon.    
