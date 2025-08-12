def solution(s):
    result = []
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)+1):
        comp = ""
        pre = s[:i]
        cnt = 1
        
        for j in range(i, len(s)+i, i):              
            if pre == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    comp += (str(cnt) + pre)
                else:
                    comp += pre
                    
                pre = s[j:i+j]
                cnt = 1
        result.append(len(comp))
        
    return min(result)