def solution(n, info):
    required_arrows = [i+1 for i in info]
    apeach = set([i for i in range(11) if info[i]>0])
    diff, r = 0, 0
    ans_perm = None
    temp = [[]]
    for num in range(11):
        temp += [i + [num] for i in temp]
    for perm in temp:
        arrows = n
        for i in perm:
            arrows -= required_arrows[i]
        if arrows >= 0:
            ryan_score = sum([10-i for i in perm])
            apeach_score = sum([10-i for i in apeach - set(perm)])
            if ryan_score - apeach_score > diff:
                ans_perm = [perm]
                diff = ryan_score - apeach_score
                r = arrows
            elif ryan_score - apeach_score == diff:
                ans_perm.append(perm)
                r = arrows

    
    if ans_perm == None:
        return [-1]
    answer = [required_arrows[i] if i in ans_perm[-1] else 0 for i in range(11)]
    answer[-1] += r
    print(ans_perm)
    return answer


info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(9, info))

###################################################
# Solution
# Code from https://velog.io/@hygge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-2022-KAKAO-BLIND-RECRUITMENT-BFS
from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear()
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]