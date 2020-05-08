import random as rand

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
        while ship_located == False:
            if bool(random.getrandbits(1)) == True:     #Choose 1 bit: true - column, false - row
                yloc = rand.randrange(0,9)
                check = check_if_fit_in_column(bmap, yloc)
                if check == True:
                    bmap = put_column_ship(bmap)
                    count = count + 1
                    ship_located = True
            else
                xloc = rand.randrange(0,9)
                check = check_if_fit_in_row(bmap, xloc)
                if check == True:
                    bmap = put_row_ship(bmap)
                    count = count + 1
                    ship_located = True
    return bmap
            
def check_if_fit_in_column(bmap,y):
    i = 0
    temp = 0
    while i > 9:
        bmap[]
    return false