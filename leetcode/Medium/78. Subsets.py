from typing import List


class Solution:
    def subsets(self, l: List[int]) -> List[List[int]]:
        out=[]
        n = len(l)
        for i in range(1 << n):
            tmp = []
            for j in range(len(l)) :
                if 1 << j & i : tmp.append(l[j])
            out.append(tmp)
        return out


def test_empty_list(self):
    s = Solution()
    assert s.subsets([]) == []

def test_single_element_list(self):
    s = Solution()
    assert s.subsets([1]) == [[], [1]]

test_empty_list()