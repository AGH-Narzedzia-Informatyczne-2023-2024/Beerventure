import pygame
from random import randint, choice
import numpy as np
from .enemy import Enemy
from .player import Player
from .upgrades import Upgrade
from settings import *

class Game():
    def __init__(self):
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.map = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
        self.player = Player(self.map, 0, 0)
        self.enemies = []
        self.upgrades = []

    def spawnEnemy(self):
        (dirx, diry) = (choice([(np.floor(self.player.x - OUTER_SPAWN_RADIUS), np.floor(self.player.x - INNER_SPAWN_RADIUS)),
                                (np.floor(self.player.x + INNER_SPAWN_RADIUS), np.floor(self.player.x + OUTER_SPAWN_RADIUS))]),
        choice([(np.floor(self.player.y - OUTER_SPAWN_RADIUS), np.floor(self.player.y - INNER_SPAWN_RADIUS)),
                                (np.floor(self.player.y + INNER_SPAWN_RADIUS), np.floor(self.player.y + OUTER_SPAWN_RADIUS))]))
        x, y = randint(*dirx), randint(*diry)
        type = randint(0, 2)
        self.enemies.append(Enemy(self.player, x, y, type))

    def renderWindow(self):
        self.map.blit(BG_IMG, (0, 0))
        self.player.render()
        for enemy in self.enemies:
            enemy.render()
        for upgrade in self.upgrades:
            upgrade.render()

        win_pos = (-((self.player.x + self.player.img.get_width() / 2) * SCALE_FACTOR - WIN_WIDTH / 2),
                   -((self.player.y + self.player.img.get_height() / 2) * SCALE_FACTOR - WIN_HEIGHT / 2))
        pygame.draw.rect(self.window, 'black', (0, 0, WIN_WIDTH, WIN_HEIGHT))
        self.window.blit(pygame.transform.scale(self.map, (MAP_WIDTH * SCALE_FACTOR, MAP_HEIGHT * SCALE_FACTOR)), win_pos)
        pygame.display.update()

    def newFunction(self):
        print('This is a function added through GitHub')

    
