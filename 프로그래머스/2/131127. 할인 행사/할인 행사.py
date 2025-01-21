from collections import Counter
def solution(want, number, discount):
    answer = 0
    days = len(discount) - 9
    
    wlist = {}
    for w, n in zip(want, number):
        wlist[w] = n

    for i in range(days):
        if wlist == Counter(discount[i:i + 10]):
            answer += 1
            
    return answer