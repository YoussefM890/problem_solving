class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ind = 0
        pos = [0, 0]
        for _ in range(4):
            for i in instructions:
                if i == 'R':
                    ind = (ind + 1) % 4
                elif i == 'L':
                    ind = (ind - 1) % 4
                else:
                    pos = [pos[0] + directions[ind][0], pos[1] + directions[ind][1]]

            if pos == [0, 0]:
                return True

        return False

class Count_Number_of_Homogenous_Substrings :
    def countHomogenous(self, s: str) -> int:
        res,c,prev = 0,0,s[0]
        for i in s :
            if i == prev :
                c += 1
            else :
                res += (c / 2 ) * (c+1)
                c = 1
                prev = i
        res += (c / 2 ) * (c+1)
        return int(res)

count_number_of_homogenous_substrings = Count_Number_of_Homogenous_Substrings()
print(count_number_of_homogenous_substrings.countHomogenous(
    "abbcccaa"
))