import pygame
import numpy as np
from Source import UI_functions as UI
from Source import battleships_functions_bot as bfb
from Source import battleships_functions_check as bfc

def Play_Game(screen, bg, cfg):
    
    #Init
    screen, bg = UI.Update_Screen_Values(screen, bg)
    pygame.time.Clock().tick(cfg["Basic"].getint("FPS"))
    
    #Resources (Images, Icons, Fonts)
    font = pygame.font.Font("Assets/Font/impact.ttf", 26)
    font_b = pygame.font.Font("Assets/Font/impact.ttf", 40)
    font_c = pygame.font.SysFont('segoeuisymbol', 34)
    square = pygame.image.load("Assets/Images/Square.png")
    rectangle = pygame.image.load("Assets/Images/Rectangle.png")
    grid = pygame.image.load("Assets/Images/WhiteGrid.png")

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
    rects, images_pos, text_pos = UI.Rect_AI_AI_Set()
    rect_map = UI.Rect_Player_AI_Map()
    images = [rectangle, square, rectangle, rectangle]
    texts = [font.render("PLAY", True, (52, 52, 54)),
             font.render("χ", True, (52, 52, 54)),
             font.render("AI 1", True, (52, 52, 54)),
             font.render("AI 2", True, (52, 52, 54)),
             font_c.render("⟳", True, (52, 52, 54)),
             font_c.render("⟳", True, (52, 52, 54)),
             font_b.render(cfg["Text"]["AI1"], True, (255, 255, 255)), 
             font_b.render(cfg["Text"]["AI2"], True, (255, 255, 255)),
             font_b.render(cfg["Text"]["SCORE"], True, (255, 255, 255)),
             font_b.render(str(cfg["Points"].getint("AI1_PTS")) + " - " + str(cfg["Points"].getint("AI2_PTS")), True, (255, 255, 255))]
    
    #InGame
    while RUNNING:
        
        #Screen properties per update
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions
        UI.Draw_Left_Map_Set(screen, Bmap1, grid)
        UI.Draw_Right_Map_Set(screen, Bmap2, grid)
        UI.Draw_Pos(screen, images, images_pos)
        UI.Draw_Pos(screen, texts, text_pos)
        
        #Clickable buttons
        if CLICK:
            if rects[0].collidepoint((mx,my)):
                return Bmap1, Bmap2, True
        
        if CLICK:
            if rects[1].collidepoint((mx,my)):
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