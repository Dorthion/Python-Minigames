import pygame
from Source import Settings as Set
from Source import UI_functions as UI
from Source import Set_Player_ai_game as spa           #spa - set player ai
from Source import Play_Player_ai_game as ppa          #ppa - play player ai

#Init
pygame.init()
screen = pygame.display.set_mode((Set.WIDTH,Set.HEIGHT))
pygame.display.set_caption(Set.TITLE)

#Resources (Images, Icons, Fonts)
icon = pygame.image.load("Assets/Images/ship.png")
bg = pygame.image.load("Assets/Images/CleanBackground.png")
#font = pygame.font.Font("Assets/Font/overpass-regular.otf", 12) #now unnecessary
pygame.display.set_icon(icon)

#Initial values
screen.blit(bg,(0,0))
rects = UI.Rect_Main_Menu()

#InGame
#try:
while Set.RUNNING:
    #Screen properties per update
    dt = pygame.time.Clock().tick(Set.FPS) / 1000.0    #DeltaTime
    mx, my = pygame.mouse.get_pos()
    screen.blit(bg,(0,0))

    #Draw
    UI.Draw_Red_Btn(screen, rects)   

    if rects[0].collidepoint((mx,my)):
        if Set.CLICK:
            Set.CLICK = False
            Temp_width = Set.WIDTH
            Temp_height = Set.HEIGHT
            print("Set")
            pmab, bmap = spa.Play_Game(screen, bg)
            print("Play")
            ppa.Play_Game(screen, bg,pmab, bmap)
            print("End")
            Set.WIDTH = Temp_width
            Set.HEIGHT = Temp_height
            screen = pygame.display.set_mode((Set.WIDTH,Set.HEIGHT))

    #Events and update
    if rects[3].collidepoint((mx,my)):
        if Set.CLICK:
            Set.RUNNING = False
            break

    pygame.display.update()
    Set.CLICK = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Set.RUNNING = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Set.CLICK = True
pygame.quit()
#except:
#    pygame.quit()