from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            i = lo + (hi - lo) // 2
            if nums[i] == target: return i
            elif nums[i] > target: hi = i-1
            else: lo = i+1
        return lo


nums = [1,3,5,6]
target = 2

solution = Solution()
print(solution.searchInsert(nums, target))