import time

def def_execution_time(func, *args):
    '''执行传入方法并计算执行时间
    打印方法起始时间，开始执行方法，执行完毕打印结束时间，计算并打印执行时间

    Arge:
        func: 方法对象
    '''

    start_time = time.time()
    print('起始时间：%s' % start_time)
    func(*args)
    end_time = time.time()
    print('结束时间：%s' % end_time)
    execution_time = end_time - start_time
    print('此方法总计执行时间：%s' % execution_time)

def decorator_execution_time(func):
    '''与上方函数功能相同'''
    def wrapper(*args, **kw):
        start_time = time.time()
        print('起始时间：%s' % start_time)
        func()
        end_time = time.time()
        print('结束时间：%s' % end_time)
        execution_time = end_time - start_time
        print('此方法总计执行时间：%s' % execution_time)
    return wrapper


if __name__ == "__main__":
    @execution_time
    def a():
        time.sleep(1)

    a()

