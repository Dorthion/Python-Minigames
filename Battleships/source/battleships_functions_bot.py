import random as rand
import numpy as np

def generate_bot_ships(bmap):
    ship_size = 4
    count = 1
    while ship_size > 0:
        bmap = put_ship_on_map(bmap, ship_size, count)
        ship_size = ship_size - 1
        count = count + 1
    return bmap

def put_ship_on_map(bmap, ss, c):
    ship_located = False
    count = 0
    while count < c:
        ship_located = False
        while ship_located == False:
            #if bool(rand.getrandbits(1)) == True:     #Choose 1 bit: true - column, false - row
            print("col1")
            yloc = rand.randrange(0,9)
            check = check_if_fit_in_column(bmap, yloc, ss)
            print("col2")
            if check == True:
                print("col3")
                bmap = put_column_ship(bmap, yloc, ss)
                count = count + 1
                ship_located = True
                print("col4")
            
    print("wyjscie")
    return bmap
            
def check_if_fit_in_column(bmap, y, ss):
    i = 0
    is_good = 0
    failed = False
    while i <= 9:
        failed = column_block(bmap,i,y)
        if failed == False:
            is_good = is_good + 1
        else:
            is_good = 0
            
        if is_good == ss:
            return True
        
        i = i + 1
    return False

def column_block(bmap,x,y):
    if bmap[x][y] == 2:          #Center
        return True
            
    if y-1 >= 0:                 #Top Side
        if bmap[x][y-1] == 2:
            return True
                
    if y+1 <= 9:                 #Bottom Side
        if bmap[x][y+1] == 2:
            return True
    
    if corners_block(bmap,x,y) == True:  #Check Corners
        return True
    else:
        return False
    
def row_block(bmap,x,y):
    if bmap[x][y] == 2:          #Center
            return True
            
    if x-1 >= 0:                 #Left Side
        if bmap[x-1][y] == 2:
            return True
                
    if x-1 >= 0 and y - 1 >= 0:  #Left Top Side
        if bmap[x-1][y-1] == 2:
            return True
    
    if corners_block(bmap,x,y) == True: #Check Corners
        return True
    else:
        return False

def corners_block(bmap,x,y):
    if y-1 >= 0 and x - 1 >= 0:  #Left Top Side
        if bmap[x-1][y-1] == 2:
            return True
                
    if y+1 <= 9 and x - 1 >= 0:  #Right Top Side
        if bmap[x-1][y+1] == 2:
            return True
                
    if y-1 >= 0 and x + 1 <= 9:  #Left Bottom Side
        if bmap[x+1][y-1] == 2:
            return True
                
    if y+1 <= 9 and x + 1 <= 9:  #Right Bottom Side
        if bmap[x+1][y+1] == 2:
            return True
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
    i_to_top = 1
    ship_size = 0
    direction = 0
    retry = False
    
    nb = rand.randrange(0,9)
    
    while bmap[nb][y] is 0:
        nb = rand.randrange(0,9)
    
    while ship_size < ss:
        if direction == 0 and nb + i_to_bottom <= 9: #Coming into bottom side
            if column_block(bmap,nb + i_to_bottom,y) == True:
                direction = 1
            else:
                bmap[nb + i_to_bottom][y] = 3 
                ship_size = ship_size + 1
                i_to_bottom = i_to_bottom + 1

        if direction == 1 and nb - i_to_bottom >= 0: #Coming into top side
            if column_block(bmap,nb - i_to_top,y) == True:
                ship_size = 0
                direction = 2
            else:
                bmap[nb - i_to_bottom][y] = 3
                ship_size = ship_size + 1
                i_to_top = i_to_top + 1
        
        if direction == 2:
            bmap = np.where(bmap == 3,0,bmap)
            direction = 0
                
        if ship_size == ss and retry == False:
            bmap = np.where(bmap == 3,1,bmap)
            print (bmap)
            return bmap
    return bmap

def put_row_ship(bmap, x, ss):
    i_to_bottom = 0
    i_to_top = 1
    ship_size = 0
    direction = 0
    retry = False
    
    nb = rand.randrange(0,9)
    
    while bmap[x][nb] is 0:
        nb = rand.randrange(0,9)
    
    while ship_size < ss:
        if direction == 0:                          #Coming into bottom side
            if column_block(bmap,x,nb + i_to_bottom) == True:
                direction = 1
            else:
                bmap[x][nb + i_to_bottom] = 3 
                ship_size = ship_size + 1
                i_to_bottom = i_to_bottom + 1

        if direction == 1:                          #Coming into top side
            if column_block(bmap,x,nb - i_to_top) == True:
                ship_size = 0
                direction = 2
            else:
                bmap[x][nb - i_to_top] = 3
                ship_size = ship_size + 1
                i_to_top = i_to_top + 1
        
        if direction == 2:
            bmap = np.where(bmap == 3,0,bmap)
            direction = 0
                
        if ship_size == ss and retry == False:
            bmap = np.where(bmap == 3,1,bmap)
            return bmap

    return bmap

#To do:
#- Check if neighbour in column (top/bottom)
#- Check if neighbour in row (left/right)