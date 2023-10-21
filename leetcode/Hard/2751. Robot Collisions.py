def f(positions,healths,directions):
    l = []
    for i in range(len(positions)):
        l.append([positions[i], healths[i], directions[i],i])
    l.sort()
    res = [0] * len(positions)
    stack = []
    for i in l:
        if i[2] == "R":
            stack.append(i)
        else:
            while stack:
                cur = stack.pop()
                if i[1] > cur[1]:
                    i[1] -= 1

                elif i[1] == cur[1]:
                    break
                else:
                    cur[1] -= 1
                    stack.append(cur)
                    break
            else :
                res[i[-1]] = i[1]
    for i in stack :
        res[i[-1]] = i[1]
    return [i for i in res if i!=0]
# [5, 4, 3, 2, 1],[2,17,9,15,10],"RRRRR"
# [3, 5, 2, 6],[10, 10, 15, 12],"RLRL"
# [1,2,5,6],[10,10,11,11],"RLRL"
print(f(  [1,2,5,6],[10,10,11,11],"RLRL"  ))
