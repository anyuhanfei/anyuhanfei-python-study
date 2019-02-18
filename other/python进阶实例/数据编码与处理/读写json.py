'''
    读写json数据
'''
# 使用标准库的json模块，其中loads,dumps函数可以完成json数据的读写
import json

# python数据类型转换称json
l = [1, 2, '3', {'name': 'bob'}]
l_json = json.dumps(l, separators=[',', ':'])
print(l_json)
# json转换为python数据类型
print(json.loads(l_json))
# dump和load是操作文件中的json