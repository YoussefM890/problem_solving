

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


# Example usage:
# source_range = [[79,92,-5]]
source_range = [[55,60,28]]
destination_range = [[56, 92, 4], [93, 96, -37]]
print(generate_all_ranges(source_range,destination_range))
# print(categorize_ranges( source_range,destination_range))
# print(categorize_ranges_list(source_range,destination_range))