import pygame, random

class particles_manager:
    def __init__(self,positions,directions,radius):
        self.posX, self.posY = positions[0], positions[1]
        self.velX, self.velY = directions[0], directions[1]
        self.rad = radius

    def draw(self,surface):
        pygame.draw.circle(surface, (255,255,255), (self.posX, self.posY), self.rad)

    def update(self):
        self.posX += self.velX
        self.posY += self.velY
        if random.randint(0, 100) < 40:
            self.rad -= 1

