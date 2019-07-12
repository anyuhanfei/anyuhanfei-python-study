'''
    进行反向迭代以及实现反向迭代
'''
'''
    实现一个连续浮点数发生器FloatRange（与range类型），根据给定范围（start，end）和步进值（step）产生一些连续浮点数
'''
# reversed()函数，返回可迭代对象,实际上是使用reversed()函数是调用了__reversed__魔法方法
list = [1, 2, 3, 4, 5]
for x in reversed(list):
    print(x)  # 5 4 3 2 1


class FloatRange():
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


if __name__ == '__main__':
    float_list = FloatRange(1, 10, 0.8)
    print('正序：')
    for x in float_list:
        print(x)
    print('倒序：')
    for x in reversed(float_list):
        print(x)
