import random as rand

def load_config_file(config):    
    global cfg
    cfg = config
    
def shot(Map1,y,x):
    if Map1[y][x] == 3 or Map1[y][x] == 4  or Map1[y][x] == 5:
        return Map1, False
    if Map1[y][x] == 1:
        Map1[y][x] = 3
    if Map1[y][x] == 0 or Map1[y][x] == 2:
        Map1[y][x] = 4
    return Map1, True

def Player_shot(Map1,y,x):
    xi = 0
    yi = 0
    
    if x - 32 > 0:
        while x - 34*xi > 0:   
            xi = xi + 1
        xi = xi - 1
    if y - 32 > 0:
        while y - 34*yi > 0:
            yi = yi + 1
        yi = yi - 1
    Map1 = shot(Map1,yi,xi)
    return Map1

def next_move(direction,x,y):
    if direction == 1 and y - 1 >= 0:
        return False, [x, y - 1]
    if direction == 2 and y + 1 < cfg["Rules"].getint("Y_RANGE"):
        return False, [x, y + 1]
    if direction == 3 and x - 1 >= 0:
        return False, [x - 1, y]
    if direction == 4 and x + 1 < cfg["Rules"].getint("X_RANGE"):
        return False, [x + 1, y]
    return True, [x, y]

def opposite_direction(direction):
    if direction == 1:
        return 2
    if direction == 2:
        return 1
    if direction == 3:
        return 4
    if direction == 4:
        return 3

def Rand_Empty_Tile(Map):
    x = rand.randrange(cfg["Rules"].getint("X_RANGE"))
    y = rand.randrange(cfg["Rules"].getint("Y_RANGE"))
    while Map[y][x] in [3,4,5]:
        x = rand.randrange(cfg["Rules"].getint("X_RANGE"))
        y = rand.randrange(cfg["Rules"].getint("Y_RANGE"))
    return x,y

def block_corners(Map,y,x):
    if y - 1 >= 0 and x - 1 >= 0 and Map[y - 1][x - 1] not in [3,4]:
        Map[y - 1][x - 1] = 5
    if y + 1 < cfg["Rules"].getint("Y_RANGE") and x - 1 >= 0 and Map[y + 1][x - 1] not in [3,4]:
        Map[y + 1][x - 1] = 5
    if y - 1 >= 0 and x + 1 < cfg["Rules"].getint("X_RANGE") and Map[y - 1][x + 1] not in [3,4]:
        Map[y - 1][x + 1] = 5
    if y + 1 < cfg["Rules"].getint("Y_RANGE") and x + 1  < cfg["Rules"].getint("X_RANGE") and Map[y + 1][x + 1] not in [3,4]:
        Map[y + 1][x + 1] = 5
    return Map
class PlayBot:
    def __init__(self, Map):
        self.Map = Map
        self.hunt_on = False
        self.rand_move = []
        self.act_val = []
        self.last_val = []
        self.direction = 0
    
    def AI_shot(self):
        #Alg1 - Full random
        if cfg["Basic"].getint("ALG") == 1:
            x, y = Rand_Empty_Tile(self.Map)
            self.Map, temp = shot(self.Map,y,x)

        #Alg2 - Random + Predict ships
        if cfg["Basic"].getint("ALG") == 2:
            self.AI_search()

            if self.rand_move and self.direction == 0:
                direction = self.rand_move.pop(0)
                self.direction = direction
            
            if self.direction != 0:
                check, self.last_val = next_move(self.direction,self.last_val[0],self.last_val[1])
                if check:
                    self.direction = 0
                else:
                    temp = opposite_direction(self.direction)
                    if self.rand_move:
                        self.rand_move = [temp]
            
            if not self.rand_move and self.direction == 0:
                self.hunt_on = False
                
    def AI_search(self):
        if self.hunt_on == False: 
            x, y = Rand_Empty_Tile(self.Map)
            self.Map, temp = shot(self.Map,y,x)
                
            if self.Map[y][x] == 3:
                self.act_val = [x,y]
                self.last_val = [x,y]
                self.rand_move = [i for i in range(1,5)]
                rand.shuffle(self.rand_move)
                self.hunt_on = True
                self.Map = block_corners(self.Map,y,x)
        else:
            x, y = self.last_val[0], self.last_val[1]
            self.Map, temp = shot(self.Map,self.last_val[1],self.last_val[0])
            if self.Map[y][x] == 3:
                self.Map = block_corners(self.Map,y,x)
            if self.Map[y][x] == 4:
                self.last_val = self.act_val
                x, y = self.last_val[0], self.last_val[1]
                self.direction = 0