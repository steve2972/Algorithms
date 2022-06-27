def dfs(cur, visited, sheep, wolf, k, dict, info, track):
    return
def solution(info, edges):
    graph = {}
    for i in edges:
        x, y = i[0], i[1]
        if x not in graph: graph[x] = [y]
        else: graph[x].append(y)
        if y not in graph: graph[y] = [x]
        else: graph[y].append(x)
    visited = set()
    track = []
