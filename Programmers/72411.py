def solution(orders, course):
    def find_perms(ors, course_len):
        if len(ors) < course_len:
            return []
        temp, ans = [[]], []
        for n in sorted(ors):
            temp += [i + [n] for i in temp]
        for arr in temp:
            if len(arr) == course_len:
                ans.append(''.join(arr))
        return ans

    ans = []
    for c_num in course:
        temp = {}
        for order in orders:
            combinations = find_perms(order, c_num)
            for c in combinations:
                if c not in temp: temp[c] = 1
                else: temp[c] += 1
        if len(temp.values()) > 0 and max(temp.values()) >= 2:
            for key in temp.keys():
                if temp[key] == max(temp.values()):
                    ans.append(key)
    return sorted(ans)
    
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,5]
print(solution(orders, course))