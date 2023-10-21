from typing import List


class Solution:
    def longestConsecutive(self, l: List[int]) -> int:
        s = set(l)
        res = 0
        for i in l:
            if i-1 not in s:
                y = i+1
                while  y in s :
                    y+=1
                res = max(res, y-i)
        return res
