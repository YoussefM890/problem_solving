import bisect
from collections import deque, Counter
from functools import reduce, cache
from math import inf, ceil, log
from typing import List


class Constrained_Subsequence_Sum :
    def constrainedSubsetSum(self, n: List[int], k: int) -> int:
        l = []
        tmp  = []
        c = 1
        i = 0
        while i < len(n):
            if n[i] >= 0 :
                l.append(n[i])
            else :
                s = i
                i += 1
                while i < len(n) and n[i] < 0 :
                    i+=1
                if i - s >= k :
                    l.extend(n[s:i])
                if i < len(n) : l.append(n[i])

            i+=1
        ln = len(l)
        @cache
        def dp(x,c) :
            if x == ln : return 0 if c >= 1 else -inf
            take = l[x] + dp(x+1,1)
            leave =  0 if c >= k or c>=1 and l[x]>=0  else dp(x+1 ,c+1)
            return max(take,leave)
        return dp(0,-inf)

constrained_subsequence_sum = Constrained_Subsequence_Sum()
constrained_subsequence_sum.constrainedSubsetSum(
[10,2,-10,-2,5,20,5,-1,1,-6,-1,1,-9],
    2
)


class Find_Building_Where_Alice_and_Bob_Can_Meet :
    def leftmostBuildingQueries(self, l: List[int], q: List[List[int]]) -> List[int]:
        res = [-1]*len(q)
        q = [[max(i,j),max(l[i],l[j])] for i,j in q]
        q.sort(key=lambda x:x[0] * 50001 + x[1])
        m = [[q[0]]]
        for i in range(1,len(q)):
            if q[i][0] == m[-1][-1][0] :
                m[-1].append(q[i])
            else :
                m.append([q[i]])
        print(m)
_2940 = Find_Building_Where_Alice_and_Bob_Can_Meet()
# print(_2940.leftmostBuildingQueries(
# [1,2,1,2,1,2]
#     ,
#     [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1],
#      [2, 2], [2, 3], [2, 4], [2, 5], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3],
#      [4, 4], [4, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
# ))



# _2147 = Number_of_Ways_to_Dividea_Long_Corridor()
# print(_2147.numberOfWays("SPSPPSSPSSSS"))


class Falling_Squares:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        l = [(i,i+j,j) for i,j in positions]

_699 = Falling_Squares()
print(_699.fallingSquares(
[[1,2],[2,3],[6,1]]
))
























