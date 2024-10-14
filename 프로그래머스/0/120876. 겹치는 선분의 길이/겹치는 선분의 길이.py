def solution(lines):
    line_map = [0] * 201

    for line in lines:
        start, end = line
        for i in range(start + 100, end + 100):
            line_map[i] += 1

    overlap_length = sum(1 for count in line_map if count > 1)
    
    return overlap_length
