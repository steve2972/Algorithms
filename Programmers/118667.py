from collections import deque

def solution(queue1, queue2):
    maxlen = len(queue1) * 2 + 2

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sumq1 = sum(queue1)
    sumq2 = sum(queue2)
    total = sumq1 + sumq2
    if total % 2 == 1: return -1
    target = total // 2
    if max(queue1) > target or max(queue2) > target: return -1
    cnt = 0
    
    while sumq1 != sumq2:
        cnt += 1
        if sumq1 > sumq2: 
            a = queue1.popleft()
            sumq1 -= a
            sumq2 += a
            queue2.append(a)
        elif sumq1 < sumq2:
            a = queue2.popleft()
            sumq1 += a
            sumq2 -= a
            queue1.append(a)

        if cnt > maxlen: return -1
    return cnt

q1 = [1,1,1,1,1]
q2 = [1,1,1,9,1]

print(solution(q1, q2))