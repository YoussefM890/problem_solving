from typing import List


class Solution:
    def lengthOfLIS(self, l: List[int]) -> int:
        lis = []
        def dp(x) :
            if x == 0 : return 1
            mx = 1
            for i in range(x) :
                if l[x] > l[i] :
                    mx = max(mx,dp(i) + 1)
            lis.append(mx)
            return mx
        for i in range(len(l)-1) :
            lis.append(dp(i))
        return max(lis)
