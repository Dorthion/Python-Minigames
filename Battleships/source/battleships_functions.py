#Functions
def text_obj(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def change_ship(pmap, clx, cly):
    xi = 0
    yi = 0
    if clx - 32 > 0:             #Pierwsze sprawdzenie musi być tylko dla -32
        while clx - 34*xi > 0:   
            xi = xi + 1
        xi = xi - 1
    if cly - 32 > 0:
        while cly - 34*yi > 0:
            yi = yi + 1
        yi = yi - 1
    print(xi)
    print(yi)
    pmap = change_number(pmap, pmap[xi][yi], xi, yi)
    #print(pmap)
    return pmap

def change_number(pmap, number, x, y):
    if number == 0:
        pmap[x][y] = 1
        if x-1 >= 0 and y-1 >= 0:
            pmap[x-1][y-1] = 2
        if x+1 <= 9 and y-1 >= 0:
            pmap[x+1][y-1] = 2
        if x-1 >= 0 and y+1 <= 9:
            pmap[x-1][y+1] = 2
        if x+1 <= 9 and y+1 <= 9:
            pmap[x+1][y+1] = 2
    return pmap

#VV do usunięcia?
def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text,l,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)
    
#def wez_se_ogarnij_statki_bocie():
    