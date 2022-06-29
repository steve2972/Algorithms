def check_complete(p):
    stack = 0
    for i in p:
        if i == '(': stack += 1
        else: stack -= 1
        if stack < 0: return False
    return True

def solution(p):
    # Base case
    if p == '': return ''
    # Split w into u and v
    stack = 0
    for i, n in enumerate(p):
        if n == '(': stack += 1
        else: stack -= 1
        if stack == 0:
            u, v = p[:i+1], p[i+1:]
            break
    if check_complete(u):
        return u + solution(v)
    else:
        u = u[1:-1]
        u = ''.join(['(' if i == ')' else ')' for i in u])
        return '(' + solution(v) + ')' + u

print(solution(")()(()"))