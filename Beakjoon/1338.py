
n,m = map(int,input().split())


graph = []
for _ in range(n):
    graph.append(list(input()))

def dfs1(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == "-":
        graph[x][y] = "x"
        dfs1(x,y-1)
        dfs1(x,y+1)
        return True

    return False

def dfs2(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False 

    if graph[x][y] == "|":
        graph[x][y] = "x"
        dfs2(x-1,y)
        dfs2(x+1,y)
        return True

    return False
count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "-":
            dfs1(i,j)
            count += 1
        elif graph[i][j] == "|":
            dfs2(i,j)
            count += 1

print(count)

