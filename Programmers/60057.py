def solution(s):
    min_len = 1e9
    if len(s) == 1: return 1
    for n in range(1, len(s)):
        len_compressed = 0
        i = 0
        while i + n < len(s):
            count = 0
            window = s[i:i+n]
            while window == s[i:i+n]:
                count += 1
                i += n
            if count > 1:
                len_compressed += len(str(count)) + n
            else: len_compressed += n

        len_compressed += len(s) - i

        print(len_compressed, window)

        if len_compressed < min_len:
            min_len = len_compressed
    return min_len

print(solution("a"))