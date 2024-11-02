def solution(n):
    a = hanoi_tower(n, 1, 3)
    return a

def hanoi_tower(n, start, end, a=[]):
    if n == 1 :
        a.append([start, end])
        return
       
    hanoi_tower(n-1, start, 6-start-end)     
    a.append([start, end])
    hanoi_tower(n-1, 6-start-end, end)
    
    return a