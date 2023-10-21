n = int(input())
l = list(map(int,input().split()))
ones = l.count(100)
if ones % 2 == 1 :
    print("NO")
elif ones == 0:
    twos = l.count(200)
    if twos % 2 == 1:
        print("NO")
    else:
        print("YES")
else :
    print("YES")