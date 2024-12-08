def solution(dirs):
    cur = [0, 0]
    history = []
    check_list = []
    
    for d in dirs:
        pre = cur.copy()
        # print(pre[0], pre[1])
        
        if d == "U" and pre[1] < 5:
            cur[1] += 1
        elif d == "D" and pre[1] > -5:
            cur[1] -= 1
        elif d == "R" and pre[0] < 5:
            cur[0] += 1
        elif d == "L" and pre[0] > -5:
            cur[0] -= 1
            
        if pre != cur and [pre[0], pre[1], cur[0], cur[1]] not in check_list:
            history.append([pre[0], pre[1], cur[0], cur[1]])
            check_list.append([pre[0], pre[1], cur[0], cur[1]])
            check_list.append([cur[0], cur[1], pre[0], pre[1]])
        
    # print(history)
    
    return len(history)