import pygame
import numpy as np
from Source import UI_functions as UI
from Source import battleships_functions_bot as bfb
from Source import battleships_functions_player as bfp
from Source import battleships_functions_check as bfc

def Play_Game(screen, bg, cfg):
    
    #Init
    screen, bg = UI.Update_Screen_Values(screen, bg)
    pygame.time.Clock().tick(cfg["Basic"].getint("FPS"))
    
    #Resources (Images, Icons, Fonts)
    haha = pygame.image.load("Assets/Images/haha.jpg")
    haha = pygame.transform.scale(haha, (34*cfg["Rules"].getint("X_RANGE"), 34*cfg["Rules"].getint("Y_RANGE")))
    square = pygame.image.load("Assets/Images/Square.png")
    rectangle = pygame.image.load("Assets/Images/Rectangle.png")
    grid = pygame.image.load("Assets/Images/WhiteGrid.png")
    font = pygame.font.Font("Assets/Font/impact.ttf", 26)
    font_b = pygame.font.Font("Assets/Font/impact.ttf", 40)
    font_c = pygame.font.SysFont('segoeuisymbol', 34)

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
    rects, images_pos, text_pos  = UI.Rect_Player_AI_Set()
    rect_map = UI.Rect_Player_AI_Map()
    Gen_again = font.render("GENERATE AGAIN MAP!", True, (1, 1, 1))
    images = [rectangle, rectangle, rectangle, square, rectangle]
    texts = [font_b.render(cfg["Text"]["PLAYER"], True, (255, 255, 255)), 
             font_b.render(cfg["Text"]["AI"], True, (255, 255, 255)),
             font_b.render(cfg["Text"]["SCORE"], True, (255, 255, 255)),
             font_b.render(str(cfg["Points"].getint("AI1_PTS")) + " - " + str(cfg["Points"].getint("AI2_PTS")), True, (255, 255, 255)),
             font.render("χ", True, (52, 52, 54)),
             font.render("PLAY", True, (52, 52, 54)),
             font.render("GEN.", True, (52, 52, 54)),
             font.render("GEN.", True, (52, 52, 54)),
             font_c.render("⟳", True, (52, 52, 54)),
             font_c.render("⟳", True, (52, 52, 54)),
             font.render("HIDE", True, (52, 52, 54))]

    #InGame
    while RUNNING:
        
        #Screen properties per update
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))

        #Draw functions 
        UI.Draw_Left_Map_Set(screen, Ptab, grid)
        UI.Draw_Right_Map_Set(screen, Bmap, grid)
        UI.Draw_Pos(screen, images, images_pos)
        UI.Draw_Pos(screen, texts, text_pos)
        
        #Clickable buttons 
        if CLICK:
            
            #Click on player map
            if rect_map.collidepoint((mx,my)):
                CANT_GENERATE = False
                if mx >= 50 and mx < 50+34*cfg["Rules"].getint("X_RANGE") and my >= 100 and my < 100+34*cfg["Rules"].getint("Y_RANGE"):
                    Ptab = bfp.change_ship(Ptab,my - 100, mx - 50)
            
            #Hide AI Map
            if rects[0].collidepoint((mx,my)):
                if SHOW_HAHA:
                    SHOW_HAHA = False
                else:
                    SHOW_HAHA = True

            #Generate again AI Map        
            if rects[1].collidepoint((mx,my)):
                Bmap = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
                Bmap, CANT_GENERATE = bfb.generate_bot_ships(Bmap)
            
            
            #Play game Player vs AI
            if rects[2].collidepoint((mx,my)):
                CANT_GENERATE = False
                lista = bfc.check_ship_size(Ptab)
                Ptab = np.where(Ptab == 4,1,Ptab)
                if bfc.check_player_map(lista):
                    return Ptab, Bmap, True
                else: 
                    CANT_GENERATE = True
            
            #Exit
            if rects[3].collidepoint((mx,my)):
                CANT_GENERATE = False
                print("Back to Menu")
                return None, None, False
            
            #Generate Map for player      
            if rects[4].collidepoint((mx,my)):
                Ptab = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
                Ptab, CANT_GENERATE = bfb.generate_bot_ships(Ptab)

        #Check to draw haha
        if(SHOW_HAHA == True):
            screen.blit(haha,((cfg["Rules"].getint("X_RANGE") * 34) + 100,100))
            
        if(CANT_GENERATE == True):
            screen.blit(Gen_again,((cfg["Basic"].getint("WIDTH")/8), cfg["Basic"].getint("HEIGHT")/2))

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