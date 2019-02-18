'''
    访问文件的状态
'''
# 系统调用：标准库os模块下的三个系统调用stat,fstat,lstat获取文件状态
# 快捷函数：标准库种os.path下一些函数,不演示

import os
print(os.stat('demo.txt'))  # 获取状态
print(os.lstat('demo.txt'))
f = open('demo.txt', 'r')
print(os.fstat(f.fileno()))  # 传参为文件描述符
# 以上三者相同，第一种方法最简单

s = os.stat('demo.txt')
import stat  # 有很多对文件的判断等函数
stat.S_ISDIR(s.st_mode)  # 判断文件是否是文件夹,s.st_mode文件类型\权限

s.st_mode & stat.S_IRUSR  # 读权限对比，大于0则有权限

# 三个时间在st_atime,st_mtime,st_ctime参数中
# 文件大小在st_size中

