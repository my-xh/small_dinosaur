# -*- coding: utf-8 -*-

'''
@File    : obstacle.py
@Time    : 2021/4/21 0:42
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
'''
import random

from config import *
from abc import ABCMeta


class Obstacle(metaclass=ABCMeta):
    """障碍物类"""
    score_audio = SCORE_AUDIO

    def __init__(self, img):
        super().__init__()
        self.x = 800
        self.y = 200
        self.image = img

        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.x, self.y

    def is_out(self):
        """判断障碍物是否移出窗口"""
        return True if self.rect.x < -self.rect.width else False

    def move(self):
        self.rect.x -= 5

    def update(self):
        SCREEN.blit(self.image, self.rect)
        self.move()

    def collide(self, obj):
        """判断障碍物与角色是否发生碰撞"""
        return pygame.sprite.collide_mask(self, obj)

    def left_of(self, obj):
        """判断障碍物是否移动到了角色左侧"""
        return True if self.rect.x + self.rect.width < obj.x else False

    @property
    def score(self):
        score = self._score
        if score != 0:
            self.score_audio.play()
            self._score = 0
        return score


class Stone(Obstacle):
    """石头障碍物"""
    _score = 1

    def __init__(self):
        super().__init__(STONE_IMG)


class Cacti(Obstacle):
    """仙人掌障碍物"""
    _score = 2

    def __init__(self):
        super().__init__(CACTI_IMG)


class ObstacleGroup():
    """障碍物组"""
    group = [Stone, Cacti]

    def __init__(self):
        self.obstacles = []
        self.add_timer = 0

    def __getitem__(self, item):
        return self.obstacles.__getitem__(item)

    def generate(self):
        # 按照一定时间间隔和概率生成障碍物
        if self.add_timer >= 1300:
            r = random.randint(1, 100)
            if r > 40:
                obstacle = random.choice(self.group)()
                self.obstacles.append(obstacle)
            self.add_timer = 0
        self.add_timer += 20

    def update(self):
        for each in self.obstacles:
            each.update()
            if each.is_out():
                self.obstacles.remove(each)
        self.generate()
