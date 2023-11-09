# This is the Enemy class file

from settings import *
import numpy as np

class Enemy():
    def __init__(self, player, x=400, y=400, type='c'):
        self.x = x
        self.y = y
        self.type = type

        self.atk_speed = ENEMY_ATK_SPD
        self.dmg = ENEMY_ATK_DMG
        self.hp = ENEMY_HP

        self.angle = 0
        self.img = ENEMY_IMGS[0]
        self.imgCount = 0
        self.player = player
        self.screen = player.screen

    def render(self):
        self.imgCount += 1

        if self.imgCount < ENEMY_ANIM_TIME:
            self.img = ENEMY_IMGS[0]
        elif self.imgCount < ENEMY_ANIM_TIME * 2:
            self.img = ENEMY_IMGS[1]
        elif self.imgCount < ENEMY_ANIM_TIME * 3:
            self.img = ENEMY_IMGS[2]
        elif self.imgCount < ENEMY_ANIM_TIME * 4:
            self.img = ENEMY_IMGS[1]
        elif self.imgCount < ENEMY_ANIM_TIME * 4 + 1:
            self.img = ENEMY_IMGS[0]
            self.imgCount = 0

        newRect = self.img.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        self.screen.blit(self.img, newRect.topleft)

    def move(self):
        ratio = np.abs((self.y - self.player.y)) / np.abs((self.x - self.player.x))
        dx = np.sqrt(ENEMY_SPD ** 2 / (ratio ** 2 + 1))
        dy = dx * ratio

        if self.player.x < self.x:
            dx = -dx
        if self.player.y < self.y:
            dy = -dy

        self.x += dx
        self.y += dy

    def attack(self):
        pass

    def takeDmg(self):
        pass

    def showDie(self):
        pass