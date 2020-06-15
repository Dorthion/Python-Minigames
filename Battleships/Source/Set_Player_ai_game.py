import pygame
import numpy as np
from Source import UI_functions as UI
from Source import battleships_functions_bot as bfb
from Source import battleships_functions_player as bfp
from Source import battleships_functions_check as bfc

def Play_Game(screen, bg, cfg):
    screen, bg = UI.Update_Screen_Values(screen, bg)
    
    #Resources (Images, Icons, Fonts)
    haha = pygame.image.load("Assets/Images/haha.jpg")
    haha = pygame.transform.scale(haha, (34*cfg["Rules"].getint("X_RANGE"), 34*cfg["Rules"].getint("Y_RANGE")))
    #font = pygame.font.Font("Resources/overpass-regular.otf", 12)

    #Initial Values
    RUNNING = True
    SHOW_HAHA = True
    CANT_GENERATE = False
    CLICK = False
    bfb.load_config_file(cfg)
    bfp.load_config_file(cfg)
    bfc.load_config_file(cfg)
    Ptab = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
    Bmap = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
    Bmap, CANT_GENERATE = bfb.generate_bot_ships(Bmap)
    rects = UI.Rect_Player_AI_Set()
    rect_map = UI.Rect_Player_AI_Map()

    #InGame
    while RUNNING:
        #Screen properties per update
        dt = pygame.time.Clock().tick(cfg["Basic"].getint("FPS")) / 1000.0    #DeltaTime
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Red_Btn(screen, rects)
        UI.Draw_Player_Map(screen, Ptab)
        UI.Draw_Player_AI2(screen, Bmap)
        
        #Clickable buttons 
        if CLICK:
            if rects[0].collidepoint((mx,my)):
                if SHOW_HAHA:
                    SHOW_HAHA = False
                else:
                    SHOW_HAHA = True

            if rect_map.collidepoint((mx,my)):
                if mx >= 50 and mx < 50+34*cfg["Rules"].getint("X_RANGE") and my >= 100 and my < 100+34*cfg["Rules"].getint("Y_RANGE"):
                    Ptab = bfp.change_ship(Ptab,my - 100,mx - 50)

            if rects[1].collidepoint((mx,my)):
                Bmap = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
                Bmap, CANT_GENERATE = bfb.generate_bot_ships(Bmap)

            if rects[2].collidepoint((mx,my)):
                bfc.check_ship_size(Ptab)
                Ptab = np.where(Ptab == 4,1,Ptab)
                return Ptab, Bmap, True
            
            if rects[3].collidepoint((mx,my)):
                print("Back to Menu")
                return None, None, False

        #Check to draw haha
        if(SHOW_HAHA == True):
            screen.blit(haha,((cfg["Rules"].getint("X_RANGE") * 34) + 100,100))

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