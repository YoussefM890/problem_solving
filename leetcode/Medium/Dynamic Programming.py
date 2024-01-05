
from typing import List

#416. Partition Equal Subset Sum
class Solution:
    def canPartition(self, l: List[int]) -> bool:
        def dp(x):
            if x < 0 : return False

class Max_Dot_Product_Of_Two_Subsequences :
    def maxDotProduct(self, n: List[int], m: List[int]) -> int:
        if m[0] * n[0] < 0 :
            x = n[0]
            for i in n :
                if i*x <= 0 : break
            else :
                x = m[0]
                for i in m :
                    if i*x <= 0 : break
                else :
                    return min(n)*max(m[0]) if n[0] > 0 else max(n[0]) * min(m[0])
        N,M = len(n) , len(m)
        def dp(i,j):
            if i == N or j == M : return 0
            x = n[i]*m[j]
            return max(dp(i+1,j+1) + x,
                           dp(i+1,j),
                           dp(i,j+1),
                           dp(i+1,j+1)
            )
        return dp(0,0)
# max_dot_product_of_two_subsequences = Max_Dot_Product_Of_Two_Subsequences()
# print(max_dot_product_of_two_subsequences.maxDotProduct([-1,-1],[1,1]))
class Knight_Dialer :
    def knightDialer(self, n: int) -> int:
        if n == 1 :
            return 10
        # moves = [[4,5],[5,7],[6,8],[4,7],[3,8,0],[1,6,0],[2,5],[1,3],[2,4]]
        moves = [[1,2],[0,0],[0,0,3],[2,2]]
        ln = len(moves)
        dp = [[0 for j in range(n-1)] for i in range(ln)]
        for j in range(n-1):
            for i in range(ln):
                if j == 0 :
                    dp[i][j] = len(moves[i])
                else :
                    res = 0
                    for move in moves[i]:
                        res += dp[move][j-1]
                    dp[i][j] = res
        # print([dp[i][n-2] for i in range(ln)])
        mult = [4,2,2,1]
        return sum([dp[i][n-2]*mult[i] for i in range(ln)]) % (10**9 +7)
_935 = Knight_Dialer()
print(_935.knightDialer(2))
print(_935.knightDialer(3))
print(_935.knightDialer(4))
print(_935.knightDialer(5))