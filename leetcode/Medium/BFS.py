from collections import deque
from typing import List


class Diagonal_Traverse_II :
    def findDiagonalOrder(self, l: List[List[int]]) -> List[int]:
        queue = deque([[0,0]])
        lengths = [len(i)-1 for i in l]
        res = []
        length = len(l) -1
        while queue :
            i,j = queue.popleft()
            res.append(l[i][j])
            if j == 0 and i < length:
                queue.append([i+1,j])
            if j < lengths[i] :
                queue.append([i,j+1])
        return res

_1424 = Diagonal_Traverse_II()
print(_1424.findDiagonalOrder(
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
))