'''
    派生内置不可变类型并修改其实例化行为
'''
'''
    定义一种新类型的元组，对于传入的迭代对象，只保留int类型且值大于0的元素
    要求IntTiple是内置tuple的子类.
    tuple元组是__new__()魔法方法创建出来的，所以在__init__()魔法方法执行时，这个元组已经完成了创建
'''
class IntTuple(tuple) :
    ''' 新类型的元组,对于传入的迭代对象，只保留int类型且值大于0的元素 '''
    def __new__(cls, iterable):
        ''' 最先执行，筛选数据并创建元组 '''
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)
    
    def __init__(self, iterable) :
        ''' 调用父类init方法 '''
        super(IntTuple, self).__init__()

if __name__ == '__main__' :
    t = IntTuple([1, -1, 3, 5, ('a', 'b'), 'c'])
    print(t)