import pygame
import numpy as np
from Source import UI_functions as UI
from Source import battleships_functions_play as play

def Play_Game(screen, bg, Ptab, Bmap, cfg):
    
    #Init
    font_s = pygame.font.Font("Assets/Font/impact.ttf", 26)
    font = pygame.font.Font("Assets/Font/impact.ttf", 40)
    grid = pygame.image.load("Assets/Images/WhiteGrid.png")
    square = pygame.image.load("Assets/Images/Square.png")
    screen, bg = UI.Update_Screen_Values(screen, bg)
    pygame.time.Clock().tick(cfg["Basic"].getint("FPS"))
    
    #Initial Values
    CLICK = False
    RUNNING = True
    shoot = True
    play.load_config_file(cfg)
    AI = play.PlayBot(Ptab, cfg["Basic"].getint("ALG1"))
    rect_map = UI.Rect_Player_AI_Map()
    rects, images_pos, text_pos = UI.Rect_Play()
    images = [square]
    texts = [font.render(cfg["Text"]["PLAYER"], True, (255, 255, 255)), 
             font.render(cfg["Text"]["AI"], True, (255, 255, 255)),
             font.render(cfg["Text"]["SCORE"], True, (255, 255, 255)),
             font.render(str(cfg["Points"].getint("PLAYER_PTS")) + " - " + str(cfg["Points"].getint("AI_PTS")), True, (255, 255, 255)),
             font_s.render("χ", True, (52, 52, 54))]
    
    #InGame
    while RUNNING:
        
        #Screen properties per update
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Left_Map_Play(screen, Ptab, grid)
        UI.Draw_Right_Map_Play(screen, Bmap, grid)
        UI.Draw_Pos(screen, images, images_pos)
        UI.Draw_Pos(screen, texts, text_pos)
        
        #Clickable buttons 
        if rect_map.collidepoint((mx,my)) and CLICK and shoot:
            if mx >= 50 and mx < 50+34*cfg["Rules"].getint("X_RANGE") and my >= 100 and my < 100+34*cfg["Rules"].getint("Y_RANGE"):
                Bmap, shooted = play.Player_shot(Bmap,my - 100,mx - 50)
                if (1 in Bmap) == False:
                    shoot = False
                    cfg.set("Points","PLAYER_PTS",str(cfg["Points"].getint("PLAYER_PTS") + 1))
                    texts[3] = font.render(str(cfg["Points"].getint("PLAYER_PTS")) + " - " + str(cfg["Points"].getint("AI_PTS")), True, (255, 255, 255))
                if shooted and shoot:
                    AI.AI_shot()
                    if (1 in AI.Map) == False:
                        shoot = False
                        cfg.set("Points","AI_PTS",str(cfg["Points"].getint("AI_PTS") + 1))
                        texts[3] = font.render(str(cfg["Points"].getint("PLAYER_PTS")) + " - " + str(cfg["Points"].getint("AI_PTS")), True, (255, 255, 255))
        
        #Exit button
        if rects[0].collidepoint((mx,my)) and CLICK:
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