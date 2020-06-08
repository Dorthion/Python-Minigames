import pygame
import numpy as np
from Source import Settings as Set
from Source import UI_functions as UI
from Source import battleships_functions_play as play

def Play_Game(screen, bg, Ptab, Bmap):
    screen, bg = UI.Update_Screen_Values(screen, bg)
    font = pygame.font.Font("Assets/Font/overpass-regular.otf", 40)

    #Initial Values
    rect_map = UI.Rect_Player_AI_Map()
    rects_play, text_pos = UI.Rect_Player_AI_Play()
    texts = [font.render(Set.PLAYER, True, (255, 255, 255)), 
             font.render(Set.AI, True, (255, 255, 255))]
    
    #InGame
    while Set.RUNNING:
        #Screen properties per update
        dt = pygame.time.Clock().tick(Set.FPS) / 1000.0    #DeltaTime
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Red_Btn(screen, rects_play)
        UI.Draw_Text_Pos(screen, texts, text_pos)
        UI.Draw_Player_Map_Play(screen, Ptab)
        UI.Draw_Player_AI2_Play(screen, Bmap)
        
        #Clickable buttons 
        if rect_map.collidepoint((mx,my)) and Set.CLICK:
            if mx >= 50 and mx < 50+34*Set.X_RANGE and my >= 100 and my < 100+34*Set.Y_RANGE:
                Bmap, shooted = play.Player_shot(Bmap,my - 100,mx - 50)
                if shooted:
                    Ptab = play.AI_shot(Ptab)

        if rects_play[0].collidepoint((mx,my)):
            if Set.CLICK:
                print("Surrendered")
                return

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