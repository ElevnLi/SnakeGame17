import os
import sys
from random import randint

import pygame
from pygame.math import Vector2

from typing import List

COLOUR_BG = (175, 215, 70)
COLOUR_FRUIT = (183, 111, 122)
COLOUR_SNAKE = (126, 166, 114)

MAX_FPS = 60
CELL_SIZE, CELL_NUMBER = 40, 20


package_base_path = os.path.dirname(os.path.abspath(__file__))

pygame.init()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 150)

canva = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
clock = pygame.time.Clock()

fruit_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "apple.png")
).convert_alpha()

head_up_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "head_up.png")
).convert_alpha()
head_down_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "head_down.png")
).convert_alpha()
head_right_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "head_right.png")
).convert_alpha()
head_left_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "head_left.png")
).convert_alpha()

tail_up_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "tail_up.png")
).convert_alpha()
tail_down_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "tail_down.png")
).convert_alpha()
tail_right_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "tail_right.png")
).convert_alpha()
tail_left_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "tail_left.png")
).convert_alpha()

body_vertical_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "body_vertical.png")
).convert_alpha()
body_horizontal_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "body_horizontal.png")
).convert_alpha()

body_tr_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "body_tr.png")
).convert_alpha()
body_tl_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "body_tl.png")
).convert_alpha()
body_br_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "body_br.png")
).convert_alpha()
body_bl_graphic = pygame.image.load(
    os.path.join(package_base_path, "Assets", "Graphics", "body_bl.png")
).convert_alpha()
crunch_sound_graphic = pygame.mixer.Sound(
    os.path.join(package_base_path, "Assets", "Sound", "crunch.wav")
)


class Fruit:
    def __init__(self):
        self.x = randint(0, CELL_NUMBER - 1)
        self.y = randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        fruit_rect = pygame.Rect(
            self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        canva.blit(fruit_graphic, fruit_rect)


class Snake:
    def __init__(self):
        self.body: List[Vector2] = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction: Vector2 = Vector2(1, 0)

    def draw(self):
        for block in self.body:
            block_rect = pygame.Rect(
                block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(canva, COLOUR_SNAKE, block_rect)

    @property
    def head(self):
        return self.body[-1]

    def move(self):
        current_head = self.head
        new_head = current_head + self.direction
        new_body = self.body[1:]
        new_body.append(new_head)
        self.body = new_body[:]


fruit = Fruit()
snake = Snake()

while True:
    # 输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_UPDATE:
            snake.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake.direction != Vector2(1, 0):
                    snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                if snake.direction != Vector2(-1, 0):
                    snake.direction = Vector2(1, 0)
            elif event.key == pygame.K_UP:
                if snake.direction != Vector2(0, 1):
                    snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                if snake.direction != Vector2(0, -1):
                    snake.direction = Vector2(0, 1)

    # 渲染
    canva.fill(COLOUR_BG)
    fruit.draw()
    snake.draw()
    pygame.display.update()
    clock.tick(MAX_FPS)
