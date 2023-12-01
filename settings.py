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
PLAYER_BORDER = 20
PLAYER_ATTACK_POWER = 15
PLAYER_ANIM_TIME = 6
PLAYER_SPD = 1.2

# Enemy settings
ENEMY_STATS = {     #per        tys         zyw
    'SPD':          [(1, 0.9),  (0.8, 0.7), (1.2, 1.1)],
    'ATK_SPD':      [FPS / 1.5, FPS / 1,    FPS / 1],
    'ATK_DMG':      [20,        10,         10],
    'MELEE_RANGE':  [25,        25,         25],
    'THROW_RANGE':  [80,        100,        80],
    'THROW_PROB':   [0.02,      0.04,       0.02],
    'HP':           [150,       180,        150]
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
MELEE_HITBOX = 35
ATK_ANIM_SCALE = 1
DEATH_ANIM_SCALE = 0.8
INNER_SPAWN_RADIUS = 80
OUTER_SPAWN_RADIUS = 140
THROW_VEL = 3
BOTTLE_HITBOX = 20
Y_SCALE = 0.4
Z_SCALE = 0.8

# Boss settings
BOSS_STATS = {
    'SPD':          [0.5],
    'MELEE_SPD':    [FPS / 0.5],
    'MELEE_DMG':    [20],
    'MELEE_RANGE':  [30],
    'ATK_DMG':      [50],
    'ATK_RANGE':    [200],
    'ATK_BREAK':    [5],
    'HP':           [1000]
}

# Upgrades settings
DROP_CHANCE = 50

# Loading textures
BG_IMG = pygame.transform.scale(pygame.image.load("textures/map/bg.jpg"), (MAP_WIDTH, MAP_HEIGHT))

PLAYER_IMGS = [[] for _ in range(2)]
WALK_IMGS = [[] for _ in range(5)]
for filename in os.listdir('textures\player'):
    path = os.path.join('textures\player', filename)
    if os.path.isfile(path):
        file = pygame.image.load(path)
        if int(filename[0]) == 1:
            WALK_IMGS[int(filename[2])].append(file)
        else:
            PLAYER_IMGS[int(filename[0])].append(file)
PLAYER_IMGS.append(WALK_IMGS)
ENEMY_TYPES = ['per', 'tys', 'zyw']
ENEMY_IMGS = []
for dirname in os.walk('textures'):
    IMGS = [[] for _ in range(3)]
    if dirname[0][9:] not in ENEMY_TYPES:
        continue
    for filename in os.listdir(dirname[0]):
        path = os.path.join(dirname[0], filename)
        if os.path.isfile(path):
            file = pygame.image.load(path)
            IMGS[int(filename[0]) - 1].append(file)
    ENEMY_IMGS.append(IMGS)

BOSS_TYPES = ['vod']
BOSS_IMGS = []
for dirname in os.walk('textures'):
    IMGS = [[] for _ in range(len(BOSS_TYPES))]
    if dirname[0][9:] not in BOSS_TYPES:
        continue
    for filename in os.listdir(dirname[0]):
        path = os.path.join(dirname[0], filename)
        if os.path.isfile(path):
            file = pygame.image.load(path)
            IMGS[int(filename[0]) - 1].append(file)
    BOSS_IMGS.append(IMGS)

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