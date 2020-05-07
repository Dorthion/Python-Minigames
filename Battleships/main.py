import pygame
import numpy as np
from source import battleships_functions as bsf
from pathlib import Path

#Init
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Battleships")

#Resources (Images, Icons, Fonts)
icon = pygame.image.load("Resources/ship.png")
bg = pygame.image.load("Resources/background.png")
haha = pygame.image.load("Resources/haha.jpg")
font = pygame.font.Font("Resources/overpass-regular.otf", 12)
pygame.display.set_icon(icon)

#Colors
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)

#Rect Buttons
btn1 = pygame.Rect(700,50,80,40)
btnplayer = pygame.Rect(55,111,361,417)

#Initial Values
Ptab = np.zeros((10,10), dtype = np.int32)
Ptab2 = np.zeros((10,10), dtype = np.int32)

running = True
click = False
hahad = False

#InGame
while running:
    screen.blit(bg,(0,0))
    mx, my = pygame.mouse.get_pos()
    
    pygame.draw.rect(screen, red, btn1)
    
    for x in range(10):
        for y in range(10):
            if Ptab[x][y] == 0:
                pygame.draw.rect(screen, blue, (55+34*y,111+34*x,32,32))
            if Ptab[x][y] == 1:
                pygame.draw.rect(screen, green, (55+34*y,111+34*x,32,32))
            if Ptab[x][y] == 2:
                pygame.draw.rect(screen, red, (55+34*y,111+34*x,32,32))
        
    if btn1.collidepoint((mx,my)):
        if click:
            if hahad:
                hahad = False
                pass 
            else:
                hahad = True
                pass 
            
    if btnplayer.collidepoint((mx,my)):
        if click:
            #print(mx)
            #print(my)
            if mx >= 55 and mx < 395 and my >= 111 and my < 451:
                Ptab = bsf.change_ship(Ptab,my - 111,mx - 55)
            #print(Ptab)
            pass
    
    if(hahad == True):
        screen.blit(haha,(400,100))
    
    pygame.display.update()
    
    click = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True