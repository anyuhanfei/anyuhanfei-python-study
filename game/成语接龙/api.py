'''
成语接龙的API方法
'''


import random


def judge_player_input(data, last_idiom, player_idiom):
    '''判断玩家输入
    Args:
        data: 成语大全
        last_idiom: 上一个成语
        player_idiom: 当前玩家输入的成语
    return:
        bool: 验证成功或失败
        str: 验证后返回的信息
    '''
    if data.get(player_idiom, None) is None:  # 判断玩家输入的是不是一个成语
        return False, '%s不是成语, 请重新输入...' % (player_idiom)
    if data.get(last_idiom)[7] != data.get(player_idiom)[6]:  # 判断玩家输入是不是符合首尾相同
        return False, "回答错误, 请重新输入..."
    return True, "回答正确, 等待电脑回应..."


def composer_input(data, last_idiom=''):
    '''电脑输入成语
    Args:
        data: 成语大全
        last_idiom: 上一个成语
    return:
        bool: 是否获取到了符合要求的成语
        str: 符合要求的成语
    '''
    temp = []
    if last_idiom != '':
        last_idiom_end_spell = data[last_idiom][7]
        for key, value in data.items():
            if value[6] == last_idiom_end_spell:
                temp.append(key)
    else:
        for key, value in data.items():
            temp.append(key)
    if temp == []:
        return False, ''
    key = random.randint(0, len(temp) - 1)
    return True, temp[key]


def history_idiom(data):
    data_str = ""
    for i in data:
        if data_str == "":
            data_str += i
        else:
            data_str += '->' + i
    return data_str
