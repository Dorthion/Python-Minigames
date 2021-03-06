def load_config_file(config):    
    global cfg
    cfg = config
    
#Functions
def change_ship(pmap, cly, clx):
    xi = 0
    yi = 0
    if clx - 32 > 0:             #Pierwsze sprawdzenie musi być tylko dla -32
        while clx - 34*xi > 0:   
            xi = xi + 1
        xi = xi - 1
    if cly - 32 > 0:
        while cly - 34*yi > 0:
            yi = yi + 1
        yi = yi - 1
    pmap = change_number(pmap, pmap[yi][xi], yi, xi)
    return pmap

def change_number(pmap, number, y, x):
    if number == 0:
        pmap[y][x] = 1
        if y - 1 >= 0 and x - 1 >= 0:
            pmap[y - 1][x - 1] = 2
        if y + 1 < cfg["Rules"].getint("Y_RANGE") and x - 1 >= 0:
            pmap[y + 1][x - 1] = 2
        if y - 1 >= 0 and x + 1 < cfg["Rules"].getint("X_RANGE"):
            pmap[y - 1][x + 1] = 2
        if y + 1 < cfg["Rules"].getint("Y_RANGE") and x + 1  < cfg["Rules"].getint("X_RANGE"):
            pmap[y + 1][x + 1] = 2
        return pmap

    #Sprawdzić trzeba 8 pól, lecz tym sposobem jest sprawdzane 16 pól
    if number == 1:
        pmap[y][x] = 0
        check_if_still_red(pmap, y - 1, x - 1)
        check_if_still_red(pmap, y + 1, x - 1)
        check_if_still_red(pmap, y - 1, x + 1)
        check_if_still_red(pmap, y + 1, x + 1)
        return pmap
    
    if number == 2:
        return pmap
    
    return pmap

def check_if_still_red(pmap, y, x):
    temp = 4
    if y - 1 >= 0 and x - 1 >= 0:
        if pmap[y - 1][x - 1] == 1:
            temp = temp - 1
    if y + 1 < cfg["Rules"].getint("Y_RANGE") and x - 1 >= 0:
        if pmap[y + 1][x - 1] == 1:
            temp = temp - 1
    if y - 1 >= 0 and x + 1 < cfg["Rules"].getint("X_RANGE"):
        if pmap[y - 1][x + 1] == 1:
            temp = temp - 1
    if y + 1 < cfg["Rules"].getint("Y_RANGE") and x + 1 < cfg["Rules"].getint("X_RANGE"):
        if pmap[y + 1][x + 1] == 1:
            temp = temp - 1
    if temp == 4 and x >= 0 and y >= 0 and x < cfg["Rules"].getint("X_RANGE") and  y < cfg["Rules"].getint("Y_RANGE"):
        pmap[y][x] = 0
    return pmap

