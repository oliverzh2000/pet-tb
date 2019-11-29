import pygame

width = 500
height = 64

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pet")
cat_image = pygame.image.load("assets/cat/cat-0.png")
pygame.display.set_icon(cat_image)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
