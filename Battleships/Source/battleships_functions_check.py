from Source import Settings as Set
def check_column(bmap,y,x):
    if bmap[y][x] == 1:            #Center
        return True
            
    if y - 1 >= 0:                 #Top Side
        if bmap[y - 1][x] == 1:
            return True
                
    if y + 1 < Set.Y_RANGE:       #Bottom Side
        if bmap[y + 1][x] == 1:
            return True
    
    if check_corners(bmap,y,x) == True:  #Check Corners
        return True
    else:
        return False
    
def check_row(bmap,y,x):
    if bmap[y][x] == 1:          #Center
            return True
            
    if x - 1 >= 0:                 #Left Side
        if bmap[y][x - 1] == 1:
            return True
                
    if x + 1 <= Set.Y_RANGE - 1:                 #Right Side
        if bmap[y][x + 1] == 1:
            return True
    
    if check_corners(bmap,y,x) == True: #Check Corners
        return True
    else:
        return False

def check_corners(bmap,y,x):
    if y - 1 >= 0 and x - 1 >= 0:  #Left Top Side
        if bmap[y - 1][x - 1] == 1:
            return True
                
    if y + 1 < Set.Y_RANGE and x - 1 >= 0:  #Left Bottom Side
        if bmap[y + 1][x - 1] == 1:
            return True
                
    if y - 1 >= 0 and x + 1 < Set.X_RANGE:  #Right Top Side
        if bmap[y - 1][x + 1] == 1:
            return True
                
    if y + 1 < Set.Y_RANGE and x + 1 < Set.X_RANGE:  #Right Bottom Side
        if bmap[y + 1][x + 1] == 1:
            return True
    return False

def check_neighbour(bmap,y,x):
    if y - 1 >= 0:               #Top Side
        if bmap[y - 1][x] == 1:
            return True
                
    if y + 1 < Set.Y_RANGE:      #Bottom Side
        if bmap[y + 1][x] == 1:
            return True
    if x - 1 >= 0:               #Left Side
        if bmap[y][x - 1] == 1:
            return True
                
    if x + 1 < Set.X_RANGE:      #Right Side
        if bmap[y][x + 1] == 1:
            return True
    return False

def check_if_fit_in_column(bmap, y, ss):
    i = 0
    is_good = 0
    failed = False
    while i < Set.Y_RANGE:
        failed = check_column(bmap,y,i)
        if failed == False:
            is_good = is_good + 1
        else:
            is_good = 0
            
        if is_good == ss:
            return True
        
        i = i + 1
    return False

def check_if_fit_in_row(bmap,x, ss):
    i = 0
    is_good = 0
    failed = False
    while i < Set.X_RANGE - 1:
        failed = check_row(bmap,x,i)
                
        if failed == False:
            is_good = is_good + 1
        else:
            is_good = 0
            
        failed = False
        
        if is_good == ss:
            return True
        
        i = i + 1
    return False

def check_ship_size(pmap):
    lista=[]
    for i in range(len(pmap)):
        for j in range(len(pmap[i])):
            if(pmap[i][j] == 1):
                size, pmap = set_ship_size(pmap, i, j, 1)
                lista.append(size)
    lista.sort()
    print(lista)

def set_ship_size(pmap,y,x,size):
    pmap[y][x] = 4
    if check_neighbour(pmap, y, x) == True:
        if x + 1 < Set.X_RANGE:
            if pmap[y][x+1]==1:
                size, pmap = set_ship_size(pmap,y,x+1,size + 1)
        if y + 1 < Set.Y_RANGE:
            if pmap[y+1][x]==1:
                size, pmap = set_ship_size(pmap,y+1,x,size + 1)
    return size, pmap