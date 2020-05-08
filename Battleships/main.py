import pygame
import numpy as np
from source import battleships_functions_bot as bfb
from source import battleships_functions_player as bfp
from pathlib import Path

#Init
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Battleships")

#Resources (Images, Icons, Fonts)
icon = pygame.image.load("Resources/ship.png")
bg = pygame.image.load("Resources/background.png")
haha = pygame.image.load("Resources/haha.jpg")
haha = pygame.transform.scale(haha, (339, 339))
font = pygame.font.Font("Resources/overpass-regular.otf", 12)
pygame.display.set_icon(icon)

#Colors
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)

#Rect Buttons
btnhidebot = pygame.Rect(700,50,80,40)
btnplayer = pygame.Rect(55,111,339,339)

#Initial Values
Ptab = np.zeros((10,10), dtype = np.int32)
Btab = np.zeros((10,10), dtype = np.int32)
Btap = bsp.generate_bot_ships(Bmap)

running = True
click = False
hahad = False

#InGame
while running:
    #Screen properties per update
    screen.blit(bg,(0,0))
    mx, my = pygame.mouse.get_pos()
    
    #Draw hiding button
    pygame.draw.rect(screen, red, btnhidebot)
    
    #Draw player 
    for x in range(10):
        for y in range(10):
            if Ptab[x][y] == 0:
                pygame.draw.rect(screen, blue, (55+34*y,111+34*x,32,32))
            if Ptab[x][y] == 1:
                pygame.draw.rect(screen, green, (55+34*y,111+34*x,32,32))
            if Ptab[x][y] == 2:
                pygame.draw.rect(screen, red, (55+34*y,111+34*x,32,32))
            if Btab[x][y] == 0
                pygame.draw.rect(screen, blue, (416+34*y,111+34*x,32,32))
            if Btab[x][y] == 1:
                pygame.draw.rect(screen, green, (416+34*y,111+34*x,32,32))
            if Btab[x][y] == 2:
                pygame.draw.rect(screen, red, (416+34*y,111+34*x,32,32))
    
    #Clickable buttons 
    if btnhidebot.collidepoint((mx,my)):
        if click:
            if hahad:
                hahad = False
                pass 
            else:
                hahad = True
                pass
            
    if btnplayer.collidepoint((mx,my)):
        if click:
            if mx >= 55 and mx < 395 and my >= 111 and my < 451:
                Ptab = bfp.change_ship(Ptab,my - 111,mx - 55)
            #print(Ptab)
            pass
    
    #Check to draw haha
    if(hahad == True):
        screen.blit(haha,(416,111))
    
    #Events and update
    pygame.display.update()
    
    click = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True