from collections import defaultdict

l = []
res = 0
id = -1
mapper = []
while True :
    s = input()
    if not s : break
    tmps,tmp = '',[]
    c = 0
    for i in range(len(s)) :
        if s[i].isdigit():
            tmps += s[i]

        else :
            if tmps :
                mapper.append(int(tmps))
                id += 1
                tmp += [id]*len(tmps)
                # print(tmp[-2], ',', id, ',',len(mapper), tmps)
                tmps = ''


            tmp += [s[i]]

    tmp += [tmps]*len(tmps)
    if tmps:
        mapper.append(int(tmps))
        id += 1
    # print(len(tmp),':',tmp)
    l.append(tmp)
# print(mapper)
directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
ii,jj = len(l),len(l[0])
for i in range(ii):
    for j in range(jj):
        # mapper = mapper.copy()
        if l[i][j] != '.' and not isinstance(l[i][j],int) :
            # print(i,j,l[i][j])
            for di,dj in directions :
                # print(mapper[l[i + di][j + dj]])
                # if i == 138 and j == 133 : print(l[i+di][j+dj])
                if 0 <= i+di < ii and 0 <= j+dj < jj and isinstance(l[i+di][j+dj],int) :
                    # addIndex = l[i+di][j+dj]
                    # add = mapper[addIndex]
                    res += mapper[l[i+di][j+dj]]
                    mapper[l[i+di][j+dj]] = 0
# print(mapper)
# for index,i in enumerate(l) :
#     print(i,index,len(i))
print(res)




