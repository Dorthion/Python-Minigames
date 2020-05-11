import pygame
from Source.Settings import *

#Rect buttons
def Rect_Main_Menu():
    return [pygame.Rect(280,100,100,80), #btn_play_player_ai
            pygame.Rect(420,100,100,80), #btn_play_ai_ai
            pygame.Rect(350,200,100,80), #btn_options
            pygame.Rect(350,500,100,80)] #btn_quit

def Rect_Player_AI():
    return [pygame.Rect(700,50,80,40), #btnhidebot
            pygame.Rect(600,50,80,40)] #btnrandbot

def Rect_Player_AI_Map():
    return pygame.Rect(55,111,339,339) #btnplayer

#Draw functions
def Draw_Red_Btn(screen, rects):
    for i in rects:
        pygame.draw.rect(screen, RED, i)

def Draw_Player_Map(screen, Ptab):
    for y in range(Y_RANGE):
        for x in range(X_RANGE):
            if Ptab[y][x] == 0:
                pygame.draw.rect(screen, BLUE, (55+34*x,111+34*y,32,32))
            if Ptab[y][x] == 1:
                pygame.draw.rect(screen, GREEN, (55+34*x,111+34*y,32,32))
            if Ptab[y][x] == 2:
                pygame.draw.rect(screen, RED, (55+34*x,111+34*y,32,32))

def Draw_Player_AI1(screen, Bmap):
    for y in range(Y_RANGE):
        for x in range(X_RANGE):
            if Bmap[y][x] == 0:
                pygame.draw.rect(screen, BLUE, (55+34*x,111+34*y,32,32))
            if Bmap[y][x] == 1:
                pygame.draw.rect(screen, GREEN, (55+34*x,111+34*y,32,32))
            if Bmap[y][x] == 2:
                pygame.draw.rect(screen, RED, (55+34*x,111+34*y,32,32))
                
def Draw_Player_AI2(screen, Bmap):
    for y in range(Y_RANGE):
        for x in range(X_RANGE):
            if Bmap[y][x] == 0:
                pygame.draw.rect(screen, BLUE, (416+34*x,111+34*y,32,32))
            if Bmap[y][x] == 1:
                pygame.draw.rect(screen, GREEN, (416+34*x,111+34*y,32,32))
            if Bmap[y][x] == 2:
                pygame.draw.rect(screen, RED, (416+34*x,111+34*y,32,32))