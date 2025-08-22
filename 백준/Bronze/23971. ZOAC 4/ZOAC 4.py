# 입력: 행 개수 H, 열 개수 W, 세로 공백 N, 가로 공백 M
# 출력: 강의실 최대 수용 인원
# 조건
# 다른 모든 참가자와 세로줄 번호의 차 >= N 또는 가로줄 번호의 차 >= M 인 곳에만 앉기 O

H, W, N, M = map(int, input().split())

import math
print(math.ceil(H / (N+1)) * math.ceil(W / (M+1)))
