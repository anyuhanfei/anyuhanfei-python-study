'''
    设置文件的缓冲
'''
'''
    将文件内容写入到硬件设备时，使用系统调用，这类i/o操作的时间长，
    为了减少i/o操作的次数，文件通常使用缓冲区；
    文件的缓冲行为，分为全缓冲，行缓冲，无缓冲
'''
# python默认的是全缓冲，就是满足一个块的大小（4096）才会执行一次i/o操作
# 不同的设备块大小是不同的

# 全缓冲：open函数的buffering设置为大于1的整数n，n为缓冲区的大小
# 行缓冲：open函数的buffering设置为1
# 无缓冲：open函数的buffering设置为0

# open('demo.txt', 'w', bufferin=1000)
