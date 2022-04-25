all_num_list = [1,2,3,4,5,6,7]
a = [1]
ans = []
choose = 6


def solve(nums):
   temp = [[]]
   for num in nums:
       temp += [i + [num] for i in temp]
   for arr in temp:
       if len(arr) == choose: ans.append(arr)

# def solve(a):
#     last_num = a[-1]
#     last_num_idx = all_num_list.index(last_num)

#     addition_count = choose - len(a)
#     addition_range = all_num_list.index(all_num_list[-addition_count])

#     if len(a) == 6:

#         ans.append(a[:])
#         return
    
#     for i in range(last_num_idx + 1, addition_range+1):
#         a.append(all_num_list[i])
#         solve(a)
#         a.pop()

solve(a)
print(ans)