import pygame
from Source import UI_functions as UI

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
                           
    rects_options, text_pos = UI.Rect_Options()
    RUNNING = True
    CLICK = False
    
    while RUNNING:
        dt = pygame.time.Clock().tick(cfg["Basic"].getint("FPS")) / 1000.0
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        
        UI.Draw_Red_Btn(screen, rects_options)
        UI.Draw_Text_Pos(screen, texts, text_pos)
        
        if rects_options[11].collidepoint((mx,my)) and CLICK:
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