R = lambda: map(int, input().split())
L = lambda: list(R())
def calc(n,k):
    if k == 0 :
        return [-1]*n
    if k < n :
        return [-1]*(k-1) + [200] + [-400] + [-1]*(n-k-1)
    elif k == n :
        return [-1]*(k-1) + [200]
    else :
        return calc(n-1,k-n)  +[1000]

for _ in range(int(input())):
    n,k = R()
    print(*calc(n,k))
