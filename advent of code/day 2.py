# res = 0
# id = 1
# while True :
#     s = input()[6+len(str(id)):]
#     print(s)
#     if s == '' : break
#     i = 0
#     while i < len(s):
#         if s[i].isdigit() and s[i+1].isdigit() :
#             if int(s[i:i+2]) > 14 :
#                 break
#             elif int(s[i:i+2]) > 13 and s[i+3:i+7] != "blue" :
#                 break
#             elif int(s[i:i+2]) > 12 and s[i+3:i+6] == "red" :
#                 break
#         i+=1
#     else :
#         # print(id)
#         res+= id
#     id+=1
# print(res)
import math
import re
res = 0
id = 1
while True :
    l = re.split(r'[,;:]',input())[1:]
    if not l : break
    red = green = blue = 0
    for i in l :
        if i.endswith('red') : red = max(red,int(i[:-3]))
        elif i.endswith('green') : green = max(green,int(i[:-5]))
        elif i.endswith('blue') : blue = max(blue,int(i[:-4]))
    res+= red*green*blue
    # print(l)
print(res)