import numpy as np

def solution(info, query):
    def get_list(arr, idx):
        tmp = []
        for i in arr:
            tmp.append(i[idx])
        return tmp

    def multiply(arr1, arr2):
        tmp = []
        for x, y in zip(arr1, arr2):
            tmp.append(x*y)
        return tmp
    
    list_candidates = [i.split(" ") for i in info]
    answer = []

    for q in query:
        criteria = [i for i in q.split(' ') if i != 'and']
        cand_scores= get_list(list_candidates, -1)
        foo = [1 if int(cand_scores[i]) >= int(criteria[-1]) else 0 for i in range(len(info))]
        for idx, c in enumerate(criteria[:-1]):
            if c != '-':
                new_foo = [1 if get_list(list_candidates, idx)[i] == c else 0 for i in range(len(info))]
                foo = multiply(foo, new_foo)
        answer.append(sum(foo))     
    return answer


def solution_numpy(info, query):
    list_candidates = np.array([i.split(" ") for i in info])
    answer = []

    for q in query:
        criteria = [i for i in q.split(' ') if i != 'and']
        foo = list_candidates[:,-1].astype(int) >= int(criteria[-1])
        for idx, c in enumerate(criteria[:-1]):
            if c != '-':
                foo = np.logical_and(foo, (np.where(list_candidates[:,idx] == c, True, False)))
        answer.append(sum(foo))
                
    return answer



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


print(solution(info, query))