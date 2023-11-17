from settings import *
import numpy as np

class Bottle():
    def __init__(self, screen, x, y, dest_x, dest_y, range, dir):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.dest_x = dest_x
        self.dest_y = dest_y
        if dir == 1:
            self.grad = (y - dest_y) / (dest_x - x)
        else:
            self.grad = -(y - dest_y) / (dest_x - x)
        self.range = range
        self.dir = dir
        self.time = 0

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
        dx = np.sqrt(THROW_VEL ** 2 / (self.grad ** 2 + 1))
        if self.dir == -1:
            self.x -= dx
        else:
            self.x += dx
        
        # Calculate x distance from start to current and plug into linear function to obtain dy
        dx = np.abs(self.start_x - self.x)
        dy = self.grad * dx
        
        # Calculate the distance from the origin and plug into quadratic function to obtain dz
        dist = np.sqrt(dx ** 2 + dy ** 2)
        dz = -dist / (self.range / 4) * (dist / 3 - self.range / 3)

        # Scale dy and dz to obtain the y-coordinate of the bottle
        if self.start_y > self.dest_y:
            self.y = self.start_y - dy * (2 * Y_SCALE) - dz * Z_SCALE
        else:
            self.y = self.start_y - dy * Y_SCALE - dz * Z_SCALE

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