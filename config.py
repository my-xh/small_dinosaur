# -*- coding: utf-8 -*-

'''
@File    : config.py
@Time    : 2021/4/21 0:27
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
'''

import pygame
from pygame.locals import *

SCREEN_WIDTH = 822
SCREEN_HEIGHT = 260
FPS = 30
FPSCLOCK = pygame.time.Clock()


def set_window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
    global SCREEN_WIDTH, SCREEN_HEIGHT
    SCREEN_WIDTH, SCREEN_HEIGHT = width, height
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def set_fps(fps=FPS):
    global FPS
    FPS = fps
    FPSCLOCK.tick(FPS)


pygame.init()

SCREEN = set_window()

# 数字图片
NUM_0 = pygame.image.load('image/0.png').convert_alpha()
NUM_1 = pygame.image.load('image/1.png').convert_alpha()
NUM_2 = pygame.image.load('image/2.png').convert_alpha()
NUM_3 = pygame.image.load('image/3.png').convert_alpha()
NUM_4 = pygame.image.load('image/4.png').convert_alpha()
NUM_5 = pygame.image.load('image/5.png').convert_alpha()
NUM_6 = pygame.image.load('image/6.png').convert_alpha()
NUM_7 = pygame.image.load('image/7.png').convert_alpha()
NUM_8 = pygame.image.load('image/8.png').convert_alpha()
NUM_9 = pygame.image.load('image/9.png').convert_alpha()
NUMS = [NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9]

# 背景图片
BACKGROUND = pygame.image.load('image/bg.png').convert_alpha()

# 恐龙图片
DINOSAUR_1 = pygame.image.load('image/dinosaur1.png').convert_alpha()
DINOSAUR_2 = pygame.image.load('image/dinosaur2.png').convert_alpha()
DINOSAUR_3 = pygame.image.load('image/dinosaur3.png').convert_alpha()

# 障碍物图片
STONE_IMG = pygame.image.load('image/stone.png').convert_alpha()
CACTI_IMG = pygame.image.load('image/cacti.png').convert_alpha()

# GAMEOVER图片
OVER_IMG = pygame.image.load('image/gameover.png').convert_alpha()

JUMP_AUDIO = pygame.mixer.Sound('audio/jump.wav')  # 跳跃音效
SCORE_AUDIO = pygame.mixer.Sound('audio/score.wav')  # 得分音效
BUMP_AUDIO = pygame.mixer.Sound('audio/bump.wav')  # 碰撞音效
