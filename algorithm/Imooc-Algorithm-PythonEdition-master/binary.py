

def binary_search_iteration_ceil_and_floor(arr, value):
    '''二分查找
    将有序数组中的符合要求的元素索引范围返回给用户，迭代版
    Arge：
        arr：有序数组
        value：要查找的值
    return：
        元组，符合要求的元素索引范围，开区间，如果是两个相连的索引则说明没有查找到符合要求的元素值
    '''
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] == value:
            floor, ceil = mid - 1, mid + 1
            while arr[floor] == value:
                floor -= 1
            while arr[floor] == value:
                ceil += 1
            return floor, ceil
        elif arr[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return right, left


def binary_search_recursion_ceil_and_floor(arr, left, right, value):
    '''二分查找
    将有序数组中的符合要求的元素索引范围返回给用户，递归版
    Arge：
        arr：有序数组
        left：左边界，闭区间
        right：右边界，闭区间
        value：要查找的值
    return：
        元组，符合要求的元素索引范围，开区间，如果是两个相连的索引则说明没有查找到符合要求的元素值
    '''
    if left > right:
        return right, left
    mid = int(left + (right - left) / 2)
    if arr[mid] == value:
        floor, ceil = mid - 1, mid + 1
        while arr[floor] == value:
            floor -= 1
        while arr[ceil] == value:
            ceil += 1
        return floor, ceil
    elif arr[mid] > value:
        return binary_search_recursion_ceil_and_floor(arr, left, mid - 1, value)
    else:
        return binary_search_recursion_ceil_and_floor(arr, mid + 1, right, value)
