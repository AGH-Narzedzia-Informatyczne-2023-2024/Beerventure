# This is the Enemy class file

from settings import *
import numpy as np

class Bottle():
    def __init__(self, screen, x, y, dir):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.dir = dir

        self.img = BOTTLE_IMGS[0]
        self.img_count = 0
        self.angle_count = 0
        self.active = 1
        self.destroy = 0

        self.screen = screen
    
    def move(self):
        if not self.active:
            self.render()
            return
        
        if self.dir == -1:
            self.x -= 2
        else:
            self.x += 2
        
        dx = np.abs(self.start_x - self.x)
        dy = -dx / (ENEMY_THROW_RANGE / 4) * (dx / 3 - ENEMY_THROW_RANGE / 3)
        self.y = self.start_y - dy

        self.render()

    def render(self):
        if not self.active:
            self.img_count += 1

            if self.img_count < ENEMY_ANIM_TIME // 2:
                self.img = BOTTLE_IMGS[1]
            elif self.img_count < ENEMY_ANIM_TIME // 2 * 2:
                self.img = BOTTLE_IMGS[2]
            elif self.img_count < ENEMY_ANIM_TIME // 2 * 3:
                self.img = BOTTLE_IMGS[3]
            elif self.img_count < ENEMY_ANIM_TIME // 2 * 4:
                self.img = BOTTLE_IMGS[4]
            elif self.img_count < ENEMY_ANIM_TIME // 2 * 5:
                self.img = BOTTLE_IMGS[5]
            elif self.img_count == ENEMY_ANIM_TIME // 2 * 5:
                self.img = BOTTLE_IMGS[6]
                self.destroy == 1
            
            self.screen.blit(self.img, (self.x, self.y))
            return

        self.angle_count += 1
        if self.angle_count % ENEMY_ANIM_TIME == 0:
            self.img = pygame.transform.rotate(BOTTLE_IMGS[0], -self.dir * self.angle_count // ENEMY_ANIM_TIME * 45)

        self.screen.blit(self.img, (self.x, self.y))

class Enemy():
    def __init__(self, player, x=400, y=400, type=0):
        self.x = x
        self.y = y
        self.type = type
        self.bottles = []

        self.atk_speed = FPS / ENEMY_ATK_SPD
        self.atk_counter = 0
        self.state = 0
        self.hp = ENEMY_HP

        self.img = ENEMY_IMGS[self.type][0]
        self.imgCount = 0

        self.player = player
        self.screen = player.screen

    def render(self):
        for idx, bottle in enumerate(self.bottles):
            bottle.move()
            if bottle.dir == 1 and bottle.x > bottle.start_x + ENEMY_THROW_RANGE or bottle.dir == -1 and bottle.x < bottle.start_x - ENEMY_THROW_RANGE:
                bottle.active = 0
            if bottle.destroy:
                del self.bottles[idx]
                
        offset = 0
        if self.state:    
            if self.imgCount == 4 * ENEMY_ANIM_TIME:
                if self.x > self.player.x:
                    offset = 0
                self.state = 0
                return
            if self.imgCount < ENEMY_ANIM_TIME:
                self.img = ENEMY_IMGS[self.type][4]
            elif self.imgCount < ENEMY_ANIM_TIME * 2:
                self.img = ENEMY_IMGS[self.type][5]
            elif self.imgCount < ENEMY_ANIM_TIME * 3:
                self.img = ENEMY_IMGS[self.type][6]
                if self.x > self.player.x:
                    offset = -11
                else:
                    offset = 2
            elif self.imgCount < ENEMY_ANIM_TIME * 4:
                self.img = ENEMY_IMGS[self.type][7]
                if self.x > self.player.x:
                    offset = -4
                else:
                    offset = 0

        else:
            if self.imgCount == FPS:
                self.imgCount = 0
            if self.imgCount < ENEMY_ANIM_TIME:
                self.img = ENEMY_IMGS[self.type][0]
            elif self.imgCount < ENEMY_ANIM_TIME * 2:
                self.img = ENEMY_IMGS[self.type][1]
            elif self.imgCount < ENEMY_ANIM_TIME * 3:
                self.img = ENEMY_IMGS[self.type][0]
            elif self.imgCount < ENEMY_ANIM_TIME * 4:
                self.img = ENEMY_IMGS[self.type][2]
            elif self.imgCount < ENEMY_ANIM_TIME * 5:
                self.img = ENEMY_IMGS[self.type][3]
            elif self.imgCount < ENEMY_ANIM_TIME * 6:
                self.img = ENEMY_IMGS[self.type][0]
    
        self.imgCount += 1
        if self.x < self.player.x:
            self.img = pygame.transform.flip(self.img, True, False)

        self.screen.blit(self.img, (self.x + offset, self.y))

    def move(self):
        if self.state:
            return

        ratio = np.abs((self.y - self.player.y)) / np.abs((self.x - self.player.x))
        dx = np.sqrt(ENEMY_SPD ** 2 / (ratio ** 2 + 1))
        dy = dx * ratio

        if self.x + self.img.get_width() / 2 < self.player.hitbox[0]:
            self.x += dx
        elif self.x + self.img.get_width() / 2 > self.player.hitbox[2]:
            self.x -= dx
        if self.y + self.img.get_height() / 2 < self.player.hitbox[1]:
            self.y += dy
        elif self.y + self.img.get_height() / 2 > self.player.hitbox[3]:
            self.y -= dy

    def checkRange(self):
        dist = np.sqrt((self.x - self.player.x) ** 2 + (self.y - self.player.y) ** 2)
        if dist < ENEMY_MELEE_RANGE:
            return 1
        elif dist < ENEMY_THROW_RANGE and self.y > self.player.y - PLAYER_HITBOX and self.y < self.player.y + self.player.img.get_height() + PLAYER_HITBOX:
            return 2
        return 0

    def attack(self):
        self.atk_counter +=1

        if self.atk_counter > self.atk_speed and self.checkRange():
            self.imgCount = 0
            self.state = 1
            self.atk_counter = 0
            return True
        return False
    
    def takeDmg(self):
        pass

    def showDie(self):
        pass

    def throw(self):
        if self.x < self.player.x:
            dir = 1
        else:
            dir = -1
        bottle = Bottle(self.screen, self.x, self.y, dir)
        self.bottles.append(bottle)

