'''
    对字符串进行左，右，居中对齐
'''
'''
    某字典中存储了一些列键值对，怎么才能打印出整齐的内容？
'''
test_dict = {'asfa':'rqeqwd', 'asfdsszz': 'qwrwfwefwf', 'aa': 'a'}

# 1.使用字符串的str.ljust(),str.rjust(),str.center()进行左，右，居中对齐
for td_key,td_value in test_dict.items() :
    print(td_key.rjust(10), ':', td_value.ljust(10))

# 2.使用format()方法，传递类似'<20','>20','^20'参数完成同样任务
for td_key,td_value in test_dict.items() :
    print(format(td_key, '>10'), ':', format(td_value, '<10'))