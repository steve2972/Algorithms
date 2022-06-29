from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_node(head: TreeNode, val: int):
    temp = head
    while temp:
        if temp.val <= val:
            if temp.right: temp = temp.right
            else: 
                temp.right = TreeNode(val)
                return
        else:
            if temp.left: temp = temp.left
            else: 
                temp.left = TreeNode(val)
                return

def print_tree(head):
    queue = [head]
    while queue:
        node = queue.pop(0)
        print(f"{node.val}", end=' ')
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    print()

def make_tree(arr: List[int]) -> Optional[TreeNode]:
    if len(arr) < 1: return None
    elif len(arr) == 1: return TreeNode(arr[0])
    head = TreeNode(val=arr[0], left=None, right=None)
    for i in arr[1:]:
        insert_node(head, i)
    return head

tree = make_tree([4,3,2,5, 1])
print_tree(tree)