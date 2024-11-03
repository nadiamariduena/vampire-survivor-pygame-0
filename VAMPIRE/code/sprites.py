from settings import *


# no collidible

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)




# Collidable Trees
class CollisionsSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        # --- it used to be the blue rectangles, now are the trees
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)