import pygame
import tkinter.messagebox as tks
window_x = 1200
window_y = 700
num = []
for i in range(1, 13):
    num.append(i)
num.sort(reverse = True)
things = []


class Thing:
    def __init__(self, x, my, png):
        self.x = x
        self.my = my
        self.png = pygame.image.load(png).convert()

    def move(self, xp, yp):
        self.x += xp
        self.my += yp


def q():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tks.showerror('stop', 'USER STOP THE STARTER RUNNING.')
            exit()


if __name__ == '__main__':
    y = -400
    pygame.init()
    screen = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption('550W starter.exe.py')
    background = pygame.image.load(r'things/background.png').convert()
    screen.blit(background, (50, 50))
    for j in num:
        things.append(Thing(0, y, 'things\\' + str(j) + '.png'))
        y += 30
    while True:
        pygame.display.update()
        for i in things:
            screen.blit(i.png, (i.x, i.my))
            i.move(0, 0.3)

        if things[0].my > 700:
            tks.showerror('errow', '你的电脑性能太低无法带动550W')
            exit()
        q()
