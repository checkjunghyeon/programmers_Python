from collections import Counter

def solution(participant, completion):
    dic_p = Counter(participant)
    dic_c = Counter(completion)
    dic = dic_p-dic_c

    return list(dic.keys())[0]