import pygame
from scripts import asset_manager

class animation_manager:

    def __init__(self):
        self.entity = None
        self.frame_list = None
        self.animation_frame = 0

    def frames_init(self,entity):
        self.entity = asset_manager.IMAGE_DATABASE[entity]

    def animate(self,state,delta_time):
        self.animation_frame += 0.1 * delta_time
        if self.animation_frame >= len(self.entity[state]):
            self.animation_frame = 0
        
        return self.entity[state][int(self.animation_frame)]
    