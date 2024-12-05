from itertools import combinations
from collections import Counter

def solution(k, tangerine):
    cnt_list = sorted(list(Counter(tangerine).values()), reverse=True)
    length = k

    for i in range(length):
        k -= cnt_list[i]
        if k <= 0:
            return i + 1