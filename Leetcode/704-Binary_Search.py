"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums, target) -> int:
        hi, lo = len(nums)-1, 0
        while lo <= hi:
            i = (hi + lo) // 2
            if nums[i] == target: return i
            elif nums[i] > target: hi = i-1
            else: lo = i+1

        return -1

nums = [-1,0,3,5,9,12]
target = 3

solution = Solution()
print(solution.search(nums, target))