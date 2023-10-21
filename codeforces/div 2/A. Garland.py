q = int(input())
for _ in range(q):
    ch = input()
    s = set(ch)
    if len(s) == 1:
        print(-1)
    elif len(s) > 2:
        print(4)
    else :
        if ch.count(ch[0]) == 2:
            print(4)
        else:
            print(6)