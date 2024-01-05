ln = int(input())
l = [int(input()) for i in range(ln)]
for i in range(1 << ln):
    tmp = 0
    for msk in range(ln):
        if 1 << msk & i :
            tmp += l[msk]
        else :
            tmp -= l[msk]
    if tmp % 360 == 0 :
        print('YES')
        break
else:
    print('NO')

