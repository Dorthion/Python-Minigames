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
    return [pygame.Rect(38,480,122,56),                                                                         #btn_play_player_ai
            pygame.Rect(236,480,122,56),                                                                        #btn_play_ai_ai
            pygame.Rect(434,480,122,56),                                                                        #btn_options
            pygame.Rect(632,480,122,56),                                                                        #btn_quit
           ],[(40,490),                                                                                         #btn_play_player_ai_text
            (260,490),                                                                                          #btn_play_ai_ai_text
            (454,490),                                                                                          #btn_options_text
            (670,490)]                                                                                          #btn_quit_text

def Rect_Player_AI_Set():
    return [pygame.Rect(cfg["Basic"].getint("WIDTH") - 154, 30, 100, 46),                                       #btn_hide_ai
            pygame.Rect((cfg["Basic"].getint("WIDTH")/4)*3 - 60, cfg["Basic"].getint("HEIGHT") - 74, 100, 48),  #btn_ai_gen
            pygame.Rect((cfg["Basic"].getint("WIDTH")/2) - 49, 30, 100, 46),                                    #btn_play
            pygame.Rect(30, 28, 50, 50),                                                                        #btn_exit
            pygame.Rect((cfg["Basic"].getint("WIDTH")/4) - 38, cfg["Basic"].getint("HEIGHT") - 74, 100, 48)     #btn_player_gen
           ],[((cfg["Basic"].getint("WIDTH")) - 160, 23),                                                       #btn_hide_image
            ((cfg["Basic"].getint("WIDTH")/4) * 3 - 66, cfg["Basic"].getint("HEIGHT") - 80),                    #btn_ai_gen_image
            ((cfg["Basic"].getint("WIDTH")/2) - 55, 23),                                                        #btn_play_image
            (25, 23, 50, 50),                                                                                   #btn_exit_image
            ((cfg["Basic"].getint("WIDTH")/4) - 44, cfg["Basic"].getint("HEIGHT") - 80)                         #btn_player_gen_image
           ],[(cfg["Basic"].getint("WIDTH")/4 - 50, 30),                                                        #player_text
            ((cfg["Basic"].getint("WIDTH")/4) * 3 - 35, 30),                                                    #ai_text
            ((cfg["Basic"].getint("WIDTH")/2) - 50, cfg["Basic"].getint("HEIGHT") - 95),                        #score_text
            ((cfg["Basic"].getint("WIDTH")/2) - 30, cfg["Basic"].getint("HEIGHT") - 55),                        #actual_score_text
            (48, 32),                                                                                           #exit_text
            ((cfg["Basic"].getint("WIDTH")/2) - 20,35),                                                         #play_text
            ((cfg["Basic"].getint("WIDTH")/4) - 25, cfg["Basic"].getint("HEIGHT") - 68),                        #gen_player_text
            ((cfg["Basic"].getint("WIDTH")/4)*3 - 45, cfg["Basic"].getint("HEIGHT") - 68),                      #gen_ai_text
            ((cfg["Basic"].getint("WIDTH")/4) + 15, cfg["Basic"].getint("HEIGHT") - 78),                        #ref_player_text
            ((cfg["Basic"].getint("WIDTH")/4)*3 - 5, cfg["Basic"].getint("HEIGHT") - 78),                       #ref_ai_text
            (cfg["Basic"].getint("WIDTH") - 130, 35)]                                                           #hide_text

def Rect_AI_AI_Set():
    return [pygame.Rect((cfg["Basic"].getint("WIDTH")/2) - 49, 30, 100, 46),                                    #Run_game
            pygame.Rect(30, 28, 50, 50),                                                                        #Exit_btn
            pygame.Rect((cfg["Basic"].getint("WIDTH")/4) - 38, cfg["Basic"].getint("HEIGHT") - 74, 100, 48),    #Ai1_gen
            pygame.Rect((cfg["Basic"].getint("WIDTH")/4)*3 - 60, cfg["Basic"].getint("HEIGHT") - 74, 100, 48)   #Ai2_gen
            ],[((cfg["Basic"].getint("WIDTH")/2) - 55,23),                                                      #Run_game_image
            (25, 23, 50, 50),                                                                                   #Exit_btn_image
            ((cfg["Basic"].getint("WIDTH")/4) - 44, cfg["Basic"].getint("HEIGHT") - 80),                        #Ai1_gen_image
            ((cfg["Basic"].getint("WIDTH")/4) * 3 - 66, cfg["Basic"].getint("HEIGHT") - 80)                     #Ai2_gen_image
            ],[((cfg["Basic"].getint("WIDTH")/2) - 20,35),                                                      #Run_game_text
            (48, 32),                                                                                           #Exit_btn_text
            ((cfg["Basic"].getint("WIDTH")/4) - 20, cfg["Basic"].getint("HEIGHT") - 68),                        #Ai1_gen_text
            ((cfg["Basic"].getint("WIDTH")/4)*3 - 40, cfg["Basic"].getint("HEIGHT") - 68),                      #Ai2_gen_text
            ((cfg["Basic"].getint("WIDTH")/4) + 15, cfg["Basic"].getint("HEIGHT") - 78),                        #Ai1_ref_text
            ((cfg["Basic"].getint("WIDTH")/4)*3 - 5, cfg["Basic"].getint("HEIGHT") - 78),                       #Ai2_ref_text
            (cfg["Basic"].getint("WIDTH")/4 - 10, 30),                                                          #text_player_text
            ((cfg["Basic"].getint("WIDTH")/4) * 3 - 35, 30),                                                    #text_ai_text
            ((cfg["Basic"].getint("WIDTH")/2) - 50, cfg["Basic"].getint("HEIGHT") - 95),                        #text_score_text
            ((cfg["Basic"].getint("WIDTH")/2) - 30, cfg["Basic"].getint("HEIGHT") - 55)]                        #text_actual_score_text
             
