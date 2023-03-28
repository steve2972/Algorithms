def solution(clothes):
    clothes_dict = {}
    for value, key in clothes:
        if key in clothes_dict:
            clothes_dict[key] += 1
        else:
            clothes_dict[key] = 2
        
    answer = 1
    for key in clothes_dict.keys():
        answer *= clothes_dict[key]
    return answer - 1