from typing import List

class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        use O(1) memory
        """
        def reverse_list(arr, p1, p2):
            while p1 < p2:
                temp = arr[p1]
                arr[p1] = arr[p2]
                arr[p2] = temp
                p1 += 1
                p2 -= 1

        k = k % len(nums)
        reverse_list(nums, 0, len(nums)-1)
        reverse_list(nums, 0, k-1)
        reverse_list(nums, k, len(nums)-1)





        
solution = Solution()

test_cases = [
    ([1,2,3,4,5,6,7],3),
    ([-1,-100,3,99], 2)
]

for test in test_cases:
    solution.rotate(test[0], test[1])
    print(test[0])