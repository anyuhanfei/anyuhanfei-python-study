'''
    拆分含有多个分隔符的字符串
'''
'''
    字符串中包含多个不同的分隔符，要依据分隔符号拆分不同的字段
'''

s = 'ab|cd/efg|hi,jkl$nm^topq;ret:uvw?xyz'

# 1.连续使用str.split()方法，每次处理一种分隔符
res = s.split(';')  # 处理;
delimiter = ['|', '/', ',', '$', '^', ';', ':', '?']
for d in delimiter :
    t = []
    map_t = map(lambda x: x.split(d), res)  # 二维，无法直接使用
    for tt in map_t :  # 降维打击
        t.extend(tt)
    res = t
print(res)

# 2.使用正则表达式的re.split()方法，一次性拆分字符串
import re

print(re.split('[|/,$^;:?]+', s))
