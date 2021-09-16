# 24. swap nodes in pairs
# 연결 리스트를 입력받아 페어 단위로 스왑.
from LinkedList import Node


def swapPairs(head: Node) -> Node:
    cur = head

    while cur and cur.next:
        # 값만 교환
        cur.data, cur.next.data = cur.next.data, cur.data
        cur = cur.next.next

    return head


linkedlist = Node(1)
linkedlist.add(Node(2))
linkedlist.add(Node(3))
linkedlist.add(Node(4))
linkedlist.add(Node(5))
linkedlist.add(Node(6))


sol = swapPairs(linkedlist)
sol.prt()
