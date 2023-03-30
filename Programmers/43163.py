def match(a, b):
    ok = 1
    for i, j in zip(a,b):
        if i!=j:
            if ok: ok = 0
            else: return False
    return True

def solution(begin, target, words):
    words = set(words)
    if target not in words: return 0    
    
    graph = {}
    for word in [*list(words), begin]:
        for t in words:
            if word != t and match(word, t):
                if word in graph: graph[word].append(t)
                else: graph[word] = [t]

    visited = set()
    queue = [begin]
    ans = 0
    while queue:
        qlen = len(queue)
        while qlen:
            word = queue.pop(0)
            if word == target: return ans
            if word not in visited:
                visited.add(word)
                for nword in graph[word]:
                    queue.append(nword)
            qlen -= 1
        ans += 1
    return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))



