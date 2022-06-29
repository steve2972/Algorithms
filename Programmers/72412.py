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


print(solution(info, query))