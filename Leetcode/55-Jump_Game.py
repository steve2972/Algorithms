from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        d, i = 0, 0
        while i <= d:
            d = max(d, i + nums[i])
            if d >= len(nums) - 1: return True
            i += 1
        return False