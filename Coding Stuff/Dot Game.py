import pygame
from pygame.locals import *
import random
import math

pygame.init()





pygame.mixer.init()

# Load your music file (supports MP3, WAV, or OGG)
pygame.mixer.music.load(f"drift_city.mp3")

# Play the music on an infinite loop (-1)
pygame.mixer.music.play(-1)

#Store sound effects here to be players by typeing the variable name and .play() after it example: "shot_noise.play()"
coin_noise = pygame.mixer.Sound("coin_noise.mp3")




WHT, BLU, RED, BLK = (255, 255, 255), (0, 200, 255), (255, 0, 0), (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("times new roman", 36)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hello Pygame")

score = 0
circle_radius = 10
circle_x = None
circle_y = None
high_score = 0
timer = 5


try:
    with open('dot_game_high_score', 'r') as hscore:
        high_score = int(hscore.read().strip())
except FileNotFoundError:
    high_score = 0







running = True
while running:

    if score > high_score:
        high_score = score
        with open('dot_game_high_score', 'w') as hscore:
            hscore.write(str(high_score))


    if score < 10:
        reset_time = 4
    else:
        if score < 20:
            reset_time = 3
        else:
            if score < 30:
                reset_time=2.5
            else:
                if score < 40:
                    reset_time = 2
                else:
                    if score < 50:
                        reset_time = 1.5
                    else:
                        reset_time = 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False



        
        #CLICK CODE -- IF YOU CLICK THE BUTTON IT CHANGES POSITION
        if event.type == pygame.MOUSEBUTTONDOWN:
            if circle_x is not None and circle_y is not None:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - circle_x
                dy = mouse_y - circle_y
                distance = math.hypot(dx, dy)

                if distance <= circle_radius:
                    circle_x = None
                    circle_y = None
                    score += 1
                    timer = reset_time
                    coin_noise.play()

                
    if circle_x is None or circle_y is None:
        circle_x = random.randint(circle_radius, 600 - circle_radius)
        circle_y = random.randint(50+circle_radius, 550 - circle_radius)
            




    screen.fill(BLK)

    #DISPLAY TEXT
    score_text = font.render(f"Score: {score}", True, WHT)
    score_rect = score_text.get_rect()
    screen.blit(score_text, score_rect)
    
    #TIMER CODE
    dt = clock.tick(60) / 500
    timer -= dt #Timer counts down

    if timer < 0:
        screen.fill(WHT)
        result_text = f"You Lost :( Final Score: {score} High Score: {high_score}"
        banner = font.render(result_text, True, BLK)
        screen.blit(banner, (10, 280))
        pygame.display.update()
        circle_x = 10000000
        circle_y = 1000000
        if timer < -5:
            running = False




    timer_text = font.render(f"Time: {timer:.2f}", True, WHT)
    screen.blit(timer_text, (430,0))


    hscore_text = font.render(f"High Score: {high_score}", True, WHT)
    screen.blit(hscore_text, (0,550))
    



    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()