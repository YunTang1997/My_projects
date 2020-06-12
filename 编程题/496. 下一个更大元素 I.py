# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/11
desc: 下一个更大的元素I
"""


# 暴力法
def nextGreaterElement_1(nums1, nums2):
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


# 单调栈
def nextGreaterElement_2(nums1, nums2):
    # 先遍历大数组nums2，首先将第一个元素入栈；
    # 继续遍历，当当前元素小于栈顶元素时，继续将它入栈；当当前元素大于栈顶元素时，栈顶元素出栈，此时应将该出栈的元素与当前元素形成key-value键值对，存入HashMap中；
    # 当遍历完nums2后，得到nums2中元素所对应的下一个更大元素的hash表；
    # 遍历nums1的元素在hashMap中去查找‘下一个更大元素’，当找不到时则为-1。
    res, stack, hashmap = [], [], dict()
    for i in nums2:
        while stack and i > stack[-1]:
            hashmap[stack.pop()] = i
        stack.append(i)  # 当stack为空或者当前元素<=栈顶元素时，全部入栈
    for i in nums1:
        res.append(hashmap.get(i, -1))
    return res


if __name__ == '__main__':
    print(nextGreaterElement_1([4,1,2], [1,3,4,2]))
    print(nextGreaterElement_1([2,4], [1,2,3,4]))
    print(nextGreaterElement_2([4,1,2], [1,3,4,2]))
    print(nextGreaterElement_2([2,4], [1,2,3,4]))



