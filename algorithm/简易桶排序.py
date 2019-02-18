'''
    简化桶排序
'''
# 将要排序的数据
init_list = [2,3,8,5,3,4]

# 桶容量（数据数+1）
bucket_count = 11
# 桶
sort_count_list = []
for bc in range(bucket_count):
    sort_count_list.append(0)

# 排序容器
sort_list = []
# 统计出现次数
for il in init_list:
    sort_count_list[il] = sort_count_list[il]+1
# 整理排序数据
for scl_key, scl_value in enumerate(sort_count_list):
    for r in range(scl_value):
        sort_list.append(scl_key)
# 打印
print(sort_list)

'''
m为桶的个数,n 为待排序数的个数
代码中`生成桶`的循环一共循环了 m次，
`统计出现次数`的代码循环了 n 次，`整理排序数据`一共循环了 m+n 次。
所以整个排序算法一共执行了 m+n+m+n 次。我们用大写字母 O来表示时间复杂度，因此该
算法的时间复杂度是 O(m+n+m+n)即 O(2*(m+n))。我们在说时间复杂度的时候可以忽略较小
的常数，最终桶排序的时间复杂度为 O(m+n)。还有一点，在表示时间复杂度的时候，n 和 m
通常用大写字母即 O(M+N)。
'''