from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT
from cmath import rect
from pickle import TRUE
from click import pass_context
from matplotlib import sankey
import pygame
import math
import random
from pygame import mixer

pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Snake Game')
icon = pygame.image.load('images\\icon.png')
pygame.display.set_icon(icon)

eatsound = mixer.Sound('sound\\eat.mp3')
hitsound = mixer.Sound('sound\\gameover.mp3')

# player
snakeX = 45
snakeY = 45
s_sizeX = 15
s_sizeY = 15
speed = 0.4
# snake = pygame.draw.rect(screen,(255,255,255),[snakeX,snakeY])
U_snakeX = speed
U_snakeY = 0

foodX = 0
foodY = 0
f_sizeX = 15
f_sizeY = 15

startimg = pygame.image.load('images\\start.png')
gameoverimg = pygame.image.load('images\\gameover.png')
# backimg = pygame.image.load('images\\background.jfif')
foodimg = pygame.image.load('images\\apple (1).png')
# foodimg = pygame.image.load('images\\apple.png')

def isgameover(l):
    le = len(l)
    head = l[le-1]
    if l[le-1][0] > 900 or l[le-1][0] < 0 or l[le-1][1] < 0 or l[le-1][1] > 600:
        return True
    if head in l[ :-1]:                                                                 # imp!!!!!!!!!!!!!!!!!!!!!
        return True
    return False

def iseaten(l,fX,fY):
    le = len(l)
    dist = math.sqrt(math.pow(l[le-1][0]-10-fX,2) + math.pow(l[le-1][1]-10-fY,2))
    if dist < 15:
        return True
    return False

score = 0
def display_score(x,y,r,b,g,sz):
    font =pygame.font.Font('font\\Stop Bullying.otf',sz)
    score_1 = font.render("Score : "+str(score),True,(r,b,g))
    screen.blit(score_1,(x,y))

def snake_plot(screen,r,b,g,snk_lst,size):
    for x,y in snk_lst:
        pygame.draw.rect(screen,(r,b,g),[x,y,size,size])

running = False
gameover = False
close = False
food_state = False
eat = False
snk_lst = []
snk_len = 10

if __name__=="__main__":
    while running == False and close == False:
        screen.fill((0,0,0))
        screen.blit(startimg,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
        
        pygame.display.update()

    while running == True and close == False:
        if gameover == False:
            screen.fill((102,180,0))
            # screen.blit(backimg,(0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if U_snakeY > 0:
                            pass
                        else:
                            U_snakeX = 0
                            U_snakeY = 0
                            U_snakeY = -speed

                    if event.key == pygame.K_DOWN:
                        if U_snakeY < 0:
                            pass
                        else:
                            U_snakeX = 0
                            U_snakeY = 0
                            U_snakeY = speed

                    if event.key == pygame.K_LEFT:
                        if U_snakeX > 0:
                            pass
                        else:
                            U_snakeX = 0
                            U_snakeY = 0
                            U_snakeX = -speed

                    if event.key == pygame.K_RIGHT:
                        if U_snakeX < 0:
                            pass
                        else:
                            U_snakeX = 0
                            U_snakeY = 0
                            U_snakeX = speed
            
            snakeX += U_snakeX
            snakeY += U_snakeY

            head = []
            head.append(snakeX)
            head.append(snakeY)
            snk_lst.append(head)

            if food_state == False:
                foodX = random.randint(30,870)
                foodY = random.randint(30,570)
                # pygame.draw.rect(screen,(200,0,0),[foodX,foodY,f_sizeX,f_sizeY])
                screen.blit(foodimg,(foodX,foodY))
                food_state = True
            else:
                screen.blit(foodimg,(foodX,foodY))
                # pygame.draw.rect(screen,(200,0,0),[foodX,foodY,f_sizeX,f_sizeY])      

            eat = iseaten(snk_lst,foodX,foodY)
            if eat == True:
                eatsound.play()
                food_state = False
                # s_sizeX += 15
                score +=1
                snk_len += 40

            if score == 10:
                speed = 0.5
            elif score == 20:
                speed = 0.6
            elif score == 30:
                speed = 0.73

            if len(snk_lst)>snk_len:
                del snk_lst[0]

            display_score(10,10,0,0,0,12)
            gameover = isgameover(snk_lst)
            if gameover == True:
                hitsound.play()
            snake_plot(screen,0,0,0,snk_lst,s_sizeX)
            pygame.display.update()

        if gameover == True:
            screen.fill((0,0,0))
            screen.blit(gameoverimg,(17,0))
            display_score(385,130,255,255,255,24)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameover = False
                        score = 0
                        snakeX = 45
                        snakeY = 45
                        U_snakeX = 0.2
                        U_snakeY = 0
                        speed = 0.4
                        snk_len = 10
                        snk_lst = []
            
            pygame.display.update()