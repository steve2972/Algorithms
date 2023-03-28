# Inefficient
def solution(prices):
    answer = [0]
    for i, p in enumerate(prices[:-1][::-1]):
        min_len = 1
        for price in prices[-(i+1):-1]:
            if price >= p: min_len += 1
            else: break
        answer.append(min_len)
    return answer[::-1]

# Much more efficient
def solution2(prices):
    answer = [0]*len(prices)
    stack = [(prices[0], 0)]
    for i in range(1, len(prices)):
        while prices[i] < stack[-1][0]:
            k,v = stack.pop()
            answer[v] = i - v
            if len(stack) == 0: break
        stack.append((prices[i], i))
    for k, v in stack:
        answer[v] = len(prices) - v - 1
    return answer