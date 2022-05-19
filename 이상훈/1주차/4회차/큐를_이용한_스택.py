# https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque

class MyStack:
    q = None

    def __init__(self):
        self.q = deque()

    def get_last_to_front(self):
        if not self.q:
            return

        cnt = len(self.q) - 1
        while cnt:
            self.q.append(self.q.popleft())
            cnt -= 1

    def push(self, x: int) -> None:
        self.q.append(x)
        self.get_last_to_front()

    def pop(self) -> int:
        return self.q.popleft()


    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
