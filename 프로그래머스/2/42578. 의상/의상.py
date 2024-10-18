import math
from collections import Counter

def solution(clothes):
    dic = {}
    for c in clothes:
        c_name = c[0]
        c_type = c[1]

        if c_type in dic:
            dic[c_type].append(c_name)
        else:
            dic[c_type] = [c_name]
    # if len(dic.keys()) < 2: 
    #     sum =-1
    # else:
    #     sum = 0
    sum = 1
    for v in dic.values():
        l = len(v)
        sum *= (math.comb(l, 0) + math.comb(l, 1))
    
    return sum - 1