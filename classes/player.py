# This is the Player class file
from settings import *
import numpy as np

class Player():
    def __init__(self, screen, x=0, y=0):
        self.x = x
        self.y = y
        self.img = ENEMY_IMGS[0][0][0]
        self.screen = screen
        self.hp = 100
        self.dmg_counter = 0

        self.hitbox = (self.x + self.img.get_width() / 2 - PLAYER_HITBOX, 
                       self.y + self.img.get_height() / 2 - PLAYER_HITBOX,
                       self.x + self.img.get_width() / 2 + PLAYER_HITBOX,
                       self.y + self.img.get_height() / 2 + PLAYER_HITBOX)

    def render(self):
        if self.dmg_counter > 0:
            self.dmg_counter -= 1
            self.img = ENEMY_IMGS[1][0][0]
            
        newRect = self.img.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        self.screen.blit(self.img, newRect.topleft)

        self.img = ENEMY_IMGS[0][0][0]

    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.x += 2
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2

        self.hitbox = (self.x + self.img.get_width() / 2 - PLAYER_HITBOX, 
                       self.y + self.img.get_height() / 2 - PLAYER_HITBOX,
                       self.x + self.img.get_width() / 2 + PLAYER_HITBOX,
                       self.y + self.img.get_height() / 2 + PLAYER_HITBOX)
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.hitbox[0], self.hitbox[1],
                          self.hitbox[2] - self.hitbox[0],
                          self.hitbox[3] - self.hitbox[1]))