def solution(numbers, k):
    answer = 0
    
    i = 1
    for _ in range(k-1):
        i += 2
    if i % len(numbers) == 0:
        return numbers[-1]
    return i % len(numbers)