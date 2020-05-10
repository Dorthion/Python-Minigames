import pygame
from Source import Settings as Set
from Source import UI_functions as UI
from Source import Player_ai_game as aig

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
            aig.Play_Game(screen, bg)
            Set.RUNNING = False
            break
    
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