# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/7/12
desc: 在一个数组nums中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
"""

def singleNumber(nums):
    res = 0
    for i in range(32):
        count = 0  # 记录每一位bit有多少个1
        bit = 1 << i  # # 当前要操作的 bit
        for num in nums:
            if (bit & num) != 0:
                count += 1
        if count % 3 != 0:  #  # 不等于0说明唯一出现的数字在这个bit上是1
            res |= bit
    return res - pow(2, 31) if res > pow(2, 31) - 1 else res  # 避免nums中元素为负数时结果出错


if __name__ == '__main__':
    print(singleNumber([3,4,3,3]))
    print(singleNumber([9,1,7,9,7,9,7]))




