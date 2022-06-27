def solution(id_list, report, k):
    unique_ids = {}
    for idx, id in enumerate(id_list): unique_ids[id] = idx
    answer = [0 for id in id_list]
    id_dict = {}
    for id in id_list:
        id_dict[id] = [0 for _ in range(len(unique_ids))]
    
    for r in report:
        a, b = r.split(" ")
        id_dict[b][unique_ids[a]] = 1
        
    for key in id_dict.keys():
        if sum(id_dict[key]) >= k:
            for idx, i in enumerate(id_dict[key]):
                if i == 1: answer[idx] += 1
        
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))