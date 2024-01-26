# This is the Player class file
from settings import *
import numpy as np

class Player():
    def __init__(self, map, x=50, y=50):

        #for now player textures as for enemy type==[self.pl_texture]
        #to change when player textures ready

        self.x = x
        self.y = y
        self.sprint = 0
        self.hp = 100
        self.attack_power = PLAYER_ATTACK_POWER
        
        self.idle_txt = PLAYER_IMGS[0]
        self.walk_txt = np.array(PLAYER_IMGS[len(PLAYER_IMGS) - 1])
        self.atk_txt = PLAYER_IMGS[2]
        self.death_txt = ENEMY_IMGS[0][2]
        self.img = self.idle_txt[0]
        self.img_counter = 0
        self.side = 1
        
        self.dmg_counter = 0
        self.atk_counter = 0
        self.atk_type = 0
        self.if_stopped = True  #true , false 
        self.map = map

    def render(self):
        idx = self.img_counter // PLAYER_ANIM_TIME
        if self.atk_type != 0:
            idx = self.img_counter // PLAYER_ATTACK_ANIM_TIME
            if idx >= len(self.atk_txt):
                idx -= 1
                self.atk_type = 0
            self.img = self.atk_txt[idx]
        
        elif not self.if_stopped:
            if self.sprint:
                idx = int(self.img_counter // (PLAYER_ANIM_TIME // 1.2))
            if idx >= len(self.walk_txt[0]):
                idx = 0
                self.img_counter = 0
            self.img = self.walk_txt[np.abs(self.side)][idx]

        elif self.if_stopped:
            self.img = self.idle_txt[0]

        if self.side > 0:
            self.img = pygame.transform.flip(self.img, True, False)

        self.img_counter += 1
        imgRect = self.img.get_rect()
        imgRect.center = (self.x, self.y)
        if self.dmg_counter > 0:
            self.dmg_counter -= 1
            self.img = self.overlayRed()
        self.map.blit(self.img, imgRect)

    def overlayRed(self):
        copied = pygame.Surface.copy(self.img)                # Overlay the image with red 
        for x in range(self.img.get_width()):                 # when taking damage
            for y in range(self.img.get_height()):            #
                color = self.img.get_at((x, y))               #
                if not color.a == 0:                          #
                    if color.r < 255 - self.dmg_counter * 50: # 
                        color.r += self.dmg_counter * 50      #
                    else:                                     #
                        color.r = 255                         #
                copied.set_at((x, y), color)                  #
        return copied

    def move(self, keys):
        # Get the state of right, up, left, and down arrow keys
        k_pressed = np.array([keys[pygame.K_d], keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s]])
        sprint = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        atk_pressed = np.array([keys[pygame.K_SPACE]])
        num_pressed = np.sum(k_pressed) # Check how many are pressed at the same time

        if self.atk_type != 0:
            return
        if atk_pressed[0]:
            self.atk_type = 1
            self.img_counter = 0
            return
        
        if num_pressed == 0:
            self.if_stopped = 1
            return
        else:
            if num_pressed > 1:
                spd = PLAYER_SPD / np.sqrt(2)
            else:
                spd = PLAYER_SPD
            self.if_stopped = 0

        if sprint:
            self.sprint = 1
            spd += 0.3
        else:
            self.sprint = 0

        # Determine which of the 8 sides the player is facing and move in that direction
        if keys[pygame.K_d]:
            self.x += spd
            self.side = 2
            if keys[pygame.K_s]:
                self.side = 1
            if keys[pygame.K_w]:
                self.side = 3
        if keys[pygame.K_w]:
            self.y -= spd
            self.side = 4
            if keys[pygame.K_a]:
                self.side = -3
            if keys[pygame.K_d]:
                self.side = 3
        if keys[pygame.K_a]:
            self.x -= spd
            self.side = -2
            if keys[pygame.K_s]:
                self.side = -1
            if keys[pygame.K_w]:
                self.side = -3
        if keys[pygame.K_s]:
            self.y += spd
            self.side = 0
            if keys[pygame.K_a]:
                self.side = -1
            if keys[pygame.K_d]:
                self.side = 1

# Attacks added locally

    def Slash(self):
        self.atk_type = 1

    def Spin(self):
        pass

    def Bomb(self):
        pass
