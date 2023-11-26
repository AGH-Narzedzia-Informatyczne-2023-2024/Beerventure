from settings import *
import numpy as np

class Upgrade():
    def __init__(self, enemy, player):

        self.enemy = enemy
        self.player = player

        self.image = UPGRADE

        self.map = player.map
        self.x = enemy.x
        self.y = enemy.y

    def render(self):
        new_rect = self.image.get_rect()
        new_rect.center = (self.x, self.y)
        self.map.blit(self.image, new_rect)

    def pick_up(self):
        dist = np.sqrt((self.x - self.player.x)**2 + (self.y - self.player.y)**2)
        if dist < 10:
            return True
        return False