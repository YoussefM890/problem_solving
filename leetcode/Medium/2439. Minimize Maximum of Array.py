from typing import List


class Solution:
    def minimizeArrayValue(self, l: List[int]) -> int:
        p = [0]
        x = l[0]
        for i in l : 
            p.append(p[-1]+i)
        for i in range(1,len(p)) :
            if p[i] > x*i :
                x+= (p[i]-x*i+i-1)//i
        return x