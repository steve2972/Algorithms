n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
one_hot = []
for idx, num in enumerate(ops): one_hot.extend([idx]*num)
min_num = 1e9
max_num = -1e9
def dfs(ops, idx, total):
    global min_num, max_num
    idx += 1
    if idx == n:
        min_num = min(min_num, total)
        max_num = max(max_num, total)
        return
    for i in range(len(ops)):    
        op, nops = ops[i], ops[:i]+ops[i+1:]
        if op == 0: dfs(nops, idx, total + nums[idx])
        elif op == 1: dfs(nops, idx, total - nums[idx])
        elif op == 2: dfs(nops, idx, total * nums[idx])
        elif op == 3:
            tmp = total * nums[idx]
            q = abs(total) // abs(nums[idx]) * -1 if tmp < 0 else total // nums[idx]
            dfs(nops, idx, q)

dfs(one_hot, 0, nums[0])
print(max_num)
print(min_num)
