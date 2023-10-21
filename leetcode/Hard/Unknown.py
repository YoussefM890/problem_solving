import bisect
from functools import reduce
from typing import List


class Painting_The_Walls:
    def paintWalls(self, c: List[int], t: List[int]) -> int:
        MAX = sum(c)
        def dp(l, p):
            if not l: return 0
            res = MAX
            if p == 0:
                for index, i in enumerate(l):
                    res = min(
                        dp(tuple(l[:index] + l[index + 1:]), t[i]) + c[i],  # p
                        res
                    )
            else:
                for index, i in enumerate(l):
                    res = min(
                        dp(tuple(l[:index] + l[index + 1:]), p - 1),
                        res
                    )
            return res

        return dp(tuple(range(len(c))), 0)


painting_the_walls = Painting_The_Walls()
# print(painting_the_walls.paintWalls(
#     [937, 252, 716, 781, 319, 198, 273, 554, 140, 68, 694, 583, 1080, 16, 450, 229, 710, 1003, 1117, 1036, 398, 874,
#      289, 664, 600, 588, 372, 1066, 375, 532, 984, 328, 1067, 746],
#     [5, 3, 1, 3, 2, 1, 3, 3, 5, 3, 5, 5, 4, 1, 3, 1, 4, 4, 4, 1, 5, 1, 2, 3, 2, 3, 3, 4, 1, 3, 4, 1, 1, 5]
# ))

class Number_Of_Ways_To_Stay_In_The_Same_Place_After_Some_Steps :
    def numWays(self, s: int, length: int) -> int:
        dp = [[0 for j in range(s)] for i in range(length)]
        dp[0][0] = 1
        for j in range(s):
            for i in range(length) :
                if j == 0 :
                    continue
                left = dp[i-1][j - 1] if i > 0 else 0
                right = dp[i+1][j - 1] if i < length -1 else 0
                stay = dp[i][j - 1]
                dp[i][j] = left + right + stay
        print(dp)
        return sum(dp[0]) % (10**9 +7)

number_of_ways_to_stay_in_the_same_place_after_some_steps = Number_Of_Ways_To_Stay_In_The_Same_Place_After_Some_Steps()
print(number_of_ways_to_stay_in_the_same_place_after_some_steps.numWays(
27,7
))