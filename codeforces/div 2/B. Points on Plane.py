for _ in range(int(input())) :
    x = int(input())
    if x == 1:
        print(0)
    else :
        ll,rr = 1,10**9
        while ll < rr:
            mid = (ll + rr) // 2
            if x < mid**2:
                rr = mid
            elif x > mid**2:
                ll = mid + 1
            else :
                ll = mid
                break
        print(ll-1)

