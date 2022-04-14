class Solution:
    def __init__(self, bad):
        self.bad = bad
    def isBadVersion(self, version:int) -> bool:
        if version >= self.bad: return True
        else: return False

    def firstBadVersion(self, n:int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            i = lo + (hi-lo)//2
            if self.isBadVersion(i): hi = i - 1
            else: lo = i+1
            
        return lo


n = 2**10
bad = 2**9

solution = Solution(bad)
print(solution.firstBadVersion(n))