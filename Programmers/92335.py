def solution(n, k):
    def is_prime(n):
        if n <= 1: return False
        elif n == 2: return True 
        for idx in range(2, int(n**.5)+1):
            if n % idx == 0: return False
        return True
    def convert_base(n, k):
        if n == 0: return '0'
        digits = []
        while n:
            digits.append(str(n % k))
            n = n // k
        return ''.join(digits[::-1])
    n_k = convert_base(n, k)
    list_nums = [i for i in n_k.split("0")]
    answer = 0
    for num in list_nums: 
        if num != '' and is_prime(int(num)): answer += 1
    return answer

print(solution(437674, 3))