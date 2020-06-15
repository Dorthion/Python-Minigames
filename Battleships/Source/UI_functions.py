import pygame

def load_config_file(config):
    global cfg
    cfg = config

#Colors
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

#Rect buttons
def Rect_Main_Menu():
    return [pygame.Rect(38,480,122,56),                                                                      #btn_play_player_ai
            pygame.Rect(236,480,122,56),                                                                     #btn_play_ai_ai
            pygame.Rect(434,480,122,56),                                                                     #btn_options
            pygame.Rect(632,480,122,56),                                                                     #btn_quit
           ],[(40,490),                                                                                      #btn_play_player_ai_text
            (260,490),                                                                                       #btn_play_ai_ai_text
            (454,490),                                                                                       #btn_options_text
            (670,490)]                                                                                       #btn_quit_text

def Rect_Player_AI_Set():
    return [pygame.Rect(700,50,80,40),                                                                       #btnhidebot
            pygame.Rect(600,50,80,40),                                                                       #btnrandbot
            pygame.Rect((cfg["Basic"].getint("WIDTH")/2) - 50,40,100,40),                                    #btnplay
            pygame.Rect(25,25,50,50)]                                                                        #Exit_btn

def Rect_Player_AI_Play():
    return [pygame.Rect(25,25,50,50),                                                                        #btnsurrender
           ],[(cfg["Basic"].getint("WIDTH")/4 - 50, 30),                                                     #text_player
           ((cfg["Basic"].getint("WIDTH")/4) * 3, 30),                                                       #text_ai
           ((cfg["Basic"].getint("WIDTH")/2)-65, cfg["Basic"].getint("HEIGHT") - 100),                       #text_score
           ((cfg["Basic"].getint("WIDTH")/2)-40, cfg["Basic"].getint("HEIGHT") - 65)]                        #text_actual_score

def Rect_AI_AI_Set():
    return [pygame.Rect((cfg["Basic"].getint("WIDTH")/2) - 49, 27, 100, 46),                                 #Run_game
            pygame.Rect(30, 30, 50, 50),                                                                     #Exit_btn
            pygame.Rect((cfg["Basic"].getint("WIDTH")/4) - 38, cfg["Basic"].getint("HEIGHT") - 74, 100, 48), #Ai1_gen
            pygame.Rect((cfg["Basic"].getint("WIDTH")/4)*3 - 60, cfg["Basic"].getint("HEIGHT") - 74, 100, 48)#Ai2_gen
            ],[((cfg["Basic"].getint("WIDTH")/2) - 55,20),                                                   #Run_game_image
            (25, 25, 50, 50),                                                                                #Exit_btn_image
            ((cfg["Basic"].getint("WIDTH")/4) - 44, cfg["Basic"].getint("HEIGHT") - 80),                     #Ai1_gen_image
            ((cfg["Basic"].getint("WIDTH")/4) * 3 - 66, cfg["Basic"].getint("HEIGHT") - 80)                  #Ai2_gen_image
            ],[((cfg["Basic"].getint("WIDTH")/2) - 20,32),                                                   #Run_game
            (48, 40),                                                                                        #Exit_btn
            ((cfg["Basic"].getint("WIDTH")/4) - 20, cfg["Basic"].getint("HEIGHT") - 68),                     #Ai1_gen
            ((cfg["Basic"].getint("WIDTH")/4)*3 - 40, cfg["Basic"].getint("HEIGHT") - 68),                   #Ai2_gen
            ((cfg["Basic"].getint("WIDTH")/4) + 15, cfg["Basic"].getint("HEIGHT") - 78),                     #Ai1_ref
            ((cfg["Basic"].getint("WIDTH")/4)*3 - 5, cfg["Basic"].getint("HEIGHT") - 78),                    #Ai2_ref
            (cfg["Basic"].getint("WIDTH")/4 - 10, 30),                                                       #text_player
            ((cfg["Basic"].getint("WIDTH")/4) * 3 - 35, 30),                                                 #text_ai
            ((cfg["Basic"].getint("WIDTH")/2) - 50, cfg["Basic"].getint("HEIGHT") - 95),                     #text_score
            ((cfg["Basic"].getint("WIDTH")/2) - 30, cfg["Basic"].getint("HEIGHT") - 55)]                     #text_actual_score
             
def Rect_Player_AI_Map():
    return pygame.Rect(50,100,34*cfg["Rules"].getint("X_RANGE"),34*cfg["Rules"].getint("Y_RANGE"))   #btnplayer

