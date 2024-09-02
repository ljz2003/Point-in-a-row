import pygame.font
from pygame.sprite import Sprite
class Num(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        #字体字号
        self.font=pygame.font.SysFont(None,48)
        self.prep()
    #渲染成图片
    def prep(self):
        self.num_image=self.font.render("0",True,(0,0,0),(0,0,0))
        self.num_rect=self.num_image.get_rect()
    #显示
    def show(self):
        self.screen.blit(self.num_image,self.num_rect)