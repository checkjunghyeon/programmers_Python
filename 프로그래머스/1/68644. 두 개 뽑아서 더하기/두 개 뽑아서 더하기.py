def solution(numbers):
    answer = []
    
    for x in range(len(numbers)):
        for y in range(x+1, len(numbers)):
            answer.append(numbers[x]+numbers[y])
    return sorted(set(answer))