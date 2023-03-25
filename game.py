# $$$$$$$$$$$$$$$$$$$$$$
# Snake game in Python
# $$$$$$$$$$$$$$$$$$$$$$

import pygame
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.fps = 10
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.snake.direction != 'right':
                    self.snake.direction = 'left'
                elif event.key == pygame.K_RIGHT and self.snake.direction != 'left':
                    self.snake.direction = 'right'
                elif event.key == pygame.K_UP and self.snake.direction != 'down':
                    self.snake.direction = 'up'
                elif event.key == pygame.K_DOWN and self.snake.direction != 'up':
                    self.snake.direction = 'down'
        return True

    def update(self):
        self.snake.move()
        if self.snake.segments[0][0] < 0 or self.snake.segments[0][0] >= self.width or \
                self.snake.segments[0][1] < 0 or self.snake.segments[0][1] >= self.height:
            self.snake.reset()

        for segment in self.snake.segments[1:]:
            if self.snake.segments[0] == segment:
                self.snake.reset()

        if self.snake.segments[0] == [self.food.x, self.food.y]:
            self.snake.add_segment()
            self.food = Food()
            self.score += 1

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        font = pygame.font.SysFont('Arial', 20)  # ustawienie czcionki i rozmiaru tekstu
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))  # tworzenie tekstu z licznikiem
        self.screen.blit(text, (10, 10))  # wyświetlenie tekstu na ekranie
        pygame.display.update()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
