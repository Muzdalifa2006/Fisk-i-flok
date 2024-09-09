import pygame
from vector import *
from fish import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

fish_1 = Fish(Vector(400, 300), Vector(1.5, 1.5), screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 128, 255))

    fish_1.update()
    fish_1.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
