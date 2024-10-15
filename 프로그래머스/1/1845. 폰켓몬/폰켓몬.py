from itertools import combinations

def solution(nums):
    dict = {}
    l = len(nums)
    h = l // 2
    
    for i in range(l):
        dict[nums[i]] = i  # i : index of  nums
        
    if len(dict.keys()) >= h:
        return h
    else:
        return len(dict.keys())