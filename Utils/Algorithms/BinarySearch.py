def binary_search(nums, target) -> int:
    hi, lo = len(nums)-1, 0
    while lo <= hi:
        i = (hi + lo) // 2
        if nums[i] == target: return i
        elif nums[i] > target: hi = i-1
        else: lo = i+1
    return -1
