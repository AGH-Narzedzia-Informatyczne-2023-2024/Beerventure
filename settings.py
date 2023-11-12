# This is the settings file
import pygame

# Display settings
WIN_WIDTH = 200
WIN_HEIGHT = 200
SCALE_FACTOR = 4
FPS = 30

# Player settings
PLAYER_HITBOX = 15
PLAYER_DMG_ANIM = 8

# Enemy settings
ENEMY_SPD = 0.6
ENEMY_ATK_SPD = 1
ENEMY_ATK_DMG = 10
ENEMY_MELEE_RANGE = 25
ENEMY_THROW_RANGE = 80
ENEMY_THROW_PROB = 0.002

ENEMY_HP = 100
ENEMY_ANIM_TIME = 5
INNER_SPAWN_RADIUS = 80
OUTER_SPAWN_RADIUS = 140

# Loading textures
BG_IMG = pygame.transform.scale(pygame.image.load("textures/bg.jpg"), (WIN_WIDTH, WIN_HEIGHT))
ENEMY_IMGS = [[pygame.image.load("textures/zyw1.png"),
              pygame.image.load("textures/zyw2.png"),
              pygame.image.load("textures/zyw3.png"),
              pygame.image.load("textures/zyw4.png"),
              pygame.image.load("textures/zyw5.png"),
              pygame.image.load("textures/zyw6.png"),
              pygame.image.load("textures/zyw7.png"),
              pygame.image.load("textures/zyw8.png"),],
              [pygame.image.load("textures/per1.png"),
              pygame.image.load("textures/per2.png"),
              pygame.image.load("textures/per3.png"),
              pygame.image.load("textures/per4.png"),
              pygame.image.load("textures/per5.png"),
              pygame.image.load("textures/per6.png"),
              pygame.image.load("textures/per7.png"),
              pygame.image.load("textures/per8.png")],
              [pygame.image.load("textures/tys1.png"),
              pygame.image.load("textures/tys2.png"),
              pygame.image.load("textures/tys3.png"),
              pygame.image.load("textures/tys4.png"),
              pygame.image.load("textures/tys5.png"),
              pygame.image.load("textures/tys6.png"),
              pygame.image.load("textures/tys7.png"),
              pygame.image.load("textures/tys8.png")]]
BOTTLE_IMGS = [pygame.image.load("textures/bottle1.png"),
          pygame.image.load("textures/bottle2.png"),
          pygame.image.load("textures/bottle3.png"),
          pygame.image.load("textures/bottle4.png"),
          pygame.image.load("textures/bottle5.png"),
          pygame.image.load("textures/bottle6.png"),
          pygame.image.load("textures/bottle7.png")]
          