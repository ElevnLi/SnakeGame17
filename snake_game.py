import os
import sys
from random import randint

import pygame
from pygame.math import Vector2

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
    os.path.join("./", "Assets", "Graphics", "apple.png")
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

while True:
    # 输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 渲染
    canva.fill(COLOUR_BG)
    pygame.display.update()
    clock.tick(MAX_FPS)
