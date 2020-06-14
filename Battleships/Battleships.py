import pygame
import os.path
import sys
from configparser import ConfigParser
from Source import Config as config
from Source import UI_functions as UI
from Source import Set_Player_ai_game as spa           #spa - set player ai
from Source import Play_Player_ai_game as ppa          #ppa - play player ai
from Source import Set_Ai_ai_game as saa               #saa - set ai ai
from Source import Play_ai_ai_game as paa              #paa - play ai ai
from Source import Options_game as opt

#Init
global cfg
cfg = ConfigParser()
if os.path.isfile("./cfg.ini") == False:
    cfg = config.create_new_config() 
else:
    cfg.read("./cfg.ini")

pygame.init()
UI.load_config_file(cfg)
screen = pygame.display.set_mode((cfg["Basic"].getint("WIDTH"),cfg["Basic"].getint("HEIGHT")))
pygame.display.set_caption(cfg["Basic"]["TITLE"])

#Resources (Images, Icons, Fonts)
icon = pygame.image.load("Assets/Images/ship.png")
bg = pygame.image.load("Assets/Images/CleanBackground.png")
#font = pygame.font.Font("Assets/Font/overpass-regular.otf", 12) #now unnecessary
pygame.display.set_icon(icon)

#Initial values
screen.blit(bg,(0,0))
rects = UI.Rect_Main_Menu()
CLICK = False
RUNNING = True

#InGame
while RUNNING:
    #Screen properties per update
    dt = pygame.time.Clock().tick(cfg["Basic"].getint("FPS")) / 1000.0    #DeltaTime
    mx, my = pygame.mouse.get_pos()
    screen.blit(bg,(0,0))

    #Draw
    UI.Draw_Red_Btn(screen, rects)   

    if CLICK:
        Temp_width = cfg["Basic"].getint("WIDTH")
        Temp_height = cfg["Basic"].getint("HEIGHT")
        if rects[0].collidepoint((mx,my)):   #Play_Player_vs_AI
            print("Set")
            pmab, bmap = spa.Play_Game(screen, bg, cfg)
            print("Play")
            ppa.Play_Game(screen, bg,pmab, bmap, cfg)
            print("End")
            screen = pygame.display.set_mode((Temp_width,Temp_height))

        if rects[1].collidepoint((mx,my)):   #Play_AI_vs_AI
            play = True
            while play == True:
                print("Set")
                bmap1, bmap2, play = saa.Play_Game(screen, bg, cfg)
                if play == True:
                    print("Play")
                    play = paa.Play_Game(screen, bg, bmap1, bmap2, cfg)
                print("End")

        if rects[2].collidepoint((mx,my)):   #Options
            config, changed_game_opt = opt.run(screen, bg, cfg)
            if changed_game_opt:
                print("Save new config file")
                cfg = opt.save_new_conf(config)
        cfg.set("Basic","WIDTH",str(Temp_width))
        cfg.set("Basic","HEIGHT",str(Temp_height))        
        screen = pygame.display.set_mode((Temp_width,Temp_height))
        
        #Events and update
        if rects[3].collidepoint((mx,my)):   #Exit_Game
            RUNNING = False
            break

    pygame.display.update()
    CLICK = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                CLICK = True
pygame.display.quit()
pygame.quit()
quit()