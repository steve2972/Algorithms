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

def solution(n, s, A, B, fares):
    graph = floyd(n, fares)
    answer = 1e9
    for i in range(1,n+1):
        cost = graph[s][i] + graph[i][A] + graph[i][B]
        answer = min(answer,cost)
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))