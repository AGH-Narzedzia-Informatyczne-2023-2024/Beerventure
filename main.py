# This is the main file
import classes.enemy as en
import classes.player as pl
from settings import *
import random

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
player = pl.Player(screen, 50, 10)
enemies = []
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
                player.hp -= 10
                player.dmg_counter = 5
        drawWindow(window, screen, enemy, player)

main()