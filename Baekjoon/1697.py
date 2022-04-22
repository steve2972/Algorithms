def BFS(n, k):
    queue = [n]
    depth = [0] * (100001)
    while queue:
        n = queue.pop(0)
        if n == k:
            print(depth[n])
            return
        for op in (n-1, n+1, n*2):
            if 0 <= op <= 100000 and not depth[op]:
                depth[op] = depth[n] + 1
                queue.append(op)

n, k = map(int, input().split())
BFS(n, k)