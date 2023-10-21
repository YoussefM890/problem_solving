from collections import Counter

R = lambda: map(int, input().split())
L = lambda: list(R())

for _ in range(int(input())):
    n, = R()
    a = L()
    c = Counter(a)
    if c[0] > (n+1) // 2 :
        if c[0] == n : print(1)
        elif c[1]+c[0] == n: print(2)
        else : print(1)
    else : print(0)