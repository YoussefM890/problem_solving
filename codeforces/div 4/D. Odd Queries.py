n = int(input())
for i in range(n):
    length, q = map(int, input().split())
    l = list(map(int, input().split()))
    p = [0]
    for j in range(length):
        p.append(p[- 1] + l[j])
    for j in range(q):
        l, r, k = map(int, input().split())
        total = p[-1] - p[r] + p[l - 1] + (r - l + 1) * k
        print("NO" if total % 2 == 0 else "YES")
