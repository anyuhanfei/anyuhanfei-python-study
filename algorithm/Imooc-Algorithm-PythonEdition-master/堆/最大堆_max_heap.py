import time


class MaxHeap:
    '''最大堆'''
    data = []
    count = 0

    def __init__(self):
        self.data.append('-')

    def size(self):
        '''元素数'''
        return self.count

    def is_empty(self):
        '''是否为空'''
        return self.count == 0

    def insert(self, value):
        '''添加一个元素'''
        self.data.append(value)
        self.count += 1
        self._shift_up(self.count)

    def extract_max(self):
        '''取出最大的元素'''
        if self.count < 1:
            return
        self.data[self.count], self.data[1] = self.data[1], self.data[self.count]
        self.count -= 1
        self._shift_down(1)
        return self.data.pop(self.count + 1)

    def _shift_down(self, k):
        '''将最上的值移动到相应位置'''
        while True:
            left_down_k = 2 * k
            temp_k = left_down_k
            if left_down_k + 1 <= self.count and self.data[left_down_k] < self.data[left_down_k + 1]:
                temp_k = left_down_k + 1
            if temp_k > self.count or self.data[temp_k] <= self.data[k]:
                break
            self.data[temp_k], self.data[k] = self.data[k], self.data[temp_k]
            k = temp_k

    def _shift_up(self, k):
        '''将新添加的值移动到相应位置'''
        up_k = int(k / 2)
        while k > 1 and self.data[up_k] < self.data[k]:
            self.data[up_k], self.data[k] = self.data[k], self.data[up_k]
            k = up_k
            up_k = int(k / 2)

    def show(self):
        print()
        level = 1
        i = 1
        while i < self.count:
            print(' ' * int(self.count / level), end="")
            print(str(self.data[i]), end="")
            print(' ' * int(self.count / level), end="")
            i += 1
            if level * 2 == i:
                print()
                level = level * 2


def heap_sort(res_list, n):
    maxHeap = MaxHeap()
    for i in range(0, n):
        maxHeap.insert(i)
    while maxHeap.is_empty() is False:
        res_list.append(maxHeap.extract_max())


if __name__ == "__main__":
    res_list = []
    start_time = time.time()
    heap_sort(res_list, 100000)
    end_time = time.time()
    print('运行时间：%s' % (end_time - start_time))
    # print(res_list)
