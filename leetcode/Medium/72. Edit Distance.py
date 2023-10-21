class Solution:
    def minDistance(self, x: str, y: str) -> int:
        Y = len(y)
        X = len(x)
        def dp(i,j) :
            if j == Y or i == X  :
                return max(Y-j,X-i)
            if x[i] != y[j] :
                return 1+ min(dp(i+1,j+1),dp(i+1,j),dp(i,j+1))
            return dp(i+1,j+1)
        return dp(0,0)