import pygame,sys
# 一些常量
from pygame.locals import *

# 初始化所有导入的 PyGame 模块
pygame.init()
size = width, height = 640, 480  # 设置窗口大小
# 创建一个屏幕
screen = pygame.display.set_mode(size)
color = (0,0,0)  # 设置黑颜色

# 设置窗口标题
pygame.display.set_caption("Hello, 该吃饭了!")

#Surface和 Rects是 PyGame 中的基本构件。可以将 Surface 看作一张白纸，你可以在上面随意绘画。我们的屏幕对象也是一个 Surface 。它们可以包含图片。Rects 是 Surface 中矩形区域的表示。
# 创建Surface 并用原则设定它的长度和宽度
# surf = pygame.Surface((50,50))
# 设定Surface的颜色，使其和屏幕分离
# surf.fill((255,255,255))
# rect = surf.get_rect()
#仅仅只是创建了 Surface 并不能在屏幕上看到它。为此我们需要将这个 Surface 绘制（Blit）到另一个 Surface 上。Blit 是一个专业术语，意思就是绘图。你仅仅只能从一个Surface Blit 到另一个Surface，我们的屏幕就是一个 Surface 对象。以下是我们如何将 surf 画到屏幕上
# screen.blit(surf,(400,300))
# pygame.display.flip()

# Pygame 提供一个叫做 Sprites 的基础类，它就是用来扩展的，可以包含想要在屏幕上呈现的对象一个或多个图形表示。我们将会扩展Sprite 类，这样可以使用它的内建方法。我们称这个新的对象为 Player 。Plyaer 将扩展 Sprite，现在只有两个属性：surf 和 rect
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

player = Player()

# print(player.rect)
ball = pygame.image.load('ball.png')
ballrect = ball.get_rect()  # 获取矩形区域

# 游戏主循环/事件循环是所有操作发生的地方。在游戏过程中，它不断的更新游戏状态，渲染游戏画面和收集输入指令。
# 用于保证主循环运行的变量
running = True
speed = [5, 5]  # 设置移动的X轴、Y轴

clock = pygame.time.Clock()  # 设置时钟

# 主循环！
while True:
    # for 循环遍历事件队列
    for event in pygame.event.get():
        clock.tick(60)  # 每秒执行60次
        # 检测 KEYDOWN 事件: KEYDOWN 是 pygame.locals 中定义的常量，pygame.locals文件开始已经导入
        if event.type == pygame.KEYDOWN:
            player.rect.move_ip(0, -5)
            # player.update(event)
        elif event.type == pygame.KEYUP:
            player.rect.move_ip(0, 5)
            player.update(event)
        # 检测 QUIT : 如果 QUIT, 终止主循环
        elif event.type == pygame.QUIT:
            running = False
            sys.exit()
    # pressed_keys = pygame.event.get_presssed()
    # player.update(pressed_keys)
    # 这一行表示：将surf画到屏幕 x：400.y:300的坐标上
    # screen.blit(player.surf, player.rect)

    # 移动小球
    ballrect = ballrect.move(speed)
    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(color)
    screen.blit(ball,ballrect)
    # 更新
    pygame.display.flip()

def update(self,event):
    if pygame.KEYDOWN:
        self.rect.move_ip(0,-5)
    if pygame.KEYUP:
        self.rect.move_ip(0,5)
    # if pressed_keys[K_LEFT]:
    #     self.rect.move_ip(-5,0)
    # if pressed_keys[K_RIGHT]:
    #     self.rect.move_ip(5,0)


