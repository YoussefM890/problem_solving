class Kth_Symbole_In_Grammar:
    def kthGrammar(self, n: int, k: int) -> int:
        lt ,rt  = 1, 2**(n-1)
        res = 0
        for i in range(n-1) :
            mid = (lt + rt) // 2
            if k <= mid :
                rt = mid
            else :
                res = 1-res
                lt = mid+1
        return res