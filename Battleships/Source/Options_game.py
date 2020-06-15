import pygame
from Source import UI_functions as UI
from configparser import ConfigParser

def run(screen, bg, cfg):
    screen = pygame.display.set_mode((400,450))
    X_RANGE_VAL = cfg["Rules"].getint("X_RANGE")
    Y_RANGE_VAL = cfg["Rules"].getint("Y_RANGE")
    SHIP_SIZE_VAL = cfg["Rules"].getint("SHIP_SIZE")
    ALG_VAL = cfg["Basic"].getint("ALG")
    FPS_VAL = cfg["Basic"].getint("FPS")
    
    font_b = pygame.font.Font("Assets/Font/overpass-regular.otf", 32)
    font = pygame.font.Font("Assets/Font/overpass-regular.otf", 26)
    font_s = pygame.font.Font("Assets/Font/overpass-regular.otf", 14) 
    
    texts = [font_b.render("X Map range", True, (255, 255, 255)), 
             font_b.render("Y Map range", True, (255, 255, 255)),
             font_b.render("No. of algorithm", True, (255, 255, 255)),
             font_b.render("Try to generate map:", True, (255,255,255)),
             font_s.render("Try it now", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font_s.render(str(X_RANGE_VAL), True, (255,255,255)),
             font_s.render(str(Y_RANGE_VAL), True, (255,255,255)),
             font_s.render(str(ALG_VAL), True, (255,255,255)),
             font_s.render(str(FPS_VAL), True, (255,255,255)),
             font_s.render(str(SHIP_SIZE_VAL), True, (255,255,255)),
             font_b.render("Frames Per Second", True, (255,255,255)),
             font_b.render("Ship Size", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("-", True, (255,255,255)),
             font.render("+", True, (255,255,255)),
             font.render("Exit", True, (255,255,255)),
             font.render("Save", True, (255,255,255))]
    
    fps_list = list(range(10,1001,10))
    pos_of_fps_list = int((FPS_VAL / 10) - 1)
    rects_options, text_pos = UI.Rect_Options()
    RUNNING = True
    CLICK = False
    
    while RUNNING:
        dt = pygame.time.Clock().tick(cfg["Basic"].getint("FPS")) / 1000.0
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        
        UI.Draw_Red_Btn(screen, rects_options)
        UI.Draw_Pos(screen, texts, text_pos)
        
        if CLICK:
            #X_RANGE
            if rects_options[0].collidepoint((mx,my)) and X_RANGE_VAL - 1 > 4:
                X_RANGE_VAL -= 1
                texts[11] = font_s.render(str(X_RANGE_VAL), True, (255,255,255))
                cfg.set("Rules","X_RANGE",str(X_RANGE_VAL))
            if rects_options[1].collidepoint((mx,my)) and X_RANGE_VAL + 1 <= 100:
                X_RANGE_VAL += 1
                texts[11] = font_s.render(str(X_RANGE_VAL), True, (255,255,255))
                cfg.set("Rules","X_RANGE",str(X_RANGE_VAL))
            
            #Y_RANGE
            if rects_options[2].collidepoint((mx,my)) and Y_RANGE_VAL - 1 > 4:
                Y_RANGE_VAL -= 1
                texts[12] = font_s.render(str(Y_RANGE_VAL), True, (255,255,255))
                cfg.set("Rules","Y_RANGE",str(Y_RANGE_VAL))
            if rects_options[3].collidepoint((mx,my)) and Y_RANGE_VAL + 1 <= 100:
                Y_RANGE_VAL += 1
                texts[12] = font_s.render(str(Y_RANGE_VAL), True, (255,255,255))
                cfg.set("Rules","Y_RANGE",str(Y_RANGE_VAL))
                
            #ALG    
            if rects_options[4].collidepoint((mx,my)) and ALG_VAL - 1 > 0:
                ALG_VAL -= 1
                texts[13] = font_s.render(str(ALG_VAL), True, (255,255,255))
                cfg.set("Basic","ALG",str(ALG_VAL))
            if rects_options[5].collidepoint((mx,my)) and ALG_VAL + 1 <= 2:
                ALG_VAL += 1
                texts[13] = font_s.render(str(ALG_VAL), True, (255,255,255))
                cfg.set("Basic","ALG",str(ALG_VAL))
            
            #FPS
            if rects_options[6].collidepoint((mx,my)) and pos_of_fps_list - 1 >= 0:
                pos_of_fps_list -= 1
                FPS_VAL = fps_list[pos_of_fps_list]
                texts[14] = font_s.render(str(FPS_VAL), True, (255,255,255))
                cfg.set("Basic","FPS",str(FPS_VAL))
            if rects_options[7].collidepoint((mx,my)) and pos_of_fps_list + 1 < 100:
                pos_of_fps_list += 1
                FPS_VAL = fps_list[pos_of_fps_list]
                texts[14] = font_s.render(str(FPS_VAL), True, (255,255,255))
                cfg.set("Basic","FPS",str(FPS_VAL))
            
            #SHIP_SIZE
            if rects_options[8].collidepoint((mx,my)) and SHIP_SIZE_VAL - 1 > 0:
                SHIP_SIZE_VAL -= 1
                texts[15] = font_s.render(str(SHIP_SIZE_VAL), True, (255,255,255))
                cfg.set("Rules","SHIP_SIZE",str(SHIP_SIZE_VAL))
            if rects_options[9].collidepoint((mx,my)) and SHIP_SIZE_VAL + 1 <= 40:
                SHIP_SIZE_VAL += 1
                texts[15] = font_s.render(str(SHIP_SIZE_VAL), True, (255,255,255))
                cfg.set("Rules","SHIP_SIZE",str(SHIP_SIZE_VAL))
                
            #EXIT and SAVE & EXIT            
            if rects_options[10].collidepoint((mx,my)):
                print("Save and back from Options")
                return cfg, True
            if rects_options[11].collidepoint((mx,my)):
                print("Back from Options")
                return cfg, False
            
            if rects_options[12].collidepoint((mx,my)):
                print("Try it button")
                
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
        "ALG":cfg["Basic"]["ALG"]
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
        "AI1":"AI1",
        "AI2":"AI2",
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