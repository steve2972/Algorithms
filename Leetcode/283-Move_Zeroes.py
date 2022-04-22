from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = 0
        p2 = 1
        while p1 < len(nums) and p2 < len(nums):
            if p2 < p1: p2 += 1
            elif nums[p1] != 0: p1 += 1
            elif nums[p1] == 0: 
                if nums[p2] == 0: p2 += 1
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
            else: p2 += 1


solution = Solution()

probs = [
    [0,1,0,3,12],
    [0],
    [2,1],
    [1,0,1],
    [4,2,4,0,0,3,0,5,1,0]
]
for prob in probs:
    solution.moveZeroes(prob)
    print(prob)