import math

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
count = 0

arr = [[0]]

# 해당 좌표가 배열 밖인지 판단하는 함수
def check_in_or_out(x, y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

# 모래 이동하기
# 나선형 이동 방향에 따라 모래가 퍼지는 방향이 변경됨
# 1%, 1%, 2%, 2%, 7%, 7%, 10%, 10%, 5%, alpha 순서

# 서, 남, 동, 북 순서
patterns = [
    # 서
    [(-1, 1, 0.01), (1, 1, 0.01), (-2, 0, 0.02), (2, 0, 0.02),
     (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1),
     (0, -2, 0.05), (0, -1, 0)],
    # 남
    [(-1, -1, 0.01), (-1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02),
     (0, -1, 0.07), (0, 1, 0.07), (1, -1, 0.1), (1, 1, 0.1),
     (2, 0, 0.05), (1, 0, 0)],
    # 동
    [(-1, -1, 0.01), (1, -1, 0.01), (-2, 0, 0.02), (2, 0, 0.02),
     (-1, 0, 0.07), (1, 0, 0.07), (-1, 1, 0.1), (1, 1, 0.1),
     (0, 2, 0.05), (0, 1, 0)],
    # 북
    [(1, -1, 0.01), (1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02),
     (0, -1, 0.07), (0, 1, 0.07), (-1, -1, 0.1), (-1, 1, 0.1),
     (-2, 0, 0.05), (-1, 0, 0)]
]


def push_sand(x, y, d, A):
    global count
    sand = A[x][y]
    alpha = sand
    pattern = patterns[d]
    
    for dx, dy, ratio in pattern[:-1]:  # 마지막은 alpha이므로 제외
        nx, ny = x + dx, y + dy
        amount = math.floor(sand * ratio)
        if check_in_or_out(nx, ny):
            count += amount
        else:
            A[nx][ny] += amount
        alpha -= amount

    # alpha 위치 따로 처리
    ax, ay, _ = pattern[-1]
    ax += x
    ay += y
    if check_in_or_out(ax, ay):
        count += alpha
    else:
        A[ax][ay] += alpha

    A[x][y] = 0

# 나선형으로 좌표 이동하기
def tornado(A):
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]    # 서-남-동-북
    y = len(A) // 2
    x = len(A) // 2
    
    dist = 1        # 한 방향으로 이동할 칸의 개수
    d_idx = 0       # 방향 인덱스
    move_count = 0  # 한 방향으로 끝까지 이동 시 1 증가
    
    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            Y = y + dy
            X = x + dx
            if (Y, X) == (0, -1):    # 배열 바깥에 도달한 경우
                return 
            push_sand(Y, X, d_idx, A)
            y, x = Y, X
        move_count += 1          # 한 방향으로 이동 완료 후 1 증가
        d_idx = (d_idx+1) % 4    # 반시계 90도 방향 회전
        if move_count == 2:
            dist += 1
            move_count = 0
            
tornado(A)
print(count)
