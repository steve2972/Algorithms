from ftplib import parse150
import sys
sys.path.append('.')
from Algorithms.LinkedList import ListNode, add_nodes, print_nodes
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def check_nth(node):
            for i in range(n):
                node = node.next
            return node
        p1 = p2 = head
        while check_nth(p2):
            p1 = p2
            p2 = p2.next
        if p1 == p2: return p1.next
        else: p1.next = p2.next
        return head


solution = Solution()
head = add_nodes([1, 2, 3, 4, 5])
print_nodes(solution.removeNthFromEnd(head, n=2))