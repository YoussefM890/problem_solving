class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        dp = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]
        for x in range(1, len(dp)):
            for y in range(1, len(dp[0])):
                if X[x - 1] == Y[y - 1]:
                    dp[x][y] = 1 + dp[x - 1][y - 1]
                else:
                    dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])
        return dp[-1][-1]
