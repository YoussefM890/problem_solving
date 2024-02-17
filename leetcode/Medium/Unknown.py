from collections import deque, Counter, defaultdict
from functools import cache, reduce
from idlelib.tree import TreeNode
from math import inf
from typing import List, Optional
from leetcode.data_structures import ListNode, TreeNode


class LongestPalindromicSubstring:
    def longestPalindrome(self, l: str) -> str:
        # @cache
        def dp(s, e):
            if s == e: return [1, l[s]]
            print(l[s:e + 1], " ", l[e:s - 1:-1], " ", [e - s + 1, l[s:e + 1]])
            if l[s:e + 1] == l[e:s - 1:-1]: return [e - s + 1, l[s:e + 1]]
            return sorted([dp(s + 1, e), dp(s, e - 1)], key=lambda x: x[0], reverse=True)[0]

        return dp(0, len(l) - 1)[1]


longest_palindromic_substring = LongestPalindromicSubstring()


# print(longest_palindromic_substring.longestPalindrome("bb"))


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


# print(rottingOranges.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
# print(rottingOranges.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))


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
class Determine_if_a_Cell_Is_Reachable_at_a_Given_Time:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x = abs(fx - sx)
        y = abs(fy - sx)
        m = min(x, y)
        return t >= m + abs(x - y)


# determine_if_a_cell_is_reachable_at_a_given_time = Determine_if_a_Cell_Is_Reachable_at_a_Given_Time()
# print(determine_if_a_cell_is_reachable_at_a_given_time.isReachableAtTime(
#     1,4,1,2,1
# ))

class Arithmetic_Subarrays:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        pass


class Longest_Turbulent_Subarray:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        l = []
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                l.append(1)
            elif arr[i - 1] > arr[i]:
                l.append(-1)
            else:
                l.append(0)
        res, i, j = 0, 0, 1
        while j < len(l):
            if l[j] == 0:
                res = max(res, j - i + 1)
                i = j + 1
                j = j + 2
            elif l[j] != l[j - 1]:
                j += 1
            else:
                res = max(res, j - i + 1)
                i = j
                j += 1
        return max(res, j - i + 1)


_978 = Longest_Turbulent_Subarray()
print(_978.maxTurbulenceSize(
    [100]
))


class Number_of_Laser_Beams_in_a_Bank:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = last = 0
        for i in bank:
            c = i.count('1')
            if c != 0:
                res += last * c
                last = c
        return res


class Amount_of_Time_for_Binary_Tree_to_Be_Infected:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        res = 0
        q = deque(root)
        while q:
            cur = q.pop()


class Out_of_Boundary_Paths:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        queue = deque((startRow, startColumn))
        res = 0
        if queue:
            r, c = queue.pop()
            if r + 1 == m: res += 1
            if r == 0: res += 1
            if c + 1 == n: res += 1
            if c == 0: res += 1
