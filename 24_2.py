# 24. swap nodes in pairs_2
# 연결 리스트를 입력받아 페어 단위로 스왑.
# 반복 구조로 스왑
from LinkedList import Node


def swapPairs(head: Node) -> Node:
    root = prev = Node(None)
    prev.next = head
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next
    return root.next



linkedlist = Node(1)
linkedlist.add(Node(2))
linkedlist.add(Node(3))
linkedlist.add(Node(4))
linkedlist.add(Node(5))
linkedlist.add(Node(6))


sol = swapPairs(linkedlist)
sol.prt()
