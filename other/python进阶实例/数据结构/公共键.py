'''
    快速找到多个字典中的公共键（key）；
    每一个字典中都出现的键就是公共键;
'''
'''
    西班牙足球甲级联赛，每轮球员进球统计：
    第一轮：{'苏亚雷斯':1, '梅西':2, '本泽马':1, 'c罗':3}
    第二轮：{'苏亚雷斯':2, 'c罗':1, '格里兹曼':2, '贝尔':1, }
    第三轮：{'苏亚雷斯':1, '托雷兹':2, '贝尔':1, '内马尔':1}
    ......
    统计出前N轮，每场比赛都有进球的球员。
'''

from random import randint, sample
sample_list = sample('abcdefg', randint(3, 6))  # 随机取样，获取进球球员
data = []
for s in range(1, 5):  # 对每轮的进球进行随机设置，并且保持到一个列表中
    data.append({x: randint(1, 4) for x in sample_list})

''' 普通方法 '''
# 对比查询
for d in data:  # 循环列表
    for k in d:  # 循环字典
        is_within = True
        for d_n in data:  # 在次循环列表，查询键是否在各个字典中
            if k not in d_n:
                is_within = False
        if is_within is True:
            print(k, end=", ")
    break  # 只需要查询第一条字典中的键的重复情况

''' 利用集合的交集操作 '''
# 使用字典的keys()函数
count = 0
for d in data:
    if count == 0:
        res = set(d.keys())
        count += 1
    else:
        res = res & set(d.keys())
print(res)
# map()函数和reduce()函数
from functools import reduce  # python3使用reduce函数需要导入
map_key_tuple = map(dict.keys, tuple(data))  # 所有字典键的合集
lambda_public_key = lambda a, b: a & b  # 交集处理的匿名函数
print(reduce(lambda_public_key, map_key_tuple))  # 获取到公共键
