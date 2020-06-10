import pygame
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("./cfg.ini")

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
            pygame.Rect((cfg["Basic"].getint("WIDTH")/2) - 50,40,100,40)]                            #btnplay

def Rect_Player_AI_Play():
    return [pygame.Rect(25,25,50,50),                                                                #btnsurrender
           ],[(cfg["Basic"].getint("WIDTH")/4 - 50, 30),                                             #text_player
           ((cfg["Basic"].getint("WIDTH")/4) * 3, 30),                                               #text_ai
           ((cfg["Basic"].getint("WIDTH")/2)-65, cfg["Basic"].getint("HEIGHT") - 60),                #text_score
           ((cfg["Basic"].getint("WIDTH")/2)-20, cfg["Basic"].getint("HEIGHT") - 20)]                #text_actual_score         

def Rect_Player_AI_Map():
    return pygame.Rect(50,100,34*cfg["Rules"].getint("X_RANGE"),34*cfg["Rules"].getint("Y_RANGE"))   #btnplayer

def Rect_Options():
    return [pygame.Rect(240,25,30,30),
            pygame.Rect(305,25,30,30),
            pygame.Rect(240,85,30,30),
            pygame.Rect(305,85,30,30),
            pygame.Rect(240,145,30,30),
            pygame.Rect(305,145,30,30),
            pygame.Rect(230,380,100,40),
            pygame.Rect(20,380,100,40)
           ],[(50,20),
            (50,80),
            (30,140),
            (50,200),
            (150,250)]
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
            if Ptab[y][x] == 0 or Ptab[y][x] == 1 or Ptab[y][x] == 2:
                pygame.draw.rect(screen, BLUE, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Ptab[y][x] == 3:
                pygame.draw.rect(screen, GREEN, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
            if Ptab[y][x] == 4:
                pygame.draw.rect(screen, RED, ((wd / 2) + 25 + 34 * x, 100 + 34 * y, 32, 32))
                
def Draw_Player_AI2_Play(screen, Bmap):
    wd, ht = New_Resolution()
    for y in range(cfg["Rules"].getint("Y_RANGE")):
        for x in range(cfg["Rules"].getint("X_RANGE")):
            if Bmap[y][x] == 0 or Bmap[y][x] == 1 or Bmap[y][x] == 2:
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