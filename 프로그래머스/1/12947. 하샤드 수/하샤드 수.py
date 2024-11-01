def solution(x):
    s = sum([int(i) for i in list(str(x))])
    if x % s == 0:
        return True

    return False