# -*- coding: utf-8 -*-

'''
@File    : game.py
@Time    : 2021/4/21 0:28
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
'''
import sys

from config import *
from background import RollBackground
from dinosaur import Dinosaur
from obstacle import ObstacleGroup


class Game:

    def __init__(self):
        self.bump_audio = BUMP_AUDIO
        self.over_img = OVER_IMG
        self.init_game()

    def init_game(self):
        # 游戏结束
        self.over = False
        # 创建滚动地图对象
        self.bg = RollBackground()
        # 创建恐龙对象
        self.dinosaur = Dinosaur()
        # 创建障碍物组合
        self.obstacles = ObstacleGroup()

    def process_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if self.over:
                    self.init_game()
                else:
                    self.dinosaur.jump()

    def start(self):
        while True:
            self.process_event()

            if not self.over:
                self.update_window()
                if self.dinosaur.collide(self.obstacles):
                    self.over = True
                    self.game_over()
            self.dinosaur.show_score()

            pygame.display.update()
            set_fps(30)

    def update_window(self):
        self.bg.update()
        self.dinosaur.update()
        self.obstacles.update()

    def game_over(self):
        self.bump_audio.play()
        x = (SCREEN_WIDTH - self.over_img.get_width()) // 2
        y = (SCREEN_HEIGHT - self.over_img.get_height()) // 2
        SCREEN.blit(self.over_img, (x, y))


if __name__ == '__main__':
    try:
        Game().start()
    finally:
        pygame.quit()
