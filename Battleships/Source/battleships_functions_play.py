import random as rand
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("./cfg.ini") #Maybe ../

def shot(Map1,y,x):
    if Map1[y][x] == 3 or Map1[y][x] == 4:
        return Map1, False
    if Map1[y][x] == 1:
        Map1[y][x] = 3
    if Map1[y][x] == 0 or Map1[y][x] == 2:
        Map1[y][x] = 4
    return Map1, True

def Player_shot(Map1,y,x):
    xi = 0
    yi = 0
    
    if x - 32 > 0:             #Pierwsze sprawdzenie musi być tylko dla -32
        while x - 34*xi > 0:   
            xi = xi + 1
        xi = xi - 1
    if y - 32 > 0:
        while y - 34*yi > 0:
            yi = yi + 1
        yi = yi - 1
    Map1 = shot(Map1,yi,xi)
    return Map1
    
def AI_shot(Map1):
    x = -1
    y = -1
    i = 0
    if cfg["Basic"].getint("ALG") == 1:
        x = rand.randrange(cfg["Rules"].getint("X_RANGE"))
        y = rand.randrange(cfg["Rules"].getint("Y_RANGE"))
        while (Map1[y][x] == 3 or Map1[y][x] == 4) and i < cfg["Rules"].getint("X_RANGE")*cfg["Rules"].getint("Y_RANGE") + 1:
            x = rand.randrange(cfg["Rules"].getint("X_RANGE"))
            y = rand.randrange(cfg["Rules"].getint("Y_RANGE"))
            i = i+1
        Map1,temp = shot(Map1,y,x)
        return Map1