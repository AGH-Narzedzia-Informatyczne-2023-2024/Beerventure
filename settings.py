# This is the settings file

import pygame
import pygame.mixer

# Display settings
WIN_WIDTH = 200
WIN_HEIGHT = 200
SCALE_FACTOR = 4
FPS = 30

# Player settings
PLAYER_HITBOX = 10
PLAYER_DMG_ANIM = 8
PLAYER_ATTACK_POWER = 5

# Enemy settings
ENEMY_SPD = 1
ENEMY_ATK_SPD = 1
ENEMY_ATK_DMG = 10
ENEMY_ATK_RANGE = 30
ENEMY_HP = 100
ENEMY_ANIM_TIME = 4

# Upgrades settings
DROP_CHANCE = 50

# Loading textures
BG_IMG = pygame.transform.scale(pygame.image.load("textures/bg.jpg"), (WIN_WIDTH, WIN_HEIGHT))
ENEMY_IMGS = [pygame.image.load("textures/enemy1.png"),
              pygame.image.load("textures/enemy1.png"),
              pygame.image.load("textures/enemy1.png"),
              pygame.image.load("textures/dmg.png")]
UPGRADE = pygame.image.load("textures/piwo.png")

# Loading sounds
pygame.mixer.init()
PLAYER_HURT = pygame.mixer.Sound("sounds/hitHurt.wav")
GET_UPGRADE = [pygame.mixer.Sound("sounds/powerUp.wav"),
               pygame.mixer.Sound("sounds/powerUp (1).wav")]