import math

def solution(clothes):
    dic = {}
    for c in clothes:
        type = c[1]
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1

    sum = 1
    for l in dic.values():
        sum *= (math.comb(l, 0) + math.comb(l, 1))
    
    return sum - 1