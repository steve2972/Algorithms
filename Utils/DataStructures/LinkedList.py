from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_nodes(nodes: List[int]) -> ListNode:
    head = ListNode(nodes.pop(0))
    tail = head
    while nodes:
        tail.next = (ListNode(nodes.pop(0)))
        tail = tail.next
    return head

def print_nodes(head):
    while head.next != None:
        print(head.val, '-> ', end='')
        head = head.next
    print(head.val)