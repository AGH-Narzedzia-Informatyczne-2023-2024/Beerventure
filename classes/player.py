# This is the Player class file
from settings import *
import numpy as np

class Player():
    def __init__(self, map, x=0, y=0):

        #for now player textures as for enemy type==[self.pl_texture]
        #to change when player textures ready
        self.pl_texture = 0

        self.x = x
        self.y = y
        self.img = ENEMY_IMGS[self.pl_texture][0][0]
        self.map = map
        self.hp = 100
        self.dmg_counter = 0
        self.attack_power = PLAYER_ATTACK_POWER

        self.walk_txt = ENEMY_IMGS[self.pl_texture][0]
        self.atk_txt = ENEMY_IMGS[self.pl_texture][1]
        self.death_txt = ENEMY_IMGS[self.pl_texture][2]
        self.img = self.walk_txt[0]
        self.img_counter = 0
        self.atk_counter = 0
        self.side = 0   #left = 0, right = 1
        self.if_stopped = True  #true , false 

        self.hitbox = (self.x + self.img.get_width() / 2 - PLAYER_HITBOX, 
                       self.y + self.img.get_height() / 2 - PLAYER_HITBOX,
                       self.x + self.img.get_width() / 2 + PLAYER_HITBOX,
                       self.y + self.img.get_height() / 2 + PLAYER_HITBOX)

    def render(self):

        if self.img_counter > 0:
            self.renderWalk()

        if self.img_counter > 29:
            self.img_counter = 0

        if self.if_stopped:
            self.img = self.walk_txt[0]

        if self.dmg_counter > 0:
            self.dmg_counter -= 1
            self.img = ENEMY_IMGS[self.pl_texture+1][0][0]

        if self.side == 1:
            self.img = pygame.transform.flip(self.img, True, False)

        newRect = self.img.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        self.map.blit(self.img, newRect.topleft)

        #self.img = ENEMY_IMGS[self.pl_texture][0][0]

    def move(self, keys):
        ratio = 1

        if (keys[pygame.K_RIGHT] and [pygame.K_UP]) or (keys[pygame.K_RIGHT] and [pygame.K_DOWN]) or (keys[pygame.K_LEFT] and [pygame.K_UP]) or (keys[pygame.K_LEFT] and [pygame.K_DOWN]):
            ratio /= np.sqrt(2)

        if keys[pygame.K_RIGHT]:
            self.x += 2 * ratio
            self.img_counter += 1 * ratio
            self.side = 1
        if keys[pygame.K_UP]:
            self.y -= 2 * ratio
            self.img_counter += 1 * ratio
        if keys[pygame.K_LEFT]:
            self.x -= 2 * ratio
            self.img_counter += 1 * ratio
            self.side = 0
        if keys[pygame.K_DOWN]:
            self.y += 2 * ratio
            self.img_counter += 1 * ratio

        if (keys[pygame.K_DOWN]==False) and (keys[pygame.K_UP]==False) and (keys[pygame.K_LEFT]==False) and (keys[pygame.K_RIGHT]==False):
            self.if_stopped = True
        else:
            self.if_stopped = False

        self.hitbox = (self.x + self.img.get_width() / 2 - PLAYER_HITBOX, 
                       self.y + self.img.get_height() / 2 - PLAYER_HITBOX,
                       self.x + self.img.get_width() / 2 + PLAYER_HITBOX,
                       self.y + self.img.get_height() / 2 + PLAYER_HITBOX)
        pygame.draw.rect(self.map, (0, 0, 0),
                         (self.hitbox[0], self.hitbox[1],
                          self.hitbox[2] - self.hitbox[0],
                          self.hitbox[3] - self.hitbox[1]))

    def renderWalk(self):

        if self.img_counter == FPS:
            self.img_counter = 0
        if self.img_counter < ENEMY_ANIM_TIME:
            self.img = self.walk_txt[0]
        elif self.img_counter < ENEMY_ANIM_TIME * 2:
            self.img = self.walk_txt[1]
        elif self.img_counter < ENEMY_ANIM_TIME * 3:
            self.img = self.walk_txt[0]
        elif self.img_counter < ENEMY_ANIM_TIME * 4:
            self.img = self.walk_txt[2]
        elif self.img_counter < ENEMY_ANIM_TIME * 5:
            self.img = self.walk_txt[3]
        elif self.img_counter < ENEMY_ANIM_TIME * 6:
            self.img = self.walk_txt[2]

    #Attacks - added on Github

    def Okolocim(self):
        pass

    def SzarzaZubra(self):
        pass
