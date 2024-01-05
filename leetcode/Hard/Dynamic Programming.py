from typing import List


class Painting_The_Walls:
    def paintWalls(self, c: List[int], t: List[int]) -> int:
        # npw : walls don't have to paint
        MAX = sum(c)

        def dp(x, npw):
            if x == len(c): return 0 if npw >= 0 else MAX
            if x + npw >= len(c): return 0
            return min(
                c[x] + dp(x + 1, npw + t[x]),
                dp(x + 1, npw - 1)
            )

        return dp(0, 0)

        def paintWallsSol(self, c: List[int], t: List[int]) -> int:
            # r : remaining
            l = len(c)
            MAX = sum(c)
            dp = [[0 for r in range(-l, l)] for x in range(-l, l)]
            for x in range(l, -l, -1):
                for r in range(-l + 1, l):
                    if r <= 0: dp[x][r] = 0
                    if x == l: dp[x][r] = MAX
                    dp[x][r] = min(
                        c[x] + dp[x + 1][r - 1 - t[x]],
                        dp[x + 1][r]
                    )
            return dp[0][4]


painting_the_walls = Painting_The_Walls()
# print(painting_the_walls.paintWalls(
#     [937, 252, 716, 781, 319, 198, 273, 554, 140, 68, 694, 583, 1080, 16, 450, 229, 710, 1003, 1117, 1036, 398, 874,
#      289, 664, 600, 588, 372, 1066, 375, 532, 984, 328, 1067, 746],
#     [5, 3, 1, 3, 2, 1, 3, 3, 5, 3, 5, 5, 4, 1, 3, 1, 4, 4, 4, 1, 5, 1, 2, 3, 2, 3, 3, 4, 1, 3, 4, 1, 1, 5]
# ))
class Number_Of_Ways_To_Stay_In_The_Same_Place_After_Some_Steps:
    def numWays(self, s: int, length: int) -> int:
        def dp(stepsLeft, currentIndex):
            if stepsLeft < currentIndex: return 0
            if stepsLeft == 0:
                return 1 if currentIndex == 0 else 0
            left = dp(stepsLeft - 1, currentIndex - 1) if currentIndex > 0 else 0
            right = dp(stepsLeft - 1, currentIndex + 1) if currentIndex < length - 1 else 0
            stay = dp(stepsLeft - 1, currentIndex)
            return left + right + stay

        return dp(s, 0) % (10 ** 9 + 7)

    def numWays2(self, s: int, length: int) -> int:
        l = min(length, s)
        dp = [[0 for j in range(s + 1)] for i in range(l)]
        dp[0][0] = 1
        for j in range(1, s + 1):
            for i in range(l - 1, -1, -1):
                res = dp[i][j - 1]
                if i > 0:
                    res += dp[i - 1][j - 1]
                if i < l - 1:
                    res += dp[i + 1][j - 1]
                dp[i][j] = res

        return dp[0][s] % (10 ** 9 + 7)



number_of_ways_to_stay_in_the_same_place_after_some_steps = Number_Of_Ways_To_Stay_In_The_Same_Place_After_Some_Steps()
print(number_of_ways_to_stay_in_the_same_place_after_some_steps.numWays(
    27, 7
))