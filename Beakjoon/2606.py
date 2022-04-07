n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n+1)
count = 0

def dfs(a):
    count = 0

    if visit[a] == 0:
        visit[a] = 1
        for i in graph[a]:
            dfs(i)

dfs(1)
print(sum(visit))


