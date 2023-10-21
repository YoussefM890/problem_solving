q = int(input())
for _ in range(q):
    even = set()
    odd = set()
    length = int(input())
    ch = input()
    for i in range(len(ch)):
        if i % 2 == 0:
            if ch[i] in odd:
                print("No")
                break
            even.add(ch[i])
        else:
            if ch[i] in even:
                print("No")
                break
            odd.add(ch[i])
    else:
        print("Yes")