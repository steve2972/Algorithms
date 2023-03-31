def solution(n, times):
    lo = min(times)
    hi = lo * n
    while lo < hi - 1:
        mid = (hi+lo)//2
        if sum([mid//time for time in times]) >= n: hi = mid
        else: lo = mid
    return hi

n = 6
times = [7, 10]
print(solution(n, times))