def affect_board(board, r1, c1, r2, c2, degree):
    list_r = range(r1, r2+1)
    list_c = range(c1, c2+1)
    for r in list_r:
        for c in list_c:
            board[r][c] += degree

def solution(board, skill):
    i, j = len(board), len(board[0])
    for s in skill:
        skill_type, r1, c1, r2, c2, degree = s
        if skill_type == 1: degree *= -1
        affect_board(board, r1, c1, r2, c2, degree)
    answer = sum([1 for r in range(i) for c in range(j) if board[r][c] > 0])
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board, skill))