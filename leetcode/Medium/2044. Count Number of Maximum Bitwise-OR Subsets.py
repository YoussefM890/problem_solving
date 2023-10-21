import collections
from functools import reduce


def countMaxOrSubsets(A):
    dp = collections.Counter([0])
    for a in A:
        for k, v in dp.items():
            dp[k | a] += v
    return dp[max(dp)]
countMaxOrSubsets([3,2,1,5])
