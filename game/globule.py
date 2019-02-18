'''
    接小球
    游戏玩法分析
    1>这个游戏一共有5个元素构成(背景颜色、得分、生命值、小球、挡板)
    2>小球在水平方向的位置随机出现,按照一定的速度垂直下落
    3>我们有一个挡板,当挡板接到小球的时候,分数上涨,否则,生命值下降。当生命值用完的时候,游戏结束。
'''
# pygame游戏库sys用于操控 Python运行时的环境
import pygame # 安装pip install pygame
import sys
import random

from pygame.locals import *


# 1,定义一个输出字体的函数准备工作
def print_text(font, x, y, text, color = (255, 255, 255)) :
    # 绘制文本内容，text内容，True抗锯齿（提高图像质量），color文字颜色
    imgText = font.render(text, True, color) 
    #1.1bLit()函数来绘制
    screen.blit(imgText, (x, y))


#1.2初始化pygame
pygame.init()
#1.3 pygame.display.set_mode()获得显示系统的访问，创建一个窗口
screen = pygame.display.set_mode((600,500))
#1.4 创建一个标题
pygame.display.set_caption('接小球')
#1.5 pygame.font.Font()将文本输出到图像的窗口,None默认字体
font_one = pygame.font.Font(None, 24)
#1.6 隐藏或显示鼠标光标,Falses鼠标不可见，True鼠标可见
pygame.mouse.set_visible(False)
#1.7 设置元素的颜色
white = 255, 255, 255
red = 220, 50, 50
yellow = 230, 230, 50
blue = 0, 0, 100
#1.8生命值和得分
lives = 3
score = 0
#1.9游戏结束的标记，鼠标点击的位置，初始化挡板，小球的位置，速度变量
game_over = True #游戏结束标记
mouse_x = mouse_y = 0 #鼠标点击的位置
pos_x = 300
pos_y = 460 #初始化挡板
bomb_x = random.randint(0,500) 
bomb_y = -50 #小球的位置,水平方向随机，垂直方向降落
vel_y = 0.5 #速度变量

#2,循环中创建一个事件处理程序(重点)(所有的事件都要放置一个循环中实时处理)
# 鼠标运动的事件、键盘事件、分析小球的状态
while True :
    for event in pygame.event.get() :
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION: #如果事件的类型是鼠标的类型
            mouse_x,mouse_y = event.pos
        elif event.type == MOUSEBUTTONUP: #如果事件的类型是鼠标抬起的类型
            #死亡，清空得分，初始化生命
            if game_over :
                game_over = False
                lives = 3
                score = 0
    #2.1获得所有键盘按钮的状态
    keys = pygame.key.get_pressed()
    #2.2如果我们的事件是计算机的退出键,那么就退出
    if keys[K_ESCAPE] :
        sys.exit()
    # 背景改为蓝色
    screen.fill(blue)
    #判断是否结束，结束就有一个开始按钮，没有就让小球动起来
    if game_over :
        print_text(font_one, 100, 200, '<CLICK TO PLAY>')
    else :
        #通过速度变量改变垂直方向的值
        bomb_y += vel_y
        #思考，什么情况下接着了小球
        #屏幕高度500，屏幕和挡板间的距离460
        #没有接住下去，重新生成小球，生命减1，生命值为0游戏结束
        if bomb_y > 500 :
            bomb_x = random.randint(0,500)
            bomb_y = -50
            lives -= 1
            if lives == 0 :
                game_over = True
        #如果接住小球，分数++，随机生成一个小球
        elif bomb_y > pos_y :
            if bomb_x > pos_x and bomb_x < pos_x + 120 :
                score += 10
                bomb_x = random.randint(0,500)
                bomb_y = -50
        #绘制小球
        pygame.draw.circle(screen, yellow, (bomb_x, int(bomb_y)), 30, 0)
        #2.3挡板位置的判断
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500 :
            pos_x = 500
        #2.4画挡板,width = 0 实心儿（填充）1空心(透明)
        pygame.draw.rect(screen, red, (pos_x, pos_y, 120, 40), 0)
    #2.5输出生命值
    print_text(font_one, 0, 0, 'LIVES:' + str(lives))
    #2,6出我们的规分值
    print_text(font_one, 500, 0,'SCORE: ' + str(score))
    #2.7更新显示
    pygame.display.update()


