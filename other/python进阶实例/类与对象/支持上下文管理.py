'''
    让对象支持上下文管理
'''
'''
    实现上下文管理协议，需要定义实例的__enter__,__exit__方法，
    它们分别在with开始和结束时被调用
'''
class my_with():
    def __enter__(self):
        print('上下文开始')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('上下文结束,报错也可以执行')

with my_with() as mw:
    print(1)