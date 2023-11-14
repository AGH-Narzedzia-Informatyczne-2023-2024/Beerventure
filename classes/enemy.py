# This is the Enemy class file

from settings import *
import numpy as np
import random

class Bottle():
    def __init__(self, screen, x, y, range, dir):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.range = range
        self.dir = dir
        self.active = 1
        self.destroy = 0

        self.img = BOTTLE_IMGS[0]
        self.img_counter = 0
        self.angle_counter = 0

        self.screen = screen
    
    def move(self):
        # If bottle has hit the ground
        if not self.active:
            self.render()
            return
        
        # Move along x axis
        if self.dir == -1:
            self.x -= 2
        else:
            self.x += 2
        
        # Calculate x distance from start to current and plug into function to obtain dy
        dx = np.abs(self.start_x - self.x)
        dy = -dx / (self.range / 4) * (dx / 3 - self.range / 3)
        
        # Move along y axis
        self.y = self.start_y - dy

        self.render()

    def render(self):
        # Breaking animation
        if not self.active:
            self.img_counter += 1

            if self.img_counter < ENEMY_ANIM_TIME // 2:
                self.img = BOTTLE_IMGS[1]
            elif self.img_counter < ENEMY_ANIM_TIME // 2 * 2:
                self.img = BOTTLE_IMGS[2]
            elif self.img_counter < ENEMY_ANIM_TIME // 2 * 3:
                self.img = BOTTLE_IMGS[3]
            elif self.img_counter < ENEMY_ANIM_TIME // 2 * 4:
                self.img = BOTTLE_IMGS[4]
            elif self.img_counter < ENEMY_ANIM_TIME // 2 * 5:
                self.img = BOTTLE_IMGS[5]
            elif self.img_counter == ENEMY_ANIM_TIME // 2 * 5:
                self.img = BOTTLE_IMGS[6]
                self.destroy == 1
            
            self.screen.blit(self.img, (self.x, self.y))
            return

        # Rotating the texture
        self.angle_counter += 1
        if self.angle_counter % ENEMY_ANIM_TIME == 0:
            self.img = pygame.transform.rotate(BOTTLE_IMGS[0], -self.dir * self.angle_counter // ENEMY_ANIM_TIME * 45)

        self.screen.blit(self.img, (self.x, self.y))


class Enemy():
    def __init__(self, player, x=400, y=400, type=0):
        self.x = x
        self.y = y
        self.type = type
        self.atk = 0
        self.active = 1
        self.destroy = 0

        # Loading stats
        stats = dict()
        for idx in ENEMY_STATS:
            stats[idx] = ENEMY_STATS[idx][type]
        self.spd = random.uniform(stats['SPD'][0], stats['SPD'][1])
        self.atk_speed = stats['ATK_SPD']
        self.dmg = stats['ATK_DMG']
        self.melee_range = stats['MELEE_RANGE']
        self.throw_range = stats['THROW_RANGE']
        self.throw_prob = stats['THROW_PROB']
        self.hp = stats['HP']

        self.textures = ENEMY_IMGS[self.type]
        self.img = self.textures[0]
        self.img_counter = 0
        self.atk_counter = 0

        self.bottles = []
        self.player = player
        self.screen = player.screen

    def render(self):
        # self.hp -= 1

        # Move and render bottles
        for idx, bottle in enumerate(self.bottles):
            bottle.move()
            if bottle.dir == 1 and bottle.x > bottle.start_x + self.throw_range or bottle.dir == -1 and bottle.x < bottle.start_x - self.throw_range:
                bottle.active = 0
            if bottle.destroy:
                del self.bottles[idx]
                
        offset = 0

        # Play death animation
        if self.hp <= 0:
            if self.active:
                self.img_counter = 0
                self.active = 0
            self.img_counter += 1

            if self.img_counter < ENEMY_ANIM_TIME / 1.6:
                self.img = DEATH_IMGS[0]
            elif self.img_counter < ENEMY_ANIM_TIME / 1.6 * 2:
                self.img = DEATH_IMGS[1]
            elif self.img_counter < ENEMY_ANIM_TIME / 1.6 * 3:
                self.img = DEATH_IMGS[2]
            elif self.img_counter < ENEMY_ANIM_TIME / 1.6 * 4:
                self.img = DEATH_IMGS[3]
            elif self.img_counter < ENEMY_ANIM_TIME / 1.6 * 6:
                self.img = DEATH_IMGS[4]
            elif self.img_counter < ENEMY_ANIM_TIME / 1.6 * 7:
                self.img = DEATH_IMGS[5]
            elif self.img_counter < ENEMY_ANIM_TIME / 1.6 * 8:
                self.img = DEATH_IMGS[6]
            elif self.img_counter >= ENEMY_ANIM_TIME / 1.6 * 8:
                self.img = DEATH_IMGS[7]
                self.destroy = 1
            
            if self.x < self.player.x:
                self.img = pygame.transform.flip(self.img, True, False)
            self.screen.blit(self.img, (self.x, self.y))
            return

        # Play melee attack animation
        if self.atk:    
            if self.img_counter == 4 * ENEMY_ANIM_TIME:
                if self.x > self.player.x:
                    offset = 0
                self.atk = 0
            elif self.img_counter < ENEMY_ANIM_TIME:
                self.img = self.textures[4]
            elif self.img_counter < ENEMY_ANIM_TIME * 2:
                self.img = self.textures[5]
            elif self.img_counter < ENEMY_ANIM_TIME * 3:
                self.img = self.textures[6]
                if self.x > self.player.x:
                    offset = -11
                else:
                    offset = 2
            elif self.img_counter < ENEMY_ANIM_TIME * 4:
                self.img = self.textures[7]
                if self.x > self.player.x:
                    offset = -4
                else:
                    offset = 0

        if not self.atk:
            if self.img_counter == FPS:
                self.img_counter = 0
            if self.img_counter < ENEMY_ANIM_TIME:
                self.img = self.textures[0]
            elif self.img_counter < ENEMY_ANIM_TIME * 2:
                self.img = self.textures[1]
            elif self.img_counter < ENEMY_ANIM_TIME * 3:
                self.img = self.textures[0]
            elif self.img_counter < ENEMY_ANIM_TIME * 4:
                self.img = self.textures[2]
            elif self.img_counter < ENEMY_ANIM_TIME * 5:
                self.img = self.textures[3]
            elif self.img_counter < ENEMY_ANIM_TIME * 6:
                self.img = self.textures[0]
    
        self.img_counter += 1
        if self.x < self.player.x:
            self.img = pygame.transform.flip(self.img, True, False)

        self.screen.blit(self.img, (self.x + offset, self.y))

    def move(self):
        if self.atk or not self.active:
            return

        ratio = np.abs((self.y - self.player.y)) / np.abs((self.x - self.player.x))
        dx = np.sqrt(self.spd ** 2 / (ratio ** 2 + 1))
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
        if dist < self.melee_range:
            return 1
        elif dist < self.throw_range and self.y > self.player.y - PLAYER_HITBOX and self.y < self.player.y + self.player.img.get_height() + PLAYER_HITBOX:
            return 2
        
        self.atk_counter = 0
        return 0

    def attack(self):
        self.atk_counter +=1

        if self.checkRange() and (self.atk_counter > FPS / self.atk_speed or self.atk_counter == 1):
            self.img_counter = 0
            self.atk = 1
            if self.atk_counter > FPS:
                self.atk_counter = 1
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
        bottle = Bottle(self.screen, self.x, self.y, self.throw_range, dir)
        self.bottles.append(bottle)

