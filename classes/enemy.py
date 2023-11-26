# This is the Enemy class file

from settings import *
from .bottle import *
import numpy as np
import random

class Enemy():
    def __init__(self, player, x=400, y=400, type=0):
        self.x = x       # Current position
        self.y = y       #
        self.type = type # Enemy type (per / tys / zyw)
        self.atk = 0     # Whether the enemy is currently in an attack animation (1) or not (0)
        self.active = 1  # Whether the enemy is alive (1) or in the dying animation (0)
        self.destroy = 0 # Whether the dying animation has completed (1) or not (0)

        # Loading stats according to the enemy type
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

        self.walk_txt = ENEMY_IMGS[self.type][0]  # Walking animation textures
        self.atk_txt = ENEMY_IMGS[self.type][1]   # Melee attack animation textures
        self.death_txt = ENEMY_IMGS[self.type][2] # Dying animation textures
        self.img = self.walk_txt[0] # Current image being rendered
        self.img_counter = 0        # Counter variable used to display the current image for a specifies number of frames
        self.atk_counter = 0        # Counter variable used to only trigger melee attacks as often as the attack speed allows
        self.fall_dir = 0           # Whether the enemy is facing backward (-1) or forward (1) while dying

        self.bottles = []           # A list of bottles currently flying towards the player
        self.player = player        # Passing the player argument
        self.map = player.map       # Surface to render the sprite on

    def move(self):
        self.hp -= 0.5

        # Don't move if an attack or dying animation is currently playing
        if self.atk or not self.active:
            return
        ratio = np.abs((self.y - self.player.y) / (self.x - self.player.x)) # Find the gradient of the line connecting the enemy to the player
        dx = np.sqrt(self.spd ** 2 / (ratio ** 2 + 1))                      # Find the distance to move on the x-axis (via pythagorean theorem)
        dy = dx * ratio                                                     # Find the distance to move on the y-axis (via the gradient)

        # Move in the correct direction and don't walk onto the player
        dist = np.sqrt((self.x - self.player.x)**2 + (self.y - self.player.y)**2)
        if dist > PLAYER_BORDER:
            if self.x < self.player.x:
                self.x += dx
            else:
                self.x -= dx
            if self.y < self.player.y:
                self.y += dy
            else:
                self.y -= dy

    def checkRange(self):
        dist = np.sqrt((self.x - self.player.x) ** 2 + (self.y - self.player.y) ** 2) # Find distance from player
        if dist < self.melee_range: # If in range for a melee attack
            return 1
        elif dist > self.throw_range - 5 and dist < self.throw_range: # If within min and max range for bottle throw
            return 2
        
        self.atk_counter = 0 # If not in range for any attack, reset the counter
        return 0
    
    def checkHit(self, type):
        if type == 'melee':
            dist = np.sqrt((self.x - self.player.x) ** 2 + (self.y - self.player.y) ** 2)
            if dist < MELEE_HITBOX:
                return 1
            return 0
        elif type == 'throw':
            for bottle in self.bottles:
                if not bottle.active:
                    dist = np.sqrt((bottle.x - self.player.x) ** 2 + (bottle.y - self.player.y) ** 2)
                    print(dist)
                    if dist < BOTTLE_HITBOX:
                        return 1
                    return 0

    def attack(self):
        self.atk_counter +=1

        # Attack if the enemy only just got in range. or has been standing near the player and enough time has passed since last attack
        if self.checkRange() and (self.atk_counter > self.atk_speed or self.atk_counter == 1):
            self.img_counter = 0
            self.atk = 1
            if self.atk_counter > self.atk_speed: # If enough time has passed since last attack, reset the counter 
                self.atk_counter = 1
            return True
        return False
    
    def throw(self):
        # Find the direction in which the bottle will fly
        if self.x < self.player.x:
            dir = 1
        else:
            dir = -1
        bottle = Bottle(self.map, self.x, self.y, self.player.x, self.player.y, self.throw_range, dir)
        self.bottles.append(bottle) # Append the new bottle to the bottle list

    def render(self):
        # Move and render bottles
        for idx, bottle in enumerate(self.bottles):
            bottle.move()
            # If the bottle has reached its destination, mark it as inactive
            if bottle.dir == 1 and bottle.x > bottle.dest_x and bottle.y >= bottle.dest_y or bottle.dir == -1 and bottle.x < bottle.dest_x and bottle.y >= bottle.dest_y :
                bottle.active = 0
            if bottle.destroy:
                del self.bottles[idx]

        # Play death animation
        if self.hp <= 0:
            # Determine which way the enemy is facing when falling
            if self.fall_dir == 0:
                if self.x < self.player.x:
                    self.fall_dir = 1
                else:
                    self.fall_dir = -1
            if self.active:
                self.img_counter = 0
                self.active = 0
            idx = int(self.img_counter // (DEATH_ANIM_SCALE * ENEMY_ANIM_TIME))
            if idx == len(self.death_txt):
                idx -= 1
                self.destroy = 1
            self.img = self.death_txt[idx]

        # Play melee attack animation
        elif self.atk:    
            idx = int(self.img_counter // (ATK_ANIM_SCALE * ENEMY_ANIM_TIME)) 
            if idx == len(self.atk_txt):
                self.img_counter = 0
                self.atk = 0
            else:
                self.img = self.atk_txt[idx]

        # Play walk animation
        if not self.atk and self.active:
            idx = int(self.img_counter // ENEMY_ANIM_TIME)
            if idx == len(self.walk_txt):
                idx = 0
                self.img_counter = 0
            self.img = self.walk_txt[idx]

        # Flip the image if facing right
        if self.x < self.player.x and self.fall_dir == 0 or self.fall_dir == 1:
            self.img = pygame.transform.flip(self.img, True, False)
        imgRect = self.img.get_rect()
        imgRect.center = (self.x, self.y)
        self.map.blit(self.img, imgRect)
        self.img_counter += 1