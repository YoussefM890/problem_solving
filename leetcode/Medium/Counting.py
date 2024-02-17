from collections import Counter
from typing import List


class Least_Number_of_Unique_Integers_after_K_Removals:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        l = sorted(Counter(arr).values())
        length = len(l)
        for i in l:
            if k >= i:
                k -= i
                length -= 1
            else:
                break
        return length

_1481 = Least_Number_of_Unique_Integers_after_K_Removals()
print(_1481.findLeastNumOfUniqueInts([4,3,1,1,3,3,2],3))