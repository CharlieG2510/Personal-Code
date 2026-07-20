
# Initialize Pygame
import pygame
from pygame.locals import *




#Class is used to create a square sprite that can be drawn on the screen
class Sq(pygame.sprite.Sprite):
    def __init__(self): #Creates a square sprite that can be drawn on the screen
        super().__init__() #initializes the sprite class
        self.surf = pygame.Surface((25, 25)) #Creates a surface of 25x25 pixels
        self.surf.fill((0, 200, 255)) #Fills the surface with a color (RGB value)



#Start up pygame - stuff should go under here except class definitions
pygame.init()

WHT, BLU, RED, BLK = (255, 255, 255), (0, 200, 255), (255, 0, 0), (0, 0, 0) # Colors

# Clock and font
clock = pygame.time.Clock() #set up a clock to control the frame rate
font = pygame.font.SysFont("times new roman", 36) #set up a font to display the score and game over message. First part is font, second is pixel size


# Create 4 squares using the Sq class and store them in variables s1, s2, s3, and s4
s1, s2, s3, s4 = Sq(), Sq(), Sq(), Sq()




# Set up the game window
screen = pygame.display.set_mode((1280, 720)) #Size of Window
pygame.display.set_caption("Hello Pygame") #Name of caption



# Game loop
running = True
while running:
    for event in pygame.event.get(): #Handles all incoming events
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):    #If x button in top left conner is clicked (before the or) or escape button pressed (after the or), the game will close
            running = False #Turn off game
    
    
    # X axis goes from left to right, Y axis goes from top to bottom
    screen.blit(s1.surf, (40, 40)) #Draws the square s1 at the position stated in the tuple (x first then y)
    screen.blit(s2.surf, (40, 530))
    screen.blit(s3.surf, (730, 40))
    screen.blit(s4.surf, (730, 530))



    pygame.display.flip() #Displays everything that has been drawn on the screen so far

# Quit Pygame
pygame.quit()