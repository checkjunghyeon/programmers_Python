import math

def solution(clothes):
    dic = {}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]].append(c[0])
        else:
            dic[c[1]] = [c[0]]

    sum = 1
    for v in dic.values():
        l = len(v)
        sum *= (math.comb(l, 0) + math.comb(l, 1))
    
    return sum - 1