# @Author: LiuYuZhao
# @Date: 2022-01-13

import pygame
import time
import sys
from action import *
import random


def draw_window(size, block_size, block_list, treasure, env_data, loc):

    window = pygame.display.set_mode((size[1]*block_size, size[0]*block_size))
    pygame.display.set_caption("RandomRobot")

    # decide what times get treasure
    i = 1
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill((255, 255, 255))
        robot_color = (187, 255, 255)

        draw_blocks(window, block_list, block_size)
        draw_treasure(window, treasure, block_size)

        if i == 1:
            pygame.draw.rect(
                window, robot_color, (loc[1]*block_size, loc[0]*block_size, block_size-8, block_size-8), 0)

        if env_data[loc[0]][loc[1]] == 3 and game_over == False:
            print("机器人在第{}回合找到宝藏！".format(i+1))
            game_over = True

        available = valid_actions(env_data, loc)
        act = random.choice(available)
        if loc != treasure:
            loc = move_robot(env_data, loc, act)
            print(loc)
        pygame.draw.rect(
            window, robot_color, (loc[1]*block_size, loc[0]*block_size, block_size-8, block_size-8), 0)

        i += 1
        pygame.display.update()
        time.sleep(0.2)


def draw_blocks(window, block_lists, block_size):
    block_color = (255, 222, 173)
    for i in range(len(block_lists)):
        x, y = block_lists[i]
        position = (y*block_size, x*block_size, block_size-5, block_size-5)
        pygame.draw.rect(window, block_color, position, 0)


def draw_treasure(window, treasure, block_size):
    treasure_color = (255, 62, 150)
    position = (treasure[1]*block_size, treasure[0] *
                block_size, block_size-5, block_size-5)
    pygame.draw.rect(window, treasure_color, position, 0)