def Rect_Play():
    return [pygame.Rect(30,28,50,50),                                                                           #exit
           ],[(25, 23, 50, 50)                                                                                  #image_exit
           ],[(cfg["Basic"].getint("WIDTH")/4 - 10, 30),                                                        #text_left_player
           ((cfg["Basic"].getint("WIDTH")/4) * 3 - 35, 30),                                                     #text_right_player
           ((cfg["Basic"].getint("WIDTH")/2) - 50, cfg["Basic"].getint("HEIGHT") - 95),                         #text_score
           ((cfg["Basic"].getint("WIDTH")/2) - 30, cfg["Basic"].getint("HEIGHT") - 55),                         #text_actual_score
           (48, 32)]                                                                                            #text_exit

def Rect_Options():
    return [pygame.Rect(275,27,32,32),   #X_RANGE_BOX_-
            pygame.Rect(345,27,32,32),   #X_RANGE_BOX_+
            pygame.Rect(275,87,32,32),   #Y_RANGE_BOX_-
            pygame.Rect(345,87,32,32),   #Y_RANGE_BOX_+
            pygame.Rect(275,147,32,32),  #ALG1_BOX_-
            pygame.Rect(345,147,32,32),  #ALG1_BOX_+
            pygame.Rect(275,207,32,32),  #ALG2_BOX_-
            pygame.Rect(345,207,32,32),  #ALG2_BOX_+
            pygame.Rect(275,267,32,32),  #FPS_BOX_-
            pygame.Rect(345,267,32,32),  #FPS_BOX_+
            pygame.Rect(275,327,32,32),  #SHIP_SIZE_BOX_-
            pygame.Rect(345,327,32,32),  #SHIP_SIZE_BOX_+
            pygame.Rect(275,385,100,50), #EXIT_AND_SAVE_BOX
            pygame.Rect(25,385,100,50),  #EXIT_WITHOUT_SAVE_BOX
           ],[(20,380),                  #EXIT_WITHOUT_SAVE_IMAGE
            (270,380),                   #EXIT_IMAGE
            (270,23),(340,23),           #X_RANGE_-/+_IMAGE
            (270,83),(340,83),           #Y_RANGE_-/+_IMAGE
            (270,143),(340,143),         #NO_ALG_-/+_IMAGE
            (270,203),(340,203),         #FPS_-/+_IMAGE
            (270,263),(340,263),         #SHIP_SIZE_-/+_IMAGE
            (270,323),(340,323)          #SHIP_SIZE_-/+_IMAGE
            ],[(60,20),                  #X_RANGE_TEXT
            (60,80),                     #Y_RANGE_TEXT
            (50,140),                    #ALG_AI1_TEXT
            (50,200),                    #ALG_AI2_TEXT
            (286,23),(354,25),           #X_RANGE_-/+_TEXT
            (286,83),(354,85),           #Y_RANGE_-/+_TEXT
            (286,143),(354,145),         #NO_ALG_-/+_TEXT
            (318,32),                    #VAL_XRANGE
            (318,92),                    #VAL_YRANGE
            (324,152),                   #VAL_ALG
            (324,212),                   #VAL_ALG2
            (318,272),                   #VAL_FPS
            (324,332),                   #VAL_SHIP_SIZE
            (10,260),                    #FPS_TEXT
            (80,320),                    #SHIP_SIZE_TEXT
            (286,203),(354,205),         #FPS_-/+_TEXT
            (286,263),(354,265),         #SHIP_SIZE_-/+_TEXT
            (286,323),(354,325),         #SHIP_SIZE_-/+_TEXT
            (54,390),(305,390)]          #EXIT/SAVE_TEXT

def Rect_Player_AI_Map():
    return pygame.Rect(50,100,34*cfg["Rules"].getint("X_RANGE"),34*cfg["Rules"].getint("Y_RANGE"))              #btnplayer

#Draw functions       
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