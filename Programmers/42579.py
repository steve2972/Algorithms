def solution(genres, plays):
    g2p, p2n = {}, {}
    for n, (g, p) in enumerate(zip(genres, plays)):
        if g in g2p: g2p[g].append((p, n))
        if g not in g2p: g2p[g] = [(p, n)]
        p2n[p] = n
    g2p = {k:v for k,v in sorted(g2p.items(), key=lambda x: sum([a[0] for a in x[1]]), reverse=True)}
    answer = []
    for key in g2p.keys():
        value = g2p[key]
        value = sorted(value, key=lambda x: x[0], reverse=True)
        answer.extend([x[1] for x in value[:2]])
    return answer


genres = ["classic", "pop", "classic", "classic", "pop", "pop"]
plays = [500, 600, 150, 800, 2500, 600]

print(solution(genres, plays))