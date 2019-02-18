'''
    类支持比较操作
'''
'''
    比较符号运算符重载，需要实现__lt__,__le__,__gt__,__eq__,__ne__.
    使用标准库下的functools下的类装饰器total_ordering可以简化此过程。
'''
from functools import total_ordering

@total_ordering
class Rectangle():
    ''' 矩形类，可以进行实例间的比较 '''
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h

    def __lt__(self, obj):
        return self.area() < obj.area()

    def __eq__(self, obj):
        return self.area() == obj.area()

    # 由上面的<和==操作符，total_ordering可以推算出<=操作符的计算，故可以省略

if __name__ == '__main__' :
    r1 = Rectangle(5,3)
    r2 = Rectangle(4,3)

    print(r1 < r2)