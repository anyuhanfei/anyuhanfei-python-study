'''
    为元组中的每个元素命名，提高程序可读性
'''
'''
    学生信息系统中数据为固定格式：（名字，年龄，性别，邮箱地址）
    学生数量很大，为了减少存储开销，对每个学生信息用元组表示
    访问时，使用序列索引（index）访问，大量序列索引降低程序可读性，如何解决？
'''
student = ('Jim', 18, 'male', '1234567@qq.com')

'''
    方法1：定义常量，常量赋值为这些序列索引值(类似其他语言的枚举类型)
'''
NAME, AGE, SEX, EMAIL = range(4)
print(student[AGE])  # student[1]

'''
    方法2：使用标准库中collections.namedtuple代替内置tuple
'''
from collections import namedtuple

s_tuple = namedtuple('student', ['name', 'age', 'sex', 'email'])  # 参数：元组名称，序列对应的元素名
student = s_tuple(name='Jim', age=16, sex='male', email='1234567@qq.com')
print(student.name)