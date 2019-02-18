'''
    冒泡排序
'''
init_list = [3,6,4,32,54,2234,5,546,434,345,6,657,453,42,2,45,346,5467,7,4,5,345,345,34,5345,34657,645,7]

for i in range(len(init_list) - 1 - 1): # n个数排序，只需要进行n-1次(列表下标从0开始，再减去1，下同理)
    for j in range(len(init_list) - i - 1): # 比较，从第1位开始比较直到最后一个尚未归位的数
        if init_list[j] < init_list[j+1]: #如果前一位小于后一位，则替换
            t = init_list[j]
            init_list[j] = init_list[j+1]
            init_list[j+1] = t

print(init_list)


# 二维
init_list = [('ha3',3),('ha6',6),('ha4',4),('ha32',32),('ha54',54),('ha2234',2234),('ha5',5),('ha546',546),('ha434',434),('ha345',345),('ha6',6),('ha657',657),('ha453',453)]
for i in range(len(init_list) - 2):
    for j in range(len(init_list) - i -1):
        if init_list[j][1] < init_list[j+1][1]:
            t = init_list[j+1]
            init_list[j+1] = init_list[j]
            init_list[j] = t
print(init_list)