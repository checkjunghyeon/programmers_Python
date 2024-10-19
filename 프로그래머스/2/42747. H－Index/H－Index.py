import copy

def solution(citations):
    n = 0
    h = max(citations)

    while True:
        if n >= h:
            break
        h -= 1
        n = len([c for c in citations if c >= h])

    return h