import random as rand

def load_config_file(config):    
    global cfg
    cfg = config

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
    #Alg1 - Full random
    if cfg["Basic"].getint("ALG") == 1:
        x, y = Rand_Empty_Tile(Map1)
        Map1,temp = shot(Map1,y,x)
        return Map1
    #Alg2 - Random + Predict ships
    if cfg["Basic"].getint("ALG") == 2:
        
        Map1,temp = shot(Map1,y,x)
        return Map1

def Rand_Empty_Tile(Map1):
    x = rand.randrange(cfg["Rules"].getint("X_RANGE"))
    y = rand.randrange(cfg["Rules"].getint("Y_RANGE"))
    while (Map1[y][x] == 3 or Map1[y][x] == 4):
        x = rand.randrange(cfg["Rules"].getint("X_RANGE"))
        y = rand.randrange(cfg["Rules"].getint("Y_RANGE"))
    return x,y