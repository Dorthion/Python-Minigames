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
    return [pygame.Rect(280,100,100,80),                                                             #btn_play_player_ai
            pygame.Rect(420,100,100,80),                                                             #btn_play_ai_ai
            pygame.Rect(350,200,100,80),                                                             #btn_options
            pygame.Rect(350,500,100,80)]                                                             #btn_quit

def Rect_Player_AI_Set():
    return [pygame.Rect(700,50,80,40),                                                               #btnhidebot
            pygame.Rect(600,50,80,40),                                                               #btnrandbot
            pygame.Rect((cfg["Basic"].getint("WIDTH")/2) - 50,40,100,40),                            #btnplay
            pygame.Rect(25,25,50,50)]                                                                #Exit_btn

def Rect_Player_AI_Play():
    return [pygame.Rect(25,25,50,50),                                                                #btnsurrender
           ],[(cfg["Basic"].getint("WIDTH")/4 - 50, 30),                                             #text_player
           ((cfg["Basic"].getint("WIDTH")/4) * 3, 30),                                               #text_ai
           ((cfg["Basic"].getint("WIDTH")/2)-65, cfg["Basic"].getint("HEIGHT") - 100),               #text_score
           ((cfg["Basic"].getint("WIDTH")/2)-40, cfg["Basic"].getint("HEIGHT") - 65)]                #text_actual_score

def Rect_AI_AI_Set():
    return [pygame.Rect((cfg["Basic"].getint("WIDTH")/2) - 50,40,100,40),                            #Run_game
            pygame.Rect(25,25,50,50),                                                                #Exit_btn
            pygame.Rect((cfg["Basic"].getint("WIDTH")/2) - 100,40,40,40),                            #Ai1_gen
            pygame.Rect((cfg["Basic"].getint("WIDTH")/2) + 60,40,40,40)]                             #Ai2_gen
             
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
        
def Draw_Text_Pos(screen, texts, text_pos):
    for i in range(len(texts)):
        screen.blit(texts[i],(text_pos[i][0],text_pos[i][1]))

def Draw_Player_Map(screen, Ptab):
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Ptab[y][x] == 0:
                pygame.draw.rect(screen, BLUE, (50 + 34 * x, 100 + 34 * y, 32, 32))
            if Ptab[y][x] == 1:
                pygame.draw.rect(screen, GREEN, (50 + 34 * x, 100 + 34 * y, 32, 32))
            if Ptab[y][x] == 2:
                pygame.draw.rect(screen, RED, (50 + 34 * x, 100 + 34 * y, 32, 32))

def Draw_Player_AI1(screen, Bmap):
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Bmap[y][x] == 0:
                pygame.draw.rect(screen, BLUE, (55+34*x,111+34*y,32,32))
            if Bmap[y][x] == 1:
                pygame.draw.rect(screen, GREEN, (55+34*x,111+34*y,32,32))
            if Bmap[y][x] == 2:
                pygame.draw.rect(screen, RED, (55+34*x,111+34*y,32,32))
                
def Draw_Player_AI2(screen, Bmap):
    wd, ht = New_Resolution()
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Bmap[y][x] == 0:
                pygame.draw.rect(screen, BLUE, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Bmap[y][x] == 1:
                pygame.draw.rect(screen, GREEN, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Bmap[y][x] == 2:
                pygame.draw.rect(screen, RED, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))

def Draw_Player_Map_Play(screen, Ptab):
    wd, ht = New_Resolution()
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Ptab[y][x] == 0 or Ptab[y][x] == 1 or Ptab[y][x] == 2 or Ptab[y][x] == 5:
                pygame.draw.rect(screen, BLUE, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Ptab[y][x] == 3:
                pygame.draw.rect(screen, GREEN, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Ptab[y][x] == 4:
                pygame.draw.rect(screen, RED, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
                
def Draw_Player_AI2_Play(screen, Bmap):
    wd, ht = New_Resolution()
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Bmap[y][x] == 0 or Bmap[y][x] == 1 or Bmap[y][x] == 2 or Bmap[y][x] == 5: #Include later similar methods
                pygame.draw.rect(screen, BLUE, (50 + 34 * x, 100 + 34 * y, 32, 32))
            if Bmap[y][x] == 3:
                pygame.draw.rect(screen, GREEN, (50 + 34 * x, 100 + 34 * y, 32, 32))
            if Bmap[y][x] == 4:
                pygame.draw.rect(screen, RED, (50 + 34 * x, 100 + 34 * y, 32, 32))
                
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