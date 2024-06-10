import pygame
import tkinter.messagebox as tks
# 下面2个值设置窗口大小
window_x = 1200
window_y = 700
# 编图片序号用
num = []
for i in range(1, 13):
    num.append(i)
num.sort(reverse = True)
things = []  # 存储图片对象


class Thing:  # 定义‘物品’
    def __init__(self, x, my, png):  
        self.x = x  # x位置
        self.my = my  # y位置
        self.png = pygame.image.load(png).convert()  # 图片

    def move(self, xp, yp):  # 移动
        self.x += xp
        self.my += yp


def q():  # 退出程序
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tks.showerror('stop', 'USER STOP THE STARTER RUNNING.')  # 警告框
            exit()


if __name__ == '__main__':
    y = -400  # 可以改变字幕的生成位置
    pygame.init()  # 初始化
    screen = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption('550W starter.exe.py')
    background = pygame.image.load(r'things/background.png').convert()
    screen.blit(background, (50, 50))  # 加载背景
    for j in num:  # 将thing实例化为字幕存储在things中
        things.append(Thing(0, y, 'things\\' + str(j) + '.png'))
        y += 30  # 改变字幕间距
    while True:
        pygame.display.update()  # 画面更新
        for i in things:
            screen.blit(i.png, (i.x, i.my))  # 重新加载things里的字幕
            i.move(0, 0.3)  # 字幕移动，第二个属性可以更改速度

        if things[0].my > 700:  # 弹出警告框，强制退出。因为我其实根本没有做界面。把48~50注释掉就只能手动退出
            tks.showerror('errow', '你的电脑性能太低无法带动550W')
            exit()
        q()
