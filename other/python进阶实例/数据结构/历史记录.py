'''
    历史记录功能
'''
'''
    制作猜数字游戏，添加历史记录功能，显示用户最近猜过的数字
'''
from random import randint
from collections import deque  # 队列

N = randint(0, 10)  # 定义一个随机数
history = deque([], 5)  # 创建一个队列

def guess(k):
    ''' 判断输入数字与随机数的关系 '''
    if k == N:
        print('you win!')
        return True
    if k < N:
        print('太小了')
    else:
        print('太大了')
    return False

while True:  # 开始游戏
    k = input('请输入一个数字')
    if k == 'history' or k == 'h':
        print(history)
    else:
        history.append(int(k))  # 把数字加入到队列中，超出5个最先加入的会自动溢出
        if guess(int(k)):
            break

# 以上为游戏内容，当需要历史记录时，
# 可以使用标准库collections中的deque，它是一个双端循环队列
# 程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入

'''
# pickle的使用
from pickle
pickle.dump(q, open('history','w+'))  # 将数据存储到文件中
pickle.load(open('history'))  # 读取文件中的数据
'''
