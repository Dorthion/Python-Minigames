import random as rand
import numpy as np
from Source import battleships_functions_check as bfc
from Source import Settings as Set

def generate_bot_ships(bmap):
    count = 1
    Temp_SHIP_SIZE = Set.SHIP_SIZE
    
    while Set.SHIP_SIZE > 0:
        bmap = put_ship_on_map(bmap, Set.SHIP_SIZE, count)
        Set.SHIP_SIZE = Set.SHIP_SIZE - 1
        count = count + 1
        if np.count_nonzero(bmap) == 100:  # if everything screw up, try again
            Set.SHIP_SIZE = 4
            count = 1
            
    bmap = color_blocked_positions(bmap)
    Set.SHIP_SIZE = Temp_SHIP_SIZE
    return bmap

def put_ship_on_map(bmap, ss, c):
    ship_located = False
    count = 0
    while count < c:
        ship_located = False
        while ship_located == False:
            if bool(rand.getrandbits(1)) == True:     #Choose 1 bit: true - column, false - row
                yloc = rand.randrange(0,9)
                check = bfc.check_if_fit_in_column(bmap, yloc, ss)
                if check == True:
                    bmap = put_column_ship(bmap, yloc, ss)
                    count = count + 1
                    ship_located = True
            else:
                xloc = rand.randrange(0,9)
                check = bfc.check_if_fit_in_row(bmap, xloc, ss)
                if check == True:
                    bmap = put_row_ship(bmap, xloc, ss)
                    count = count + 1
                    ship_located = True
    return bmap

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
            if bfc.check_column(bmap, y + i_to_bottom, nb) == True or bfc.check_neighbour(bmap,y + i_to_bottom,nb) == True:
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
            if bfc.check_column(bmap,y - i_to_top, nb) == True or bfc.check_neighbour(bmap,y - i_to_top,nb) == True:
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
            if bfc.check_row(bmap, nb, x + i_to_right) == True or bfc.check_neighbour(bmap,nb, x + i_to_right) == True:#???
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
            if bfc.check_row(bmap,nb, x - i_to_left) == True or bfc.check_neighbour(bmap,nb,x - i_to_left) == True:
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

def color_blocked_positions(bmap):
    print(bmap)
    for i in range(len(bmap)):
        for j in range(len(bmap[i])):
            if bmap[i][j] != 1:
                if bfc.check_neighbour(bmap, i, j) == True or bfc.check_corners(bmap, i, j) == True:
                    bmap[i][j] = 2
    return bmap