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
