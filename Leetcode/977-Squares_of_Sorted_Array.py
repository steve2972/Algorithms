from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0: return [n * n for n in nums] # naive solution
        elif nums[-1] <= 0: return [n * n for n in nums[::-1]]
        else:
            descending = list()
            new_list = list()
            for i in range(len(nums)-1):
                if nums[i] <= nums[i+1] and nums[i+1] <= 0: descending.append(abs(nums[i]))
                else: 
                    pos = i
                    descending.append(abs(nums[i]))
                    break
            nums = nums[pos+1:]

            p1 =0
            p2 =0

            while p1 < len(descending) and p2 < len(nums):
                if descending[::-1][p1] < nums[p2]:
                    new_list.append(descending[::-1][p1])
                    p1 += 1
                else: 
                    new_list.append(nums[p2])
                    p2 += 1
            while p1 < len(descending):
                new_list.append(descending[::-1][p1])
                p1 += 1
            while p2 < len(nums):
                new_list.append(nums[p2])
                p2 += 1

            return [n * n for n in new_list]


    def sortedSquares2(self, nums: List[int]) -> List[int]:
        # better solution
        p1 = 0
        p2 = len(nums) - 1

        new_list = []
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[p1]) < abs(nums[p2]):
                new_list.append(nums[p2] * nums[p2])
                p2 -= 1
            else:
                new_list.append(nums[p1] * nums[p1])
                p1 += 1

        return new_list[::-1]

solution = Solution()

test_cases = [
    [-3,-3,-2,1],
    [-4,-1,0,3,10],
    [-10, -9, -7, -5, 0, 0, 10],
    [-5, -4, -3, -2, -1],
    [-5,-4,1,2,5],
    [-9,-7,-5,-3,-1,2,4,4,7,10]
]

for test in test_cases:
    print(solution.sortedSquares2(test))