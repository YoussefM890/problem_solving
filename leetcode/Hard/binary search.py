from bisect import bisect, bisect_left
from typing import List


class Number_Of_Flowers_In_Full_Bloom:
    def fullBloomFlowers(self, f: List[List[int]], p: List[int]) -> List[int]:
        first = sorted(map(lambda x : x[0],f))
        second = sorted(map(lambda x:x[1],f))
        res = []
        for i in p :
            left = bisect.bisect_right(first,i)
            right = bisect.bisect_left(second,i)
            res.append(left - right)
            print(i,left,right)
        return res


number_of_flowers_in_full_bloom = Number_Of_Flowers_In_Full_Bloom()
# print(number_of_flowers_in_full_bloom.fullBloomFlowers(
#     [[19, 37], [19, 38], [19, 35]]
#     ,
#     [6, 7, 21, 1, 13, 37, 5, 37, 46, 43]
#     ))
print(number_of_flowers_in_full_bloom.fullBloomFlowers(
    [[1,6],[3,7],[9,12],[4,13]]
    ,
    [2,3,7,11]
    ))

class MountainArray:
    def __init__(self, array):
        self.array = array

    def get(self, index: int) -> int:
        return self.array[index]

    def length(self) -> int:
        return len(self.array)


class Find_In_Mountain_Array:
    def findInMountainArray(self, target: int, arr:'MountainArray') -> int:
        def bs_left(lt, rt, target):
            while lt <= rt:
                mid = (lt + rt) // 2
                mid_value = arr.get(mid)
                if mid_value == target:
                    return (True, mid)
                elif mid_value < target:
                    lt = mid + 1
                else:
                    rt = mid - 1
            return (True, mid) if mid_value == target else (False, mid)
        def bs_right(lt,rt,target) :
            while lt <= rt:
                mid = (lt + rt) // 2
                mid_value = arr.get(mid)
                if mid_value == target:
                    return (True, mid)
                elif mid_value < target:
                    rt = mid - 1
                else:
                    lt = mid + 1
            return (True, mid) if mid_value == target else (False, mid)
        mountain = 0
        length = arr.length()
        # find the mountain index
        lt, rt = 0, length - 1
        while lt < rt:
            mid = (lt + rt) // 2
            mid_value = arr.get(mid)
            after_mid = arr.get(mid + 1)
            if mid_value > after_mid:
                rt = mid
            else:
                lt = mid + 1
        peak = lt
        # print(lt, arr.get(lt))
        res, ind = bs_left(0, peak, target)
        if res: return ind
        res, ind = bs_right(peak + 1, length - 1, target)
        return ind if res else -1


mountain_array = MountainArray([0,5,3,1])
find_in_mountain_array = Find_In_Mountain_Array()
print(find_in_mountain_array.findInMountainArray(1, mountain_array))

class Find_Median_from_Data_Stream :
    def __init__(self):
        self.l = []
        self.median = 0
    def addNum(self, num: int) -> None:
        x = bisect_left(self.l,num)
        self.l.insert(x,num) # this should be optimized

    def findMedian(self) -> float:
        mid = len(self.l) // 2
        if mid == 0 : return self.l[0]
        if len(self.l) % 2 :return self.l[mid]
        return (self.l[mid] + self.l[mid - 1]) / 2

_295 = Find_Median_from_Data_Stream()
_295.addNum(1)
print(_295.l)
print(_295.findMedian())
_295.addNum(2)
print(_295.l)
print(_295.findMedian())
_295.addNum(3)
print(_295.l)
print(_295.findMedian())
