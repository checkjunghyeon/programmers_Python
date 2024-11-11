import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True

def divideWithPrime(numbers):
    common_divisor = []
    remaining_numbers = numbers[:]
    
    for x in range(2, max(numbers)+1):
        if isPrime(x) == True:
            for i, n in enumerate(numbers):
                while sum(n % x == 0 for n in remaining_numbers) >= 2:
                    common_divisor.append(x)
                    remaining_numbers = [n // x if n % x == 0 else n for n in remaining_numbers]

    common_divisor += [n for n in remaining_numbers if n > 1]
    print(common_divisor)
    return common_divisor

def solution(arr):
    cd = divideWithPrime(arr)

    answer = 1
    for i in cd:
        answer *= i
    
    return answer