'''
    为创建大量实例节省内存
'''


# 定义类的__slots__属性，用来声明实例属性名字的列表
class Player():
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2():
    __slots__ = ['uid', 'name', 'stat', 'level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

# 第一个类消耗内存大，存在__dict__方法，这个方法是一个字典，可以快速增删改查数据，故会占用过多的内存
