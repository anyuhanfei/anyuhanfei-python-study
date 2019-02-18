'''
    使用生成器函数实现可迭代对象
'''
'''
    实现可迭代对象的类，能迭代出给定范围内的所有素数
    pn = PrimeNumbers(1, 30)
    for k in pn:
        print(k, end=' ')
    结果为：2 3 5 7 11 13 17 19 23 29
'''
# 将该类的__iter__方法实现称生成器函数，每次yield返回一个素数
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2, 9):
            if k % i == 0:
                return False
        return True
    
    def __iter__(self):
        for k in range(self.start, self.end+1):
            if self.isPrimeNum(k):
                yield k

if __name__ == '__main__' :
    for x in PrimeNumbers(1,100):
        print(x)