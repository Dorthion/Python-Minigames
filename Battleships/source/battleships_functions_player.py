#Functions
def change_ship(pmap, clx, cly):
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
    pmap = change_number(pmap, pmap[xi][yi], xi, yi)
    return pmap

def change_number(pmap, number, x, y):
    if number == 0:
        print("pressed 0")
        pmap[x][y] = 1
        if x-1 >= 0 and y-1 >= 0:
            pmap[x-1][y-1] = 2
        if x+1 <= 9 and y-1 >= 0:
            pmap[x+1][y-1] = 2
        if x-1 >= 0 and y+1 <= 9:
            pmap[x-1][y+1] = 2
        if x+1 <= 9 and y+1 <= 9:
            pmap[x+1][y+1] = 2
        return pmap

    #Sprawdzić trzeba 8 pól, lecz tym sposobem jest sprawdzane 16 pól
    if number == 1:
        print("pressed 1")
        pmap[x][y] = 0
        check_if_still_red(pmap, x-1, y-1)
        check_if_still_red(pmap, x+1, y-1)
        check_if_still_red(pmap, x-1, y+1)
        check_if_still_red(pmap, x+1, y+1)
        return pmap
    
    if number == 2:
        print("pressed 2")
        return pmap
    
    return pmap

def check_if_still_red(pmap, x, y):
    temp = 4
    if x-1 >= 0 and y-1 >= 0:
        if pmap[x-1][y-1] == 1:
            temp = temp - 1
    if x+1 <= 9 and y-1 >= 0:
        if pmap[x+1][y-1] == 1:
            temp = temp - 1
    if x-1 >= 0 and y+1 <= 9:
        if pmap[x-1][y+1] == 1:
            temp = temp - 1
    if x+1 <= 9 and y+1 <= 9:
        if pmap[x+1][y+1] == 1:
            temp = temp - 1
    if temp == 4 and x >= 0 and y >= 0 and x <= 9 and y <= 9:
        pmap[x][y] = 0
    return pmap