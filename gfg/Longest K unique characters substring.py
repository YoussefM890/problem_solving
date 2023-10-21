from collections import defaultdict

def longestKSubstr(s, k):
    lt,rt = 0,1
    mx = 1
    d = defaultdict(int)
    d[s[lt]] = 1
    while rt < len(s) :
        while len(d) == k:
            if s[rt] in d :
                d[s[rt]]+=1
                rt+=1
                mx = max(mx, rt - lt)
                break
            else :
                d[s[lt]] -= 1
                if d[s[lt]] == 0: del d[s[lt]]
                lt+=1

        d[s[rt]] +=1
        rt+=1
        mx = max(mx,rt-lt)

    return mx

print(longestKSubstr("aabacbebebe",3))