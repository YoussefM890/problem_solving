from collections import Counter
from typing import List


class Reduction_Operations_to_Make_the_Array_Elements_Equal :
    def reductionOperations(self, l: List[int]) -> int:
        c = Counter(l)
        s = sorted(c)
        length = len(l)
        res = 0
        prev = 0
        for i in s :
            prev += c[i]
            res += length - prev
        return res




_1887 = Reduction_Operations_to_Make_the_Array_Elements_Equal()
print(_1887.reductionOperations(
[5,1,3]
))


class Convert_an_Array_Into_a_2D_Array_With_Conditions:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []

        for num in nums:
            found = False
            for group in res:
                if num in group:
                    continue
                else:
                    found = True
                    group.add(num)
                    break

            if not found:
                res.append(set([num]))

        return res


_2610 = Convert_an_Array_Into_a_2D_Array_With_Conditions()
print(_2610.findMatrix([2, 1, 1]))

class Minimum_Number_of_Operations_to_Make_Array_Empty :
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for i in list(c.values()) :
            if i == 1 : return -1
            m = i % 3
            res += i // 3
            if m != 0 : res+=1
        return res
