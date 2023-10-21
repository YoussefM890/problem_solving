l = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def fun(l):
    def checkLines():

        for i in range(9):
            crow = set()
            ccol = set()
            for j in range(9):
                if l[i][j] != '.' :
                    if l[i][j] in crow: return False
                    crow.add(l[i][j])
                if l[j][i] != '.' :
                    if l[j][i] in ccol: return False
                    ccol.add(l[j][i])
        return True

    def checkSquares():
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                csquare = set()
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if l[m][n] == '.': continue
                        if l[m][n] in csquare: return False
                        csquare.add(l[m][n])
        return True

    a = checkLines()
    b = checkSquares()
    print(a and b)
    # return checkLines() and checkSquares()


fun(l)
