for _ in range(int(input())) :
    length = int(input())
    l = list(map(int,input().split()))
    p = [0]
    for i in l:
        p.append(p[-1] + i)
    ll ,rr = 1 ,length
    while ll < rr:
        mid =(ll + rr) // 2
        s = p[mid] - p[ll-1]
        r = list(range(ll, mid+1))
        x = int(input(f"? {len(r)} {' '.join(str(i) for i in r)}\n"))
        if x == s:
            ll = mid + 1
        else:
            rr = mid
    print("! "+str(ll))
