N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [0] * 7  # 인덱스 0번째는 사용 X

# 주사위 이동 규칙 정의
def roll(dice, dir):
    top, east, west, north, south, bottom = 1, 3, 4, 2, 5, 6
    new = dice[:]
    if dir == 1:
        new[top], new[bottom], new[east], new[west] = dice[west], dice[east], dice[top], dice[bottom]
    elif dir == 2:
        new[top], new[bottom], new[east], new[west] = dice[east], dice[west], dice[bottom], dice[top]
    elif dir == 3:
        new[top], new[bottom], new[north], new[south] = dice[south], dice[north], dice[top], dice[bottom]
    elif dir == 4:
        new[top], new[bottom], new[north], new[south] = dice[north], dice[south], dice[bottom], dice[top]
    return new

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for cmd in commands:
    # 이동 가능성 확인
    nx, ny = x + dx[cmd - 1], y + dy[cmd - 1]
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    # 이동 지점
    x, y = nx, ny
    # 주사위 굴리기
    dice = roll(dice, cmd)

    # 이동 지점 값이 0이라면
    if board[x][y] == 0:
        board[x][y] = dice[6]  # 아랫면 복사
    # 이동 지점 값이 0이 아니라면
    else:
        dice[6] = board[x][y]  # 칸 값을 주사위에 복사
        board[x][y] = 0        # 칸 값은 0으로 초기화

    print(dice[1]) # 주사위 윗면 출력