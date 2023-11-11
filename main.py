# This is the main file
import pygame.mixer

import classes.upgrades as up
import classes.enemy as en
import classes.player as pl
from Beerventure.settings import *
import random

def drawWindow(window, screen, enemy, player):
    screen.blit(BG_IMG, (0, 0))
    for enemy in enemies:
        enemy.render()
    for upgrade in upgrades:
        upgrade.render()
    player.render()
    window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
    pygame.display.update()

pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 40)
window = pygame.display.set_mode((WIN_WIDTH * SCALE_FACTOR, WIN_HEIGHT * SCALE_FACTOR))
screen = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
player = pl.Player(screen, 50, 10)
enemies = []
upgrades = []
for i in range(5):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    enemies.append(en.Enemy(player, x, y))
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
                pygame.mixer.Sound.play(PLAYER_HURT)
                player.hp -= 10
                player.dmg_counter = 5
            if enemy.showDie():
                enemies.remove(enemy)
                drop = random.randint(0,100)
                if drop <= DROP_CHANCE:
                    upgrades.append(up.Upgrade(enemy, player))
        for upgrade in upgrades:
            if upgrade.pick_up():
                upgrades.remove(upgrade)
                pygame.mixer.Sound.play(GET_UPGRADE[random.randint(0,1)])

        drawWindow(window, screen, enemy, player)

main()