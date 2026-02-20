import pygame

class Pato_1():
    def __init__(self, x, y):
        
        self.forma = pygame.Rect(0, 0, 20, 20)
        self.forma.center = (x,y)
        
        pass