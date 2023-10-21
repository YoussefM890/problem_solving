
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
max_dot_product_of_two_subsequences = Max_Dot_Product_Of_Two_Subsequences()
print(max_dot_product_of_two_subsequences.maxDotProduct([-1,-1],[1,1]))
