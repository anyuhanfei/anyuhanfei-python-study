'''
    对迭代器做切片操作
'''
'''
    有一个文本文件，想读取某个范围内的内容，python中文本文件是可迭代对象。
    使用类似列表切片的方式得到一个范围内容的生成器。
'''
# 使用标准库中的itertools.islice，它能返回一个迭代对象切片的生成器
# islice(可迭代对象, 开始行, 结束行)，如果从第一行读可省略开始行，如果要一直到结束结束行可以写完None，不支持负数参数
# 使用islice()函数后，可迭代对象的指针在定义的结束行位置
from itertools import islice

f = open('迭代器切片txt.txt','r')
for line in islice(f, 10, 20) :
    print(line)