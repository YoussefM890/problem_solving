class Number_of_Ways_to_Dividea_Long_Corridor :
    def numberOfWays(self, s: str) -> int :
        start = s.find('S')
        end = s.rfind('S')
        c = 0
        p = last = res = 1
        for i in range(start,end+1) :
            if s[i] == 'S' :
                c += 1
            elif c%2 == 0:
                if c//2 == last :
                    p += 1
                else :
                    last = c//2
                    res *= p
                    p = 2

        return res*p if c != 0 and c%2 == 0 else 0