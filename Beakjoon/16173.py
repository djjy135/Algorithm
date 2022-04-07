import sys
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

visited = [[False]* n for i in range(n)]

dx = [1, 0]
dy = [0, 1]

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n or visited[x][y] ==1 :
        return 
    
    if graph[x][y] == -1:
        visited[x][y] == 1
        return
    visited[x][y] = 1
    dfs(x+graph[x][y],y)
    dfs(x-graph[x][y],y)
    dfs(x,y+graph[x][y])
    dfs(x,y-graph[x][y])

dfs(0,0)

if visited[-1][-1] == 1:
    print("HaruHaru")
else:
    print("Hing")