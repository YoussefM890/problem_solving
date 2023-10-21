l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lt,rt,t,b = 0 , len(l[0])-1, 0, len(l)
out = []
while lt <= rt and t <= b:
    for i in range(lt,rt):
        out.append(l[t][i])
    t += 1
    for i in range(t,b):
        out.append(l[i][rt-1])
    rt -= 1
    if not (lt < rt and t < b):
        break

    for i in range(rt-1,lt-1,-1):
        out.append(l[b-1][i])
    b -= 1
    for i in range(b-1,t-1,-1):
        out.append(l[i][lt])
    lt += 1