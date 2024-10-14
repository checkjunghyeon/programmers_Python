def solution(babbling):
    cnt = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for babble in babbling:
        tmp = babble
        for word in words:
            tmp = tmp.replace(word, " ")
        
        if tmp.strip() == "":
            cnt += 1
    
    return cnt