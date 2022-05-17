# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def fill_output(self):
        while self.input:
            self.output.append(self.input.pop())

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if not self.output:
            self.fill_output()

        return self.output.pop()


    def peek(self) -> int:
        if not self.output:
            self.fill_output()

        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output

