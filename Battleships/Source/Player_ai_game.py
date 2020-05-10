import pygame
import numpy as np
from Source.Settings import *
from Source import battleships_functions_bot as bfb
from Source import battleships_functions_player as bfp

def Play_Game(screen, bg):
    #Resources (Images, Icons, Fonts)
    haha = pygame.image.load("Assets/Images/haha.jpg")
    haha = pygame.transform.scale(haha, (339, 339))
    #font = pygame.font.Font("Resources/overpass-regular.otf", 12)

    #Rect Buttons
    btnhidebot = pygame.Rect(700,50,80,40)
    btnrandbot = pygame.Rect(600,50,80,40)
    btnplayer = pygame.Rect(55,111,339,339)

    #Initial Values
    Ptab = np.zeros((10,10), dtype = np.int32)
    Bmap = np.zeros((10,10), dtype = np.int32)
    Bmap = bfb.generate_bot_ships(Bmap)

    click = False
    hahad = False

    #InGame
    while RUNNING:
        #Screen properties per update
        dt = pygame.time.Clock().tick(FPS) / 1000.0    #DeltaTime
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw hiding button
        pygame.draw.rect(screen, RED, btnhidebot)
        pygame.draw.rect(screen, RED, btnrandbot)

        #Draw player 
        for x in range(10):
            for y in range(10):
                if Ptab[x][y] == 0:
                    pygame.draw.rect(screen, BLUE, (55+34*y,111+34*x,32,32))
                if Ptab[x][y] == 1:
                    pygame.draw.rect(screen, GREEN, (55+34*y,111+34*x,32,32))
                if Ptab[x][y] == 2:
                    pygame.draw.rect(screen, RED, (55+34*y,111+34*x,32,32))
                if Bmap[x][y] == 0:
                    pygame.draw.rect(screen, BLUE, (416+34*y,111+34*x,32,32))
                if Bmap[x][y] == 1:
                    pygame.draw.rect(screen, GREEN, (416+34*y,111+34*x,32,32))
                if Bmap[x][y] == 2:
                    pygame.draw.rect(screen, RED, (416+34*y,111+34*x,32,32))

        #Clickable buttons 
        if btnhidebot.collidepoint((mx,my)):
            if click:
                if hahad:
                    hahad = False
                else:
                    hahad = True

        if btnplayer.collidepoint((mx,my)):
            if click:
                if mx >= 55 and mx < 395 and my >= 111 and my < 451:
                    Ptab = bfp.change_ship(Ptab,my - 111,mx - 55)

        if btnrandbot.collidepoint((mx,my)):
            if click:
                Bmap = np.zeros((10,10), dtype = np.int32)
                Bmap = bfb.generate_bot_ships(Bmap)


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
    pygame.quit()