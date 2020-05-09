import random as rand
import numpy as np

def generate_bot_ships(bmap):
    ship_size = 4
    count = 1
    while ship_size > 0:
        bmap = put_ship_on_map(bmap, ship_size, count)
        ship_size = ship_size - 1
        count = count + 1
        
        if np.count_nonzero(bmap) == 100:  # if everything screw up, try again
            ship_size = 4
            count = 1
            
    return bmap

def put_ship_on_map(bmap, ss, c):
    ship_located = False
    count = 0
    while count < c:
        ship_located = False
        while ship_located == False:
            if bool(rand.getrandbits(1)) == True:     #Choose 1 bit: true - column, false - row
                yloc = rand.randrange(0,9)
                check = check_if_fit_in_column(bmap, yloc, ss)
                if check == True:
                    bmap = put_column_ship(bmap, yloc, ss)
                    count = count + 1
                    ship_located = True
            else:
                xloc = rand.randrange(0,9)
                check = check_if_fit_in_row(bmap, xloc, ss)
                if check == True:
                    bmap = put_row_ship(bmap, xloc, ss)
                    count = count + 1
                    ship_located = True
    return bmap

def column_block(bmap,y,x):
    if bmap[y][x] == 1:          #Center
        return True
            
    if y - 1 >= 0:                 #Top Side
        if bmap[y - 1][x] == 1:
            return True
                
    if y + 1 <= 9:                 #Bottom Side
        if bmap[y + 1][x] == 1:
            return True
    
    if corners_block(bmap,y,x) == True:  #Check Corners
        return True
    else:
        return False
    
def row_block(bmap,y,x):
    if bmap[y][x] == 1:          #Center
            return True
            
    if x - 1 >= 0:                 #Left Side
        if bmap[y][x - 1] == 1:
            return True
                
    if x + 1 <= 9:                 #Right Side
        if bmap[y][x + 1] == 1:
            return True
    
    if corners_block(bmap,y,x) == True: #Check Corners
        return True
    else:
        return False

def corners_block(bmap,y,x):
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
        failed = column_block(bmap,y,i)
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
        failed = row_block(bmap,x,i)
                
        if failed == False:
            is_good = is_good + 1
        else:
            is_good = 0
            
        failed = False
        
        if is_good == ss:
            return True
        
        i = i + 1
    return False

def put_column_ship(bmap, y, ss):
    i_to_bottom = 0
    i_to_top = 0
    ship_size = 0
    direction = 0
    first_put = False
    retry = False
    retrying = 0
    
    nb = rand.randrange(0,9)
    
    while bmap[y][nb] is 0:
        nb = rand.randrange(0,9)
    
    while ship_size < ss:
        if direction == 0 and y + i_to_bottom <= 9: #Coming into bottom side
            if column_block(bmap, y + i_to_bottom, nb) == True or check_neighbour(bmap,y + i_to_bottom,nb) == True:
                direction = 1
            else:
                bmap[y + i_to_bottom][nb] = 3 
                ship_size = ship_size + 1
                i_to_bottom = i_to_bottom + 1
                if first_put == False:
                    first_put = True
                    i_to_top = 1
        else:
            if y + i_to_bottom == 10:
                direction = 1
            
        if direction == 1 and y - i_to_top >= 0: #Coming into top side
            if column_block(bmap,y - i_to_top, nb) == True or check_neighbour(bmap,y - i_to_top,nb) == True:
                direction = 2
            else:
                bmap[y - i_to_top][nb] = 3
                ship_size = ship_size + 1
                i_to_top = i_to_top + 1
        else:
            if y - i_to_top == -1:
                direction = 2

        
        if direction == 2:
            bmap = np.where(bmap == 3,0,bmap)
            ship_size = 0
            i_to_bottom = 0
            i_to_top = 0
            direction = 0
            first_put = False
            retrying = retrying + 1
            nb = rand.randrange(0,9)
            y = rand.randrange(0,9)
            while bmap[y][nb] is 0:
                nb = rand.randrange(0,9)
                y = rand.randrange(0,9)
            
        if retrying == 100:
            Bmap = np.zeros((10,10), dtype = np.int32) #Clear map and try again
            return bmap
            
        if ship_size == ss and retry == False:
            bmap = np.where(bmap == 3,1,bmap)
            return bmap
    return bmap


def put_row_ship(bmap, x, ss):
    i_to_right = 0
    i_to_left = 0
    ship_size = 0
    direction = 0
    first_put = False
    retry = False
    retrying = 0
    
    nb = rand.randrange(0,9)
    
    while bmap[nb][x] is 0:
        nb = rand.randrange(0,9)
    
    while ship_size < ss:
        if direction == 0 and x + i_to_right <= 9: #Coming into bottom side
            if row_block(bmap, nb, x + i_to_right) == True or check_neighbour(bmap,nb, x + i_to_right) == True:#???
                direction = 1
            else:
                bmap[nb][x + i_to_right] = 3 
                ship_size = ship_size + 1
                i_to_right = i_to_right + 1
                if first_put == False:
                    first_put = True
                    i_to_left = 1
        else:
            if x + i_to_right == 10:
                direction = 1
            
        if direction == 1 and x - i_to_left >= 0: #Coming into top side
            if row_block(bmap,nb, x - i_to_left) == True or check_neighbour(bmap,nb,x - i_to_left) == True:
                direction = 2
            else:
                bmap[nb][x - i_to_left] = 3
                ship_size = ship_size + 1
                i_to_left = i_to_left + 1
        else:
            if x - i_to_left == -1:
                direction = 2

        
        if direction == 2:
            bmap = np.where(bmap == 3,0,bmap)
            ship_size = 0
            i_to_right = 0
            i_to_left = 0
            direction = 0
            first_put = False
            retrying = retrying + 1
            nb = rand.randrange(0,9)
            x = rand.randrange(0,9)
            while bmap[nb][x] is 0:
                nb = rand.randrange(0,9)
                x = rand.randrange(0,9)
        
        if retrying == 100:
            Bmap = np.zeros((10,10), dtype = np.int32) #Clear map and try again 
            return bmap
                
        if ship_size == ss and retry == False:
            bmap = np.where(bmap == 3,1,bmap)
            return bmap
    return bmap