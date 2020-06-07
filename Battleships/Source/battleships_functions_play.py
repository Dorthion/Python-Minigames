def shot(Map1,y,x):
    xi = 0
    yi = 0
    
    if x - 32 > 0:             #Pierwsze sprawdzenie musi być tylko dla -32
        while x - 34*xi > 0:   
            xi = xi + 1
        xi = xi - 1
    if y - 32 > 0:
        while y - 34*yi > 0:
            yi = yi + 1
        yi = yi - 1
        
    print("PRZED X:" + str(x) + "PRZED Y:" + str(y))
    print("X:" + str(xi) + "Y:" + str(yi)) 
    
    if Map1[yi][xi] == 1:
        Map1[yi][xi] = 3
    if Map1[yi][xi] == 0 or Map1[yi][xi] == 2:
        Map1[yi][xi] = 4
    return Map1