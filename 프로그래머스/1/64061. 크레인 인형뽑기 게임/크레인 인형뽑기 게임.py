def solution(board, moves):
    answer = 0
    stack = []
    pop_stack = []

    for i in range(len(board)):  # col
        tmp = []
        for j in range(len(board)-1, -1, -1):  # row
            if board[j][i] != 0:
                tmp.append(board[j][i])
        stack.append(tmp)

    for m in moves:
        column = stack[m - 1]
        if not column:
            continue

        doll = column.pop()
        
        if not pop_stack or pop_stack[-1] != doll:
            pop_stack.append(doll)
        else:
            pop_stack.pop()
            answer += 2

    return answer
