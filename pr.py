import sys
import pygame
import random
import numpy as np
from cell import Cell
from num import Num
from button import Button
class pr:
    def __init__(self):
        pygame.init()
        #屏幕设置
        self.screen=pygame.display.set_mode((800,800))
        pygame.display.set_caption("Point in a row")
        self.bg_color = (230, 230, 230)
        self.button = Button(self, 'Start')
        self.button.rect.center=400,400
        self.button.msg_image_rect.center=400,400
        # 创建棋盘
        self.cells = pygame.sprite.Group()
        for row in range(15):
            for number in range(15):
                cell = Cell(self)
                cell.rect.x = 100 + 40 * number
                cell.rect.y = 100 + 40 * row
                cell.x_y = (number, row)
                self.cells.add(cell)
        # 填充数字
        self.nums = pygame.sprite.Group()
        self.restart()
    def restart(self):
        self.board_matrix = np.zeros((15, 15), dtype=int)
        self.nums.empty()
        for cell in self.cells:
            cell.used = False
        # 创建初始化按钮
        self.button = Button(self, 'Restart')
        # 取初始数
        self.red = random.randint(1, 8)
        self.blue = random.randint(self.red + 1, 9)
        # 设置奇偶次红蓝
        self.a=0
    def check_winner(self,is_red,):
        if heng(self) or shu(self) or pie(self) or na(self):
            return 1 if is_red else -1
    def red_win(self):
        self.board_matrix = np.zeros((15, 15), dtype=int)
        self.button = Button(self, 'Red win!',(255,0,0))
    def blue_win(self):
        self.board_matrix = np.zeros((15, 15), dtype=int)
        self.button = Button(self, 'Blue win!',(0,0,255))
    def run(self):
        while True:
            #红方显示初始值
            num_red=Num(self)
            num_red.num_image = num_red.font.render(str(self.red), True,(255, 0, 0), (255, 255, 255))
            num_red.num_rect.x, num_red.num_rect.y = 50, 400
            self.nums.add(num_red)
            # 蓝方显示初始值
            num_blue = Num(self)
            num_blue.num_image = num_blue.font.render(str(self.blue), True,(0, 0, 255), (255, 255, 255))
            num_blue.num_rect.x, num_blue.num_rect.y = 750, 400
            self.nums.add(num_blue)
            #键鼠互动
            for event in pygame.event.get():
                #退出
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        sys.exit()
                elif event.type==pygame.QUIT:
                    sys.exit()


                #鼠标点击方格
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    for cell in self.cells:
                        if cell.rect.collidepoint(pos) and not cell.used and self.button.button_color==(0,255,0):
                            cell.used = True
                            #奇数次红方
                            if self.a % 2 == 0:
                                self.a += 1
                                #本次数字显示
                                num = Num(self)
                                num.num_rect.center = cell.rect.center
                                self.nums.add(num)
                                num.num_image = num.font.render(str(self.red), True,
                                                                (255, 0, 0), (255, 255, 255))
                                self.board_matrix[cell.x_y[1]][cell.x_y[0]]=self.red
                                self.red=random.randint(1, 9)

                                #下次数字显示
                                num_ = Num(self)
                                num_.num_image = num.font.render(str(self.red), True,
                                                                (255, 0, 0), (255, 255, 255))
                                num_.num_rect.x,num_.num_rect.y=50,400
                                self.nums.add(num_)
                            #偶数次蓝方
                            else:
                                self.a += 1
                                #本次数字显示
                                num = Num(self)
                                num.num_rect.center = cell.rect.center
                                num.num_image = num.font.render(str(self.blue), True,
                                                                (0, 0, 255), (255, 255, 255))
                                self.board_matrix[cell.x_y[1]][cell.x_y[0]] -=self.blue
                                self.blue = random.randint(1, 9)

                                self.nums.add(num)
                                #下次数字显示
                                num_ = Num(self)
                                num_.num_image = num.font.render(str(self.blue), True,
                                                                 (0, 0, 255), (255, 255, 255))
                                num_.num_rect.x, num_.num_rect.y = 750, 400
                                self.nums.add(num_)
                    #按钮重置游戏
                    if self.button.rect.collidepoint(pos):
                        self.restart()

            #显示背景色、棋盘、数字、初始化按钮
            self.screen.fill(self.bg_color)
            self.cells.draw(self.screen)
            for num in self.nums:
                num.show()
            self.button.draw()

            for i in range(15):
                row=self.board_matrix[i]
                for j in range(15):
                    for k in range(j, 15):
                        if min(row[j:k+1]) > 0 and sum(row[j:k+1]) > 24:
                            self.red_win()
                        if max(row[j:k + 1]) < 0 and sum(row[j:k + 1]) <-24:
                            self.blue_win()
            for i in range(15):
                row=self.board_matrix[:,i]
                for j in range(15):
                    for k in range(j, 15):
                        if min(row[j:k+1]) > 0 and sum(row[j:k+1]) > 24:
                            self.red_win()
                        if max(row[j:k + 1]) < 0 and sum(row[j:k + 1]) <-24:
                            self.blue_win()
            for i in range(-12,13):
                row=np.diagonal(self.board_matrix,offset=i)
                for j in range(15-abs(i)):
                    for k in range(j,15-abs(i)):
                        if min(row[j:k+1]) > 0 and sum(row[j:k+1]) > 24:
                            self.red_win()
                        if max(row[j:k + 1]) < 0 and sum(row[j:k + 1]) <-24:
                            self.blue_win()
            for i in range(-12,13):
                row=np.diagonal(np.fliplr(self.board_matrix),offset=i)
                for j in range(15-abs(i)):
                    for k in range(j,15-abs(i)):
                        if min(row[j:k+1]) > 0 and sum(row[j:k+1]) > 24:
                            self.red_win()
                        if max(row[j:k + 1]) < 0 and sum(row[j:k + 1]) <-24:
                            self.blue_win()
            #屏幕绘制
            pygame.display.flip()
#游戏实例运行
if __name__=='__main__':
    pr1=pr()
    pr1.run()