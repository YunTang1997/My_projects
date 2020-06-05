# coding = utf-8

"""
Author: YunTang
version: 0.1
date: 2020/6/4
desc: 新21点
"""


def new21Game(N, K, W):
    dp = [0] * (K + W)  # dp[x]为手上牌面为x时，能获胜的概率
    tmp_sum = 0
    for i in range(K, K + W):  # 此时手上牌面大于等于K，已无法抽牌，能抽取的最大牌面为K+W-1,即倒数第二次手上牌面为K-1，最后一次抽取W
        if i <= N:  # 游戏结束，牌面不超过N，赢
            dp[i] = 1
        else:  # 游戏结束，牌面超过N，输
            dp[i] = 0
        tmp_sum += dp[i]  # 记录这部分和，为转移方程做准备
    for i in range(K - 1, -1, -1):  # 状态转移方程：dp[x]=1/w * (dp[x+1]+dp[x+2]+dp[x+3]...+dp[x+w]，因为每张牌抽取的概率一样
        dp[i] = tmp_sum / W
        tmp_sum = tmp_sum - dp[W + i] + dp[i]  # 更新方程
    return dp[0]  # 返回结果，手上牌面为0时，能获胜的概率


if __name__ == '__main__':
    print(new21Game(N=10, K=1, W=10))
    print(new21Game(N=6, K=1, W=10))
    print(new21Game(N=21, K=17, W=10))
