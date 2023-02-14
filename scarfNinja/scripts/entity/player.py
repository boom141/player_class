import pygame,random
from scripts.entity.manager import entity_manager
from scripts.game_particles.particle_types import dust

class player(entity_manager):
    def __init__(self,player_rect,player_offset):
        super().__init__(player_rect,player_offset)
        self.animation_init.frames_init('player')
        self.particles = []
        self.play_particle = False
        self.current_time = 0
        self.offset_time = 0

    def player_event_handler(self):
        self.current_time = pygame.time.get_ticks()
        if self.collision_types['bottom'] and self.jump_once == False:
            self.jump_once = True
            self.play_particle = True
            self.offset_time = pygame.time.get_ticks()

        if self.current_time - self.offset_time > 100:
            self.play_particle = False

        if self.play_particle:
            self.particles.append(dust(self.rect.midbottom,[random.randint(-2, 2), random.randint(-10, 0)*.1],radius=5))

    def player_particles(self,surface):
        for particle in self.particles:
            particle.update()
            particle.draw(surface)

    def render(self,surface,delta_time):
        self.entity_state()

        sprite_image = self.animation_init.animate(self.init_state,delta_time)
        render_image = pygame.transform.flip(sprite_image, self.facing, False)
        image_rect = render_image.get_rect(center=(self.rect.x,self.rect.y))
        
        surface.blit(pygame.transform.scale(render_image,(45,50)), (image_rect.x - self.offset[0],image_rect.y - self.offset[1]))