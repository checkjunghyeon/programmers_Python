def solution(n, left, right):
    arr= [0] * (right-left+1)

    for k in range(right-left+1):
        i = (left + k) // n
        j = (left + k) % n

        arr[k] = max(i, j) + 1
    
    return arr