import heapq

def solution(alp, cop, problems):
    problems += [[0,0,1,0,1], [0,0,0,1,1]]
    ralp = max(map(lambda x: x[0], problems))
    rcop = max(map(lambda x: x[1], problems))

    dp = {(alp, cop): 0}
    q = [(0, (alp, cop))]

    while q[0][1][0] < ralp or q[0][1][1] < rcop:
        ct, (alp, cop) = heapq.heappop(q)
        for a, c, ra, rc, cost in problems:
            if alp >= a and cop >= c:
                nalp = min(alp+ra, 200)
                ncop = min(cop+rc, 200)
                if (nalp, ncop) not in dp or dp[(nalp, ncop)] > ct + cost:
                    dp[(nalp, ncop)] = ct + cost
                    heapq.heappush(q, (ct + cost, (nalp, ncop)))

    return q[0][0]

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))