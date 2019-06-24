'''
    字符串a是否以字符串b开头或结尾
'''
'''
    某文件系统目录下有一系列文件，需要对后缀为某些的加上可执行权限。
    处理这个问题就要判断后缀是否是符合。
'''
# 使用字符串的str.startswith()和str.endswith()方法分别判断开头和结尾
# 注意：多个匹配时参数使用元组
import stat

file_name_list = ['a.sh', 'b.py', 'c.h', 'd.php']

start_condition = ('c', 'b')
end_condition = ('.sh', '.py')

print('判断结尾:')
for fl in file_name_list:
    if fl.endswith(end_condition):
        print(fl)

print('判断开头:')
for fl in file_name_list:
    if fl.startswith(start_condition):
        print(fl)
