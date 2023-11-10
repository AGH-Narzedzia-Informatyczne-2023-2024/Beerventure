# This is the settings file

import pygame

# Display settings
WIN_WIDTH = 200
WIN_HEIGHT = 200
SCALE_FACTOR = 4
FPS = 30

# Player settings
PLAYER_HITBOX = 10
PLAYER_DMG_ANIM = 8

# Enemy settings
ENEMY_SPD = 1
ENEMY_ATK_SPD = 1
ENEMY_ATK_DMG = 10
ENEMY_ATK_RANGE = 30
ENEMY_HP = 100
ENEMY_ANIM_TIME = 4

# Loading textures
BG_IMG = pygame.transform.scale(pygame.image.load("textures/bg.jpg"), (WIN_WIDTH, WIN_HEIGHT))
ENEMY_IMGS = [pygame.image.load("textures/enemy1.png"),
              pygame.image.load("textures/enemy1.png"),
              pygame.image.load("textures/enemy1.png"),
              pygame.image.load("textures/dmg.png")]