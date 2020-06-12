# 导入pygame库
import pygame,os

# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,255)

#初始化pygame,为使用硬件做准备
init = pygame.init()
# print(init)
# 设置窗口出现的位置
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200,100)
#创建了一个窗口
screen = pygame.display.set_mode([SCREEN_HEIGHT,SCREEN_WIDTH], pygame.RESIZABLE, 32)
#设置窗口标题
pygame.display.set_caption("帅气的自动化!")
# 创建时钟对象 (可以控制游戏循环频率)
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button (msg, x, y, w, h, ic, ac):
    mouse =pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)



while True:
# pygame.display.update()
# 遍历事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出事件后退出程序
            pygame.quit()
            quit()
    screen.fill(white)

    button("GO", 150, 450, 100, 50, green, bright_green)
    button("Quit",550, 450, 100, 50, red, bright_red)
    pygame.display.update()
    clock.tick(15) #fps=15