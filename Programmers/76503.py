import sys
sys.setrecursionlimit(10 ** 6)

def solution(a, edges):
    if sum(a) != 0: return -1
    graph = [[] for i in range(len(a))]
    for k,v in edges:
        graph[k].append(v)
        graph[v].append(k)

    def dfs(prev, cur):
        children = [i for i in graph[cur] if i!=prev]
        sum_children = sum([dfs(cur, i) for i in children])
        a[prev] += a[cur]
        acur, a[cur] = abs(a[cur]), 0
        return sum_children + acur
    
    return dfs(0, 0)


a = [-2, 8, -5, -5, -3, 0, 5, 2]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]]

print(solution(a, edges))
