import pygame


class Snake:
    def __init__(self):
        self.segments = [[100, 100], [90, 100], [80, 100]]
        self.direction = 'right'

    def move(self):
        head = self.segments[0][:]
        if self.direction == 'right':
            head[0] += 10
        elif self.direction == 'left':
            head[0] -= 10
        elif self.direction == 'up':
            head[1] -= 10
        elif self.direction == 'down':
            head[1] += 10
        self.segments.insert(0, head)
        self.segments.pop()

    def add_segment(self):
        tail = self.segments[-1][:]
        self.segments.append(tail)

    def reset(self):
        self.segments = [[100, 100], [90, 100], [80, 100]]
        self.direction = 'right'

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], 10, 10))
