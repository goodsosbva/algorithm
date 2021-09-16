# 24. swap nodes in pairs_3
# 연결 리스트를 입력받아 페어 단위로 스왑.
# 재귀 구조로 스왑
from LinkedList import Node


def swapPairs(head: Node) -> Node:
    if head and head.next:
        p = head.next
        head.next = swapPairs(p.next)
        p.next = head
        return p
    return head


linkedlist = Node(1)
linkedlist.add(Node(2))
linkedlist.add(Node(3))
linkedlist.add(Node(4))


sol = swapPairs(linkedlist)
sol.prt()