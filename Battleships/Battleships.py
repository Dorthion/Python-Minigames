import pygame
import os.path
import sys
from configparser import ConfigParser
from Source import Config
from Source import UI_functions as UI                  #UI - User Interface
from Source import Set_Player_ai_game as spa           #spa - set player ai
from Source import Play_Player_ai_game as ppa          #ppa - play player ai
from Source import Set_Ai_ai_game as saa               #saa - set ai ai
from Source import Play_ai_ai_game as paa              #paa - play ai ai
from Source import Options_game as opt                 #opt - options

#Init config file
global cfg
cfg = ConfigParser()
if os.path.isfile("./cfg.ini") == False:
    cfg = Config.create_new_config() 
else:
    cfg.read("./cfg.ini")

#Init
pygame.init()
UI.load_config_file(cfg)
screen = pygame.display.set_mode((cfg["Basic"].getint("WIDTH"),cfg["Basic"].getint("HEIGHT")))
pygame.display.set_caption(cfg["Basic"]["TITLE"])
pygame.time.Clock().tick(cfg["Basic"].getint("FPS"))

#Resources (Images, Icons, Fonts)
icon = pygame.image.load("Assets/Images/ship.png")
bg = pygame.image.load("Assets/Images/CleanBackground.png")
menubg = pygame.image.load("Assets/Images/MenuGame.png")
font = pygame.font.Font("Assets/Font/impact.ttf", 24)
pygame.display.set_icon(icon)

#Initial values
CLICK = False
RUNNING = True
RUN_BTN = False
rects, text_pos = UI.Rect_Main_Menu()
texts = [font.render("PLAY PLAYER", True, (52, 52, 54)),
         font.render("PLAY AI", True, (52, 52, 54)),
         font.render("OPTIONS", True, (52, 52, 54)),
         font.render("EXIT", True, (52, 52, 54))] 

#InGame
while RUNNING:
    
    #Screen properties per update and Draw Buttons
    mx, my = pygame.mouse.get_pos()
    screen.blit(menubg,(0,0))
    UI.Draw_Pos(screen, texts, text_pos)
    
    #Buttons functions
    if CLICK:
        Temp_width = cfg["Basic"].getint("WIDTH")
        Temp_height = cfg["Basic"].getint("HEIGHT")
        
        #Play_Player_vs_AI
        if rects[0].collidepoint((mx,my)):   
            play = True
            RUN_BTN = True
            while play == True:
                pmab, bmap, play = spa.Play_Game(screen, bg, cfg)
                if play == True:
                    ppa.Play_Game(screen, bg, pmab, bmap, cfg)
        
        #Play_AI_vs_AI
        if rects[1].collidepoint((mx,my)):
            play = True
            RUN_BTN = True
            while play == True:
                bmap1, bmap2, play = saa.Play_Game(screen, bg, cfg)
                if play == True:
                    paa.Play_Game(screen, bg, bmap1, bmap2, cfg)
        
        #Options
        if rects[2].collidepoint((mx,my)):
            RUN_BTN = True
            config, changed_game_opt = opt.run(screen, bg, cfg)
            if changed_game_opt:
                cfg = opt.save_new_conf(config)
                UI.load_config_file(cfg)
        
        #Exit_Game
        if rects[3].collidepoint((mx,my)):
            RUNNING = False
            break
        
        if RUN_BTN == True:
            cfg.set("Basic","WIDTH", str(Temp_width))
            cfg.set("Basic","HEIGHT", str(Temp_height))        
            screen = pygame.display.set_mode((Temp_width, Temp_height))
        
        RUN_BTN = False
            
    #Events and update
    CLICK = False
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                CLICK = True
#Quit game
pygame.display.quit()
pygame.quit()