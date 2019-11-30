import pygame
from cat import Cat
from level import Level
from asset_manager import AssetManager

class Render:
    def __init__(self, width, height):

        self.width = width
        self.height = int(Level.height * (width / Level.width))
        # Then scale the prerender surface to the screen and draw.
        self.screen = pygame.display.set_mode((self.width, self.height))

    def render_level(self, level):
        # Draw to prerender surface first.
        prerender = pygame.Surface((Level.width, Level.height))
        prerender.fill((255, 255, 255))
        level_background_image = AssetManager.getLevel(4)
        prerender.blit(level_background_image, (0, 0))
        cat_image = AssetManager.getCat(2)
        prerender.blit(cat_image, (level.cat.location, Level.height - cat_image.get_rect().height))

        prerender = pygame.transform.scale(prerender, (self.width, self.height))
        self.screen.blit(prerender, (0, 0))
