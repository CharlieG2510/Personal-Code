import random
import sys
import time
import os
import pygame

#Music at top and code is put in between the two lines of code below
#This is done if I want background music to play and also have sound effect play on top



# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Load your music file (supports MP3, WAV, or OGG)
pygame.mixer.music.load(f"specialist.mp3")

# Play the music on an infinite loop (-1)
pygame.mixer.music.play(-1)

#Store sound effects here to be players by typeing the variable name and .play() after it example: "shot_noise.play()"
shot_noise = pygame.mixer.Sound("shot_noise.mp3")
spin_noise = pygame.mixer.Sound("gun-spin.mp3")

# Basic game loop boilerplate
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False









    def player(bullet_chamber):
        word = ", 3 to spin the chamber"
        spun = 0
        while True:
            
            options = input(f"Type 1 to shoot self, 2 to shoot opponent{word}")
            if options == "1":
                if bullet_chamber[0] == 0:
                    shot_noise.play()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(2)
                    print("You got hit")
                    return 1
                else:
                    shot_noise.play()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(2)
                    print("It was a blank")
                    return 2
            
            

            elif options == "2":
                if bullet_chamber[0] == 0:
                    shot_noise.play()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(2)
                    print("You hit the AI")
                    return 3
                else:
                    shot_noise.play()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(2)
                    print("It was a blank")
                    return 4
                
            
            
            elif options == "3":
                
                if spun == 0:
                    random.shuffle(bullet_chamber)
                    word = ''
                    spun = spun + 1
                    spin_noise.play()
                    print("You spun the chamber")
                else:
                    print("You already spun the chamber")
            
            elif options == "cheat":
                print(bullet_chamber)
            
            else:
                print("Invalid input, try again")

            


    def ai(bullet_chamber):
        if len(bullet_chamber) == 1: #If theres one bullet left, they should know that whats in the chamber and if its live shoot player and shoot selves if its blank
            if bullet_chamber[0] == 0:
                print("The AI shot you and it was a live bullet")
                return 3
            else:
                print("The AI shot itself and it was a blank")
                return 2
        else: #There is more than one bullet left, so they will randomly choose to shoot themselves or the player
            choice = random.randint(1,2)
            if choice == 1:
                    if bullet_chamber[0] == 0:
                        print("The AI shot itself and it was a live bullet")
                        return 1
                    else:
                        print("The AI shot itself and it was a blank")
                        return 2
                
                

            elif choice == 2:
                if bullet_chamber[0] == 0:
                    print("The AI shot you and it was a live bullet")
                    return 3
                else:
                    print("The AI shot you and it was a blank")
                    return 4




    def chamber():
        bullet_chamber = list()
        total_bullets = 0
        max_live = 5
        
        while total_bullets < 6:
            live_or_blank = random.randint (0,1) #0=live 1=blank
            if live_or_blank == 0:
                if max_live > 0:
                    max_live = max_live - 1
                    bullet = 0
                    
                else:
                    bullet = 1
                    
            else:
                bullet = 1
                
            bullet_chamber.append(bullet)
            total_bullets = total_bullets + 1
        return bullet_chamber

    def main():

        bullet_chamber = chamber()
        while True:
            turn = 1 #1=player 0=ai
            p_health = 3
            ai_health = 3
            print(f"Total Lives: {bullet_chamber.count(0)}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                print(f"Player health: {p_health}, AI health: {ai_health}, Bullets left: {len(bullet_chamber)}")

                if turn == 1:
                    print("Player's turn")
                    
                    result = player(bullet_chamber)
                    if result == 1: #shoots self and live
                        p_health -= 1
                        del bullet_chamber[0]
                        turn = 0
                    elif result == 2: #shoots self and blank
                        del bullet_chamber[0]
                        pass
                    elif result == 3: #shoots ai and live
                        ai_health -= 1
                        del bullet_chamber[0]
                        turn = 0
                    elif result == 4: #shoots ai and blank
                        del bullet_chamber[0]
                        turn = 0

                else:
                    print("AI's turn")
                    time.sleep(2)
                    shot_noise.play()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(2)
                    result = ai(bullet_chamber)
                    if result == 1: #shoots self and live
                        del bullet_chamber[0]
                        ai_health -= 1
                        turn = 1
                    elif result == 2: #shoots self and blank
                        del bullet_chamber[0]
                        pass
                    elif result == 3: #shoots player and live
                        p_health -= 1
                        del bullet_chamber[0]
                        turn = 1
                    elif result == 4: #shoots player and blank
                        del bullet_chamber[0]
                        turn = 1

                time.sleep(2)

                if p_health == 0:
                    print("You lost")
                    restart = input("Type 1 to restart, 2 to quit")
                    if restart == "1":
                        break
                    else:
                        sys.exit()


                elif ai_health == 0:
                    print("You won")
                    restart = input("Type 1 to restart, 2 to quit")
                    if restart == "1":
                        bullet_chamber = chamber()
                        break
                    else:
                        sys.exit()
                
                    
    main()









pygame.quit()








