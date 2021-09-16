# 328. odd even linked list
from LinkedList import Node


def oddEvenList(head: Node) -> Node:
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next


    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head


linkedlist = Node(1)
linkedlist.add(Node(2))
linkedlist.add(Node(3))
linkedlist.add(Node(4))
linkedlist.add(Node(5))
linkedlist.add(Node(None))
linkedlist.prt()

sol = oddEvenList(linkedlist)
sol.prt()


