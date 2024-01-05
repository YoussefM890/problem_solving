class Make_Three_Strings_Equal :
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] == s2[0] == s3[0] :
            ops=0
            mn = min(len(s1),len(s2),len(s3))
            for i in range(1,mn):
                if s1[i] == s2[i] == s3[i] :
                    continue
                else :
                    ops += len(s1) - i + len(s2) - i + len(s3) - i
                    break
            else :
                ops += len(s1) - mn + len(s2) - mn + len(s3) - mn
            return ops
        else :
            return -1
_2937 = Make_Three_Strings_Equal()
print(_2937.findMinimumOperations(
'a'
,
    'aabc'
    ,
    'a'
))
