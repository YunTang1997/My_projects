# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/4/25
desc: 利用归并排序法计算数组的逆序对数
"""


class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:  # 判断列表只有一个元素或为空的情况
            return 0  # 递归必须有终止条件

        mid = (l + r) // 2
        ans_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l  # 注意此处i、pos随着l变化
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                ans_count += (j - (mid + 1))
                i += 1
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1

        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            ans_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1

        nums[l : (r + 1)] = tmp[l : (r + 1)]  # 更新nums列表

        return ans_count


    def reversePairs(self, nums):
        n = len(nums)
        tmp = [0] * n
        l, r = 0, n - 1
        return self.mergeSort(nums, tmp, l, r)



print(Solution().reversePairs([7,5,6,4]))