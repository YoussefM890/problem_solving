from collections import defaultdict

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    if n == 1:
        l= list(map(int, input().split()))
        print(0)
    else:
        s = 0
        d = [defaultdict(int) for i in range(m)]
        for i in range(n):
            l=list(map(int, input().split()))
            for j in l :
                d[m][j] += 1
        for i in range(n):
            keys = d[i].keys()
            for j in range(i,n):
                for k in range()
