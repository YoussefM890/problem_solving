import string
from collections import defaultdict, deque

input_file = "consistency_chapter_2_input.txt"  # Define the input file name
input_file = "correct_output_88.txt"  # Define the input file name
output_file = "consistency_chapter_2"

with open(input_file, 'r') as infile:
    lines = infile.readlines()
    pos = 0
    T = int(lines[pos].strip())
    pos += 1

    with open(f"{output_file}_output.txt", 'w') as outfile:
        for _ in range(T):
            s = lines[pos].strip()
            pos += 1
            d = defaultdict(list)
            k = int(lines[pos].strip())
            pos += 1
            for __ in range(k):
                cur = lines[pos].strip()
                pos += 1
                d[cur[1]].append(cur[0])
            res = 2700
            for letter in string.ascii_uppercase:
                distance = {i: 2700 for i in string.ascii_uppercase}
                distance[letter] = 0
                visited = set()
                l = deque(letter)
                while l:
                    cur = l.popleft()
                    visited.add(cur)
                    for i in d[cur]:
                        if i in visited:
                            continue
                        l.append(i)
                        distance[i] = distance[cur] + 1
                cur = 0
                for j in s:
                    cur += distance[j]
                res = min(cur, res)
            output_line = f"Case #{_+1}: {res if res != 2700 else -1}\n"
            outfile.write(output_line)  # Write the output to the file
