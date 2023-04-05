from math import ceil
def solution(cap, n, deliveries, pickups):
    moves = 0
    give_overflow = get_overflow = 0
    for idx in range(n-1, -1, -1):
        if deliveries[idx] or pickups[idx]:
            nd = min(deliveries[idx], give_overflow)
            np = min(pickups[idx], get_overflow)
            deliveries[idx] -= nd
            pickups[idx] -= np
            give_overflow -= nd
            get_overflow -= np

            cnt = ceil(max(deliveries[idx], pickups[idx]) / cap)
            moves += 2 * (idx+1) * cnt
            give = get = cnt * cap
            give_overflow += give - deliveries[idx]
            get_overflow += get - pickups[idx]

            deliveries[idx] = pickups[idx] = 0
    return moves
            

cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [1, 0, 2, 0, 1, 0, 2]

print(solution(	4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
