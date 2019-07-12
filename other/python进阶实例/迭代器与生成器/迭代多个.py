'''
    在for语句中迭代多个可迭代对象
'''
'''
    1.学生考试，语文，数学，英语成绩分别在3个列表中，同时迭代3个列表，计算每个学生的总分（并行）
    2.4个班，英语成绩在4个列表中，依次迭代每个列表，统计全年成绩高于90分的人数（串行）
'''
# 并行情况使用内置函数zip，能将多个可迭代对象合并，每次迭代返回一个元组
from random import randint

chinese = [randint(60, 100) for _ in range(10)]
math = [randint(60, 100) for _ in range(10)]
english = [randint(60, 100) for _ in range(10)]

total = []  # 存储每个学生平均成绩列表
for c, m, e in zip(chinese, math, english) :
    total.append(c + m +e)
print(total)

# 串行情况使用标准库中的itertools.chain，能将多个可迭代对象连接
from random import randint
from itertools import chain

e1 = [randint(60, 100) for _ in range(10)]
e2 = [randint(60, 100) for _ in range(10)]
e3 = [randint(60, 100) for _ in range(10)]
e4 = [randint(60, 100) for _ in range(10)]

count = 0

for s in chain(e1, e2, e3, e4):
    if s > 90:
        count += 1
print(count)
