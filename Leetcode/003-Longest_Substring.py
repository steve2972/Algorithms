class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = curmax = start_idx = 0
        visited = {}
        for idx, c in enumerate(s):
            if c in visited and visited[c] >= start_idx:
                maxlen = max(maxlen, curmax)
                curmax = idx - visited[c]
                start_idx = visited[c]
            else: curmax += 1
            visited[c] = idx
        return max(maxlen, curmax)

solution = Solution()
probs = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    " ",
    "dvdf",  
    "qrsvbspk",
    "abba"
]
for prob in probs:
    print(solution.lengthOfLongestSubstring(prob))