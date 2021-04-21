# -*- coding: utf-8 -*-

'''
@File    : background.py
@Time    : 2021/4/21 0:27
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
'''

from config import *


class Background:
    """背景"""

    def __init__(self, x, y):
        self.image = BACKGROUND
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.image.get_width()

    def rolling(self):
        if self.x < -790:
            self.x = 800
        else:
            self.x -= 5

    def update(self):
        SCREEN.blit(self.image, (self.x, self.y))
        self.rolling()


class RollBackground():
    """滚动背景"""

    def __init__(self, x=0, y=0):
        bg1 = Background(x, y)
        bg2 = Background(x + bg1.width, y)
        self.roll_bg = [bg1, bg2]

    def update(self):
        for bg in self.roll_bg:
            bg.update()
