# This is the main file
import classes.enemy as en
import classes.player as pl
import numpy as np
from settings import *
import random

def initializeWave(size):
    enemies = []
    for i in range(size):
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        type = random.randint(0, 2)
        dx = player.x - x
        dy = player.y - y

        while dx**2 + dy**2 < INNER_SPAWN_RADIUS**2:
            if x < player.x:
                x -= 1
            else:
                x += 1
            if y < player.y:
                y -= 1
            else:
                y += 1

            dx = player.x - x
            dy = player.y - y

        while dx**2 + dy**2 > OUTER_SPAWN_RADIUS**2:
            if x < player.x:
                x += 1
            else:
                x -= 1
            if y < player.y:
                y += 1
            else:
                y -= 1
                
            dx = player.x - x
            dy = player.y - y

        enemies.append(en.Enemy(player, x, y, type))
    return enemies

def drawWindow(window, screen, enemy, player):
    screen.blit(BG_IMG, (0, 0))
    for enemy in enemies:
        enemy.render()
    player.render()
    window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
    pygame.display.update()

pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 40)
window = pygame.display.set_mode((WIN_WIDTH * SCALE_FACTOR, WIN_HEIGHT * SCALE_FACTOR))
screen = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
player = pl.Player(screen, 100 - ENEMY_IMGS[0][0].get_width() / 2, 100 - ENEMY_IMGS[0][0].get_height() / 2)
enemies = initializeWave(10)
clock = pygame.time.Clock()

def main():
    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()

        player.move(pygame.key.get_pressed())
        for enemy in enemies:
            if enemy.move():
                player.hp -= 10
                player.dmg_counter = PLAYER_DMG_ANIM
        drawWindow(window, screen, enemy, player)

main()