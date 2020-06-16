import pygame
from Source import UI_functions as UI
from configparser import ConfigParser

def run(screen, bg, cfg):
    
    #Init
    screen = pygame.display.set_mode((400,450))
    pygame.time.Clock().tick(cfg["Basic"].getint("FPS"))
    X_RANGE_VAL = cfg["Rules"].getint("X_RANGE")
    Y_RANGE_VAL = cfg["Rules"].getint("Y_RANGE")
    SHIP_SIZE_VAL = cfg["Rules"].getint("SHIP_SIZE")
    ALG_VAL1 = cfg["Basic"].getint("ALG1")
    ALG_VAL2 = cfg["Basic"].getint("ALG2")
    FPS_VAL = cfg["Basic"].getint("FPS")
    
    font_b = pygame.font.Font("Assets/Font/impact.ttf", 32)
    font = pygame.font.Font("Assets/Font/impact.ttf", 26)
    font_s = pygame.font.Font("Assets/Font/impact.ttf", 14) 
    
    square = pygame.image.load("Assets/Images/Square.png")
    square = pygame.transform.scale(square, (40, 40))
    rectangle = pygame.image.load("Assets/Images/Rectangle.png")
    
    texts = [font_b.render("X Map range", True, (192,192,192)), 
             font_b.render("Y Map range", True, (192,192,192)),
             font_b.render("AI 1 algorithm", True, (192,192,192)),
             font_b.render("AI 2 algorithm", True, (192,192,192)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font_s.render(str(X_RANGE_VAL), True, (255,255,255)),
             font_s.render(str(Y_RANGE_VAL), True, (255,255,255)),
             font_s.render(str(ALG_VAL1), True, (255,255,255)),
             font_s.render(str(ALG_VAL2), True, (255,255,255)),
             font_s.render(str(FPS_VAL), True, (255,255,255)),
             font_s.render(str(SHIP_SIZE_VAL), True, (255,255,255)),
             font_b.render("Frames Per Second", True, (192,192,192)),
             font_b.render("Ship Size", True, (192,192,192)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("Exit", True, (52, 52, 54)),
             font.render("Save", True, (52, 52, 54))]
    
    #Exit, Save and Exit, 12 * +/- buttons
    images = [rectangle, rectangle]
    for i in range(12):
        images.append(square)
    
    fps_list = list(range(10,1001,10))
    pos_of_fps_list = int((FPS_VAL / 10) - 1)
    rects_options, images_pos, text_pos = UI.Rect_Options()
    RUNNING = True
    CLICK = False
    
    while RUNNING:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        
        #Draw
        UI.Draw_Pos(screen, images, images_pos)
        UI.Draw_Pos(screen, texts, text_pos)
        
        #Click buttons
        if CLICK:
            #X_RANGE
            if rects_options[0].collidepoint((mx,my)) and X_RANGE_VAL - 1 > 4:
                X_RANGE_VAL -= 1
                texts[10] = font_s.render(str(X_RANGE_VAL), True, (255,255,255))
                cfg.set("Rules","X_RANGE",str(X_RANGE_VAL))
            if rects_options[1].collidepoint((mx,my)) and X_RANGE_VAL + 1 <= 100:
                X_RANGE_VAL += 1
                texts[10] = font_s.render(str(X_RANGE_VAL), True, (255,255,255))
                cfg.set("Rules","X_RANGE",str(X_RANGE_VAL))
            
            #Y_RANGE
            if rects_options[2].collidepoint((mx,my)) and Y_RANGE_VAL - 1 > 4:
                Y_RANGE_VAL -= 1
                texts[11] = font_s.render(str(Y_RANGE_VAL), True, (255,255,255))
                cfg.set("Rules","Y_RANGE",str(Y_RANGE_VAL))
            if rects_options[3].collidepoint((mx,my)) and Y_RANGE_VAL + 1 <= 100:
                Y_RANGE_VAL += 1
                texts[11] = font_s.render(str(Y_RANGE_VAL), True, (255,255,255))
                cfg.set("Rules","Y_RANGE",str(Y_RANGE_VAL))
                
            #ALG1   
            if rects_options[4].collidepoint((mx,my)) and ALG_VAL1 - 1 > 0:
                ALG_VAL1 -= 1
                texts[12] = font_s.render(str(ALG_VAL1), True, (255,255,255))
                cfg.set("Basic","ALG1",str(ALG_VAL1))
            if rects_options[5].collidepoint((mx,my)) and ALG_VAL1 + 1 <= 2:
                ALG_VAL1 += 1
                texts[12] = font_s.render(str(ALG_VAL1), True, (255,255,255))
                cfg.set("Basic","ALG1",str(ALG_VAL1))
                
            #ALG2   
            if rects_options[6].collidepoint((mx,my)) and ALG_VAL2 - 1 > 0:
                ALG_VAL2 -= 1
                texts[13] = font_s.render(str(ALG_VAL2), True, (255,255,255))
                cfg.set("Basic","ALG2",str(ALG_VAL2))
            if rects_options[7].collidepoint((mx,my)) and ALG_VAL2 + 1 <= 2:
                ALG_VAL2 += 1
                texts[13] = font_s.render(str(ALG_VAL2), True, (255,255,255))
                cfg.set("Basic","ALG2",str(ALG_VAL2))
            
            #FPS
            if rects_options[8].collidepoint((mx,my)) and pos_of_fps_list - 1 >= 0:
                pos_of_fps_list -= 1
                FPS_VAL = fps_list[pos_of_fps_list]
                texts[14] = font_s.render(str(FPS_VAL), True, (255,255,255))
                cfg.set("Basic","FPS",str(FPS_VAL))
            if rects_options[9].collidepoint((mx,my)) and pos_of_fps_list + 1 < 100:
                pos_of_fps_list += 1
                FPS_VAL = fps_list[pos_of_fps_list]
                texts[14] = font_s.render(str(FPS_VAL), True, (255,255,255))
                cfg.set("Basic","FPS",str(FPS_VAL))
            
            #SHIP_SIZE
            if rects_options[10].collidepoint((mx,my)) and SHIP_SIZE_VAL - 1 > 0:
                SHIP_SIZE_VAL -= 1
                texts[15] = font_s.render(str(SHIP_SIZE_VAL), True, (255,255,255))
                cfg.set("Rules","SHIP_SIZE",str(SHIP_SIZE_VAL))
            if rects_options[11].collidepoint((mx,my)) and SHIP_SIZE_VAL + 1 <= 40:
                SHIP_SIZE_VAL += 1
                texts[15] = font_s.render(str(SHIP_SIZE_VAL), True, (255,255,255))
                cfg.set("Rules","SHIP_SIZE",str(SHIP_SIZE_VAL))
                
            #EXIT and SAVE & EXIT            
            if rects_options[12].collidepoint((mx,my)):
                print("Save and back from Options")
                return cfg, True
            if rects_options[13].collidepoint((mx,my)):
                print("Back from Options")
                return cfg, False
                
        pygame.display.update()

        CLICK = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    CLICK = True
                    
def save_new_conf(cfg):
    config = ConfigParser()

    #Basic Settings of App
    config["Basic"] = {
        "TITLE":"Battleships",
        "WIDTH":"800",
        "HEIGHT":"600",
        "FPS":cfg["Basic"]["FPS"],
        "ALG1":cfg["Basic"]["ALG1"],
        "ALG2":cfg["Basic"]["ALG2"]
    }

    #Game Rules
    config["Rules"] = {
        "SHIP_SIZE":cfg["Rules"]["SHIP_SIZE"],
        "X_RANGE":cfg["Rules"]["X_RANGE"],
        "Y_RANGE":cfg["Rules"]["Y_RANGE"]
    }

    #Text
    config["Text"] = {
        "PLAYER":"PLAYER",
        "AI":"AI",
        "AI1":"AI 1",
        "AI2":"AI 2",
        "SCORE":"SCORE"
    }

    #Points
    config["Points"] = {
        "PLAYER_PTS":cfg["Points"]["PLAYER_PTS"],
        "AI_PTS":cfg["Points"]["AI_PTS"],
        "AI1_PTS":"0",
        "AI2_PTS":"0"
    }

    with open('./cfg.ini', 'w') as f:
        config.write(f)
    return config