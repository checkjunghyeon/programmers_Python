def solution(s):
    answer = 0
    for i in range(len(s)):
        rotate = s[i+1:] + s[0:i+1]
        if isRight(rotate):
            answer += 1
    return answer


def isRight(s):
    stack_1, stack_2, stack_3 = [], [], []
    flag = []
        
    for c in s:
        if c == "(":
            flag.append(0)
            stack_1.append(c)
        elif c == ")":
            if not stack_1:
                return False
            else:
                if flag.pop() == 0:
                    stack_1.pop()
                
        if c == "{":
            flag.append(1)
            stack_2.append(c)
        elif c == "}":
            if not stack_2:
                return False
            else:
                if flag.pop() == 1:
                    stack_2.pop()
                
        if c == "[":
            flag.append(2)
            stack_3.append(c)
        elif c == "]":
            if not stack_3:
                return False
            else:
                if flag.pop() == 2:
                    stack_3.pop()
                
    if stack_1 or stack_2 or stack_3:
        return False
    else:
        return True