import pygame
import numpy as np
from Source import UI_functions as UI
from Source import battleships_functions_play as play

def Play_Game(screen, bg, Bmap1, Bmap2, cfg):
    font = pygame.font.Font("Assets/Font/overpass-regular.otf", 40)
    screen, bg = UI.Update_Screen_Values(screen, bg)
    #pygame.time.Clock().tick(cfg["Basic"].getint("FPS"))

    #Initial Values
    CLICK = False
    RUNNING = True
    play.load_config_file(cfg)
    rect_map = UI.Rect_Player_AI_Map()
    rects_play, text_pos = UI.Rect_Player_AI_Play()
    texts = [font.render(cfg["Text"]["AI1"], True, (255, 255, 255)), 
             font.render(cfg["Text"]["AI2"], True, (255, 255, 255)),
             font.render(cfg["Text"]["SCORE"], True, (255, 255, 255)),
             font.render(str(cfg["Points"].getint("AI1_PTS")) + " - " + str(cfg["Points"].getint("AI2_PTS")), True, (255, 255, 255))]
    
    AI1 = play.PlayBot(Bmap1)
    AI2 = play.PlayBot(Bmap2)
    ai1_win_con = False
    ai2_win_con = False
    shoot = True
    #InGame
    while RUNNING:
        #Screen properties per update
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Red_Btn(screen, rects_play)
        UI.Draw_Text_Pos(screen, texts, text_pos)
        UI.Draw_Player_Map_Play(screen, Bmap1)
        UI.Draw_Player_AI2_Play(screen, Bmap2)
        
        #Clickable buttons 
        if rects_play[0].collidepoint((mx,my)) and CLICK:
            print("End of simulation")
            return True
        
        #pygame.time.wait(500)
        
        if shoot:
                #Bmap1 = play.AI_shot(Bmap1,1)
                AI1.AI_shot()
                if (1 in AI1.Map) == False:
                    ai1_win_con = True
                    cfg.set("Points","AI1_PTS",str(cfg["Points"].getint("AI1_PTS")+1))
                    shoot = False
        
        #pygame.time.wait(500)
        
        if shoot:
                #Bmap2 = play.AI_shot(Bmap2,2)
                AI2.AI_shot()
                if (1 in AI2.Map) == False:
                    ai2_win_con = True
                    cfg.set("Points","AI2_PTS",str(cfg["Points"].getint("AI2_PTS")+1))
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