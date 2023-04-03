import heapq

def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)

    graph = [[] for _ in range(n+1)]
    for a,b, cst in paths:
        graph[a].append([b, cst])
        graph[b].append([a, cst])

    intensity = [1e9] * (n+1)

    def shortest_path(a):
        q = [(0, a)]
        while q:
            dist, node = heapq.heappop(q)
            if node in summits: continue
            if intensity[node] < dist: continue
            for b, cst in graph[node]:
                if b in gates: continue
                cost = max(dist, cst)
                if intensity[b] > cost:
                    intensity[b] = cost
                    heapq.heappush(q, (cost, b))

    for gate in gates:
        shortest_path(gate)

    answer = [-1, 1e9]
    
    for summit in summits:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
        elif intensity[summit] == answer[1]:
            answer[0] = min(answer[0], summit)

    return answer

n = 4
paths = [[1, 3, 1], [1, 4, 1], [4, 2, 1]]
gates = [1]
summits = [2,3,4]
print(solution(n, paths, gates, summits))



def solution2(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)
    INF = 1e9
    fw_graph = [[INF] * (n+1) for _ in range(n+1)]
    for a, b, c in paths:
        fw_graph[a][b] = c
        fw_graph[b][a] = c
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                if k in gates:
                    if a in gates or b in gates: continue
                if k in summits:
                    if a in summits or b in summits: continue
                if a in gates and b in gates: continue
                if a in summits and b in summits: continue
                fw_graph[a][b] = min(fw_graph[a][b], max(fw_graph[a][k], fw_graph[k][b]))
    
    min_len = [-1, INF]
    for summit in summits:
        for gate in gates:
            if fw_graph[summit][gate] < min_len[1]:
                min_len = [summit, fw_graph[summit][gate]]

    return min_len