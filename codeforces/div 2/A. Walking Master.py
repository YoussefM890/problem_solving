R = lambda: map(int, input().split())
L = lambda: list(R())

for _ in range(int(input())):
    a, b, c, d = R()
    if b > d or c - a > d - b:
        print(-1)
    else:
        y = d - b
        print(2 * y - c + a)