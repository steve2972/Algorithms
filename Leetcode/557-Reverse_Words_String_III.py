class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseWord(w):
            w = [c for c in w]
            p1 = 0
            p2 = len(w)-1
            while p1 < p2:
                w[p1], w[p2] = w[p2], w[p1]
                p1 += 1
                p2 -= 1
            return ''.join(w)
        return ' '.join([reverseWord(w) for w in s.split()])

solution = Solution()
s = "Let's take LeetCode contest"
print(solution.reverseWords(s))