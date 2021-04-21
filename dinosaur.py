# -*- coding: utf-8 -*-

'''
@File    : dinosaur.py
@Time    : 2021/4/20 22:32
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
'''

from config import *
from itertools import cycle


class Score:

    def __init__(self, val=0):
        self.val = val

    def add_val(self, val):
        self.val += val

    def show(self):
        total_width = 0
        digit_score = [int(i) for i in str(self.val)]
        for digit in digit_score:
            total_width += NUMS[digit].get_width()  # 计算分数图片的整体宽度

        x = (SCREEN_WIDTH - total_width) // 2
        y = SCREEN_HEIGHT // 10
        for digit in digit_score:
            image = NUMS[digit]
            SCREEN.blit(image, (x, y))
            x += image.get_width()


class Dinosaur():
    """恐龙类"""

    def __init__(self):
        self.x = 50
        self.y = self.lowest_y = 140
        self.images = [DINOSAUR_1, DINOSAUR_2, DINOSAUR_3]
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.jump_state = False  # 跳跃状态
        self.jump_value = 0  # 跳跃增量
        self.jump_height = 130  # 跳跃高度

        self.images = cycle(self.images)

        self.jump_audio = JUMP_AUDIO  # 加载跳跃音效

        self.score = Score()  # 得分

    def jump(self):
        if not self.jump_state:
            self.jump_state = True  # 开启跳跃状态
            self.jump_audio.play()

    def move(self):
        if self.jump_state:
            if self.y >= self.lowest_y:  # 在地面时，往上跳
                self.jump_value = -5
            elif self.y <= self.lowest_y - self.jump_height:  # 跳到最大高度，往下落
                self.jump_value = 5
            self.y += self.jump_value
            if self.y >= self.lowest_y:  # 落回地面时，关闭跳跃状态
                self.y = self.lowest_y
                self.jump_state = False
        self.rect.topleft = self.x, self.y

    def update(self):
        SCREEN.blit(next(self.images), self.rect)
        self.move()

    def show_score(self):
        self.score.show()

    def collide(self, obstacles):
        for each in obstacles:
            if each.collide(self):
                return True
            elif each.left_of(self):
                self.score.add_val(each.score)
        return False
