# 92. reverse linked list2
from LinkedList import Node


def reverseBetween(head: Node, m: int, n: int) -> Node:
    # except
    if not head or m == n:
        return head

    root = st = Node(None)
    root.next = head
    # st, end 지정
    for _ in range(m - 1):
        st = st.next
    end = st.next

    # important!!
    for _ in range(n - m):
        tmp, st.next, end.next = st.next, end.next, end.next.next
        st.next.next = tmp
    return root.next


linkedlist = Node(1)
linkedlist.add(Node(2))
linkedlist.add(Node(3))
linkedlist.add(Node(4))
linkedlist.add(Node(5))
linkedlist.add(Node(None))
linkedlist.prt()

sol = reverseBetween(linkedlist, 2, 4)
sol.prt()