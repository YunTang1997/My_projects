# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/11
desc: 下一个更大的元素I
"""


# 暴力法
def nextGreaterElement(nums1, nums2):
    nums2_dict = {value: index for index, value in enumerate(nums2)}
    res = []
    n = len(nums2)
    for value in nums1:
        mark = 0  # 0代表nums2中不存在比value大的元素，1代表存在
        tmp_index = nums2_dict.get(value)
        for i in range(tmp_index + 1, n):
            if nums2[i] > value:
                res.append(nums2[i])
                mark += 1
                break
        if mark == 0:
            res.append(-1)
    return res


if __name__ == '__main__':
    print(nextGreaterElement([4,1,2], [1,3,4,2]))
    print(nextGreaterElement([2,4], [1,2,3,4]))



