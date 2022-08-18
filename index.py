# from turtle import Screen
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("imgs.png")
pygame.display.set_icon(icon)

playerIMG = pygame.image.load('ufo.png')
playerX = 370
playerY = 480
playerXchange = 0
# playerYchange = 0

enemyIMG = pygame.image.load('asteroid.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyXchange = 0

def player(x, y):
    screen.blit(playerIMG, (x, y))

def enemy(x, y):
    screen.blit(enemyIMG, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.3
            
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.3
            
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
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
