def text_obj(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def draw_text(text,font,color,surface,x,y):
    textobj = font.render(text,l,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)