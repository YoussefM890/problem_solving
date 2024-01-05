# res = 0
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# while True :
#     s = input()
#     if not s: break
#     s = s.strip(alphabet).rstrip(alphabet)
#     res+=int(s[0]+s[-1])
#
#
# print(res)
res = 0
word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
while True :
    s = input()
    if not s: break
    first = last = ''
    i = 0
    while not (first and last) :
        if not first :
            if s[i].isdigit():
                first = s[i]
            else :
                for j in word_to_digit :
                    if s[i:].startswith(j) :
                        first = word_to_digit[j]
        if not last :
            if s[~i].isdigit():
                last = s[~i]
            else:
                for j in word_to_digit :
                    if s[~i:].startswith(j) :
                        last = word_to_digit[j]
        i+=1
    print(first,last)
    res += int(first+last)


print(res)
