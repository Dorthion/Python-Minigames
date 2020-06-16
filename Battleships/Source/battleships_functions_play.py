import random as rand

def load_config_file(config):    
    global cfg
    cfg = config
    
def shot(Map1,y,x):
    if Map1[y][x] in [3, 4, 5]:
        return Map1, False
    if Map1[y][x] == 1:
        Map1[y][x] = 3
    if Map1[y][x] in [0, 2]:
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
        return True, [x, y - 1]
    if direction == 2 and y + 1 < cfg["Rules"].getint("Y_RANGE"):
        return True, [x, y + 1]
    if direction == 3 and x - 1 >= 0:
        return True, [x - 1, y]
    if direction == 4 and x + 1 < cfg["Rules"].getint("X_RANGE"):
        return True, [x + 1, y]
    return False, [x, y]

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
    if y - 1 >= 0 and x - 1 >= 0 and Map[y - 1][x - 1] in [0,1,2,5]:
        Map[y - 1][x - 1] = 5
    if y + 1 < cfg["Rules"].getint("Y_RANGE") and x - 1 >= 0 and Map[y + 1][x - 1] in [0,1,2,5]:
        Map[y + 1][x - 1] = 5
    if y - 1 >= 0 and x + 1 < cfg["Rules"].getint("X_RANGE") and Map[y - 1][x + 1] in [0,1,2,5]:
        Map[y - 1][x + 1] = 5
    if y + 1 < cfg["Rules"].getint("Y_RANGE") and x + 1  < cfg["Rules"].getint("X_RANGE") and Map[y + 1][x + 1] in [0,1,2,5]:
        Map[y + 1][x + 1] = 5
    return Map

class PlayBot:
    def __init__(self, Map, alg):
        self.Map = Map
        self.alg = alg
        self.hunt_on = False
        self.rand_move = []
        self.act_val = []
        self.last_val = []
        self.direction = 0
        self.hunt_dir = False

    def AI_shot(self):
        
        #Alg1 - Full random
        if self.alg == 1:
            x, y = Rand_Empty_Tile(self.Map)
            self.Map, temp = shot(self.Map,y,x)
                
        #Alg2 - Random + Predict ships
        if self.alg == 2:
            self.AI_search()

            if not self.rand_move and self.direction == 0:
                self.reset_hunt()
    
    def new_dir(self):
        
        if self.rand_move and self.hunt_on: 
            self.direction = self.rand_move.pop(0)
        else:
            self.direction = 0
            
    def check_new_dir(self):
        check, wtf = next_move(self.direction,self.last_val[0],self.last_val[1])
        while check == False and self.rand_move:
            self.new_dir()
            check, wtf = next_move(self.direction,self.last_val[0],self.last_val[1])
            if self.Map[wtf[1]][wtf[0]] == 3:
                check = True
            if self.Map[wtf[1]][wtf[0]] == 4:
                check = False      
        if self.direction != 0 and check:
            self.last_val = wtf

    def reset_hunt(self):
        self.hunt_on = False
        self.rand_move = []
        self.act_val = []
        self.last_val = []
        self.direction = 0
        
    def remove_hit(self):
        if self.act_val[1] - 1 >= 0 and self.Map[self.act_val[1] - 1][self.act_val[0]] in [3,4,5] and 1 in self.rand_move:
            self.rand_move.remove(1)
        if self.act_val[1] + 1 < cfg["Rules"].getint("Y_RANGE") and self.Map[self.act_val[1] + 1][self.act_val[0]] in [3,4,5] and 2 in self.rand_move:
            self.rand_move.remove(2)
        if self.act_val[0] - 1 >= 0 and self.Map[self.act_val[1]][self.act_val[0] - 1] in [3,4,5] and 3 in self.rand_move:
            self.rand_move.remove(3)
        if self.act_val[0] + 1 < cfg["Rules"].getint("X_RANGE") and self.Map[self.act_val[1]][self.act_val[0] + 1] in [3,4,5] and 4 in self.rand_move:
            self.rand_move.remove(4)

                
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
                self.remove_hit()
                self.new_dir()
                self.check_new_dir()

        else:
            
            if self.last_val == self.act_val:
                if not self.rand_move:
                    self.reset_hunt()
                    x, y = Rand_Empty_Tile(self.Map)                    
                else:
                    self.new_dir()
                    self.check_new_dir()

                    x, y =  self.last_val
                    temp1, temp2 = next_move(self.direction, x, y)
                    
                    if temp1:
                        self.last_val = temp2
                    elif not self.rand_move:
                        self.reset_hunt()
                        
            else:
                x, y = self.last_val[0], self.last_val[1]
                temp1, temp2 = next_move(self.direction,x, y)
                
                if not temp1:
                    self.last_val = self.act_val
                    self.remove_hit()
                    self.new_dir()
                    self.check_new_dir()
                    x, y = self.last_val[0], self.last_val[1]

                else:
                    self.remove_hit()
                    if not self.rand_move and self.direction == 0:
                        x, y = Rand_Empty_Tile(self.Map)
                        self.reset_hunt()
                    else:
                        self.last_val = temp2

            self.Map, temp = shot(self.Map,y,x)
            
            if self.Map[y][x] == 3:
                self.Map = block_corners(self.Map,y,x)
                
            if self.Map[y][x] in [4,5]:
                self.last_val = self.act_val
