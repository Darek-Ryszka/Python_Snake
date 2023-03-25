import random
import pygame


class Food:
    def __init__(self):
        self.x = random.randrange(0, 590, 10)
        self.y = random.randrange(0, 590, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))
