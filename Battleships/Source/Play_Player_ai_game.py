import pygame
import numpy as np
from Source import UI_functions as UI
from Source import battleships_functions_play as play

def Play_Game(screen, bg, Ptab, Bmap, cfg):
    font = pygame.font.Font("Assets/Font/overpass-regular.otf", 40)
    grid = pygame.image.load("Assets/Images/WhiteGrid.png")
    screen, bg = UI.Update_Screen_Values(screen, bg)
    pygame.time.Clock().tick(cfg["Basic"].getint("FPS"))
    
    #Initial Values
    CLICK = False
    RUNNING = True
    play.load_config_file(cfg)
    AI = play.PlayBot(Ptab)
    rect_map = UI.Rect_Player_AI_Map()
    rects_play, text_pos = UI.Rect_Player_AI_Play()
    texts = [font.render(cfg["Text"]["PLAYER"], True, (255, 255, 255)), 
             font.render(cfg["Text"]["AI"], True, (255, 255, 255)),
             font.render(cfg["Text"]["SCORE"], True, (255, 255, 255)),
             font.render(str(cfg["Points"].getint("PLAYER_PTS")) + " - " + str(cfg["Points"].getint("AI_PTS")), True, (255, 255, 255))]
    
    #InGame
    while RUNNING:
        #Screen properties per update
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Red_Btn(screen, rects_play)
        UI.Draw_Pos(screen, texts, text_pos)
        UI.Draw_Left_Map_Play(screen, Ptab, grid)
        UI.Draw_Right_Map_Play(screen, Bmap, grid)
        
        #Clickable buttons 
        if rect_map.collidepoint((mx,my)) and CLICK:
            if mx >= 50 and mx < 50+34*cfg["Rules"].getint("X_RANGE") and my >= 100 and my < 100+34*cfg["Rules"].getint("Y_RANGE"):
                Bmap, shooted = play.Player_shot(Bmap,my - 100,mx - 50)
                if shooted:
                    AI.AI_shot()

        if rects_play[0].collidepoint((mx,my)) and CLICK:
            print("Surrendered")
            return

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
    return cfg, False