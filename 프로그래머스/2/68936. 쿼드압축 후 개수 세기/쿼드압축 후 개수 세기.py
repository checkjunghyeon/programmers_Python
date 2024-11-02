def solution(arr):
    n = len(arr)
    count = []
    quadtree(n, arr, count)
    
    answer = [count.count(0), count.count(1)]
    
    return answer

def quadtree(n, arr, count):
    upperLeft, upperRight, lowerLeft, lowerRight = [], [], [], []
    half_n = n // 2
    
    if all(x == 0 for row in arr for x in row):
        count.append(0)
        return
    elif all(x == 1 for row in arr for x in row):
        count.append(1)
        return
    
    for u in arr[:half_n]:  
        upperLeft.append(u[:half_n])
        upperRight.append(u[half_n:])
    for l in arr[half_n:]:
        lowerLeft.append(l[:half_n])
        lowerRight.append(l[half_n:])
        
    quadtree(half_n, upperLeft, count)  # upperLeft
    quadtree(half_n, upperRight, count)  # upperRight
    quadtree(half_n, lowerLeft, count)  # lowerLeft
    quadtree(half_n, lowerRight, count)  # lowerRight
