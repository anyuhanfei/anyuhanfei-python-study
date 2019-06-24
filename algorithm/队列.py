'''
    队列
    首先将第 1个数删除，紧接着将第 2 个数放到这串数的末尾，再将第 3 个数删除并将第 4 个数放到这串数的末尾，再将第 5 个数删除……直到剩下最后一个数，将最后一个数也删除。按照刚才删除的顺序，把这些删除的数连在一起打印出来
'''
init_list = [1, 5, 3, 3, 7, 9, 4, 3, 5]

result_list = []

while len(init_list) != 0:
    init_list.append(init_list[0])  # 将第一个数值添加到最后
    result_list.append(init_list[1])  # 将第二个数值添加到结果集中
    init_list = init_list[2:]  # 删除前两个数值

print(result_list)
