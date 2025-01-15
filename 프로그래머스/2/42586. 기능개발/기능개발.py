import math
def solution(progresses, speeds):
    answer = []        
    n = len(progresses)
    # 각 기능마다의 배포 가능일()
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    print(days_left)
    cnt = 0
    max_day = days_left[0]
    
    for i in range(n):
        # 배포 가능일이 가장 늦은 배포일보다 빠르면(맨 앞 친구와 같이 배포 가능하면)
        if days_left[i] <= max_day:
            cnt += 1
        # 배포 가능일이 기준 배포일보다 느리면(맨 앞 친구보다 늦게 배포해야 한다면)
        else:
            answer.append(cnt)
            cnt = 1
            max_day = days_left[i]
    answer.append(cnt)

    return answer