from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        solvedBoard = []
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def getValidNumbers(b, row, col):
            # print((row,col))
            p = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
            for i in b[row]:
                if i != '.' and i in p: p.remove(i)
            for i in b:
                if i[col] != '.' and i[col] in p: p.remove(i[col])

            squareNumber = (row//3 , col//3)
            # print(squareNumber)
            middle = ((squareNumber[0])*3 +1 ,(squareNumber[1])*3 +1)
            # print(middle)
            for i in neighbors:
                x = b[i[0] + middle[0]][i[1] + middle[1]]
                if x != '.' and x in p: p.remove(x)
            return p

        def f(b, row):
            for i in range(row, 9):
                for j in range(9):
                    print(i,j)
                    if b[i][j] == '.':
                        p = getValidNumbers(b, i, j)
                        solved = False
                        for k in p:
                            b[i][j] = k
                            solved = solved or f(b, i)
                        return solved
            print(b)
            solvedBoard = b
            return True

        f(board, 0)
        print(solvedBoard)


instance = Solution()
instance.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                      [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                      ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                      [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                      [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
