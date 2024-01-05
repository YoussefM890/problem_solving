class Eliminate_Maximum_Number_of_Monsters:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        length = len(speed)
        l = sorted([(dist[i] - 1) // speed[i] for i in range(length)])
        i,j = 0 ,length -1
        while i < j :
            mid = (i+j)//2
            if mid <= l[mid] :
                i = mid +1
            else :
                j = mid
        if i == length and l[-1] >= length-1 : return length
        return i

eliminate_maximum_number_of_monsters = Eliminate_Maximum_Number_of_Monsters()
print(eliminate_maximum_number_of_monsters.eliminateMaximum(
[5,4,3,3,3]
    ,
[1,1,5,3,1]
))

class Sort_Vowels_In_A_String :
    def sortVowels(self, s: str) -> str :
        vowels = {'a', 'e', 'i', 'u', 'o'}
        c = Counter([i for i in s if i.lower() in vowels])
        generated_vowels = (vowel for vowel in sorted(c.keys()) for _ in range(c[vowel]))
        replaced_string = ''.join(next(generated_vowels) if char.lower() in vowels else char for char in s)
        return replaced_string

sort_vowels_in_a_string = Sort_Vowels_In_A_String()
print(sort_vowels_in_a_string.sortVowels(
"lEetcOde"
))
class Diagonal_Traverse_II :
    def findDiagonalOrder(self, l: List[List[int]]):
        res = []
        length = len(l)
        for indexI,i in  enumerate(l) :
            for indexJ,j in  enumerate(i) :
                res.append([length * (indexI + indexJ) - indexI,j])
        return list(map(lambda  x : x[1],sorted(res , key= lambda x : x[0])))

_1424 = Diagonal_Traverse_II()
print(_1424.findDiagonalOrder(
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
))