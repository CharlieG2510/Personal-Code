import pygame
from pygame.locals import *
import random
import sys





window_x = 720
window_y = 480


snake_speed = 15




#Start up pygame - stuff should go under here except class definitions
pygame.init()



fps = pygame.time.Clock()


WHT, BLU, RED, BLK = (255, 255, 255), (0, 200, 255), (255, 0, 0), (0, 0, 0) # Colors

# Clock and font
clock = pygame.time.Clock() #set up a clock to control the frame rate
font = pygame.font.SysFont("times new roman", 36) #set up a font to display the score and game over message. First part is font, second is pixel size




# Set up the game window
screen = pygame.display.set_mode((window_x, window_y)) #Size of Window
pygame.display.set_caption("Snake") #Name of caption



snake_position = [100, 50] #Initial position of the snake
snake_body = [[100, 50]]


# fruit position 
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# initial score
score = 0


def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHT) #Render the score text using the specified font and color
    
    # create a rectangular object for the text surface object
    score_rect = score_text.get_rect()
    screen.blit(score_text, score_rect) #Blit the score text on the screen at the specified position (In the rectangle object created above)

def game_over(score):
    game_over = font.render(f"Game over, final score: {score}", True, WHT) #Render the score text using the specified font and color
    screen.blit(game_over, (window_x // 2 - 150, window_y // 2)) #Places text in middle of screen
    pygame.display.flip() #Displays text
    pygame.time.wait(2000) #Waits 1 second before closing the game



direction = 'RIGHT'

# Game loop
running = True
while running:
    screen.fill(BLK) #Choose color for the background of the window using variables created before
    for event in pygame.event.get(): #Handles all incoming events
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    #If x button in top left conner is clicked (before the or) or escape button pressed (after the or), the game will close
            running = False #Turn off game
    
    
    



    #If keys are pressed, change the direction of the snake accordingly. The snake cannot move in the opposite direction of its current movement.

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and direction != 'RIGHT':
        direction = 'LEFT'
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and direction != 'LEFT':
        direction = 'RIGHT'
    if keys[pygame.K_UP] or keys[pygame.K_w] and direction != 'DOWN':
        direction = 'UP'
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and direction != 'UP':
        direction = 'DOWN'


    #Ensures the snake can't move diagonally by checking if any other movement keys are pressed while a direction key is pressed. If so, the snake will not change direction.
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and (keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]) and direction != 'RIGHT':
        direction = 'LEFT'
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]) and direction != 'LEFT':
        direction = 'RIGHT'
    if keys[pygame.K_UP] or keys[pygame.K_w] and (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_DOWN] or keys[pygame.K_s]) and direction != 'DOWN':
        direction = 'UP'   
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_UP] or keys[pygame.K_w]) and direction != 'UP':
        direction = 'DOWN'

     # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    #Makes the new position of the snake the first element in the snake_body list. This is done so that the snake can grow when it eats a fruit. The new position is added to the front of the list and the last element is removed if the snake has not eaten a fruit. If the snake has eaten a fruit, the last element is not removed and the snake grows by one segment.
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]: #If snake head and fruit in same spot
        score += 1 #Increase score by 1
        fruit_spawn = False #Makes fruit_spawn False so that a new fruit can be spawned in a new location
    else:
        snake_body.pop() #Removes the last element of the snake_body list so that the snake does not grow when it has not eaten a fruit (This doesn't happen when it eats a fruit meaning that the last location is added to the list)
    
    #When a fruit has been earen
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10] #Make a new location
        
    fruit_spawn = True #Sets fruit_spawn to True so that the fruit can be drawn on the screen in the new location


    #Drawing the snake and fruit on the screen. The snake is drawn as a series of rectangles (one for each segment of the snake) and the fruit is drawn as a rectangle. The color of the snake is green and the color of the fruit is white.    
    for pos in snake_body:  #For every segment of the snake
        pygame.draw.rect(screen, RED, pygame.Rect(pos[0], pos[1], 10, 10)) #Draw a red square at the position of the segment
    pygame.draw.rect(screen, WHT, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)) #Draw a white square at the position of the fruit


     # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10: #If it hits the walls
        game_over(score)
        running = False #Turn off game
    if snake_position[1] < 0 or snake_position[1] > window_y-10: #If it hits the ground or roof
        game_over(score)
        running = False #Turn off game
    
    num = 1

    for block in snake_body[1:]: #If it hits itself
        if snake_body[0] == snake_body[num]: #If the head of the snake is in the same position as any other segment of the snake
            game_over(score)



    # displaying score continuously
    display_score(score)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)

# Quit Pygame
pygame.quit()