class Node:
    def __init__(self, type, id_):
        # 0 = sheep, 1 = wolf
        self.type = type
        self.id = id_
        self.parent = None

    def __str__(self):
        return f"{'sheep' if not self.type else 'wolf'}: id:{self.id}"

def last_safe(n):
    count = 0
    while n.type == 1:
        count += 1
        n = n.parent
    return n, count

def solution(info, edges):
    graph = {}
    nodes = [Node(i, idx) for idx, i in enumerate(info)]
    for node in nodes:
        graph[node] = []
    for edge in edges:
        u, v = edge
        nodes[v].parent = nodes[u]
        graph[nodes[u]].append(nodes[v])
    total_sheep = len(info) - sum(info)
    num_sheep, num_wolves = 1, 0
    root = nodes[0]

    for n in nodes:
        print(n, "|parent:", n.parent)
        for child in graph[n]:
            print("\t", child)
    
    # DFS
    stack = [nodes[0]]
    visited = {}
    for node in nodes: visited[node] = 0
    while stack:
        node = stack.pop(0)
        for n in graph[node]:
            # Check neighbors
            if n and n.type == 0:
                # Node is a sheep
                n.type = -1
                num_sheep += 1
                if visited[n] < total_sheep:
                    visited[n] += 1
                    stack.insert(0, n)
            elif n and n.type == 1:
                # Node is a wolf
                if num_wolves + 1 < num_sheep:
                    # Sheep outnumber wolves
                    num_wolves += 1
                    if visited[n] < total_sheep:
                        visited[n] += 1
                        stack.insert(0, n)
                else:
                    n, count = last_safe(n)
                    num_wolves -= count
                    if visited[n] < total_sheep:
                        visited[n] += 1
                        stack.insert(0, n)
            elif n and n.type == -1:
                # Node is empty (sheep or wolf already taken)
                if visited[n] < total_sheep:
                    visited[n] += 1
                    stack: stack.insert(0, n)

        
    return num_sheep

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges =	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]


print(solution(info, edges))
