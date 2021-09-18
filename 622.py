# 622.design circular queue
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return print(True)
        else:
            return print(False)

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return print(False)
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return print(True)

    def Front(self) -> int:
        return print(-1) if self.q[self.p1] is None else print(self.q[self.p1])

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else print(self.q[self.p2 - 1])

    # 네가 구현
    def ptr(self):
        print("[", end= " ")
        for i in range(len(self.q)):
            print(self.q[i], end=" ")
        print("]")


mycircularTest = MyCircularQueue(5)

mycircularTest.enQueue(1)
mycircularTest.enQueue(2)
mycircularTest.enQueue(3)
mycircularTest.enQueue(4)

mycircularTest.Rear()
mycircularTest.ptr()

mycircularTest.deQueue()
mycircularTest.deQueue()
mycircularTest.enQueue(5)
mycircularTest.enQueue(6)
mycircularTest.ptr()

mycircularTest.Rear()
mycircularTest.Front()