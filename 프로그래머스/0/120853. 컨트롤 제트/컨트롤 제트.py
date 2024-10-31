def solution(s):
    answer = 0
    s_list = s.split()
    for i, c in enumerate(s_list):
        if c == 'Z':
            answer -= int(s_list[i-1])
        else:
            answer += int(c)
    return answer