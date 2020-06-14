import pygame
import numpy as np
from Source import UI_functions as UI
from Source import battleships_functions_bot as bfb
from Source import battleships_functions_check as bfc

def Play_Game(screen, bg, cfg):
    screen, bg = UI.Update_Screen_Values(screen, bg)
    
    #Resources (Images, Icons, Fonts)
    #font = pygame.font.Font("Resources/overpass-regular.otf", 12)

    #Initial Values
    RUNNING = True
    SHOW_HAHA = True
    CANT_GENERATE1 = False
    CANT_GENERATE2 = False
    CLICK = False
    bfb.load_config_file(cfg)
    Bmap1 = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
    Bmap2 = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
    Bmap1, CANT_GENERATE1 = bfb.generate_bot_ships(Bmap1)
    Bmap2, CANT_GENERATE2 = bfb.generate_bot_ships(Bmap2)
    rects = UI.Rect_AI_AI_Set()
    rect_map = UI.Rect_Player_AI_Map()


    #InGame
    while RUNNING:
        #Screen properties per update
        dt = pygame.time.Clock().tick(cfg["Basic"].getint("FPS")) / 1000.0    #DeltaTime
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Red_Btn(screen, rects)
        UI.Draw_Player_Map(screen, Bmap1)
        UI.Draw_Player_AI2(screen, Bmap2)
        
        #Clickable buttons
        if CLICK:
            if rects[0].collidepoint((mx,my)):
                print("Play game")
                return Bmap1, Bmap2, True
        
        if CLICK:
            if rects[1].collidepoint((mx,my)):
                print("Back to menu")
                return None, None, False
            
            if rects[2].collidepoint((mx,my)):
                Bmap1 = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
                Bmap1, CANT_GENERATE1 = bfb.generate_bot_ships(Bmap1)
                
            if rects[3].collidepoint((mx,my)):
                Bmap2 = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
                Bmap2, CANT_GENERATE2 = bfb.generate_bot_ships(Bmap2)

        #Events and update
        pygame.display.update()
        CLICK = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    CLICK = True
 #pygame.quit()