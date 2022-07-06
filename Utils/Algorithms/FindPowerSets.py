arr = [1,2,3,4,5,6,7]

def power_set(nums, n:int):
    ans = []
    temp = [[]]
    for num in nums:
        temp += [i + [num] for i in temp]
    for arr in temp:
        if len(arr) == n: ans.append(arr)
    return ans

print(power_set(arr, 6))