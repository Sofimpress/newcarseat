import pygame
from settings import *

class Lol:

    def __init__(self, down_key, ddd):
        self.down_key = down_key
        self.ddd = 0
 
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.down_key]:
            self.ddd = 1

    def get_ddd(self):
        return self.ddd
