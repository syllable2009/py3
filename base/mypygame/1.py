# !/usr/bin/env python

# 导入pygame库
import pygame
# 导入一些常用的函数和常量,例如set_mode里面窗口的标志（flags）、消息事件（event）的类型等等
from pygame.locals import *
#向sys模块借一个exit函数用来退出程序
from sys import exit

# 指定图像文件名称
background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


#初始化pygame,为使用硬件做准备
init = pygame.init()
print(init)
#创建了一个窗口
screen = pygame.display.set_mode([SCREEN_HEIGHT,SCREEN_WIDTH], 0, 32)
#设置窗口标题
pygame.display.set_caption("Hello, 该吃饭了!")

#加载并转换图像
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

offset = {pygame.K_LEFT:0, pygame.K_RIGHT:0, pygame.K_UP:0, pygame.K_DOWN:0}

while True:
    # 游戏主循环

    # 获得鼠标位置
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出事件后退出程序
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in offset:
                offset[event.key] = 3
                y = 1
            elif event.type == pygame.KEYUP:
                if event.key in offset:
                    offset[event.key] = 0
                    x = 1
    # 将背景图画上去
    screen.blit(background, (0, 0))



    # x -= mouse_cursor.get_width() / 2
    # y -= mouse_cursor.get_height() / 2
    # 计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    # 把光标画上去

    # 更新屏幕,刷新一下画面
    pygame.display.update()




