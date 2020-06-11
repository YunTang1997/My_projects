# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/11
desc: 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组[3,4,5,1,2]为[1,2,3,4,5]的一个旋转，该数组的最小值为1。  
"""


def minArray(numbers):  # 注意未旋转之前numbers是升序
    n = len(numbers)
    for i in range(n - 1):
        if numbers[i + 1] < numbers[i]:  # 找到第一个不符合升序的元素
            return numbers[i + 1]
    return numbers[0]  # 若前面的for循环没有return，说明numbers本身没有旋转，直接返回第一个元素即可


if __name__ == '__main__':
    print(minArray([3,4,5,1,2]))
    print(minArray([2,2,2,0,1]))
    print(minArray([2,2,2,2,2]))
    print(minArray([1,3,5]))

