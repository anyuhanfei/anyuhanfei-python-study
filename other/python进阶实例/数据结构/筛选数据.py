'''
    在列表，字典，集合中根据条件筛选数据
'''
from random import randint
data_list = [randint(-10, 10) for _ in range(10)]  # 随机生成列表
data_dist = {x: randint(60, 100) for x in range(1, 21)}  # 随机生成字典

''' 通用做法 '''
# 把这些数据通过迭代和条件过滤将数据存放到列表中，在进行数据类型转换
res = []
for x in data_list:
    if x >= 0:
        res.append(x)
print(res)

''' 列表 '''
# filter()函数
res = filter(lambda x: x >= 0, data_list)
print(res)
# 列表解析
print([x for x in data_list if x >= 0])

''' 字典 '''
# 字典解析
print({k: v for k, v in data_dist.items() if v > 90})

''' 集合 '''
# 集合解析
data_set = set(data_list)
print({x for x in data_set if x > 0})
