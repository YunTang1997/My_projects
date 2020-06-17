# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/17
desc: 矩阵中的路径
"""


def exist(board, word):
    def dfs(i, j ,k):
        if not 0 <= i < n or not 0 <= j < m or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        tmp, board[i][j] = board[i][j], ''
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = tmp
        return res

    n, m = len(board), len(board[0])
    if not board or not word:
        return False

    for i in range(n):
        for j in range(m):
            if dfs(i, j, 0):
                return True
    return False


if __name__ == '__main__':
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(exist([["a","b"],["c","d"]], "abcd"))
