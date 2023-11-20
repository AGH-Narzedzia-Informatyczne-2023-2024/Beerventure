# This is the settings file

import pygame
import pygame.mixer
import os

# Display settings
WIN_WIDTH = 800
WIN_HEIGHT = 800
MAP_WIDTH = 1000
MAP_HEIGHT = 1000
SCALE_FACTOR = 4
FPS = 30

# Player settings
PLAYER_HITBOX = 15
PLAYER_DMG_ANIM = 8
PLAYER_ATTACK_POWER = 15

# Enemy settings
ENEMY_STATS = {
    'SPD': [(1, 0.9), (0.8, 0.7), (1.2, 1.1)],
    'ATK_SPD': [FPS / 1.5, FPS / 1, FPS / 1],
    'ATK_DMG': [20, 10, 10],
    'MELEE_RANGE': [30, 25, 25],
    'THROW_RANGE': [80, 100, 80],
    'THROW_PROB': [0.02, 0.04, 0.02],
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
THROW_VEL = 3
Y_SCALE = 0.4
Z_SCALE = 0.8

# Upgrades settings
DROP_CHANCE = 50

# Loading textures
BG_IMG = pygame.transform.scale(pygame.image.load("textures/map/bg.jpg"), (MAP_WIDTH, MAP_HEIGHT))

ENEMY_TYPES = ['per', 'tys', 'zyw']
ENEMY_IMGS = []
for dirname in os.walk('textures'):
    IMGS = [[] for _ in range(3)]
    if dirname[0][9:] not in ENEMY_TYPES:
        continue
    for filename in os.listdir(dirname[0]):
        path = os.path.join(dirname[0], filename)
        if os.path.isfile(path):
            IMGS[int(filename[0]) - 1].append(pygame.image.load(path))
    ENEMY_IMGS.append(IMGS)

BOTTLE_IMGS = [pygame.image.load("textures/bottle/bottle1.png"),
          pygame.image.load("textures/bottle/bottle2.png"),
          pygame.image.load("textures/bottle/bottle3.png"),
          pygame.image.load("textures/bottle/bottle4.png"),
          pygame.image.load("textures/bottle/bottle5.png"),
          pygame.image.load("textures/bottle/bottle6.png"),
          pygame.image.load("textures/bottle/bottle7.png")]
UPGRADE = pygame.image.load("textures/piwo.png")

# Loading sounds
pygame.mixer.init()
PLAYER_HURT = pygame.mixer.Sound("sounds/hitHurt.wav")
GET_UPGRADE = [pygame.mixer.Sound("sounds/powerUp.wav"),
               pygame.mixer.Sound("sounds/powerUp (1).wav")]