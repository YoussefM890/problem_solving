import bisect
def decodeAtIndex(s: str, k: int) -> str:
    integers_set = {'0','1','2','3','4','5','6','7','8','9'}
    length_list = [0]
    strings_list = []
    temp_string = ""
    temp = 0
    for i in s :
        if i in integers_set :
            length_list += [temp,temp*int(i)]
            temp = length_list[-1]
            strings_list.append(temp_string)
            temp_string = ""
        else :
            temp += 1
            temp_string += i
    print(length_list)
    print(strings_list)
    def find_k(k) :
        print("k = ",k)
        ind = bisect.bisect_right(length_list,k) -1
        if ind % 2 == 0 :
            return strings_list[ind//2][k-length_list[ind]]
        else :
            return find_k(k % length_list[ind])
    return find_k(k-1)
print(decodeAtIndex("abc1",1))

class Separate_Black_and_White_Balls :
    def minimumSteps(self, s: str) -> int:
        ones = 0
        res = 0
        for i in s :
            if i == '1' :
                ones+=1
            else :
               res+=ones
        return res
_2938 = Separate_Black_and_White_Balls()
print(_2938.minimumSteps("0111"))
