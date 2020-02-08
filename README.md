# Pong with Pygame
This is a pong game coded in python 3 with pygame. Simpy run the program and a pygame window shows up. The program waits
one second for you to get ready, so you will see a black screen at the start for a second. You will see 2 paddles and a 
moving ball appear on the screen. Use the 'w' and 's' keys to control the paddle on the left, and the up and down arrow 
keys to control the paddle on right. If you want to play this pong game by yourself, on line 130 change the code from 
     "elif ball_x == 740 and ball_y > rect1_y and ball_y < rect1_y + 160:"
to 
     "elif ball_x == 740:# and ball_y > rect1_y and ball_y < rect1_y + 160:"
which comments out the code that makes the ball bounce off only the paddle. 

Thanks, varun31415
