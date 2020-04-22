# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/21
desc: 统计优美子数组
"""


import sys

# 方法一：
class Solution1():
    def numberOfSubarrays1(self, nums, k):
        len_nums = len(nums)
        odd = [i for i in range(len_nums) if nums[i] % 2 == 1]
        len_odd = len(odd)
        if len_odd < k:
            return 0

        result = 0
        for i in range(len_odd - k + 1):  # 移动窗口
            start, end = odd[i], odd[i + k - 1]
            if i == 0:
                left_rest = odd[i]
            else:
                left_rest = start - odd[i - 1] - 1
            if i + k - 1 < (len_odd - 1):
                right_rest = odd[i + k] - end - 1
            else:
                right_rest = len_nums - 1 - end
            result += (left_rest + right_rest + left_rest * right_rest + 1)
        return result


# 方法二:
class Solution2():
    def numberOfSubarrays2(self, nums, k):
        len_nums = len(nums)
        odd = [-1]  # 处理左边界
        odd += [i for i in range(len_nums) if nums[i] % 2 == 1]  # 按序获取所有奇数的下标
        odd.append(len_nums)  # 处理右边界

        ans = 0
        for i in range(1, len(odd) - k):  # 移动窗口
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k -1])
        return  ans


if __name__ == '__main__':
    input_ = sys.stdin.readline().strip('[]\n').split(',')
    nums = list(map(int, input_))
    k = int(sys.stdin.readline().strip())
    print(Solution1().numberOfSubarrays1(nums, k))
    print(Solution2().numberOfSubarrays2(nums, k))