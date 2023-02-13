import pygame
from scripts import SCREEN_DIMENSION

class map_manager:
    
    collectibles = {}
    enitities = {}
    hash_map = {}
    tile_rects = []

    def load_map_file(self,map_file):
        pass 

    def render_tiles(self,surface):
        self.tile_rects = []
        rect2 = pygame.draw.rect(surface, (60,60,60), (0, 400, 50,50))
        self.tile_rects.append(rect2)
        rect3 = pygame.draw.rect(surface, (60,60,60), (150, 350, 50,50))
        self.tile_rects.append(rect3)
        rect4 = pygame.draw.rect(surface, (60,60,60), (250, 300, 50,50))
        self.tile_rects.append(rect4)
        for i in range(SCREEN_DIMENSION[0]//50):
            rect1 = pygame.draw.rect(surface, (60,60,60), (i * 50,450,50,50))
            self.tile_rects.append(rect1)
           