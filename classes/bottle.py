from settings import *
import numpy as np

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