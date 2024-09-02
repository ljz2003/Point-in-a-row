import pygame.font
class Button:
    def __init__(self,ai_game,msg,color=(0,255,0)):
        #设置按钮属性
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.width,self.height=200,50
        self.button_color=color
        #设置字体
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=400,50
        self.prep_msg(msg)
    #渲染成图片
    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=400,50
    #展示
    def draw(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)