import pygame
import numpy as np
from Source import UI_functions as UI
from Source import battleships_functions_play as play

def Play_Game(screen, bg, Bmap1, Bmap2, cfg):
    
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
    play.load_config_file(cfg)
    rect_map = UI.Rect_Player_AI_Map()
    rects, images_pos, text_pos = UI.Rect_Play()
    texts = [font.render(cfg["Text"]["AI1"], True, (255, 255, 255)), 
             font.render(cfg["Text"]["AI2"], True, (255, 255, 255)),
             font.render(cfg["Text"]["SCORE"], True, (255, 255, 255)),
             font.render(str(cfg["Points"].getint("AI1_PTS")) + " - " + str(cfg["Points"].getint("AI2_PTS")), True, (255, 255, 255)),
             font_s.render("χ", True, (52, 52, 54))]
    images = [square]
    
    AI1 = play.PlayBot(Bmap1, cfg["Basic"].getint("ALG1"))
    AI2 = play.PlayBot(Bmap2, cfg["Basic"].getint("ALG2"))
    shoot = True
    
    #InGame
    while RUNNING:
        
        #Screen properties per update
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Left_Map_Play(screen, Bmap1, grid)
        UI.Draw_Right_Map_Play(screen, Bmap2, grid)
        UI.Draw_Pos(screen, images, images_pos)
        UI.Draw_Pos(screen, texts, text_pos)
        
        #Clickable buttons 
        if rects[0].collidepoint((mx,my)) and CLICK:
            return True
        
        if shoot:
            AI1.AI_shot()
            if (1 in AI1.Map) == False:
                cfg.set("Points","AI2_PTS",str(cfg["Points"].getint("AI2_PTS") + 1))
                texts[3] = font.render(str(cfg["Points"].getint("AI1_PTS")) + " - " + str(cfg["Points"].getint("AI2_PTS")), True, (255, 255, 255))
                shoot = False

        pygame.display.update()
        if shoot:
            AI2.AI_shot()
            if (1 in AI2.Map) == False:
                cfg.set("Points","AI1_PTS",str(cfg["Points"].getint("AI1_PTS") + 1))
                texts[3] = font.render(str(cfg["Points"].getint("AI1_PTS")) + " - " + str(cfg["Points"].getint("AI2_PTS")), True, (255, 255, 255))
                shoot = False
           
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