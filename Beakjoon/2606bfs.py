from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n+1)
count = 0

def bfs(a):
    queue = deque()
    queue.append(a)
    while queue:
        a = queue.popleft()
        if visit[a] == 0:
            visit[a] = 1
            for i in graph[a]:
                queue.append(i)

bfs(1)
print(sum(visit)-1)


