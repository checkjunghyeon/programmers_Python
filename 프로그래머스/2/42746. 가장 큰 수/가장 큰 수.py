def solution(numbers):
    if set(numbers) == {0}:
        return "0"
    
    sorted_num = sorted(numbers, key=lambda x: str(x)*6, reverse=True)
    answer = "".join(str(i) for i in sorted_num)
    
    return answer