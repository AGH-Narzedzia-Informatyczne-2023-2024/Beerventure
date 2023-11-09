# This is the Player class file
from settings import *
import numpy as np

class Player():
    def __init__(self, screen, x=0, y=0):
        self.x = x
        self.y = y
        self.img = ENEMY_IMGS[0]
        self.screen = screen

    def render(self):
        newRect = self.img.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        self.screen.blit(self.img, newRect.topleft)

    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.x += 2
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2