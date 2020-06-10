import pygame
from Source import UI_functions as UI

def run(screen, bg, cfg):
    screen = pygame.display.set_mode((350,450))
    font = pygame.font.Font("Assets/Font/overpass-regular.otf", 26)
    font_s = pygame.font.Font("Assets/Font/overpass-regular.otf", 14)
    texts = [font.render("X Map range", True, (255, 255, 255)), 
             font.render("Y Map range", True, (255, 255, 255)),
             font.render("No. of algorithm", True, (255, 255, 255)),
             font.render("Try to generate map:", True, (255,255,255)),
             font_s.render("Try it now", True, (255,255,255))]
    rects_options, text_pos = UI.Rect_Options()
    RUNNING = True
    CLICK = False
    
    while RUNNING:
        dt = pygame.time.Clock().tick(cfg["Basic"].getint("FPS")) / 1000.0
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        
        UI.Draw_Text_Pos(screen, texts, text_pos)
        UI.Draw_Red_Btn(screen, rects_options)
        
        if rects_options[6].collidepoint((mx,my)) and CLICK:
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