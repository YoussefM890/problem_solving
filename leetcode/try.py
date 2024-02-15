from math import inf
import sys
from collections import defaultdict, Counter
from functools import reduce
from heapq import *
from itertools import *
arr = [1,2,3,4,5]
c = Counter(arr)
print(len(set(i for i in c.values())) == len(c))
