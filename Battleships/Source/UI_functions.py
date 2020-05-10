import pygame
from Source.Settings import *

#Rect of Buttons
def Rect_Main_Menu():
    ttt = []
    btn_play_player_ai = pygame.Rect(280,100,100,80)
    btn_play_ai_ai = pygame.Rect(420,100,100,80)
    btn_options = pygame.Rect(350,200,100,80)
    btn_quit = pygame.Rect(350,500,100,80)
    ttt.append(btn_play_player_ai)
    ttt.append(btn_play_ai_ai)
    ttt.append(btn_options)
    ttt.append(btn_quit)
    return ttt
    
def Draw_Red_Btn(screen, rects):
    for i in rects:
        pygame.draw.rect(screen, RED, i)