def check_column(bmap,y,x):
    if bmap[y][x] == 1:          #Center
        return True
            
    if y - 1 >= 0:                 #Top Side
        if bmap[y - 1][x] == 1:
            return True
                
    if y + 1 <= 9:                 #Bottom Side
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
                
    if x + 1 <= 9:                 #Right Side
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
                
    if y + 1 <= 9 and x - 1 >= 0:  #Left Bottom Side
        if bmap[y + 1][x - 1] == 1:
            return True
                
    if y - 1 >= 0 and x + 1 <= 9:  #Right Top Side
        if bmap[y - 1][x + 1] == 1:
            return True
                
    if y + 1 <= 9 and x + 1 <= 9:  #Right Bottom Side
        if bmap[y + 1][x + 1] == 1:
            return True
    return False

def check_neighbour(bmap,y,x):
    if y - 1 >= 0:  #Top Side
        if bmap[y - 1][x] == 1:
            return True
                
    if y + 1 <= 9:  #Bottom Side
        if bmap[y + 1][x] == 1:
            return True
    if x - 1 >= 0:  #Left Side
        if bmap[y][x - 1] == 1:
            return True
                
    if x + 1 <= 9:  #Right Side
        if bmap[y][x + 1] == 1:
            return True
    return False

def check_if_fit_in_column(bmap, y, ss):
    i = 0
    is_good = 0
    failed = False
    while i <= 9:
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
    while i < 9:
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