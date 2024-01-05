# # 8:22
# # 25:
# res = 0
# while True :
#     s = input()
#     if not s : break
#     lt = s[10:39]
#     rt = s[42:]
#     # print(lt)
#     # print(rt)
#     ln = len(set(lt.split()).intersection(set(rt.split())))
#     res += 2**(ln-1) if ln else 0
# print(res)

def dp(index,value):
    res = value
    for i in range(index,index+value):
        res += dp(i+1,l[i])
    return res

n =  3
l = [2,1,0]
print(dp(0,n))
print(l)
n = 192
l = []
for i in range(n):
    s = input()
    lt = s[10:39]
    rt = s[42:]
    # print(lt)
    # print(rt)
    l.append(len(set(lt.split()).intersection(set(rt.split()))))
res = dp(0,n)
print(l)
print(res)