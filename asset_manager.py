import pygame, os.path

class AssetManager:
    assets_base_dir = "assets"
    _images = {}

    _images["cat-0"] = pygame.image.load(os.path.join(assets_base_dir, "cat\cat-0.png"))
    _images["cat-1"] = pygame.image.load(os.path.join(assets_base_dir, "cat\cat-1.png"))
    _images["cat-2"] = pygame.image.load(os.path.join(assets_base_dir, "cat\cat-2.png"))

    _images["level-0"] = pygame.image.load(os.path.join(assets_base_dir, "level\level-0.png"))
    _images["level-1"] = pygame.image.load(os.path.join(assets_base_dir, "level\level-1.png"))
    _images["level-2"] = pygame.image.load(os.path.join(assets_base_dir, "level\level-2.png"))
    _images["level-3"] = pygame.image.load(os.path.join(assets_base_dir, "level\level-3.png"))
    _images["level-4"] = pygame.image.load(os.path.join(assets_base_dir, "level\level-4.png"))

    @staticmethod
    def getCat(seq):
        return AssetManager._images["cat-" + str(seq)]

    @staticmethod
    def getLevel(seq):
        return AssetManager._images["level-" + str(seq)]