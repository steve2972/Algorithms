def solution(array, commands):
    answer = []
    for command in commands:
        p1, p2, k = command
        answer.append(sorted(array[p1-1:p2])[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))