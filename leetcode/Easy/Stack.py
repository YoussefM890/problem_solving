from cmath import inf
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(': ')', '{': '}', '[': ']'}
        keys = set(opening.keys())
        values = set(opening.values())
        for i in s:
            if i in keys:
                stack.append(i)
            elif i in values:
                if len(stack) == 0: return False
                if opening[stack.pop()] != i: return False
        return len(stack) == 0


class MinStack:
    def __init__(self):
        self.stack = []
        self.mn = [2 ** 32]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mn[-1] >= val: self.mn.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.mn[-1] == val: self.mn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mn[-1]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
