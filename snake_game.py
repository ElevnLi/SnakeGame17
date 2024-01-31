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

LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)
UP = Vector2(0, -1)
DOWN = Vector2(0, 1)

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
        self.random_place()

    def random_place(self):
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
        self.direction: Vector2 = RIGHT
        self.add_body = False
        self.head_graphic = head_right_graphic
        self.tail_graphic = tail_left_graphic

    def draw(self):
        self.update_head_graphic()
        self.update_tail_graphic()
        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(
                block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            if index == len(self.body) - 1:
                canva.blit(self.head_graphic, block_rect)
            elif index == 0:
                canva.blit(self.tail_graphic, block_rect)
            else:
                prev_block = self.body[index - 1] - block
                next_block = self.body[index + 1] - block
                if prev_block.x == next_block.x:
                    canva.blit(body_vertical_graphic, block_rect)
                elif prev_block.y == next_block.y:
                    canva.blit(body_horizontal_graphic, block_rect)
                else:
                    # bl
                    if (
                        prev_block.x == -1
                        and next_block.y == 1
                        or next_block.x == -1
                        and prev_block.y == 1
                    ):
                        canva.blit(body_bl_graphic, block_rect)
                    # br
                    elif (
                        prev_block.x == 1
                        and next_block.y == 1
                        or next_block.x == 1
                        and prev_block.y == 1
                    ):
                        canva.blit(body_br_graphic, block_rect)
                    # tl
                    elif (
                        prev_block.x == -1
                        and next_block.y == -1
                        or next_block.x == -1
                        and prev_block.y == -1
                    ):
                        canva.blit(body_tl_graphic, block_rect)
                    # tr
                    elif (
                        prev_block.x == 1
                        and next_block.y == -1
                        or next_block.x == 1
                        and prev_block.y == -1
                    ):
                        canva.blit(body_tr_graphic, block_rect)
                    else:
                        pygame.draw.rect(canva, COLOUR_SNAKE, block_rect)

    @property
    def head(self):
        return self.body[-1]

    @property
    def tail(self):
        return self.body[0]

    def move(self):
        current_head = self.head
        new_head = current_head + self.direction
        if not self.add_body:
            new_body = self.body[1:]
            new_body.append(new_head)
            self.body = new_body[:]
        else:
            self.body.append(new_head)
            self.add_body = False

    def grow(self):
        self.add_body = True

    def update_head_graphic(self):
        head_direction = self.head - self.body[-2]
        if head_direction == RIGHT:
            self.head_graphic = head_right_graphic
        elif head_direction == LEFT:
            self.head_graphic = head_left_graphic
        elif head_direction == UP:
            self.head_graphic = head_up_graphic
        elif head_direction == DOWN:
            self.head_graphic = head_down_graphic

    def update_tail_graphic(self):
        tail_direction = self.tail - self.body[1]
        if tail_direction == RIGHT:
            self.tail_graphic = tail_right_graphic
        elif tail_direction == LEFT:
            self.tail_graphic = tail_left_graphic
        elif tail_direction == UP:
            self.tail_graphic = tail_up_graphic
        elif tail_direction == DOWN:
            self.tail_graphic = tail_down_graphic


class SnakeGame:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()

    def draw(self):
        self.fruit.draw()
        self.snake.draw()

    def update(self):
        self.snake.move()
        # 检测吃没吃到
        self.check_eat()
        # 检测撞没撞死
        self.check_fail()

    def check_eat(self):
        if self.fruit.pos == self.snake.head:
            # 长长一节
            self.snake.grow()
            # 重新摆放水果
            self.fruit.random_place()

    def check_fail(self):
        # 蛇头撞墙
        if (
            not 0 <= self.snake.head.x < CELL_NUMBER
            or not 0 <= self.snake.head.y < CELL_NUMBER
        ):
            self.game_over()
        # 蛇头撞自己
        for block in self.snake.body[:-1]:
            if block == self.snake.head:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


snake_game = SnakeGame()

while True:
    # 输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake_game.game_over()
        if event.type == SNAKE_UPDATE:
            snake_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake_game.snake.direction != RIGHT:
                    snake_game.snake.direction = LEFT
            elif event.key == pygame.K_RIGHT:
                if snake_game.snake.direction != LEFT:
                    snake_game.snake.direction = RIGHT
            elif event.key == pygame.K_UP:
                if snake_game.snake.direction != DOWN:
                    snake_game.snake.direction = UP
            elif event.key == pygame.K_DOWN:
                if snake_game.snake.direction != UP:
                    snake_game.snake.direction = DOWN

    # 渲染
    canva.fill(COLOUR_BG)
    snake_game.draw()
    pygame.display.update()
    clock.tick(MAX_FPS)
