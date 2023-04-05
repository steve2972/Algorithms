def nonDivisibleSubset(k, s):
    remainder = [0] * k
    for i in s:
        remainder[i % k] += 1
    result = min(remainder[0], 1)
    if k % 2 == 0:
        result += min(remainder[k // 2], 1)
    for i in range(1, (k + 1) // 2):
        if i != k - i:
            result += max(remainder[i], remainder[k - i])
    return result


nonDivisibleSubset(3, [1, 7, 2, 4])