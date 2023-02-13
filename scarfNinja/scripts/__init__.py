import pygame, sys, os, json, time
from pygame.locals import*
pygame.init()


SCREEN_DIMENSION = (500,500)
SCALED_DIMENSION = (250,250)
CLOCK = pygame.time.Clock()
FPS = 60

SCREEN = pygame.display.set_mode(SCREEN_DIMENSION,0,32)
WINDOW = pygame.Surface(SCALED_DIMENSION)
pygame.display.set_caption('SCARF NINJA')

with open('scripts/json/key_bindings.json') as file:
    bindings = json.load(file)

file.close()

from scripts.misc.caching import asset_manager 

for entity in os.listdir('asset'):
    asset_manager().asset_init(entity)