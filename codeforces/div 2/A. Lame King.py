for _ in range(int(input())):
    r,c = map(int,input().split())
    r = abs(r)
    c = abs(c)
    print(r+c+ (abs(r-c)-1 if abs(r-c)!=0 else 0))