def Rect_Options():
    return [pygame.Rect(290,25,30,30),   #X_RANGE_BOX_-
            pygame.Rect(355,25,30,30),   #X_RANGE_BOX_+
            pygame.Rect(290,85,30,30),   #Y_RANGE_BOX_-
            pygame.Rect(355,85,30,30),   #Y_RANGE_BOX_+
            pygame.Rect(290,145,30,30),  #ALG_BOX_-
            pygame.Rect(355,145,30,30),  #ALG_BOX_+
            pygame.Rect(290,205,30,30),  #FPS_BOX_-
            pygame.Rect(355,205,30,30),  #FPS_BOX_+
            pygame.Rect(290,265,30,30),  #SHIP_SIZE_BOX_-
            pygame.Rect(355,265,30,30),  #SHIP_SIZE_BOX_+
            pygame.Rect(280,380,100,40), #EXIT_AND_SAVE_BOX
            pygame.Rect(20,380,100,40),  #EXIT_WITHOUT_SAVE_BOX
            pygame.Rect(165,340,75,24)   #TRY_IT_BOX
           ],[(50,20),                   #X_RANGE_TEXT
            (50,80),                     #Y_RANGE_TEXT
            (30,140),                    #No_ALG_TEXT
            (50,300),                    #Try_gen_TEXT
            (170,340),                   #Try_gen_btn_TEXT
            (300,23),(362,23),           #X_RANGE_-/+_TEXT
            (300,83),(362,83),           #Y_RANGE_-/+_TEXT
            (300,143),(362,143),         #NO_ALG_-/+_TEXT
            (330,32),                    #VAL_XRANGE
            (330,92),                    #VAL_YRANGE
            (330,152),                   #VAL_ALG
            (330,212),                   #VAL_FPS
            (330,272),                   #VAL_SHIP_SIZE
            (10,200),                    #FPS_TEXT
            (80,260),                    #SHIP_SIZE_TEXT   
            (300,203),(362,203),         #FPS_-/+_TEXT
            (300,263),(362,263),         #SHIP_SIZE_-/+_TEXT
            (40,383),(300,383)]          #EXIT/SAVE_TEXT

#Draw functions
def Draw_Red_Btn(screen, rects):
    for i in rects:
        pygame.draw.rect(screen, RED, i)
        
def Draw_Pos(screen, list_of_object, position_object):
    for i in range(len(list_of_object)):
        screen.blit(list_of_object[i],(position_object[i][0],position_object[i][1]))

def Draw_Left_Map_Set(screen, Map, grid):
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Map[y][x] == 0:
                pygame.draw.rect(screen, BLUE, (50 + 34 * x, 100 + 34 * y, 32, 32))
            if Map[y][x] == 1:
                pygame.draw.rect(screen, GREEN, (50 + 34 * x, 100 + 34 * y, 32, 32))
            if Map[y][x] == 2:
                pygame.draw.rect(screen, RED, (50 + 34 * x, 100 + 34 * y, 32, 32))
            screen.blit(grid,(50 + 34 * x, 100 + 34 * y))

def Draw_Right_Map_Set(screen, Map, grid):
    wd, ht = New_Resolution()
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Map[y][x] == 0:
                pygame.draw.rect(screen, BLUE, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Map[y][x] == 1:
                pygame.draw.rect(screen, GREEN, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Map[y][x] == 2:
                pygame.draw.rect(screen, RED, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            screen.blit(grid,(((wd / 2) + 25 + 34 * x, 100 + 34 * y)))

def Draw_Left_Map_Play(screen, Map, grid):
    wd, ht = New_Resolution()
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Map[y][x] in [0, 1, 2, 5]:
                pygame.draw.rect(screen, BLUE, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Map[y][x] == 3:
                pygame.draw.rect(screen, GREEN, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Map[y][x] == 4:
                pygame.draw.rect(screen, RED, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            screen.blit(grid,(((wd / 2) + 25 + 34 * x, 100 + 34 * y)))
                        
def Draw_Right_Map_Play(screen, Map, grid):
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Map[y][x] in [0, 1, 2, 5]:
                pygame.draw.rect(screen, BLUE, (50 + 34 * x, 100 + 34 * y, 32, 32))
            if Map[y][x] == 3:
                pygame.draw.rect(screen, GREEN, (50 + 34 * x, 100 + 34 * y, 32, 32))
            if Map[y][x] == 4:
                pygame.draw.rect(screen, RED, (50 + 34 * x, 100 + 34 * y, 32, 32))
            screen.blit(grid,(50 + 34 * x, 100 + 34 * y))
                
def Update_Screen_Values(screen, bg):
    wd, ht = New_Resolution()
    screen = pygame.display.set_mode((wd, ht))
    bg = pygame.transform.scale(bg, (wd, ht))
    
    return screen, bg

def New_Resolution():
    WIDTH = 150 + cfg["Rules"].getint("X_RANGE") * 68
    HEIGHT = 200 + cfg["Rules"].getint("Y_RANGE") * 34
    cfg.set("Basic","WIDTH",str(WIDTH))
    cfg.set("Basic","HEIGHT",str(HEIGHT))
    return WIDTH, HEIGHT