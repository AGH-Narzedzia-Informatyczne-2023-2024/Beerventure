# This is the main file
import pygame.mixer

from classes.game import Game
import classes.upgrades as up
import classes.enemy as en
import classes.player as pl
from settings import *
import random

pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 40)
game = Game()
clock = pygame.time.Clock()

def main():
    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()

        rand = random.uniform(0, 1)
        if rand < ENEMY_STATS['THROW_PROB'][0]:
            game.spawnEnemy()

        game.player.move(pygame.key.get_pressed())
        for idx, enemy in enumerate(game.enemies):
            if enemy.active:
                enemy.move()
                
                if enemy.checkRange() == 1:
                    enemy.attack()

                elif enemy.checkRange() == 2:
                    rand = random.uniform(0, 1)
                    if rand < enemy.throw_prob:
                        enemy.throw()

                if enemy.atk and enemy.img_counter == ENEMY_ANIM_TIME * 3 and enemy.checkRange() == 1:
                    game.player.hp -= 10
                    game.player.dmg_counter = PLAYER_DMG_ANIM

            if enemy.destroy:
                drop = random.randint(0, 100)
                if drop <= DROP_CHANCE:
                    game.upgrades.append(up.Upgrade(enemy, game.player))
                del game.enemies[idx]

        for upgrade in game.upgrades:
            if upgrade.pick_up():
                game.upgrades.remove(upgrade)
                pygame.mixer.Sound.play(GET_UPGRADE[random.randint(0,1)])

        game.renderWindow()

main()
