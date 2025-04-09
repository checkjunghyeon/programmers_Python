'''
문제)
<그림 1>과 같이 정사각형 모양의 지도가 있다. 
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. 
지도를 입력하여 단지수를 출력하고, 
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력)
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
ex) 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
 
출력)
첫 번째 줄에는 총 단지수를 출력하시오. 
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
ex) 
3
7
8
9
'''

from collections import deque

# 입력 처리
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

def BFS(G, x, y):
    ''' BFS 구현 '''
    queue = deque()    
    queue.append((x, y))
    visited[x][y] = True 
    
    count = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and G[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count+1    # 한 영역 당 단지 개수 반환

area = []
visited = [[False] * N for _ in range(N)]
# 시작점에 따라 BFS 반복 실행
for row in range(N):
    for col in range(N):
        if graph[row][col] == 1 and not visited[row][col]:
            area.append(BFS(graph, row, col))
            
print(len(area))
for a in sorted(area):
    print(a)
