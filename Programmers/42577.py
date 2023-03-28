def solution(phone_book):
    prefix = set()
    for num in [*phone_book, *phone_book]:
        for i in range(len(num)):
            head = num[:i]
            if head in prefix:
                return False
        prefix.add(num)
    return True

a = ["1195524421", "119", "97674223"]
print(solution(a))