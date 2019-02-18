'''
    让字典保持有序
'''
'''
    在竞赛中需要把该选手的用时记录到字典中，以便赛后按选手名查询成绩。
    比赛结束后，需要按排名顺序依次打印选手成绩。
    加入字典的次序就是选手的排名，但是字典是无序的，不会按照添加的顺序排列
'''
from random import randint, sample
data = {'xyzabchijkl'[i-1] :(i, i*10) for i in range(1,10)}
print(data)  # 会发现此字典是无序的（违心，python3.6之后的字典修改为了有序）
# 即使是有序的，也依旧可以使用collections.OrderedDict替代内置字典
from collections import OrderedDict
data = OrderedDict({'xyzabchijkl'[i-1] :(i, i*10) for i in range(1,10)})
print(data)

'''
    此方法在python3.6版本以上无效，因为字典已经被修改为有序的
'''
