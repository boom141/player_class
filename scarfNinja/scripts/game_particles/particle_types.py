import pygame
from scripts.game_particles.particles import particles_manager

class dust:
    def __init__(self,positions,directions,radius):
        self.particles = []
        for i in range(100):
            self.particles.append(particles_manager(positions,directions,radius))
    
    def update(self):
        for i in self.particles:
            i.update()
            self.particles = [particle for particle in self.particles if particle.rad > 0]

    def draw(self, surface):
        for i in self.particles:
            i.draw(surface)
