# This is the main file
import pygame.mixer

import classes.upgrades as up
import classes.enemy as en
import classes.player as pl
from settings import *
import random

def initializeWave(player_x, player_y, size):
    enemies = []
    for i in range(size):
        (dirx, diry) = (choice([(np.floor(player_x - OUTER_SPAWN_RADIUS), np.floor(player_x - INNER_SPAWN_RADIUS)),
                                (np.floor(player_x + INNER_SPAWN_RADIUS), np.floor(player_x + OUTER_SPAWN_RADIUS))]),
        choice([(np.floor(player_y - OUTER_SPAWN_RADIUS), np.floor(player_y - INNER_SPAWN_RADIUS)),
                (np.floor(player_y + INNER_SPAWN_RADIUS), np.floor(player_y + OUTER_SPAWN_RADIUS))]))
        x, y = randint(*dirx), randint(*diry)
        type = randint(0, 2)
        self.enemies.append(Enemy(self.player, x, y, type))

        enemies.append(en.Enemy(player, x, y, type))
    return enemies

def drawWindow(window, screen, enemies, player):
    screen.blit(BG_IMG, (0, 0))
    player.render()
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
player = pl.Player(screen, 100 - ENEMY_IMGS[0][0][0].get_width() / 2, 100 - ENEMY_IMGS[0][0][0].get_height() / 2)
enemies = initializeWave(player, 10)
upgrades = []
clock = pygame.time.Clock()

def main():
    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()

        player.move(pygame.key.get_pressed())
        for idx, enemy in enumerate(enemies):
            if enemy.active:
                enemy.move()
                if enemy.checkRange() == 1:
                    enemy.attack()
                elif enemy.checkRange() == 2:
                    rand = random.uniform(0, 1)
                    if rand < enemy.throw_prob:
                        enemy.throw()
                if enemy.atk and enemy.img_counter == ENEMY_ANIM_TIME * 3 and enemy.checkRange() == 1:
                    player.hp -= 10
                    player.dmg_counter = PLAYER_DMG_ANIM

            if enemy.destroy:
                drop = random.randint(0, 100)
                if drop <= DROP_CHANCE:
                    upgrades.append(up.Upgrade(enemy, player))
                del enemies[idx]
        for upgrade in upgrades:
            if upgrade.pick_up():
                upgrades.remove(upgrade)
                pygame.mixer.Sound.play(GET_UPGRADE[random.randint(0,1)])
        drawWindow(window, screen, enemies, player)

main()
