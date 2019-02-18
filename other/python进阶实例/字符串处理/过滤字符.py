'''
    过滤掉字符串中不需要的字符
'''
# 1.字符串strip(),lstrip(),rstrip()方法去掉字符串两端字符
s = '    123   33355   '
print(s.strip(' '))  # 默认空格，可设置，也可设置多个
print(s.lstrip(' '))
print(s.rstrip(' 5'))

# 2.删除单个固定位置的字符，使用切片+拼接的方式
s = 'abc:123'
print(s[:3] + s[4:])

# 3.字符串的replace()方法或正则表达式re.sub()删除任意位置字符
s = 'a1a2a3a4a5'
print(s.replace('a', ''))  # 仅能替换一种
import re
print(re.sub('[a2]', '', s))  # 正则，可替换多种字符

# 4.字符串translate()方法，可以同时删除多种不同字符
s = 'abc123456789xyz'
# import string
# #string.maketrans('abcxyz', 'xyzabc')  # 映射
# print(s.translate(string.maketrans('abcxyz', 'xyzabc'))) # 替换
