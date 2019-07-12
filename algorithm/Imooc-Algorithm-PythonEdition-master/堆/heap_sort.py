import random
import time
from max_heap import MaxHeap


def heap_sort_one(init_list):
    '''堆排序1
    循环未排序数组，将数组依次添加到堆中。
    计算数组的个数或者获取堆的元素个数。
    下标倒序循环，依次取出堆的最大值并在此下标赋值。
    '''
    max_heap = MaxHeap()
    for i in init_list:
        max_heap.insert(i)
    list_count = len(init_list)
    # list_count = max_heap.size()
    for c in range(list_count, 0, -1):
        init_list[c - 1] = max_heap.extract_max()
    return init_list


def heap_sort_two(init_list):
    '''堆排序2
    将整个数组添加到堆中。
    计算数组的个数或者获取堆的元素个数。
    下标倒序循环，依次取出堆的最大值并在此下标赋值。
    '''
    max_heap = MaxHeap()
    max_heap.all_insert_heap(init_list)
    list_count = len(init_list)
    for c in range(list_count, 0, -1):
        init_list[c - 1] = max_heap.extract_max()
    return init_list


if __name__ == "__main__":
    max = 1000000
    init_list = [random.randint(0, 1000) for x in range(max)]
    start_time = time.time()
    res = heap_sort_one(init_list)
    end_time = time.time()
    print('运行时间：%s' % (end_time - start_time))
