import pygame
from scripts.entity.manager import entity_manager

class player(entity_manager):
    def __init__(self,player_rect,player_offset):
        super().__init__(player_rect,player_offset)
        self.animation_init.frames_init('player')

    def render(self,surface,delta_time):
        self.entity_state()

        sprite_image = self.animation_init.animate(self.init_state,delta_time)
        render_image = pygame.transform.flip(sprite_image, self.facing, False)
        image_rect = render_image.get_rect(center=(self.rect.x,self.rect.y))
        
        surface.blit(pygame.transform.scale(render_image,(45,50)), (image_rect.x - self.offset[0],image_rect.y - self.offset[1]))