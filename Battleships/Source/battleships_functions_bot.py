import random as rand
import numpy as np
from Source import battleships_functions_check as bfc

def load_config_file(config):    
    global cfg
    cfg = config
    bfc.load_config_file(config)

def generate_bot_ships(bmap):
    count = 1
    SHIP_SIZE = cfg["Rules"].getint("SHIP_SIZE")
    Temp_trying_to_generate = 0
    
    #while Set.SHIP_SIZE > 0:
    while SHIP_SIZE > 0:
        bmap = put_ship_on_map(bmap, SHIP_SIZE, count)
        SHIP_SIZE = SHIP_SIZE - 1
        count = count + 1
        
        if np.count_nonzero(bmap) == 0:  # if everything screw up, try again
            Temp_trying_to_generate = Temp_trying_to_generate + 1
            SHIP_SIZE = cfg["Rules"].getint("SHIP_SIZE")
            count = 1
            if Temp_trying_to_generate == 100:
                #Set.CANT_GENERATE = True
                bmap = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
                return bmap, True
         
    bmap = color_blocked_positions(bmap)
    return bmap, False

def put_ship_on_map(bmap, ss, c):
    ship_located = False
    count = 0
    temp = 0
    while count < c:
        ship_located = False
        while ship_located == False:
            if bool(rand.getrandbits(1)) == True:     #Choose 1 bit: true - column, false - row
                yloc = rand.randrange(0, cfg["Rules"].getint("Y_RANGE"))
                check = bfc.check_if_fit_in_column(bmap, yloc, ss)
                if check == True:
                    bmap = put_column_ship(bmap, yloc, ss)
                    if np.count_nonzero(bmap) == 0:
                        return bmap
                    count = count + 1
                    ship_located = True
                else:
                    temp = temp + 1
                if temp == 10000:
                    bmap = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
                    return bmap
            else:
                xloc = rand.randrange(0,cfg["Rules"].getint("X_RANGE"))
                check = bfc.check_if_fit_in_row(bmap, xloc, ss)
                if check == True:
                    bmap = put_row_ship(bmap, xloc, ss)
                    if np.count_nonzero(bmap) == 0:
                        return bmap
                    count = count + 1
                    ship_located = True
                else:
                    temp = temp + 1
                if temp == 10000:
                    bmap = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32)
                    return bmap
            
    return bmap

def put_column_ship(bmap, y, ss):
    i_to_bottom = 0
    i_to_top = 0
    ship_size = 0
    direction = 0
    first_put = False
    retry = False
    retrying = 0
    
    nb = rand.randrange(0,cfg["Rules"].getint("X_RANGE"))
    
    while bmap[y][nb] == 1:
        nb = rand.randrange(0,cfg["Rules"].getint("X_RANGE"))
    
    while ship_size < ss:
        if direction == 0 and y + i_to_bottom < cfg["Rules"].getint("Y_RANGE"): #Coming into bottom side
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
            if y + i_to_bottom == cfg["Rules"].getint("Y_RANGE"):
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
            nb = rand.randrange(0,cfg["Rules"].getint("X_RANGE") - 1)
            y = rand.randrange(0,cfg["Rules"].getint("Y_RANGE") - 1)
            while bmap[y][nb] is 0:
                nb = rand.randrange(0,cfg["Rules"].getint("X_RANGE"))
                y = rand.randrange(0,cfg["Rules"].getint("Y_RANGE"))
            
        if retrying == 100:
            bmap = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32) #Clear map and try again
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
    
    nb = rand.randrange(0,cfg["Rules"].getint("Y_RANGE") - 1)
    
    while bmap[nb][x] == 1:
        nb = rand.randrange(0,cfg["Rules"].getint("Y_RANGE") - 1)
    
    while ship_size < ss:
        if direction == 0 and x + i_to_right <= cfg["Rules"].getint("X_RANGE") - 1: #Coming into bottom side
            if bfc.check_row(bmap, nb, x + i_to_right) == True or bfc.check_neighbour(bmap,nb, x + i_to_right) == True:
                direction = 1
            else:
                bmap[nb][x + i_to_right] = 3 
                ship_size = ship_size + 1
                i_to_right = i_to_right + 1
                if first_put == False:
                    first_put = True
                    i_to_left = 1
        else:
            if x + i_to_right == cfg["Rules"].getint("X_RANGE"):
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
            nb = rand.randrange(0,cfg["Rules"].getint("Y_RANGE") - 1)
            x = rand.randrange(0,cfg["Rules"].getint("X_RANGE") - 1)
            while bmap[nb][x] is 0:
                nb = rand.randrange(0,cfg["Rules"].getint("Y_RANGE") - 1)
                x = rand.randrange(0,cfg["Rules"].getint("X_RANGE") - 1)
        
        if retrying == 10000:
            bmap = np.zeros((cfg["Rules"].getint("Y_RANGE"),cfg["Rules"].getint("X_RANGE")), dtype = np.int32) #Clear map and try again 
            return bmap
                
        if ship_size == ss and retry == False:
            bmap = np.where(bmap == 3,1,bmap)
            return bmap
    return bmap

def color_blocked_positions(bmap):
    for i in range(len(bmap)):
        for j in range(len(bmap[i])):
            if bmap[i][j] != 1:
                if bfc.check_neighbour(bmap, i, j) == True or bfc.check_corners(bmap, i, j) == True:
                    bmap[i][j] = 2
    return bmap