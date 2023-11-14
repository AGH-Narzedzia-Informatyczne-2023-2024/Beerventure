# This is the settings file
import pygame
import os

# Display settings
WIN_WIDTH = 200
WIN_HEIGHT = 200
SCALE_FACTOR = 4
FPS = 30

# Player settings
PLAYER_HITBOX = 15
PLAYER_DMG_ANIM = 8

# Enemy settings
ENEMY_STATS = {
    'SPD': [(1.05, 0.95), (0.85, 0.75), (1.25, 1.15)],
    'ATK_SPD': [1.2, 1.8, 1],
    'ATK_DMG': [20, 10, 10],
    'MELEE_RANGE': [30, 25, 25],
    'THROW_RANGE': [80, 100, 80],
    'THROW_PROB': [0.002, 0.004, 0],
    'HP': [150, 180, 150]
}

# Base enemy settings
# ENEMY_SPD = 0.6
# ENEMY_ATK_SPD = 1
# ENEMY_ATK_DMG = 10
# ENEMY_MELEE_RANGE = 25
# ENEMY_THROW_RANGE = 80
# ENEMY_THROW_PROB = 0.002
# ENEMY_HP = 100
ENEMY_ANIM_TIME = 5
INNER_SPAWN_RADIUS = 80
OUTER_SPAWN_RADIUS = 140

# Loading textures
BG_IMG = pygame.transform.scale(pygame.image.load("textures/bg.jpg"), (WIN_WIDTH, WIN_HEIGHT))

ENEMY_TYPES = ['per', 'tys', 'zyw']
ENEMY_IMGS = []
for dirname in os.walk('textures'):
    IMGS = []
    if dirname[0][9:] not in ENEMY_TYPES:
        print(dirname[0], 'a')
        continue
    for filename in os.listdir(dirname[0]):
        path = os.path.join(dirname[0], filename)
        if os.path.isfile(path):
            IMGS.append(pygame.image.load(path))
            print(path)
    ENEMY_IMGS.append(IMGS)

# ENEMY_IMGS = [[pygame.image.load("textures/zyw1.png"),
#               pygame.image.load("textures/zyw2.png"),
#               pygame.image.load("textures/zyw3.png"),
#               pygame.image.load("textures/zyw4.png"),
#               pygame.image.load("textures/zyw5.png"),
#               pygame.image.load("textures/zyw6.png"),
#               pygame.image.load("textures/zyw7.png"),
#               pygame.image.load("textures/zyw8.png"),],
#               [pygame.image.load("textures/per1.png"),
#               pygame.image.load("textures/per2.png"),
#               pygame.image.load("textures/per3.png"),
#               pygame.image.load("textures/per4.png"),
#               pygame.image.load("textures/per5.png"),
#               pygame.image.load("textures/per6.png"),
#               pygame.image.load("textures/per7.png"),
#               pygame.image.load("textures/per8.png")],
#               [pygame.image.load("textures/tys1.png"),
#               pygame.image.load("textures/tys2.png"),
#               pygame.image.load("textures/tys3.png"),
#               pygame.image.load("textures/tys4.png"),
#               pygame.image.load("textures/tys5.png"),
#               pygame.image.load("textures/tys6.png"),
#               pygame.image.load("textures/tys7.png"),
#               pygame.image.load("textures/tys8.png")]]
DEATH_IMGS = [pygame.image.load("textures/death1.png"),
              pygame.image.load("textures/death2.png"),
              pygame.image.load("textures/death3.png"),
              pygame.image.load("textures/death4.png"),
              pygame.image.load("textures/death5.png"),
              pygame.image.load("textures/death6.png"),
              pygame.image.load("textures/death7.png"),
              pygame.image.load("textures/death8.png")]
BOTTLE_IMGS = [pygame.image.load("textures/bottle/bottle1.png"),
          pygame.image.load("textures/bottle/bottle2.png"),
          pygame.image.load("textures/bottle/bottle3.png"),
          pygame.image.load("textures/bottle/bottle4.png"),
          pygame.image.load("textures/bottle/bottle5.png"),
          pygame.image.load("textures/bottle/bottle6.png"),
          pygame.image.load("textures/bottle/bottle7.png")]
          