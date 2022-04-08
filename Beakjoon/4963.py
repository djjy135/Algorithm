import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드

def dfs(x,y):

    if 0 <= x < m and 0 <= y < n:
        if graph[x][y] == 1:
            graph[x][y] = 2
            dfs(x-1,y)
            dfs(x-1,y-1)
            dfs(x-1,y+1)
            dfs(x+1,y)
            dfs(x+1,y-1)
            dfs(x+1,y+1)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
            
        return False

#dx = [-1, -1, -1, 0, 0, 1, 1, 1]
#dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    
    n,m = map(int,input().split())
    if not n and not m:
        break
    
    # graph = []
    # for _ in range():
    #     graph.append(list(input()))
    graph = [list(map(int, input().split())) for _ in range(m)]

    count = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)

