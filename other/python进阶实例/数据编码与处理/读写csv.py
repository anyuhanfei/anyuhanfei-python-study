'''
    读写csv文件
'''
'''
    csv是excel文件中的一类，可以使用标准库中的csv模块
    csv每行都是一行数据，字段之间用逗号隔开
'''
import csv

# 读
rf = open('1.csv', 'rb')  # 以二进制打开
reader = csv.reder(rf)  # 生成一个迭代器

# 写
wf = open('1_1.csv', 'wb')
write = csv.writer(wf)
write.writerow(reader.next())  # 将读的一行写入

# 如果是整理写数据，则可以做如下代码
import csv

with open('文件名', 'rb') as rf :
    reader = csv.reader(rf)
    with open('文件名', 'wb') as wf :
        write = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)  # 将头部信息添加到第一行
        for row in reader :  # 指针已经在第一行了，所以循环从第二行开始
            # 进行循环插入数据，插入前可以随意进行判断等其他操作
            writer.writerow(row)