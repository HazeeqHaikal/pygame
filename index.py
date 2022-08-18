# from turtle import Screen
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("imgs.png")
pygame.display.set_icon(icon)

playerIMG = pygame.image.load('ufo.png')
playerX = 370
playerY = 480
playerXchange = 0

def player(x, y):
    screen.blit(playerIMG, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))
    playerY -= 0.2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player(playerX, playerY)
    pygame.display.update()
