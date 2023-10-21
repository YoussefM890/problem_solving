from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix
        a,b = len(self.m),len(self.m[0])
        self.p = [[0 for i in range(b+1)] for j in range(a+1)]
        for i in range(a-1,-1,-1):
            for j in range(b-1,-1,-1) :
                self.p[i][j] = self.p[i+1][j]+self.p[i][j+1]-self.p[i+1][j+1]+self.m[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.p[row1][col1] - self.p[row1][col2+1] - self.p[row2+1][col1]+self.p[row2+1][col2+1]

x = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(x.sumRegion(2,1,4,3))
print(x.sumRegion(1,1,2,2))
print(x.sumRegion(1,2,2,4))