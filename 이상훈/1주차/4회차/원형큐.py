# https://leetcode.com/problems/design-circular-queue/

from collections import deque

class MyCircularQueue:
    Q = None
    size = None

    def __init__(self, k: int):
        self.Q = deque([], maxlen=k)
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.Q.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.Q.popleft()

        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[0]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[-1]


    def isEmpty(self) -> bool:
        return not self.Q

    def isFull(self) -> bool:
        return self.size == len(self.Q)

