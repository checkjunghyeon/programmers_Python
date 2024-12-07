def solution(answers):  
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0, 0, 0]
    for i, a in enumerate(answers):
        if a == ans1[i%len(ans1)]:
            cnt[0] += 1
        if a == ans2[i%len(ans2)]:
            cnt[1] += 1
        if a == ans3[i%len(ans3)]:
            cnt[2] += 1
            
    m = max(cnt)
    answer = [i + 1 for i, v in enumerate(cnt) if v == m]
    
    return answer