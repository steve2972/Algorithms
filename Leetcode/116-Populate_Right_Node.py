
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if root == None: return None
        queue = [root]
        level = 0
        while queue:
            level_size = len(queue)
            while level_size > 0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
                level_size -= 1
                if level_size > 0: node.next = queue[0]
            node.next = None
            level += 1
        return root