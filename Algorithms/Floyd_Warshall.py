def floyd(n, edges):
    INF = 1e9
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for a in range(n+1):
        graph[a][a] = 0
    for f in edges:
        graph[f[0]][f[1]] = f[2]
        graph[f[1]][f[0]] = f[2]
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])
    return graph