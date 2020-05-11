from Source import Settings as Set
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
    print("CLX:" + str(clx) + "CLY:" + str(cly))
    print("X:" + str(xi) + "Y:" + str(yi))
    pmap = change_number(pmap, pmap[yi][xi], yi, xi)
    return pmap

def change_number(pmap, number, y, x):
    if number == 0:
        pmap[y][x] = 1
        if y - 1 >= 0 and x - 1 >= 0:
            pmap[y - 1][x - 1] = 2
        if y + 1 < Set.Y_RANGE and x - 1 >= 0:
            pmap[y + 1][x - 1] = 2
        if y - 1 >= 0 and x + 1 < Set.X_RANGE:
            pmap[y - 1][x + 1] = 2
        if y + 1 < Set.Y_RANGE and x + 1  < Set.X_RANGE:
            pmap[y + 1][x + 1] = 2
        return pmap

    #Sprawdzić trzeba 8 pól, lecz tym sposobem jest sprawdzane 16 pól
    if number == 1:
        pmap[y][x] = 0
        check_if_still_red(pmap, x - 1, y - 1)
        check_if_still_red(pmap, x + 1, y - 1)
        check_if_still_red(pmap, x - 1, y + 1)
        check_if_still_red(pmap, x + 1, y + 1)
        return pmap
    
    if number == 2:
        return pmap
    
    return pmap

def check_if_still_red(pmap, x, y):
    temp = 4
    if y - 1 >= 0 and x - 1 >= 0:
        if pmap[y - 1][x - 1] == 1:
            temp = temp - 1
    if y + 1 < Set.Y_RANGE and x - 1 >= 0:
        if pmap[y + 1][x - 1] == 1:
            temp = temp - 1
    if y - 1 >= 0 and x + 1 < Set.X_RANGE:
        if pmap[y - 1][x + 1] == 1:
            temp = temp - 1
    if y + 1 < Set.Y_RANGE and x + 1 < Set.X_RANGE:
        if pmap[y + 1][x + 1] == 1:
            temp = temp - 1
    if temp == 4 and x >= 0 and y >= 0 and x < Set.X_RANGE and  y < Set.Y_RANGE:
        pmap[y][x] = 0
    return pmap