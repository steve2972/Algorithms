def permutation(arr):
    if len(arr) == 0: return []
    elif len(arr) == 1: return [arr]
    ans = []
    for i in range(len(arr)):
        a, r = arr[i], arr[:i]+arr[i+1:]
        for r in permutation(r): ans.append([a, *r])
    return ans

a = [1, 2, 3]
print(permutation(a))