from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Slow solution (6040ms)
        if len(s2) < len(s1): return False
        letters = {}
        for c in s1:
            if c in letters: letters[c] += 1
            else: letters[c] = 1
        idx = 0
        while idx <= len(s2) - len(s1):
            counter = {}
            for c in s2[idx:idx+len(s1)]:
                if c in letters:
                    if c in counter: counter[c] += 1
                    else: counter[c] = 1 
            if counter == letters: return True
            else: idx += 1
        return False

    def checkInclusion2(self, s1:str, s2:str) -> bool:
        # Better solution (79ms)
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for c in s1: dict1[c] += 1
        for c in s2[:len(s1)]: dict2[c] += 1

        if len(s2) < len(s1): return False
        for i in range(len(s2) - len(s1)):
            if dict1 == dict2: return True
            dict2[s2[i+len(s1)]] += 1
            dict2[s2[i]] -= 1
            if dict2[s2[i]] == 0: dict2.pop(s2[i])
        if dict1 == dict2: return True
        return False

solution = Solution()
probs = [
    ('adc', 'dcda'),
    ("ab", "eidbaooo"),
    ("ab", "eidboaoo"),
    ("ab", "ab"),
    ("hello", "ooolleoooleh"),
    ("abc", "ccccbbbbaaaa"),
    ("abcdxabcde", "abcdeabcdx")
]

for s1, s2 in probs:
    print(solution.checkInclusion2(s1, s2))