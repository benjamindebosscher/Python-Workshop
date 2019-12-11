'''Supporting script for the pygame visualisation

Drawing functions:
    - window(xmax,ymax) = set up window
    - paste(image,x,y) = paste pixels in image at x,y in video memory
    - clear()  = clear window (make black)
    - loadimage(filename) = load image, returns pixels in an image
    - scaleimage(image, size) = returns scaled image
    - showframe() = update the simulation screen
    - closewindow() = close the pygame simulation window
'''

import pygame as pg

# Globals
scr = None
xmax, ymax = 500, 500

def window(xmaxin, ymaxin):
    global xmax, ymax, scr

    xmax = int(round(xmaxin))
    ymax = int(round(ymaxin))
    pg.init()
    scr = pg.display.set_mode((xmax, ymax))

def paste(img, x, y):
    # Paste bitmap on screen at position x,y in video memory
    xctr = int(round(x))
    yctr = int(round(y))
    rect = img.get_rect()
    rect.midbottom = xctr, yctr
    scr.blit(img, rect)

def clear(bgcolor=(0, 0, 0)):
    scr.fill(bgcolor)

def loadimage(filename):
    return pg.image.load(filename)

def scaleimage(image, size):
    return pg.transform.scale(image, size)

def showframe():
    # Update screenw with frame from video memeory
    pg.display.flip()

    # Check current events
    events = pg.event.get()
    keys = pg.key.get_pressed()
    
    close = False
    for event in events:
        if event.type == pg.QUIT:
            close = True
    if keys[pg.K_ESCAPE]:
        close = True
    return close

def closewindow():
    pg.quit()
