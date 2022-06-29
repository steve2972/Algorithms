class TrieNode:
    def __init__(self, char, level:int=0):
        self.char = char
        self.is_end = False
        self.counter = 1
        self.level = level
        self.children = {}

    def __str__(self):
        return f"char: {self.char} | counter: {self.counter} | level: {self.level} | children: {self.children}"
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
        self.count = 0

    def insert(self, word):
        self.count += 1
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
                node.counter += 1
            else:
                new_node = TrieNode(char, node.level+1)
                node.children[char] = new_node
                node = new_node
        
        node.is_end = True

    def query(self, x):
        target_level = len(x)
        node_stack = [self.root]
        self.output = 0
        level = 0
        while node_stack and level < target_level:
            char = x[level]
            level_size = len(node_stack)
            while level_size > 0:
                node = node_stack.pop(0)
                if char in node.children:
                    node_stack.append(node.children[char])
                elif char == '?':
                    node_stack.extend(node.children.values())
                    if x[level:] == '?' * (len(x) - level):
                        for node in node_stack:
                            self.output += node.counter
                        return self.output
                level_size -= 1
            level += 1
            if level == target_level:
                for node in node_stack:
                    self.output += node.counter
                break

        return self.output

def solution(words, queries):
    reverse = lambda x: x[::-1]
    trie1, trie2 = {}, {}
    answer = []

    for word in words:
        if len(word) not in trie1:
            trie1[len(word)] = Trie()
            trie2[len(word)] = Trie()

        trie1[len(word)].insert(word)
        trie2[len(word)].insert(reverse(word))

    for query in queries:
        if len(query) not in trie1:
            answer.append(0)
        elif query == '?' * len(query):
            answer.append(trie1[len(query)].count)
        elif query[0] == '?':
            answer.append(trie2[len(query)].query(reverse(query)))
        else:
            answer.append(trie1[len(query)].query(query))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]

print(solution(words, queries))