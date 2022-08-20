# from turtle import Screen
import math
import pygame
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
bg = pygame.image.load("spaces.png")

mixer.music.load("backgrounds.mp3")
mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("imgs.png")
pygame.display.set_icon(icon)

playerIMG = pygame.image.load('ufo.png')
playerX = 370
playerY = 480
playerXchange = 0
# playerYchange = 0

enemyIMG = []
enemyX = []
enemyY = []
enemyYchange = []
enemyXchange = []

numOfEnemies = 6

for i in range(numOfEnemies):
    enemyIMG.append(pygame.image.load('asteroid.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyXchange.append(2)
    enemyYchange.append(30)

bulletIMG = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletXchange = 0
bulletYchange = 5
bulletState = "ready"
# bullets = []
# score = 0

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

overFont = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
def gameOverText():
    overText = overFont.render("GAME OVER", True, (255, 255, 255))
    textRect = overText.get_rect(center=(800/2, 600/2))
    screen.blit(overText, textRect)
    # screen.blit(overText, (200, 250))
    
def player(x, y):
    screen.blit(playerIMG, (x, y))

def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))

def fire(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletIMG, (x+16, y+10))
    # return x, y

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -5
            
            if event.key == pygame.K_RIGHT:
                playerXchange = 5
            
            if event.key == pygame.K_SPACE and bulletState == "ready":
                bulletSound = mixer.Sound("laser.wav")
                bulletSound.play()
                bulletX = playerX
                fire(bulletX, bulletY)
                # bullets.append(fire(bulletX, bulletY))
                # print(bullets)
            
            # if event.key == pygame.K_UP:
            #     playerYchange = -0.3
                
            # if event.key == pygame.K_DOWN:
            #     playerYchange = 0.3
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0
            
            # if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            #     playerYchange = 0
            
    playerX += playerXchange
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736    
    # playerY += playerYchang
    
    for i in range(numOfEnemies):
        
        if enemyY[i] > 440:
            for j in range(numOfEnemies):
                enemyY[j] = 2000
            gameOverText()
            break
        
        enemyX[i] += enemyXchange[i]
        if enemyX[i] <= 0:
            enemyXchange[i] = 2
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] >= 736:
            enemyXchange[i] = -2 
            enemyY[i] += enemyYchange[i]
    
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletSound = mixer.Sound("explosion.wav")
            bulletSound.play()
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            
        enemy(enemyX[i], enemyY[i], i)
            
            
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"
        
    if bulletState is "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletYchange
    
    show_score(textX, textY)
    player(playerX, playerY)
    pygame.display.update()
