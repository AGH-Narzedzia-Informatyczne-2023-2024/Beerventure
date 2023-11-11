# This is the Enemy class file

from Beerventure.settings import *
import numpy as np

class Enemy():
    def __init__(self, player, x=400, y=400, type='c'):
        self.x = x
        self.y = y
        self.type = type

        self.atk_speed = FPS / ENEMY_ATK_SPD
        self.atk_counter = 0
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

        newRect = self.img.get_rect(center = (self.x + self.img.get_width() / 2, self.y + self.img.get_height() / 2))
        self.screen.blit(self.img, newRect.topleft)

    def move(self):
        ratio = np.abs((self.y - self.player.y)) / np.abs((self.x - self.player.x))
        dx = np.sqrt(ENEMY_SPD ** 2 / (ratio ** 2 + 1))
        dy = dx * ratio

        if self.x + self.img.get_width() / 2 < self.player.hitbox[0]:
            self.x += dx
        elif self.x + self.img.get_width() / 2 > self.player.hitbox[2]:
            self.x -= dx
        if self.y + self.img.get_height() / 2< self.player.hitbox[1]:
            self.y += dy
        elif self.y + self.img.get_height() / 2 > self.player.hitbox[3]:
            self.y -= dy

        if np.sqrt((self.x - self.player.x) ** 2 + (self.y - self.player.y) ** 2) < ENEMY_ATK_RANGE:
            return self.attack()

        if self.in_range():
            self.takeDmg()

    def attack(self):
        self.atk_counter +=1

        if self.atk_counter > self.atk_speed:
            self.atk_counter = 0
            return True
        else:
            return False

    def takeDmg(self):
        if self.in_range():
            self.hp -= self.player.attack_power

    def showDie(self):
        if self.hp == 0:
            return True

    #Funkcja in_range do zmiany

    def in_range(self):
        if self.x + self.img.get_width() / 2 >= self.player.hitbox[0] :
            return True

        elif self.x + self.img.get_width() / 2 <= self.player.hitbox[2] :
            return True

        if self.y + self.img.get_height() / 2 >= self.player.hitbox[1] :
            return True

        elif self.y + self.img.get_height() / 2 <= self.player.hitbox[3] :
            return True
        return False