# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/4
desc: 摆动序列
"""


def wiggleMaxLength(nums):
    n = len(nums)
    if n < 2:
        return n
    # dp[i][0]表示以下标为i的元素结尾的摆动序列，且序列最后两个元素是递减的最大长度
    # dp[i][1]表示以下标为i的元素结尾的摆动序列，且序列最后两个元素是递增的最大长度
    # 初始化，两者最短均为1
    dp = [[1, 1]for _ in range(n)]
    res = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] < nums[j]:  # 如果递减，更新dp[i][0]
                dp[i][0] = max(dp[j][1] + 1, dp[i][0])  # 该种情况下，由此前最长且最后两个元素是递增的摆动序列转移过来
            elif nums[i] > nums[j]:  #  如果递增，更新dp[i][1]
                dp[i][1] = max(dp[j][0] + 1, dp[i][1])  # # 该种情况下，由此前最长且最后两个元素是递减的摆动序列转移过来
            # 如果相等，则不需要操作
            # 更新最大值
            res = max(dp[i][0], dp[i][1])
    return res


if __name__ == '__main__':
    print(wiggleMaxLength([]))
    print(wiggleMaxLength([1]))
    print(wiggleMaxLength([1,7]))
    print(wiggleMaxLength([1,7,4,9,2,5]))
    print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    print(wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
