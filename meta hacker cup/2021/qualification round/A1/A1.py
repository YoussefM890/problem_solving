from collections import defaultdict

for _ in range(int(input())):
    vowels = {"A", "E", "I", "O","U"}
    v = c = 0
    s = input()
    letters = defaultdict(int)
    score = 2 * len(s)
    for i in s:
        if i in vowels:
            v += 1
        else:
            c += 1
        letters[i] += 1
    if c * v == 0: score = len(s)
    for i in s:
        if i in vowels:
            score = min(score, (v - letters[i]) * 2 + c)
        else:
            score = min(score, (c - letters[i]) * 2 + v)
    print(f"Case #{_ +1}: {score}")
