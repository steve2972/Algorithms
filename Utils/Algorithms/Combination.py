def combination(arr, n):
    if n == 0: return [[]]
    ans = []
    for i in range(len(arr)):
        x, r = arr[i], arr[i+1:]
        for r in combination(r, n-1): ans.append([x, *r])
    return ans

a = [1,2,3,4,5]
n = 2
print(combination(a, n))