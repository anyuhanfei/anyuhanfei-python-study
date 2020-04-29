import random

import __init__ as init


def 移动矩阵(矩阵, 方向):
    '''将矩阵向某个方向移动
    Args:
        矩阵: 矩阵对象
        方向: 方向字符串(up down right left)
    return:
        最新生成的矩阵对象
    '''
    生成矩阵边长 = init.生成矩阵边长

    if 方向 == 'up':
        for i in range(0, 生成矩阵边长):
            for o in range(0, 生成矩阵边长):
                if i != 0:  # 第一排不动
                    up_label_num = i - 1  # 当前判断块的上面一块
                    now_label_num = i  # 当前判断块
                    while(up_label_num >= 0):
                        if 矩阵[up_label_num][o].text() == '0' and 矩阵[now_label_num][o].text() != '0':  # 上面没有, 移动
                            矩阵 = 互换值竖向(矩阵, now_label_num, up_label_num, o)
                        elif 矩阵[up_label_num][o].text() == 矩阵[now_label_num][o].text() and 矩阵[now_label_num][o].text() != '0' and 矩阵[up_label_num][o].text() != '0':  # 上面有并且值和我相同, 合并
                            矩阵[up_label_num][o].setText(str(int(矩阵[up_label_num][o].text()) * 2))
                            矩阵[now_label_num][o].setText('0')
                        else:
                            break
                        now_label_num -= 1
                        up_label_num -= 1
    elif 方向 == 'down':
        for i in range(生成矩阵边长 - 1, -1, -1):
            for o in range(0, 生成矩阵边长):
                if i != 生成矩阵边长 - 1:  # 最后排不动
                    down_label_num = i + 1  # 当前判断块的下面一块
                    now_label_num = i  # 当前判断块
                    while(down_label_num <= 生成矩阵边长 - 1):
                        if 矩阵[down_label_num][o].text() == '0' and 矩阵[now_label_num][o].text() != '0':  # 上面没有, 移动
                            矩阵 = 互换值竖向(矩阵, now_label_num, down_label_num, o)
                        elif 矩阵[down_label_num][o].text() == 矩阵[now_label_num][o].text() and 矩阵[now_label_num][o].text() != '0' and 矩阵[down_label_num][o].text() != '0':  # 上面有并且值和我相同, 合并
                            矩阵[down_label_num][o].setText(str(int(矩阵[down_label_num][o].text()) * 2))
                            矩阵[now_label_num][o].setText('0')
                        else:
                            break
                        now_label_num += 1
                        down_label_num += 1
    elif 方向 == 'left':
        for o in range(0, 生成矩阵边长):
            for i in range(0, 生成矩阵边长):
                if o != 0:  # 第一排不动
                    up_label_num = o - 1  # 当前判断块的上面一块
                    now_label_num = o  # 当前判断块
                    while(up_label_num >= 0):
                        if 矩阵[i][up_label_num].text() == '0' and 矩阵[i][now_label_num].text() != '0':  # 上面没有, 移动
                            矩阵 = 互换值横向(矩阵, now_label_num, up_label_num, i)
                        elif 矩阵[i][up_label_num].text() == 矩阵[i][now_label_num].text() and 矩阵[i][now_label_num].text() != '0' and 矩阵[i][up_label_num].text() != '0':  # 上面有并且值和我相同, 合并
                            矩阵[i][up_label_num].setText(str(int(矩阵[i][up_label_num].text()) * 2))
                            矩阵[i][now_label_num].setText('0')
                        else:
                            break
                        now_label_num -= 1
                        up_label_num -= 1
    elif 方向 == 'right':
        for o in range(生成矩阵边长 - 1, -1, -1):
            for i in range(0, 生成矩阵边长):
                if o != 生成矩阵边长 - 1:  # 第一排不动
                    down_label_num = o + 1  # 当前判断块的上面一块
                    now_label_num = o  # 当前判断块
                    while(down_label_num <= 生成矩阵边长 - 1):
                        if 矩阵[i][down_label_num].text() == '0' and 矩阵[i][now_label_num].text() != '0':  # 上面没有, 移动
                            矩阵 = 互换值横向(矩阵, now_label_num, down_label_num, i)
                        elif 矩阵[i][down_label_num].text() == 矩阵[i][now_label_num].text() and 矩阵[i][now_label_num].text() != '0' and 矩阵[i][down_label_num].text() != '0':  # 上面有并且值和我相同, 合并
                            矩阵[i][down_label_num].setText(str(int(矩阵[i][down_label_num].text()) * 2))
                            矩阵[i][now_label_num].setText('0')
                        else:
                            break
                        now_label_num += 1
                        down_label_num += 1
    return 矩阵


def 生成新方块(矩阵):
    '''
    当移动结束后, 生成新的方块, 有死亡判断
    Args:
        矩阵: 矩阵对象
    return:
        返回列表
        元素一是已修改的矩阵
        元素二是是否死亡, True 为死亡
    '''
    random_number = random.randint(0, 9)
    生成数量 = int(('1' * int(init.每回合方块生成数量概率['1'] * 10) + '2' * int(init.每回合方块生成数量概率['2'] * 10))[random_number: random_number + 1])
    一号方块 = '2' if random.randint(0, 9) > (init.方块生成高数值概率 * 10) else '4'
    二号方块 = ('2' if random.randint(0, 9) > (init.方块生成高数值概率 * 10) else '4') if 生成数量 == '2' else '0'

    已生成数量 = 0
    # 随机位置生成新元素(这个实现方法可用, 不美观)
    type = random.randint(0, 3)
    if type == 0:
        for i in range(0, init.生成矩阵边长):
            for o in range(0, init.生成矩阵边长):
                if 矩阵[i][o].text() == '0' and 已生成数量 < 生成数量:
                    矩阵[i][o].setText(一号方块 if 已生成数量 == 0 else 二号方块)
                    已生成数量 += 1
    elif type == 1:
        for o in range(0, init.生成矩阵边长):
            for i in range(0, init.生成矩阵边长):
                if 矩阵[i][o].text() == '0' and 已生成数量 < 生成数量:
                    矩阵[i][o].setText(一号方块 if 已生成数量 == 0 else 二号方块)
                    已生成数量 += 1
    elif type == 2:
        for o in range(init.生成矩阵边长 - 1, -1, -1):
            for i in range(0, init.生成矩阵边长):
                if 矩阵[i][o].text() == '0' and 已生成数量 < 生成数量:
                    矩阵[i][o].setText(一号方块 if 已生成数量 == 0 else 二号方块)
                    已生成数量 += 1
    elif type == 3:
        for i in range(init.生成矩阵边长 - 1, -1, -1):
            for o in range(0, init.生成矩阵边长):
                if 矩阵[i][o].text() == '0' and 已生成数量 < 生成数量:
                    矩阵[i][o].setText(一号方块 if 已生成数量 == 0 else 二号方块)
                    已生成数量 += 1
    return (矩阵, False if 已生成数量 < 生成数量 else True)


def 互换值竖向(矩阵, one_line, two_line, row):
    temp = 矩阵[one_line][row].text()
    矩阵[one_line][row].setText(矩阵[two_line][row].text())
    矩阵[two_line][row].setText(temp)
    return 矩阵


def 互换值横向(矩阵, one_row, two_row, line):
    temp = 矩阵[line][one_row].text()
    矩阵[line][one_row].setText(矩阵[line][two_row].text())
    矩阵[line][two_row].setText(temp)
    return 矩阵
