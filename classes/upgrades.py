from settings import *

class Upgrade():
    def __init__(self, enemy, player):

        self.enemy = enemy
        self.player = player

        self.image = UPGRADE

        self.map = player.map
        self.x = enemy.x
        self.y = enemy.y

    def render(self):
        new_rect = self.image.get_rect(center=(self.x + self.image.get_width() / 2, self.y + self.image.get_height() / 2))
        self.map.blit(self.image, new_rect.topleft)

    def pick_up(self):
        if ((self.x + self.image.get_width() / 2) >= self.player.hitbox[0] and (self.x + self.image.get_width() / 2) <= self.player.hitbox[2]) and ((self.y + self.image.get_height() / 2) >= self.player.hitbox[1] and (self.y + self.image.get_height() / 2 <= self.player.hitbox[3])):
            return True
        return False