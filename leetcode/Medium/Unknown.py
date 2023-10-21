from typing import List


class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        r = l = 0
        while r < len(n):
            c = 1

            while r + 1 < len(n) and n[r] == n[r + 1]:
                c += 1
                r += 1
            for i in range(min(2, c)):
                n[l] = n[r]
                l += 1
            r += 1
        return l


ins = Solution()


# print(ins.removeDuplicates([1, 1, 1, 2, 2, 3]))


class RottingOranges:
    def orangesRotting(self, l: List[List[int]]) -> int:
        willRoteen = set()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def willRotten(x):
            if x in willRoteen:
                return True
            else:
                will_all_rotten = False
                stack = [x]
                visited = set(stack)
                while stack:
                    i, j = stack.pop()
                    for x in directions:
                        new_i, new_j = (x[0] + i, x[1] + j)
                        if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m:
                            if l[new_i][new_j] != 0 and (new_i, new_j) not in visited:
                                stack.append((new_i, new_j))
                                visited.add((i, j))
                    if l[i][j] == 2: will_all_rotten = True

                if will_all_rotten:
                    for x in visited:
                        willRoteen.add(x)
                    return True
                return False

        n = len(l)
        m = len(l[0])
        fresh = set()
        rotten = set()
        for i in range(n):
            for j in range(m):
                if l[i][j] == 1:
                    if willRotten((i, j)):
                        fresh.add((i, j))
                    else:
                        return -1
                elif l[i][j] == 2:
                    rotten.add((i, j))
        if len(fresh) == 0: return 0
        if len(rotten) == 0: return -1
        minutes = 0
        while True:
            if len(fresh) == 0: return minutes
            minutes += 1
            for i in rotten.copy():
                if (i[0] + 1, i[1]) in fresh:
                    fresh.remove((i[0] + 1, i[1]))
                    rotten.add((i[0] + 1, i[1]))
                if (i[0] - 1, i[1]) in fresh:
                    fresh.remove((i[0] - 1, i[1]))
                    rotten.add((i[0] - 1, i[1]))
                if (i[0], i[1] + 1) in fresh:
                    fresh.remove((i[0], i[1] + 1))
                    rotten.add((i[0], i[1] + 1))
                if (i[0], i[1] - 1) in fresh:
                    fresh.remove((i[0], i[1] - 1))
                    rotten.add((i[0], i[1] - 1))
                rotten.remove(i)


rottingOranges = RottingOranges()
print(rottingOranges.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(rottingOranges.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))


class Build_Array_Where_You_Can_Find_The_Maximum_Exactly_K_Comparisons:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k > m or k > n: return 0
        if k == 1:
            res = 0
            for i in range(m):
                res += (m - i) ** (n - 1)
            return res
        if k >= 3:
            res = 0
            for x in range(n - k + 1):
                res += (m - 1) ** (k - 1 + x) + k ** (n - k - x)
            return res + self.numOfArrays(n, m - 1, k)


buildArrayWhereYouCanFindTheMaximumExactlyKComparisons = Build_Array_Where_You_Can_Find_The_Maximum_Exactly_K_Comparisons()
# print(buildArrayWhereYouCanFindTheMaximumExactlyKComparisons.numOfArrays(5,3,3))
