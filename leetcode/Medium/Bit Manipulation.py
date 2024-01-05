class Maximum_Xor_Product :
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 +7
        if n == 0 :
            return ((a^0) * (b^0)) % MOD
        a = bin(a)[2:]
        b = bin(b)[2:]
        mxlen = max(len(a),len(b))
        mx = max(mxlen,n)
        a = f"{a:0>{mx}}"
        b = f"{b:0>{mx}}"
        resA = ''
        resB = ''
        if n < mxlen :
            resA = a[:mx - n]
            resB = b[:mx - n]
            if resA != resB :
                incA = resB > resA
                for i in range(mx-n,mx):
                    if a[i] == b[i] :
                        resA += '1'
                        resB += '1'
                    elif incA :
                        resA += '1'
                        resB += '0'
                    else :
                        resA += '0'
                        resB += '1'
                return (int(resA,2) * int(resB,2))% MOD

        incA = True
        for i in range(mx-n,mx):
            if a[i] == b[i]:
                resA += '1'
                resB += '1'
            elif incA:
                resA += '1'
                resB += '0'
                incA = False
            else :
                resA += '0'
                resB += '1'
        return (int(resA,2) * int(resB,2))% MOD
_2939 = Maximum_Xor_Product()
# print(_2939.maximumXorProduct(53446911838892,712958946092406,6))
# print(_2939.maximumXorProduct(12,5,4))
# print(_2939.maximumXorProduct(13,10,2))
print(_2939.maximumXorProduct(4,6,2))