def solution(s):
    n = len(s)
    if n == 1:
        return 1
    
    
    ans = n
    for k in range(1, n//2 + 1):
        pre = s[:k] # [0,k] 구간
        cnt = 1
        result = []
        
        # 초반 k까지를 제외한 나머지 구간, k만큼 step
        for i in range(k, n, k):
            cur = s[i:i+k]  # k만큼 자른 문자열 구간
            if cur == pre:  # 이전과 비교해서 중복되면
                cnt += 1    # 카운팅
            else:           # 이전과 중복되지 않는다면
                result.append((str(cnt) if cnt > 1 else "") + pre)  # 1이상인 경우에 앞에 카운팅 숫자 추가
                pre = cur   # 이전(비교대상) 갱신
                cnt = 1     # 카운트 초기화
        
        # 마지막 남은 이전(비교대상) 추가
        result.append((str(cnt) if cnt > 1 else "") + pre)
        ans = min(ans, len("".join(result)))
        
    return ans