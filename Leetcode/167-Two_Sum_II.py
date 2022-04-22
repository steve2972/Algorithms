from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1
        while numbers[p1] + numbers[p2] != target:
            if numbers[p1] + numbers[p2] > target: p2 -= 1
            else: p1 += 1
        return [p1+1, p2+1]

solution = Solution()

probs = [
    ([2,7,11,15], 9),
    ([2,3,4], 6),
    ([-1,0], -1)
]

for numbers, target in probs:
    print(solution.twoSum(numbers, target))