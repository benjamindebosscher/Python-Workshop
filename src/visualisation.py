import pygame as pg
import matplotlib.pyplot as plt

class Environment(object):
    '''TBC
    '''
    def __init__(self):
        pg.init()
        
        self.screen = pg.display.set_mode([1056, 594])
        pg.display.set_caption('Python Workshop')
        
        self.rocket_image = pg.image.load('src/images/rocket.png')
        self.rocket_image = pg.transform.scale(self.rocket_image, (128, 128))
        self.rocket_rect = self.rocket_image.get_rect()
        self.background_image = pg.image.load('src/images/background.png')
        self.background_image = pg.transform.scale(self.background_image, (1056, 594))
        self.background_rect = self.background_image.get_rect()
        
        pg.display.set_icon(self.rocket_image)
    
    def update(self, y):
        self.screen.blit(self.background_image, self.background_rect)
        self.rocket_rect.midbottom = (528,624-y) # Because of pygame coor sys
        self.screen.blit(self.rocket_image, self.rocket_rect)
        pg.display.flip()
        pg.event.pump()
        
class Rocket(object):
    '''TBC
    '''
    def __init__(self):
        self.mass = [333400]        
        self.ay = [0]
        self.vy = [0]
        self.y = [0]
        self.time = [0]
    
    def savemass(self, mass):
        self.mass.append(mass)
        
    def saveacceleration(self, ay):
        self.ay.append(ay)
        
    def savevelocity(self, vy):
        self.vy.append(vy)
    
    def saveposition(self, y):
        self.y.append(y)
        
    def savetime(self, t):
        self.time.append(t)

def plotter(y, vy, ay, mass, time):
    plt.subplot(2, 2, 1)
    plt.plot(time, y)
    plt.xlabel('Time [s]')
    plt.ylabel('Altitude [m]')
    
    plt.subplot(2, 2, 2)
    plt.plot(time, mass)
    plt.xlabel('Time [s]')
    plt.ylabel('Mass [kg]')

    plt.subplot(2, 2, 3)
    plt.plot(time, vy)
    plt.xlabel('Time [s]')
    plt.ylabel('Velocity [m/s]')

    plt.subplot(2, 2, 4)
    plt.plot(time[1:], ay[1:])
    plt.xlabel('Time [s]')
    plt.ylabel(r'Acceleration [m/s$^2$]')
    
    plt.suptitle('Rocket Launch Characteristics')

    plt.show()
