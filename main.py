'''Python workshop
'''

import pygame as pg

class Environment(object):
    '''TBC
    '''
    def __init__(self):
        self.screen = pg.display.set_mode([960, 540])
        pg.display.set_caption('Python Workshop')
        
        self.rocket_image = pg.image.load('src/images/rocket.png')
        self.background_image = pg.image.load('src/images/background.png')
        self.background_image = pg.transform.scale(self.background_image, (960, 540))
        self.background_rect = self.background_image.get_rect()
        
        pg.display.set_icon(self.rocket_image)
    
    def update(self):
        self.screen.blit(self.background_image, self.background_rect)
        pg.display.flip()
        
class Rocket(object):
    '''TBC
    '''
    def __init__(self):
        self.vy = 0
        self.y = 0
        
    def changespeed(self, delta_vy):
        self.vy += delta_vy
        
    def changeposition(self, delta_y):
        self.y += delta_y
        
def main():
    pg.init()
    environment = Environment()
    rocket = Rocket()
    
    t_previous = pg.time.get_ticks()*0.001
    running = True

    while running:
        t = pg.time.get_ticks()*0.001
        dt = t-t_previous
        t_previous = t
        
        # Game logic

        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        environment.update()
        pg.event.pump()
    pg.quit()
    
if __name__ == "__main__":
    main()