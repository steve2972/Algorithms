# Path-Finding: Use Floyd-Warshall

N = int(input())
edges = {}
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(N):
        if row[j]: 
            if i in edges:
                edges[i].append(j)
            else:
                edges[i] = [j]

INF = 1e3
graph = [[INF]*N for _ in range(N)]
for i in edges.keys():
    for j in edges[i]:
        graph[i][j] = 1


for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(N):
    for j in range(N):
        print(f"{1 if graph[i][j] < 1000 else 0}", end=' ')
    print()