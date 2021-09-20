# 23. merge k sorted lists
from typing import List
import heapq
from LinkedList import Node


class Solution:
    def mergeKLists(self, lists: List[Node]) -> Node:
        root = result = Node(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].data, i + 500, lists[i]))
        print("heap: ", heap)
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.data, idx, result.next))
        print(result)
        return root.next


# linkedlist.add(Node(2))
l1 = Node(1)
l1.add(Node(4))
l1.add(Node(5))
l1.prt()

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)
l2.prt()

l3 = Node(2)
l3.next = Node(6)

sol = Solution().mergeKLists([l1, l2, l3])
sol.prt()