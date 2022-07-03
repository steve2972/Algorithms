max_sheep = 0


def solution(info, edges):
    graph = {}
    for node in range(len(info)): graph[node] = []
    for (u, v) in edges: graph[u].append(v)
    visited = [False] * len(info)

    def recursive_find(cur, visited, num_sheep, num_wolf, neighbors):
        global max_sheep
        if visited[cur]: return
        visited[cur] = True
        if info[cur]: num_wolf += 1
        else:
            num_sheep += 1
            max_sheep = max(max_sheep, num_sheep)
        if num_wolf >= num_sheep: return

        neighbors.extend(graph[cur])
        for n in neighbors:
            list_n = [i for i in neighbors if not visited[i] and i != n]
            recursive_find(n, visited[:], num_sheep, num_wolf, list_n)


    recursive_find(0, visited, 0, 0, [])
    return max_sheep

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges =	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]


print(solution(info, edges))
