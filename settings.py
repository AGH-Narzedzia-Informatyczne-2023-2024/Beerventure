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
ENEMY_SPD = 0.6
ENEMY_ATK_SPD = 0.5
ENEMY_ATK_DMG = 10
ENEMY_ATK_RANGE = 30
ENEMY_HP = 100
ENEMY_ANIM_TIME = 5
INNER_SPAWN_RADIUS = 80
OUTER_SPAWN_RADIUS = 140

# Loading textures
BG_IMG = pygame.transform.scale(pygame.image.load("textures/bg.jpg"), (WIN_WIDTH, WIN_HEIGHT))
ENEMY_IMGS = [[pygame.image.load("textures/zyw1.png"),
              pygame.image.load("textures/zyw2.png"),
              pygame.image.load("textures/zyw3.png"),
              pygame.image.load("textures/zyw4.png")],
              [pygame.image.load("textures/per1.png"),
              pygame.image.load("textures/per2.png"),
              pygame.image.load("textures/per3.png"),
              pygame.image.load("textures/per4.png")],
              [pygame.image.load("textures/tys1.png"),
              pygame.image.load("textures/tys2.png"),
              pygame.image.load("textures/tys3.png"),
              pygame.image.load("textures/tys4.png")]]