import pygame
import numpy as np
from Source import Settings as Set
from Source import UI_functions as UI
from Source import battleships_functions_bot as bfb
from Source import battleships_functions_player as bfp

def Play_Game(screen, bg):
    screen, bg = UI.Update_Screen_Values(screen, bg)
    
    #Resources (Images, Icons, Fonts)
    haha = pygame.image.load("Assets/Images/haha.jpg")
    haha = pygame.transform.scale(haha, (339, 339))
    #font = pygame.font.Font("Resources/overpass-regular.otf", 12)

    #Initial Values
    Ptab = np.zeros((Set.Y_RANGE,Set.X_RANGE), dtype = np.int32)
    Bmap = np.zeros((Set.Y_RANGE,Set.X_RANGE), dtype = np.int32)
    Bmap = bfb.generate_bot_ships(Bmap)
    rects = UI.Rect_Player_AI()
    rect_map = UI.Rect_Player_AI_Map()

    #InGame
    while Set.RUNNING:
        #Screen properties per update
        dt = pygame.time.Clock().tick(Set.FPS) / 1000.0    #DeltaTime
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Red_Btn(screen, rects)
        UI.Draw_Player_Map(screen, Ptab)
        UI.Draw_Player_AI2(screen, Bmap)
        
        #Clickable buttons 
        if rects[0].collidepoint((mx,my)):
            if Set.CLICK:
                if Set.SHOW_HAHA:
                    Set.SHOW_HAHA = False
                else:
                    Set.SHOW_HAHA = True

        if rect_map.collidepoint((mx,my)):
            if Set.CLICK:
                if mx >= 55 and mx < 395 and my >= 111 and my < 451:
                    Ptab = bfp.change_ship(Ptab,my - 111,mx - 55)

        if rects[1].collidepoint((mx,my)):
            if Set.CLICK:
                Bmap = np.zeros((Set.Y_RANGE,Set.X_RANGE), dtype = np.int32)
                Bmap = bfb.generate_bot_ships(Bmap)

        #Check to draw haha
        if(Set.SHOW_HAHA == True):
            screen.blit(haha,(416,111))

        #Events and update
        pygame.display.update()

        Set.CLICK = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Set.RUNNING = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Set.CLICK = True
    pygame.quit()