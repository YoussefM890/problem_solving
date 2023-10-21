from bisect import bisect_left
l = [3,5]
n = len(l)
l.sort()
lt, rt = 1, l[-1]
while lt <= rt:
    mid = (lt + rt) // 2
    x = bisect_left(l, mid)
    print(x, mid)
    if n - x == mid:
        print(mid)
        break
    if n - x < mid:
        rt = mid - 1
    else:
        lt = mid + 1
print(-1)