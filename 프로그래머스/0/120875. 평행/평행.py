from itertools import combinations
def solution(dots):
    for c in combinations(dots, 2):
        c2 = [i for i in dots if i not in c]
        if (c[0][1]-c[1][1])/(c[0][0]-c[1][0]) == (c2[0][1]-c2[1][1])/(c2[0][0]-c2[1][0]):
            return 1
    return 0
        