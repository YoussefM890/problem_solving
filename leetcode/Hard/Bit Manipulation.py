from math import ceil, log


class Minimum_One_Bit_Operations_to_Make_Integers_Zero :
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        for msk in range(ceil(log(n+1,2))):
            if n & 1 << msk != 0 :
                res = -res + (1 << msk+1) - 1
        return res

_1611 = Minimum_One_Bit_Operations_to_Make_Integers_Zero()
print(_1611.minimumOneBitOperations(16))