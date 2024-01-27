import pygame
import sys
from pygame.math import Vector2


pygame.init()

COLOUR_BG = (175, 215, 70)
COLOUR_FRUIT = (183, 111, 122)

canvas = pygame.display.set_mode(size=(800, 800))


class Fruit:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.direction = Vector2(0, 0)

    def draw(self):
        fruit_rect = pygame.Rect(self.position.x, self.position.y, 50, 50)
        pygame.draw.rect(canvas, COLOUR_FRUIT, fruit_rect)

    def move(self):
        self.position += self.direction * 5


fruit = Fruit()
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fruit.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                fruit.direction = Vector2(1, 0)
            elif event.key == pygame.K_UP:
                fruit.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                fruit.direction = Vector2(0, 1)
    canvas.fill(COLOUR_BG)
    fruit.draw()
    fruit.move()
    pygame.display.update()
    clock.tick(60)
