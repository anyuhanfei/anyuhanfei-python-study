'''
    创建可管理的对象属性
'''
'''
    在正常的类中，一般调用方法来获取或操作一些属性，这样可以增加一些判断或者其他操作，由很大的灵活行
    但是在使用方面确实比较繁琐；
    使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问;
'''
from math import pi

class Circle() :
    ''' 圆 '''
    def __init__(self, radius) :
        ''' 初始化一个圆的半径 '''
        self.radius = radius

    def getRadius(self) :
        ''' 获取圆的半径 '''
        return self.radius
    
    def setRadius(self, value) :
        ''' 修改圆的半径 '''
        if not isinstance(value, (int, long, float)) :
            raise ValueError('wrong rype')
        self.radius = float(value)

    def getArer(self):
        ''' 计算圆的面积 '''
        return self.radius ** 2 * pi
    
    # 操作属性时自动调用的方法，查看，设置，删除
    R = property(getRadius, setRadius)

if __name__ == '__main__' :
    c = Circle(3.2)
    print(c.R)
    