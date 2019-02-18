'''
    快速排序
'''
def quick_sort(init_list, left_key, right_key):
    if left_key >= right_key: # 如果左大于右，说明已经完成了排序
        return
    temp = init_list[left_key] #基准数
    sentry_left = left_key #左哨兵
    sentry_right = right_key #右哨兵
    while sentry_left != sentry_right: #两个哨兵相遇，停止行动
        while init_list[sentry_right] >= temp and sentry_left < sentry_right: #右哨兵向左，遇到小于基准数的数停止
            sentry_right = sentry_right - 1
        while init_list[sentry_left] <= temp and sentry_left < sentry_right: #左哨兵向右，遇到大于基准数的数停止
            sentry_left = sentry_left + 1
        if sentry_left < sentry_right: #如果两个哨兵还没碰面，互换站位的值
            init_list[sentry_left], init_list[sentry_right] = init_list[sentry_right], init_list[sentry_left]
        else: #此处按理可以省略，但是当sentry_left和sentry_right相同时却没有跳出while循环，只能添加此处
            break
    init_list[left_key], init_list[sentry_left] = init_list[sentry_left], init_list[left_key] #基准数位置的值与哨兵相遇位置的值互换
    quick_sort(init_list, left_key, sentry_left-1) #基准数位置的左部分
    quick_sort(init_list, sentry_right+1, right_key) #基准数位置的右部分

init_list = [4,6,74,3,43,5,8,2,123,5,7,41,6,82]
init_list = [2,3,4,5,5,6,6,7,8,41,43,74,82,123]

quick_sort(init_list, 0, len(init_list)-1)
print(init_list)
