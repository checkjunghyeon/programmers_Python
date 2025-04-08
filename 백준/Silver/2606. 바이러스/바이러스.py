'''
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 
컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
4
'''

from collections import deque

num = int(input())
edge = int(input())
graph = {}

for _ in range(edge):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = []
    if n2 not in graph:
        graph[n2] = []

    graph[n1].append(n2)
    graph[n2].append(n1)
        
def bfs(graph, start):
    queue, visited = deque(), []
    queue.append(start)
    
    while queue:
        current = queue.popleft()
        
        if current not in visited:
            visited.append(current)
            queue.extend(graph.get(current, [])) # 불완전연결그래프 고려
    return visited

print(len(bfs(graph, 1)) - 1)  # ← 1번 자신 제외
    