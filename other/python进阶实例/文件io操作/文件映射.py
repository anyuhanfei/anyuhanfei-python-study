'''
    文件映射到内存
'''
# 使用标准库种的mmap模块的mmap()函数，它需要一个打开的文件描述符作为参数
import mmap

f = open('demo.txt', 'r+b')
#f.fileno()  # 文件描述符

m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)  # 写权限

print(m[0])  # 查询此位置的内容
m[0] = 88   # 修改此位置的内容