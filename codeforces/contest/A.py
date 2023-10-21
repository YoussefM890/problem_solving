R = lambda: map(int, input().split())
L = lambda: list(R())

for _ in range(int(input())):
    l,r = input().split()
    if len(l) == len(r):
        c = 0
        minn = 9
        for i in range(len(l)):
            if l[i] == r[i]:
                minn = min(minn, int(l[i]))
                c+=1
            else : break
        if len(l) - c >= 3 :
            print(f'{l[:c+1]}{r[c+1]}09{l[c+2:]}')
        elif len(l) - c == 2 :
            left = f'{l[:c+1]}'
            if 9 - (int(l[c+1])  > int(r[c+1]) - minn :
                right = f'{l[c+1]}9'


