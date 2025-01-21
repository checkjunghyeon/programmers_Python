from collections import Counter
def solution(want, number, discount):
    answer = 0
    days = len(discount) - 9
    
    wlist = {}
    for w, n in zip(want, number):
        wlist[w] = n

    for i in range(days):
        flag = []
        counts = Counter(discount[i:i + 10])
        
        for k, v in counts.items():
            if k in wlist.keys():
                if v == wlist[k]:
                    flag.append(True)
                else:
                    flag.append(False)
            else:
                 flag.append(False)   

        if all(flag) == True:
            answer += 1
            
    return answer