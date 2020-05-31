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
    stack = []  # 利用列表创建一个栈
    res = 0
    for i in range(n):
        while len(stack) > 0 and heights[i] < heights[stack[-1]]:  # 只有当stack非空且heights[i] < height[stack[-1]]时出栈
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and heights[stack[-1]] == cur_height:  # 相同的柱子高度，直接出栈
                stack.pop()
            # 跳出前一个while循环，说明向在stack中向左扩散找到第一个柱子高度严格小于cur_height的下标，并计算出组合矩形的最大宽度
            if len(stack) > 0:
                cur_max_width = i - stack[-1] - 1
            else:
                cur_max_width = i
            res = max(res, cur_max_width * cur_height)
        stack.append(i)  # 当heights[i] >= height[stack[-1]]时入栈，所以stack也称为单调栈，因为其中元素所对应的柱子高度呈不减趋势
    while len(stack) > 0:  # 跳出第一个while循环，若stack非空，说明还有未处理的柱子高度
        cur_height = heights[stack.pop()]
        while len(stack) > 0 and heights[stack[-1]] == cur_height:
            stack.pop()
        if len(stack) > 0:
            cur_max_width = n - stack[-1] - 1  # 注意n为heights的长度
        else:
            cur_max_width = n
        res = max(res, cur_max_width * cur_height)
    return res


# 方法三（单调栈+哨兵）：
def largestRectangleArea_3(heights):
    # 在原本heights的基础上，添加前后两个高度为0的柱子（哨兵），第一个0保证原本heights中的元素全部入栈，而后一个0保证stack中的元素全部出栈
    heights = [0] + heights + [0]
    n = len(heights)
    stack = [0]
    res = 0
    for i in range(1, n):  # 由于加入了哨兵，所以从1开始
        while heights[i] < heights[stack[-1]]:
            cur_height = heights[stack.pop()]
            while heights[-1] == cur_height:  # 相同的柱子高度，直接出栈
                stack.pop()
            cur_max_width = i - stack[-1] - 1
            res = max(res, cur_max_width * cur_height)
        stack.append(i)
    return res


if __name__ == '__main__':
    print(largestRectangleArea_1([2,1,5,6,2,3]))
    print(timeit("largestRectangleArea_1([2,1,5,6,2,3])", globals=globals(), number=1000))
    print(largestRectangleArea_2([2,1,5,6,2,3]))
    print(timeit("largestRectangleArea_2([2,1,5,6,2,3])", globals=globals(), number=1000))
    print(largestRectangleArea_3([2,1,5,6,2,3]))
    print(timeit("largestRectangleArea_3([2,1,5,6,2,3])", globals=globals(), number=1000))
