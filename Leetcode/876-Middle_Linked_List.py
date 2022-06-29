import sys
sys.path.append('.')
from Utils.DataStructures.LinkedList import ListNode, add_nodes, print_nodes
from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        len = 0
        while p2 != None:
            p2 = p2.next
            len += 1
        for _ in range(len // 2):
            p1 = p1.next
        return p1


solution = Solution()
head = add_nodes([1,2,3,4,5])
print_nodes(solution.middleNode(head))

