import time

import pygame
from asset_manager import AssetManager
from renderer import Render
from level import Level
from cat import Cat

width = 256 * 6
height = 24 * 6

pygame.init()
pygame.display.init()
pygame.display.set_caption("pet")
pygame.display.set_icon(AssetManager.getCat(seq=0))

done = False
fps = 2
renderer = Render(width, height)

cat = Cat()
level = Level(cat)
renderer.render_level(level)
clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    renderer.render_level(level)
    cat.location += 1
    print(cat.location)

    pygame.display.flip()
    clock.tick(fps)

