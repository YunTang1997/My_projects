# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/13
desc: 给定一个32位正整数n，你需要找到最小的32位整数，其与n中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
"""


# 方法一
def nextGreaterElement_1(n):
    n_list = [int(i) for i in str(n)]
    if n_list == sorted(n_list, reverse=1):  # 若满足该条件，说明n在题目条件下已经最大
        return -1
    n_len = len(n_list)
    for i in range(n_len - 1, -1, -1):  # 从后往前遍历，找到第一次出现右边元素比左边元素大的下标（解题重点）
        if n_list[i - 1] < n_list[i]:
            need_i = i - 1
            break
    tmp = float('inf')  # 记录need_i右边比n_list[need_i]大的最小元素
    for i in range(n_len - 1, need_i, -1):
        if n_list[i] > n_list[need_i]:
            if n_list[i] < tmp:
                need_j = i  # 记录tmp对应的下标
                tmp = n_list[i]
    # 交换n_list[need_i]和n_list[need_j]的位置
    n_list[need_j] = n_list[need_i]
    n_list[need_i] = tmp
    # 将need_i右边（不包括need_i）元素从小到大排序
    n_list = n_list[ : need_i + 1] + sorted(n_list[need_i + 1 : ])
    res = int(''.join(map(str, n_list)))
    return res if res < pow(2, 31) else -1


# 方法二（单调栈）
def nextGreaterElement_2(n):
    n_list = list(map(int, str(n)))
    stack, n_len = [], len(n_list)
    stack.append(n_list.pop())
    while n_list and stack[-1] <= n_list[-1]:  # 从后往前遍历，找到第一次出现右边元素比左边元素大的下标（解题重点）
        stack.append(n_list.pop())
    if not n_list:  # 若经过上述while循环以后，n_list为空说明n_list本身已经是从大到小排序，对应的n在题设条件下已是最大值
        return -1
    for j in range(len(stack)):  # 注意经过上述过程，stack中的元素已是n_list对应部分元素从小到大排列（栈底到栈顶，递增栈）
        if stack[j] > n_list[-1]:  # 因此从左往右遍历找到的第一个大于n_list[-1]的元素即为大于它的最小元素
            stack[j], n_list[-1] = n_list[-1], stack[j]  # 交换两者位置
            break
    n_list += stack
    res = int(''.join(map(str, n_list)))
    return res if res < pow(2, 31) else -1


if __name__ == '__main__':
    print(nextGreaterElement_1(21))
    print(nextGreaterElement_1(12))
    print(nextGreaterElement_1(2302431))
    print(nextGreaterElement_2(21))
    print(nextGreaterElement_2(12))
    print(nextGreaterElement_2(2302431))


