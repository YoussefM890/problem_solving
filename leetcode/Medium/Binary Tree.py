from collections import deque
from math import inf
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Find_Largest_Value_In_Each_Tree_Row:
    def largestValues(self, r: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([r, 0])
        row = 0
        mx = -inf
        while deque:
            node, nodeRow = deque.popleft()
            if nodeRow == row:
                mx = max(mx, node.val)
            else:
                res.append(mx)
                mx = -inf
            if node.left != None: q.append([node.left, nodeRow + 1])
            if node.right != None: q.append([node.right, nodeRow + 1])
        q.append(mx)
        return q


class BinaryTreeWithFactors:
    def numFactoredBinaryTrees(self, l: List[int]) -> int:
        leng = len(l)
        MOD = 10**9 +7
        l.sort(reverse=True)
        d = {l[i] : i for i in range(leng)}
        dp = [1]*leng
        for x in range(leng-1,-1,-1) :
            for i in range(x + 1, len(l)):
                rest = l[x] // l[i]
                if l[x] % l[i] == 0 and rest in d:
                    dp[x] += dp[i] * dp[d[rest]]
        return sum(dp) % MOD

binary_tree_with_factors = BinaryTreeWithFactors()
print(binary_tree_with_factors.numFactoredBinaryTrees(
    [2,3,6]
))
