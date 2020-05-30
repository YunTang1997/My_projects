# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/5/30
desc: 柱状图中最大的矩形
"""


from timeit import timeit

# 方法一（暴力法，超时）
def largestRectangleArea_1(heights):
    """遍历每一个高度，以该高度为基准，向两边扩散"""
    n = len(heights)
    res = 0
    for i in range(n):
        cur_height = heights[i]
        left_i = i  # 向左扩散
        while left_i > 0 and heights[left_i - 1] >= heights[i]:
            left_i -= 1
        right_i = i  # 向右扩散
        while right_i < n - 1 and heights[right_i + 1] >= heights[i]:
            right_i += 1
        res = max(res, (right_i - left_i + 1) * heights[i])  # 更新矩形最大面积
    return res


# 方法二（单调栈）
def largestRectangleArea_2(heights):
    n = len(heights)
    stack = []
    res = 0
    for i in range(n):
        while len(stack) > 0 and heights[i] < heights[stack[-1]]:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and heights[stack[-1]] == cur_height:
                stack.pop()
            if len(stack) > 0:
                cur_max_weight = i - stack[-1] - 1
            else:
                cur_max_weight = i
            res = max(res, cur_max_weight * cur_height)
        stack.append(i)
    while len(stack) > 0:
        cur_height = heights[stack.pop()]
        while len(stack) > 0 and heights[stack[-1]] == cur_height:
            stack.pop()
        if len(stack) > 0:
            cur_max_weight = n - stack[-1] - 1
        else:
            cur_max_weight = n
        res = max(res, cur_max_weight * cur_height)
    return res


# 方法三（单调栈+哨兵）：
def largestRectangleArea_3(heights):
    heights = [0] + heights + [0]
    n = len(heights)
    stack = [0]
    res = 0
    for i in range(1, n):
        while heights[i] < heights[stack[-1]]:
            cur_height = heights[stack.pop()]
            while heights[-1] == cur_height:
                stack.pop()
            cur_max_weight = i - stack[-1] - 1
            res = max(res, cur_max_weight * cur_height)
        stack.append(i)
    return res


if __name__ == '__main__':
    print(largestRectangleArea_1([2,1,5,6,2,3]))
    print(timeit("largestRectangleArea_1([2,1,5,6,2,3])", globals=globals(), number=1000))
    print(largestRectangleArea_2([2,1,5,6,2,3]))
    print(timeit("largestRectangleArea_2([2,1,5,6,2,3])", globals=globals(), number=1000))
    print(largestRectangleArea_3([2,1,5,6,2,3]))
    print(timeit("largestRectangleArea_3([2,1,5,6,2,3])", globals=globals(), number=1000))
