import math
from collections import defaultdict

# empty_lines = 0
# mapper_number = -1
# mapper = defaultdict(list)
# res = math.inf
# while True :
#     s = input()
#     if not s :
#         empty_lines += 1
#         if empty_lines == 8 :
#             break
#         continue
#     if not s[0].isdigit() :
#         mapper_number += 1
#         if mapper_number == 0 : seed = list(map(int,s[7:].split()))
#     else :
#         l = list(map(int, s.split()))
#         l = [l[1],l[1]+l[2]-1,l[0]-l[1]]
#         mapper[mapper_number].append(l)
# for i in seed :
#     number = i
#     id = 1
#     while id < 8 :
#         for j in mapper[id]:
#             if j[0] <= number <= j[1] :
#                 number += j[2]
#                 break
#         id += 1
#     res = min(res,number)
# print(res)

def categorize_ranges(source, destination):
    result = []
    if source[1] >= destination[0] and source[0] <= destination[1]:
        # Type 1: Overlapping Ranges
        overlap = [max(source[0], destination[0]), min(source[1], destination[1]), source[2] + destination[2]]
        result.append(overlap)
        return result
    else:
        return []

def fill_gaps_in_range(range, ranges):
    a,b,c = range
    # Sort the ranges based on their start points
    ranges.sort(key=lambda x: x[0])
    res = ranges.copy()
    current_start = a

    for start, end ,_ in ranges:
        if current_start < start:
            res.append([current_start, start-1,c])
        current_start = end+1

    if current_start < b:
        res.append([current_start, b,c])

    return res

def generate_all_ranges(sources,destinations):
    result = []
    for source in sources:
        tmp = []
        for destination in destinations:
            tmp.extend(categorize_ranges(source, destination))
        tmp = fill_gaps_in_range(source, tmp)
        result.extend(tmp)
    return result


def solve():
    seeds = []
    convert = defaultdict(list)
    with open("a.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue

            if line.startswith("seeds: "):
                line = line.split(': ')
                line = list(map(int,line[1].split()))
                for i in range(0,len(line),2):
                    seeds.append([line[i],line[i]+line[i+1]-1,0])
                continue

            if line.endswith(" map:"):
                src, _, dest = line.split()[0].split('-')
            else:
                a, b, c = line.split()
                convert[src].append((int(b), int(c)+int(b)-1, int(a)-int(b), dest))
    print(convert)
    print(seeds)

    for i in convert :
        res = generate_all_ranges(seeds,convert[i])
        if res : seeds = res

        print(seeds)
#
    ans = math.inf
    for i in res :
        ans = min(ans,i[0]+i[2])
    print(ans)

if __name__ == "__main__":
    print(solve())