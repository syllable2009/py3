# 导入pygame库
import pygame,os,sys

# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
bg_location = 'bg.jpg'

white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)
red = (255,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,255)




#初始化pygame,为使用硬件做准备
init = pygame.init()
# print(init)
# 设置窗口出现的位置
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200,100)



class Button(object):
	def __init__(self, text, color, x=None, y=None, **kwargs):
		self.surface = myfont.render(text, True, color)

		self.WIDTH = self.surface.get_width()
		self.HEIGHT = self.surface.get_height()

		if 'centered_x' in kwargs and kwargs['centered_x']:
			self.x = SCREEN_WIDTH // 2 - self.WIDTH // 2
		else:
			self.x = x

		if 'centered_y' in kwargs and kwargs['cenntered_y']:
			self.y = SCREEN_HEIGHT // 2 - self.HEIGHT // 2
		else:
			self.y = y

	def display(self):
		screen.blit(self.surface, (self.x, self.y))

	def check_click(self, position):
		x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
		y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT
		print("{},{}",format(x_match,y_match))


#创建了一个窗口
screen = pygame.display.set_mode([SCREEN_HEIGHT,SCREEN_WIDTH], pygame.RESIZABLE, 32)
myfont = pygame.font.Font(None,36) #创建字体对象
textImage = myfont.render("hello Pygame",True,red)
play_button = Button('Fresh', black, SCREEN_WIDTH // 4 , 350)
exit_button = Button('Save', black, SCREEN_WIDTH // 4 * 3, 350)

#设置窗口标题
pygame.display.set_caption("帅气的自动化!")
# 创建时钟对象 (可以控制游戏循环频率)
clock = pygame.time.Clock()

def keyboardEventHander(event):
    # 如果按下 Esc 那么主循环终止
    if event.key == pygame.K_ESCAPE:
        quit()
        sys.exit()
    elif event.key == pygame.K_F5:
        print("f5")
    else:
        print(pygame.event)

# 用于保证主循环运行的变量
while True:
# 遍历事件所有的用户输入和其他事件都会进入 PyGame 的事件队列，通过调用 pygame.event.get() 可以访问该队列
    for event in pygame.event.get():
        # 检测 KEYDOWN 事件: KEYDOWN 是 pygame.locals 中定义的常量，pygame.locals文件开始已经导入
        if event.type == pygame.KEYDOWN:
            keyboardEventHander(event)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("{},{}".format(mouse_x,mouse_y))
        elif event.type == pygame.QUIT:
            # 接收到退出事件后退出程序,界面的叉号
            quit()
            sys.exit()
    screen.fill(white)
    #字体显示
    screen.blit(textImage,(100,100))
    screen.blit(textImage,(100,120))
    screen.blit(textImage,(100,140))
    #按钮
    play_button.display()
    exit_button.display()
    pygame.display.update() # pygame.display.flip()

    clock.tick(60) #fps=15






