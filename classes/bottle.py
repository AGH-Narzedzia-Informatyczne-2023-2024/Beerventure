from settings import *
import numpy as np

class Bottle():
    def __init__(self, screen, x, y, dest_x, dest_y, range, dir):
        self.x = x           # Current position
        self.y = y           #
        self.start_x = x     # Starting position
        self.start_y = y     #
        self.dest_x = dest_x # Destination
        self.dest_y = dest_y #
        
        # Find the gradient of the line connecting the starting position and destination;
        # Flip the gradient if the bottle is flying towards negative x
        if dir == 1:
            self.grad = (y - dest_y) / (dest_x - x)
        else:
            self.grad = -(y - dest_y) / (dest_x - x)
        self.range = range
        self.dir = dir

        self.active = 1  # Specifies whether the bottle is flying (1) or has hit the ground (0)
        self.destroy = 0 # Specifies whether the breaking animation has finished (1) or not (0)

        self.img = BOTTLE_IMGS[0] # Loading textures
        self.img_counter = 0      # Expleined in enemy.__init__()
        self.angle_counter = 0    # Counter variable keeping track of the rotation of the bottle

        self.screen = screen      # Surface to render the sprite on
    
    def move(self):
        # Don't move if bottle has hit the ground
        if not self.active:
            self.render()
            return
        
        # Move along x-axis
        dx = np.sqrt(THROW_VEL ** 2 / (self.grad ** 2 + 1)) # Explained in enemy.move()
        if self.dir == -1:
            self.x -= dx
        else:
            self.x += dx
        
        # Find x distance from start to current and plug into linear function to obtain y displacement
        dx = np.abs(self.start_x - self.x)
        dy = self.grad * dx
        
        # Find overall distance from start to current and plug into quadratic function to obtain z displacement
        dist = np.sqrt(dx ** 2 + dy ** 2)
        dz = -dist / (self.range / 4) * (dist / 3 - self.range / 3)

        # Scale dy and dz to obtain the y-coordinate of the bottle; move along y-axis
        if self.start_y > self.dest_y:
            self.y = self.start_y - dy * (2 * Y_SCALE) - dz * Z_SCALE
        else:
            self.y = self.start_y - dy * Y_SCALE - dz * Z_SCALE

        self.render()

    def render(self):
        # Play breaking animation
        if not self.active:
            idx = int(self.img_counter // (ENEMY_ANIM_TIME // 2)) + 1
            if idx == len(BOTTLE_IMGS):
                idx -= 1
                self.destroy = 1
            self.img = pygame.transform.rotate(BOTTLE_IMGS[idx], -self.dir * self.angle_counter // ENEMY_ANIM_TIME * 45)
            self.img_counter += 1
            
        else:
            # Appropriately rotate the texture
            self.angle_counter += 1
            if self.angle_counter % ENEMY_ANIM_TIME == 0:
                self.img = pygame.transform.rotate(BOTTLE_IMGS[0], -self.dir * self.angle_counter // ENEMY_ANIM_TIME * 45)

        self.screen.blit(self.img, (self.x, self.y))