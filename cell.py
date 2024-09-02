import pygame
from pygame.sprite import Sprite
class Cell(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen=game.screen
        self.screen_rect=game.screen.get_rect()
        #棋盘格图片文件
        self.image=pygame.image.load('cell.bmp')
        self.rect=self.image.get_rect()
        #第一个棋盘格位置
        self.rect.x=100
        self.rect.y=100
        self.used=False


