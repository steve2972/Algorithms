import numpy as np

class TrieNode:
    def __init__(self, word, level:int=0):
        self.word = word
        self.is_end = False
        self.counter = 1
        self.level = level
        self.children = {}
    def __str__(self):
        return f"word: {self.word} | counter: {self.counter} | level: {self.level} | children: {self.children}"
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
        self.count = 0

    def insert(self, words):
        self.count += 1
        node = self.root
        for word in words:
            if word in node.children:
                node = node.children[word]
                node.counter += 1
            else:
                new_node = TrieNode(word, node.level+1)
                node.children[word] = new_node
                node = new_node
        
        node.is_end = True

    def query(self, x, direction=True):
        target_level = len(x)
        node_stack = [self.root]
        output = 0
        level = 0
        while level < target_level:
            word = x[level]
            level_size = len(node_stack)
            while level_size > 0:
                node = node_stack.pop(0)
                if direction:
                    if level == target_level-1:
                        for node in node.children.values():
                            if int(node.word) >= int(x[level]):
                                output += node.counter
                    elif word in node.children:
                        node_stack.append(node.children[word])
                    elif word == '-':
                        node_stack.extend(node.children.values())
                else:
                    if level == 0:
                        for n in node.children.values():
                            if int(n.word) >= int(word):
                                node_stack.append(n)
                    elif level == target_level-1:
                        for n in node.children.values():
                            if n.word == x[-1] or word == '-':
                                output += n.counter
                    elif word in node.children:
                        node_stack.append(node.children[word])
                    elif word == '-':
                        node_stack.extend(node.children.values())
                
                level_size -= 1
            level += 1
        return output
def solution(info, query):
    trie1, trie2 = Trie(), Trie()
    answer = []
    specs = [i.split(" ") for i in info]
    for spec in specs:
        trie1.insert(spec)
        trie2.insert(spec[::-1])
    
    for q in query:
        criteria = [i for i in q.split(' ') if i != 'and']
        if criteria == ['-'*5]: answer.append(trie1.count)
        elif criteria[0] == '-':
            answer.append(trie2.query(criteria[::-1], False))
        else:
            answer.append(trie1.query(criteria))
    
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

def solution2(info, query):
    specs = [i.split(" ") for i in info]
    answer = []

    for q in query:
        criteria = [i for i in q.split(' ') if i != 'and']
        res = [specs[i] for i in range(len(specs))
                if (specs[i][0] == criteria[0] or criteria[0] == '-') and
                (specs[i][1] == criteria[1] or criteria[1] == '-') and
                (specs[i][2] == criteria[2] or criteria[2] == '-') and
                (specs[i][3] == criteria[3] or criteria[3] == '-') and
                (int(specs[i][4]) >= int(criteria[4]) or criteria[4] == '-')]
        answer.append(len(res))

    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]


print(solution2(info, query))


####################정답 코드
#https://soniacomp.medium.com/%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%88%9C%EC%9C%84%EA%B2%80%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2021-blind-test-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-ba2325d9598f

from bisect import bisect_left
from itertools import combinations

def make_all_cases(separate_info):
    cases = []
    for k in range(5):
        for condition in combinations([0,1,2,3], k):
            case = []
            for idx in range(4):
                if idx not in condition:
                    case.append(separate_info[idx])
                else:
                    case.append('-')
            cases.append(''.join(case))
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(seperate_info)
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(seperate_info[4])]
            else:
                all_people[case].append(int(seperate_info[4]))
    
    for key in all_people.keys():
        all_people[key].sort()
        
    for q in query:
        seperate_q = q.split(' and ')
        seperate_q.extend(seperate_q.pop().split())
        target = ''
        for sq in seperate_q[:4]:
            target += sq
        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[4]), lo=0, hi=len(all_people[target])))
        else:
            answer.append(0)
    return answer