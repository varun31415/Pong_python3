# section 1 of the program 


# This part of the program sets up the variables, and libraries

# imports the necassary packages
import pygame
import sys
import math
import time
import random

#initiates the pygame library
pygame.init()

# defines the basic colors needed
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

# defines the score of the players 
score1 = 0 
score2 = 0

# variables for the 2 paddles in the game
rect1_x = 750
rect1_y = 200
rect2_x = 25
rect2_y = 200

# this is the rate of the change of the paddles' y position
rect1_y_change = 0
rect2_y_change = 0

# variables for the ball in the game
ball_x = 400
ball_y = 300

# rate of change of the ball's x and y position. You can also change the ball's speed dbx and dby but it may not work. 
dbx = 0.5
dby = 0.5

# create a bool called running to siginifie if the program is running or not
running = True

# this function will reset up the ball when we needed to
def set_up_ball():
    global ball_x,ball_y
    time.sleep(0.5)
    ball_x = random.randint(200,600)
    ball_y = random.randint(200,400)

# section 2 of the program


# this part of the program and actually shows the graphics and has most (all) of the logic

# creates the font
font = pygame.font.Font('freesansbold.ttf', 64) 

# creates the screen, sprites, and sets it's background color to white
screen = pygame.display.set_mode((800,600))
screen.fill(white)
pygame.draw.rect(screen, black,[rect1_x,rect1_y,25,150])
pygame.draw.rect(screen, black,[rect2_x,rect2_y,25,150])
set_up_ball()
pygame.draw.circle(screen, blue, [math.floor(ball_x), math.floor(ball_y)], 15)

# runs the program while it is running or when running is True
while running:
    
    # Lucky for us, pygame does all the background handling for us. It feeds us information for each event 
    # happening such as a keypressed, mouseclicked, or somebody clicking the 'X' button to leave the program.
    # to get the background handling, we use "for event in pygame.event.get():"
    
    for event in pygame.event.get():
        
        # this event stops the program when the 'x' is clicked on the pygame window 
        if event.type == pygame.QUIT:
            # stops the while loop from running by setting running to false which then exists the program
            running = False
        
        # in the following keydown and keyup events it sets the rect1_y_change to -1 or 1 when key is pressed, 
        # and it sets the rect1_y_change or rect2_y_change to 0 when the key is released
        # this causes rect1_y_change or rect2_y_change to be 1 or -1 while a key is being pressed, 
        # and once it is released, it will set it to 0
        # we will later say what rect1_y_change does to affect the program
        
        # event for when a key is pressed or "keydown"
        if event.type == pygame.KEYDOWN:
            # if you press the w key, it sets rect2_y_change to -1
            if event.key == pygame.K_w:
                rect2_y_change = -1 # change this to change the speed paddle2 goes up
            # if you press the s key, it sets rect2_y_change to 1
            elif event.key == pygame.K_s:
                rect2_y_change = 1 # change this to change the speed paddle2 goes down
            
            # if you press the down arrow key, it will set rect1_y_change to 1
            elif event.key == pygame.K_DOWN:
                rect1_y_change = 1 # change this to change the speed paddle1 goes down

            # if you press the up arrow key, it will set rect1_change to -1
            elif event.key == pygame.K_UP:
                rect1_y_change = -1 # change this to change the speed paddle1 goes up
        
        # event for when a key is released on the keyboard, or "keyup"
        if event.type == pygame.KEYUP:
            
            # if you release the up or down arrow keys, it will change rect1_y_change to 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rect1_y_change = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                rect2_y_change = 0
    
    # we want to make sure the ball bouces on the walls and the paddles.
    # To do this, we will change dbx and dby based on if it is not touching a wall, or paddles.
    
    if ball_x == 60 and ball_y > rect2_y and ball_y < rect2_y + 160:
        dbx = -dbx
    elif ball_x == 60:
        # puts the ball back in place and changes the score if the 2nd paddle misses the ball
        score1 = score1 + 1
        set_up_ball()
    elif ball_y == 585:
        dby = -dby
    elif ball_y == 15:
        dby = -dby
    elif ball_x == 740 and ball_y > rect1_y and ball_y < rect1_y + 160:
        dbx = -dbx
    elif ball_x == 740:
        # puts the ball back in place and changes the score if the 1st paddle misses the ball
        score2 = score2 + 1 
        set_up_ball()
    
    ball_y = ball_y + dby
    ball_x = ball_x + dbx
    
    # earlier, we set rect1_y_change to 1 while the down key was being held down, -1 while the up key 
    # was being held down, 0 when no keys were being held down, and similar for the 2nd paddle.
    # We can change the paddles' y position based on when the up and down arrow keys & k and w keys are pressed 
    # using the code "rect1_y = rect1_y + rect1_y_change" as shown in the code

    # we also want to make sure the paddle stays in the boundaries of the pygame window.
    # to do this, we only move the paddle a certain direction if the rect1 y position follows 
    # some of the bounds. The bounds depend on if which key is pressed. For example, we say:
    # "if rect1_y_change == 1 and rect1_y < 430:" to make sure the paddle is not to down below when the down
    # key is pressed. 
    
    if rect1_y_change == 1 and rect1_y < 450:
        rect1_y = rect1_y + rect1_y_change
    elif rect1_y_change == -1 and rect1_y > 0:
        rect1_y = rect1_y + rect1_y_change
    elif rect2_y_change == 1 and rect2_y < 450:
        rect2_y = rect2_y + rect2_y_change
    elif rect2_y_change == -1 and rect2_y > 0:
        rect2_y = rect2_y + rect2_y_change
    
    # here, we move the ball based on the rate of change of the ball's x position, and the ball's y position
    
    # this fills the screen blue so that we don't keep creating rectangles and balls that leave
    # annoying marks on the screen
    screen.fill(blue)
    
    # draws the 2 paddles on to the screen with color black. The position of the rectangles is based on the 
    # variables, so we write it here. We also signify 25,150 as the size of the rectangles
    pygame.draw.rect(screen, black,[rect1_x,rect1_y,25,150])
    pygame.draw.rect(screen, black,[rect2_x,rect2_y,25,150])
    
    # shows the score
    text1 = font.render(str(score2), True, black, blue) 
    textRect1 = text1.get_rect()
    textRect1.center = (350, 200) 
    screen.blit(text1, textRect1) 
    
    text2 = font.render(str(score1),True,black,blue)
    textRect2 = text2.get_rect()
    textRect2.center = (450,200)
    screen.blit(text2,textRect2)
    
    # draws the circle onto the screen with color blue. The position of the circle is 
    # 'math.floor(ball_x), math.floor(ball_y)' because the ball_x and ball_y are floats and there is 
    # no such thing as 'half a pixel'
    pygame.draw.circle(screen, red, [math.floor(ball_x), math.floor(ball_y)], 15)
    
    # draws the line between the 2 sides
    pygame.draw.line(screen,white,[400,0],[400,600],10)
    
    # updates the screen to show the ball and rect1
    pygame.display.update()

# when the while loop is done, it will do the following to quit the program

# prints that the program is done
print('The program has ended.')

# leaves the pygame window
pygame.display.quit()

# quits the pygame library
pygame.quit()

# exits the program
sys.exit()
